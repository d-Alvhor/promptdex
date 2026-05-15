const state = {
  prompts: [],
  categories: [],
  rating: 3,
  favoriteOnly: false,
  copiedId: null,
};

const selectors = {
  search: document.querySelector("#searchInput"),
  categoryFilter: document.querySelector("#categoryFilter"),
  tagFilter: document.querySelector("#tagFilter"),
  favoriteFilter: document.querySelector("#favoriteFilter"),
  list: document.querySelector("#promptList"),
  empty: document.querySelector("#emptyState"),
  count: document.querySelector("#promptCount"),
  template: document.querySelector("#promptCardTemplate"),
  form: document.querySelector("#promptForm"),
  formTitle: document.querySelector("#formTitle"),
  resetForm: document.querySelector("#resetForm"),
  id: document.querySelector("#promptId"),
  title: document.querySelector("#titleInput"),
  category: document.querySelector("#categoryInput"),
  tags: document.querySelector("#tagsInput"),
  body: document.querySelector("#bodyInput"),
  favorite: document.querySelector("#favoriteInput"),
  rating: document.querySelector("#ratingInput"),
};

async function request(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Request failed: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

function parseTags(value) {
  return value
    .split(",")
    .map((tag) => tag.trim().toLowerCase())
    .filter(Boolean);
}

function formatDate(value) {
  if (!value) {
    return "Never used";
  }

  return `Used ${new Intl.DateTimeFormat(undefined, {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date(value))}`;
}

function renderRating(container, value, onChange) {
  container.replaceChildren();

  for (let score = 1; score <= 5; score += 1) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `star-button${score <= value ? " active" : ""}`;
    button.textContent = "★";
    button.setAttribute("aria-label", `${score} star${score === 1 ? "" : "s"}`);
    button.addEventListener("click", () => onChange(score));
    container.append(button);
  }
}

function populateCategories() {
  for (const category of state.categories) {
    const filterOption = new Option(category, category);
    const formOption = new Option(category, category);
    selectors.categoryFilter.append(filterOption);
    selectors.category.append(formOption);
  }
}

function promptMatchesFilters(prompt) {
  const search = selectors.search.value.trim().toLowerCase();
  const category = selectors.categoryFilter.value;
  const tag = selectors.tagFilter.value.trim().toLowerCase();

  if (state.favoriteOnly && !prompt.favorite) {
    return false;
  }

  if (category && prompt.category !== category) {
    return false;
  }

  if (tag && !prompt.tags.includes(tag)) {
    return false;
  }

  if (!search) {
    return true;
  }

  return [prompt.title, prompt.body, prompt.category, prompt.tags.join(" ")]
    .join(" ")
    .toLowerCase()
    .includes(search);
}

function renderPrompts() {
  const prompts = state.prompts.filter(promptMatchesFilters);
  selectors.list.replaceChildren();
  selectors.count.textContent = `${prompts.length} prompt${prompts.length === 1 ? "" : "s"}`;
  selectors.empty.hidden = prompts.length > 0;

  for (const prompt of prompts) {
    const card = selectors.template.content.firstElementChild.cloneNode(true);
    card.querySelector(".badge").textContent = prompt.category;
    card.querySelector("h3").textContent = prompt.title;
    card.querySelector(".body-preview").textContent = prompt.body;
    card.querySelector(".last-used").textContent = formatDate(prompt.last_used_at);

    const favoriteButton = card.querySelector(".favorite-button");
    favoriteButton.textContent = prompt.favorite ? "★" : "☆";
    favoriteButton.classList.toggle("is-favorite", prompt.favorite);
    favoriteButton.addEventListener("click", () =>
      updatePrompt(prompt.id, { favorite: !prompt.favorite }),
    );

    const tags = card.querySelector(".tags");
    for (const tag of prompt.tags) {
      const tagElement = document.createElement("span");
      tagElement.className = "tag";
      tagElement.textContent = `#${tag}`;
      tags.append(tagElement);
    }

    renderRating(card.querySelector(".card-stars"), prompt.rating, (rating) =>
      updatePrompt(prompt.id, { rating }),
    );

    const copyButton = card.querySelector(".copy-button");
    copyButton.textContent = state.copiedId === prompt.id ? "Copied" : "Copy";
    copyButton.addEventListener("click", async () => {
      await navigator.clipboard.writeText(prompt.body);
      state.copiedId = prompt.id;
      renderPrompts();
      await markUsed(prompt.id);
      window.setTimeout(() => {
        if (state.copiedId === prompt.id) {
          state.copiedId = null;
          renderPrompts();
        }
      }, 1100);
    });

    card.querySelector(".edit-button").addEventListener("click", () => fillForm(prompt));
    card.querySelector(".delete-button").addEventListener("click", () => deletePrompt(prompt));
    selectors.list.append(card);
  }
}

function resetForm() {
  selectors.form.reset();
  selectors.id.value = "";
  selectors.formTitle.textContent = "New prompt";
  selectors.favorite.checked = false;
  setFormRating(3);
}

function setFormRating(rating) {
  state.rating = rating;
  renderRating(selectors.rating, state.rating, setFormRating);
}

function fillForm(prompt) {
  selectors.id.value = prompt.id;
  selectors.title.value = prompt.title;
  selectors.category.value = prompt.category;
  selectors.tags.value = prompt.tags.join(", ");
  selectors.body.value = prompt.body;
  selectors.favorite.checked = prompt.favorite;
  selectors.formTitle.textContent = "Edit prompt";
  setFormRating(prompt.rating);
  selectors.title.focus();
}

async function loadPrompts() {
  state.prompts = await request("/api/prompts");
  renderPrompts();
}

async function updatePrompt(id, payload) {
  const updated = await request(`/api/prompts/${id}`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
  state.prompts = state.prompts.map((prompt) => (prompt.id === id ? updated : prompt));
  renderPrompts();
}

async function markUsed(id) {
  const updated = await request(`/api/prompts/${id}/use`, { method: "POST" });
  state.prompts = state.prompts.map((prompt) => (prompt.id === id ? updated : prompt));
  renderPrompts();
}

async function deletePrompt(prompt) {
  const confirmed = window.confirm(`Delete "${prompt.title}"?`);
  if (!confirmed) {
    return;
  }

  await request(`/api/prompts/${prompt.id}`, { method: "DELETE" });
  state.prompts = state.prompts.filter((item) => item.id !== prompt.id);
  renderPrompts();

  if (selectors.id.value === String(prompt.id)) {
    resetForm();
  }
}

selectors.form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = {
    title: selectors.title.value,
    body: selectors.body.value,
    category: selectors.category.value,
    tags: parseTags(selectors.tags.value),
    rating: state.rating,
    favorite: selectors.favorite.checked,
  };

  const id = selectors.id.value;
  if (id) {
    await updatePrompt(id, payload);
  } else {
    const created = await request("/api/prompts", {
      method: "POST",
      body: JSON.stringify(payload),
    });
    state.prompts = [...state.prompts, created];
    renderPrompts();
  }

  resetForm();
});

selectors.resetForm.addEventListener("click", resetForm);
selectors.search.addEventListener("input", renderPrompts);
selectors.categoryFilter.addEventListener("change", renderPrompts);
selectors.tagFilter.addEventListener("input", renderPrompts);
selectors.favoriteFilter.addEventListener("click", () => {
  state.favoriteOnly = !state.favoriteOnly;
  selectors.favoriteFilter.setAttribute("aria-pressed", String(state.favoriteOnly));
  renderPrompts();
});

state.categories = await request("/api/categories");
populateCategories();
setFormRating(3);
await loadPrompts();
