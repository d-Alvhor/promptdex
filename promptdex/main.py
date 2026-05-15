from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query, Response, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import Session

from promptdex.database import Base, make_engine, make_session_factory, session_dependency
from promptdex.models import Prompt, utc_now
from promptdex.schemas import CATEGORIES, PromptCreate, PromptRead, PromptUpdate

DEFAULT_DATABASE_URL = "sqlite:///./promptdex.db"
STATIC_DIR = Path(__file__).parent / "static"


def create_app(database_url: str = DEFAULT_DATABASE_URL) -> FastAPI:
    engine = make_engine(database_url)
    session_factory = make_session_factory(engine)
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="PromptDex", version="0.1.0")
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    def get_session():
        yield from session_dependency(session_factory)

    @app.get("/", include_in_schema=False)
    def index() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    @app.get("/api/categories")
    def categories() -> list[str]:
        return CATEGORIES

    @app.get("/api/prompts", response_model=list[PromptRead])
    def list_prompts(
        session: Session = Depends(get_session),
        search: str | None = Query(default=None),
        category: str | None = Query(default=None),
        tag: str | None = Query(default=None),
        favorite: bool | None = Query(default=None),
    ) -> Sequence[Prompt]:
        prompts = session.scalars(select(Prompt).order_by(Prompt.id.asc())).all()
        return [
            prompt
            for prompt in prompts
            if _matches_filters(
                prompt,
                search=search,
                category=category,
                tag=tag,
                favorite=favorite,
            )
        ]

    @app.post("/api/prompts", response_model=PromptRead, status_code=status.HTTP_201_CREATED)
    def create_prompt(payload: PromptCreate, session: Session = Depends(get_session)) -> Prompt:
        prompt = Prompt(**payload.model_dump())
        session.add(prompt)
        session.commit()
        session.refresh(prompt)
        return prompt

    @app.get("/api/prompts/{prompt_id}", response_model=PromptRead)
    def get_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Prompt:
        return _get_prompt_or_404(session, prompt_id)

    @app.put("/api/prompts/{prompt_id}", response_model=PromptRead)
    def update_prompt(
        prompt_id: int,
        payload: PromptUpdate,
        session: Session = Depends(get_session),
    ) -> Prompt:
        prompt = _get_prompt_or_404(session, prompt_id)
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(prompt, field, value)
        prompt.updated_at = utc_now()
        session.commit()
        session.refresh(prompt)
        return prompt

    @app.post("/api/prompts/{prompt_id}/use", response_model=PromptRead)
    def use_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Prompt:
        prompt = _get_prompt_or_404(session, prompt_id)
        now = utc_now()
        prompt.last_used_at = now
        prompt.updated_at = now
        session.commit()
        session.refresh(prompt)
        return prompt

    @app.delete("/api/prompts/{prompt_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Response:
        prompt = _get_prompt_or_404(session, prompt_id)
        session.delete(prompt)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return app


def _get_prompt_or_404(session: Session, prompt_id: int) -> Prompt:
    prompt = session.get(Prompt, prompt_id)
    if prompt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found")
    return prompt


def _matches_filters(
    prompt: Prompt,
    *,
    search: str | None,
    category: str | None,
    tag: str | None,
    favorite: bool | None,
) -> bool:
    if favorite is not None and prompt.favorite is not favorite:
        return False

    if category and prompt.category.lower() != category.strip().lower():
        return False

    tags = [item.lower() for item in prompt.tags]
    if tag and tag.strip().lower() not in tags:
        return False

    if search:
        needle = search.strip().lower()
        haystack = " ".join([prompt.title, prompt.body, prompt.category, *prompt.tags]).lower()
        if needle not in haystack:
            return False

    return True


app = create_app()
