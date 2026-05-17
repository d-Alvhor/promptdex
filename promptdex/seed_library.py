from __future__ import annotations

from promptdex.schemas import PromptCreate

LIBRARY_VERSION_TAG = "library-2026-05"


def builtin_prompt_library() -> list[PromptCreate]:
    shared = [LIBRARY_VERSION_TAG, "es", "en"]
    return [
        PromptCreate(
            title="Codex task spec / Especificacion para Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "coding", "spec"],
            rating=5,
            favorite=True,
            body="""ES:
Actua como mi senior founding engineer. Antes de tocar codigo, resume el objetivo, inspecciona el repositorio y convierte esta tarea en cambios pequenos y verificables. Implementa solo lo necesario, respeta el estilo existente, no reviertas cambios ajenos y termina con pruebas ejecutadas, estado de git y siguientes mejoras.

EN:
Act as my senior founding engineer. Before touching code, summarize the goal, inspect the repository, and turn this task into small verifiable changes. Implement only what is needed, respect the existing style, do not revert other people's changes, and finish with executed checks, git status, and next improvements.""",
        ),
        PromptCreate(
            title="Bug reproduction loop / Bucle de reproduccion de bug",
            category="Debugging",
            tags=[*shared, "debugging", "repro", "tests"],
            rating=5,
            body="""ES:
Diagnostica este bug con disciplina: reproduce el fallo, reduce el caso, formula 2-3 hipotesis, instrumenta lo minimo, arregla la causa raiz y agrega una prueba de regresion. No propongas cambios hasta tener evidencia.

EN:
Diagnose this bug with discipline: reproduce the failure, minimize the case, form 2-3 hypotheses, instrument only what is needed, fix the root cause, and add a regression test. Do not propose changes until you have evidence.""",
        ),
        PromptCreate(
            title="Architecture decision record / ADR de arquitectura",
            category="Architecture",
            tags=[*shared, "architecture", "adr", "tradeoffs"],
            rating=5,
            body="""ES:
Escribe un ADR breve para esta decision. Incluye contexto, fuerzas en tension, opciones consideradas, decision, consecuencias, riesgos y senales para reconsiderarla. Se claro sobre lo que queda fuera de alcance.

EN:
Write a concise ADR for this decision. Include context, competing forces, options considered, decision, consequences, risks, and signals that should trigger reconsideration. Be explicit about what is out of scope.""",
        ),
        PromptCreate(
            title="Prompt upgrade for reasoning models / Mejora para modelos de razonamiento",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "reasoning", "prompting"],
            rating=5,
            favorite=True,
            body="""ES:
Reescribe este prompt para un modelo de razonamiento moderno. Hazlo directo, con objetivo claro, contexto suficiente, restricciones, formato de salida y criterios de exito. Evita pedir cadena de pensamiento; pide una respuesta verificable y concisa.

EN:
Rewrite this prompt for a modern reasoning model. Make it direct, with a clear goal, enough context, constraints, output format, and success criteria. Avoid asking for chain-of-thought; request a verifiable and concise answer.""",
        ),
        PromptCreate(
            title="Claude XML task frame / Marco XML para Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "xml", "prompting"],
            rating=5,
            body="""ES:
Usa esta estructura para una tarea compleja:
<contexto>...</contexto>
<objetivo>...</objetivo>
<restricciones>...</restricciones>
<ejemplos>...</ejemplos>
<salida>Define el formato exacto.</salida>
Primero verifica ambiguedades criticas; despues responde.

EN:
Use this structure for a complex task:
<context>...</context>
<goal>...</goal>
<constraints>...</constraints>
<examples>...</examples>
<output>Define the exact format.</output>
First check for critical ambiguity; then answer.""",
        ),
        PromptCreate(
            title="Code review severity pass / Revision de codigo por severidad",
            category="Coding",
            tags=[*shared, "review", "quality", "codex"],
            rating=5,
            body="""ES:
Revisa este diff como reviewer senior. Prioriza bugs, regresiones, seguridad, datos y pruebas faltantes. Devuelve hallazgos ordenados por severidad con archivo/linea, por que importa y el cambio minimo recomendado. Si no hay hallazgos, dilo claramente.

EN:
Review this diff as a senior reviewer. Prioritize bugs, regressions, security, data issues, and missing tests. Return findings by severity with file/line, why it matters, and the minimal recommended change. If there are no findings, say so clearly.""",
        ),
        PromptCreate(
            title="Design critique / Critica de diseno",
            category="Design",
            tags=[*shared, "ui", "ux", "design"],
            rating=4,
            body="""ES:
Critica esta interfaz para un producto real. Evalua jerarquia, densidad, accesibilidad, estados vacios/error, responsive, copy y flujos frecuentes. Propone 5 mejoras concretas, ordenadas por impacto.

EN:
Critique this interface for a real product. Evaluate hierarchy, density, accessibility, empty/error states, responsiveness, copy, and frequent workflows. Propose 5 concrete improvements ordered by impact.""",
        ),
        PromptCreate(
            title="Landing page copy / Copy de landing",
            category="Marketing",
            tags=[*shared, "marketing", "copy", "landing"],
            rating=4,
            body="""ES:
Escribe copy para una landing. Audiencia: [audiencia]. Producto: [producto]. Diferenciador: [diferenciador]. Devuelve H1, subtitulo, 3 beneficios, prueba social, CTA principal/secundario y objeciones frecuentes con respuestas.

EN:
Write landing page copy. Audience: [audience]. Product: [product]. Differentiator: [differentiator]. Return H1, subtitle, 3 benefits, social proof, primary/secondary CTA, and common objections with responses.""",
        ),
        PromptCreate(
            title="Research synthesis / Sintesis de investigacion",
            category="Research",
            tags=[*shared, "research", "synthesis", "sources"],
            rating=5,
            body="""ES:
Sintetiza esta investigacion. Separa hechos, inferencias y opiniones. Incluye una tabla con fuente, fecha, afirmacion clave, confianza y contradicciones. Termina con preguntas abiertas y proximos pasos.

EN:
Synthesize this research. Separate facts, inferences, and opinions. Include a table with source, date, key claim, confidence, and contradictions. End with open questions and next steps.""",
        ),
        PromptCreate(
            title="Agent handoff brief / Brief para agentes",
            category="Agents",
            tags=[*shared, "agents", "handoff", "workflow"],
            rating=5,
            body="""ES:
Prepara un brief para un agente autonomo. Incluye mision, contexto, limites, herramientas permitidas, criterios de exito, riesgos, comandos de verificacion y formato de reporte final. Hazlo accionable y sin ambiguedad.

EN:
Prepare a brief for an autonomous agent. Include mission, context, boundaries, allowed tools, success criteria, risks, verification commands, and final report format. Make it actionable and unambiguous.""",
        ),
        PromptCreate(
            title="Meeting to execution plan / Reunion a plan de ejecucion",
            category="Productivity",
            tags=[*shared, "productivity", "planning", "meeting"],
            rating=4,
            body="""ES:
Convierte estas notas de reunion en un plan. Extrae decisiones, responsables, tareas, dependencias, fechas, riesgos y preguntas abiertas. Marca cualquier accion sin owner como bloqueada.

EN:
Turn these meeting notes into a plan. Extract decisions, owners, tasks, dependencies, dates, risks, and open questions. Mark any action without an owner as blocked.""",
        ),
        PromptCreate(
            title="SQL query helper / Ayudante SQL",
            category="Coding",
            tags=[*shared, "sql", "data", "debugging"],
            rating=4,
            body="""ES:
Ayudame con esta consulta SQL. Primero explica el objetivo en una frase, luego propone la consulta, indices utiles, casos borde y como validarla con 3 filas de ejemplo. Evita optimizaciones prematuras.

EN:
Help me with this SQL query. First explain the goal in one sentence, then propose the query, useful indexes, edge cases, and how to validate it with 3 example rows. Avoid premature optimization.""",
        ),
        PromptCreate(
            title="API contract design / Diseno de contrato API",
            category="Architecture",
            tags=[*shared, "api", "backend", "contracts"],
            rating=5,
            body="""ES:
Disena este contrato API local. Define recursos, endpoints, esquemas request/response, errores, paginacion si aplica, idempotencia, validaciones y pruebas de contrato. Mantenerlo simple es un requisito.

EN:
Design this local API contract. Define resources, endpoints, request/response schemas, errors, pagination if applicable, idempotency, validations, and contract tests. Keeping it simple is a requirement.""",
        ),
        PromptCreate(
            title="Test plan from requirements / Plan de pruebas desde requisitos",
            category="Debugging",
            tags=[*shared, "qa", "tests", "requirements"],
            rating=5,
            body="""ES:
Crea un plan de pruebas desde estos requisitos. Incluye happy path, errores, bordes, persistencia, accesibilidad si hay UI, y una matriz requisito -> prueba. Prioriza pruebas que detectarian regresiones reales.

EN:
Create a test plan from these requirements. Include happy path, errors, edge cases, persistence, accessibility if there is UI, and a requirement -> test matrix. Prioritize tests that would catch real regressions.""",
        ),
        PromptCreate(
            title="Refactor without behavior change / Refactor sin cambiar comportamiento",
            category="Coding",
            tags=[*shared, "refactor", "tests", "codex"],
            rating=5,
            body="""ES:
Refactoriza este codigo sin cambiar comportamiento. Primero identifica responsabilidades mezcladas y riesgos. Propone pasos pequenos, cada uno con prueba o verificacion. Manten nombres claros y evita abstracciones que no eliminen complejidad real.

EN:
Refactor this code without changing behavior. First identify mixed responsibilities and risks. Propose small steps, each with a test or verification. Keep names clear and avoid abstractions that do not remove real complexity.""",
        ),
        PromptCreate(
            title="Competitive positioning / Posicionamiento competitivo",
            category="Marketing",
            tags=[*shared, "positioning", "strategy", "marketing"],
            rating=4,
            body="""ES:
Ayudame a posicionar este producto. Compara alternativas, jobs-to-be-done, usuarios ideales, mensaje principal, razones para creer y riesgos de percepcion. Devuelve una tabla y un pitch de 30 segundos.

EN:
Help me position this product. Compare alternatives, jobs-to-be-done, ideal users, main message, reasons to believe, and perception risks. Return a table and a 30-second pitch.""",
        ),
        PromptCreate(
            title="Long context extraction / Extraccion con contexto largo",
            category="Research",
            tags=[*shared, "long-context", "extraction", "claude"],
            rating=5,
            body="""ES:
Extrae informacion de este documento largo. Usa solo el contenido proporcionado, cita secciones o frases cortas, marca lo no encontrado como 'no consta' y devuelve JSON valido con los campos solicitados.

EN:
Extract information from this long document. Use only the provided content, cite sections or short phrases, mark missing information as 'not found', and return valid JSON with the requested fields.""",
        ),
        PromptCreate(
            title="Personal knowledge distiller / Destilador de conocimiento",
            category="Productivity",
            tags=[*shared, "notes", "knowledge", "summary"],
            rating=4,
            body="""ES:
Convierte estas notas dispersas en conocimiento reutilizable. Crea resumen, principios, decisiones, snippets accionables, etiquetas y recordatorios. Manten lo importante; elimina relleno.

EN:
Turn these scattered notes into reusable knowledge. Create a summary, principles, decisions, actionable snippets, tags, and reminders. Preserve what matters; remove filler.""",
        ),
        PromptCreate(
            title="Frontend implementation brief / Brief de frontend",
            category="Design",
            tags=[*shared, "frontend", "ui", "implementation"],
            rating=5,
            body="""ES:
Implementa esta UI con criterio de producto. Define estados completos, responsive, accesibilidad, microinteracciones y datos de ejemplo. Evita landing generica: construye la experiencia usable desde la primera pantalla.

EN:
Implement this UI with product judgment. Define complete states, responsiveness, accessibility, microinteractions, and sample data. Avoid a generic landing page: build the usable experience on the first screen.""",
        ),
        PromptCreate(
            title="Risk register / Registro de riesgos",
            category="Architecture",
            tags=[*shared, "risk", "planning", "systems"],
            rating=4,
            body="""ES:
Crea un registro de riesgos para este proyecto. Para cada riesgo incluye probabilidad, impacto, senales tempranas, mitigacion, owner y decision requerida. Separa riesgos tecnicos, producto y operacion.

EN:
Create a risk register for this project. For each risk include probability, impact, early warning signs, mitigation, owner, and required decision. Separate technical, product, and operational risks.""",
        ),
        PromptCreate(
            title="Codex PR finishing pass / Cierre de PR con Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "git", "release"],
            rating=5,
            body="""ES:
Prepara este trabajo para cerrar. Revisa diff, ejecuta pruebas relevantes, actualiza README si aplica, resume cambios, riesgos restantes, comandos ejecutados, estado de git y commit sugerido. No hagas push.

EN:
Prepare this work for completion. Review the diff, run relevant checks, update README if needed, summarize changes, remaining risks, commands run, git status, and suggested commit. Do not push.""",
        ),
        PromptCreate(
            title="ChatGPT structured answer / Respuesta estructurada ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "structured-output", "analysis"],
            rating=4,
            body="""ES:
Responde con esta estructura: conclusion breve, supuestos, pasos recomendados, riesgos, y ejemplo. Si falta informacion critica, haz maximo 3 preguntas; si puedes avanzar con supuestos razonables, hazlo y declaralos.

EN:
Answer with this structure: brief conclusion, assumptions, recommended steps, risks, and example. If critical information is missing, ask at most 3 questions; if you can proceed with reasonable assumptions, do so and state them.""",
        ),
        PromptCreate(
            title="Performance investigation plan / Plan de investigacion de rendimiento",
            category="Debugging",
            tags=[*shared, "performance", "profiling", "observability"],
            rating=5,
            body="""ES:
Ayudame a investigar un problema de rendimiento. Primero define el sintoma medible (latencia, CPU, memoria, I/O) y el objetivo. Luego propone:
1) Hipotesis (max 5) ordenadas por probabilidad/impacto
2) Instrumentacion minima (logs, metrics, traces) para confirmar/refutar cada hipotesis
3) Experimentos reproducibles y como evitar sesgos
4) Cambio minimo para corregir la causa raiz
5) Prueba/alerta de regresion y como monitorear despues
Devuelve una lista accionable con comandos sugeridos y criterios de exito.

EN:
Help me investigate a performance issue. First define the measurable symptom (latency, CPU, memory, I/O) and the goal. Then propose:
1) Hypotheses (max 5) ordered by probability/impact
2) Minimal instrumentation (logs, metrics, traces) to confirm/refute each hypothesis
3) Reproducible experiments and how to avoid bias
4) Minimal change to fix the root cause
5) Regression test/alert and post-fix monitoring plan
Return an actionable checklist with suggested commands and success criteria.""",
        ),
        PromptCreate(
            title="Security threat model / Modelo de amenazas",
            category="Architecture",
            tags=[*shared, "security", "threat-model", "risk"],
            rating=5,
            body="""ES:
Haz un threat model para este sistema/feature. Define activos, limites de confianza, actores, vectores de ataque y supuestos. Luego produce:
- Tabla STRIDE (amenaza, impacto, probabilidad, mitigacion, owner)
- Controles minimos recomendados (auth, autorizacion, validacion, logging, rate limits)
- Lista de "no hacer" (antipatrones)
No inventes requisitos: si falta info, pregunta maximo 3 cosas y continua con supuestos claramente marcados.

EN:
Do a threat model for this system/feature. Define assets, trust boundaries, actors, attack vectors, and assumptions. Then produce:
- STRIDE table (threat, impact, likelihood, mitigation, owner)
- Minimal recommended controls (auth, authorization, validation, logging, rate limits)
- "Do not do" list (anti-patterns)
Do not invent requirements: if key info is missing, ask at most 3 questions and proceed with clearly labeled assumptions.""",
        ),
        PromptCreate(
            title="PRD one-pager / PRD de una pagina",
            category="Productivity",
            tags=[*shared, "product", "requirements", "writing"],
            rating=4,
            body="""ES:
Convierte esta idea en un PRD de una pagina. Incluye: problema, usuario objetivo, objetivos medibles, no-objetivos, alcance (MVP), UX a alto nivel, requisitos funcionales, requisitos no funcionales, riesgos, dependencia y como se medira el exito. Mantenerlo corto es requisito.

EN:
Turn this idea into a one-page PRD. Include: problem, target user, measurable goals, non-goals, scope (MVP), high-level UX, functional requirements, non-functional requirements, risks, dependencies, and how success will be measured. Keeping it short is a requirement.""",
        ),
        PromptCreate(
            title="User story mapping / Mapa de historias de usuario",
            category="Productivity",
            tags=[*shared, "product", "user-stories", "prioritization"],
            rating=4,
            body="""ES:
Crea un user story map para este producto/feature. Define: actividades del usuario, pasos (journey), historias por paso, prioridades (MVP / despues), criterios de aceptacion y riesgos. Devuelve una tabla y una lista de entregables por iteracion.

EN:
Create a user story map for this product/feature. Define: user activities, journey steps, stories per step, priorities (MVP / later), acceptance criteria, and risks. Return a table plus a deliverables list per iteration.""",
        ),
        PromptCreate(
            title="UX copy tone guide / Guia de tono para UX copy",
            category="Design",
            tags=[*shared, "ux-writing", "copy", "tone"],
            rating=4,
            body="""ES:
Define una guia de tono para este producto. Incluye: personalidad, palabras a usar/evitar, ejemplos de microcopy (errores, vacio, confirmaciones), longitud objetivo, y reglas para mensajes de error (accionable, sin culpar, con siguiente paso). Devuelve ejemplos listos para pegar.

EN:
Define a tone guide for this product. Include: personality, words to use/avoid, microcopy examples (errors, empty states, confirmations), target length, and error-message rules (actionable, no blame, clear next step). Return copy-ready examples.""",
        ),
        PromptCreate(
            title="Email campaign outline / Esquema de campana de email",
            category="Marketing",
            tags=[*shared, "email", "campaign", "copy"],
            rating=4,
            body="""ES:
Disena una campana de email de 3-5 correos para este producto. Define segmento, propuesta de valor, objetivo por email, asunto (3 opciones), estructura, CTA, y como medir resultados. Evita promesas exageradas; se especifico.

EN:
Design a 3-5 email campaign for this product. Define segment, value proposition, goal per email, subject lines (3 options), structure, CTA, and how to measure results. Avoid hype; be specific.""",
        ),
        PromptCreate(
            title="SEO content brief / Brief de contenido SEO",
            category="Marketing",
            tags=[*shared, "seo", "content", "research"],
            rating=4,
            body="""ES:
Crea un brief SEO para un articulo. Incluye: keyword principal, intent, keywords secundarias, estructura H1/H2, preguntas a responder, ejemplos, contraejemplos, y criterios de calidad. Si faltan datos, pide maximo 3 aclaraciones y continua con supuestos.

EN:
Create an SEO content brief for an article. Include: primary keyword, intent, secondary keywords, H1/H2 outline, questions to answer, examples, counterexamples, and quality criteria. If key data is missing, ask at most 3 clarifying questions and proceed with assumptions.""",
        ),
        PromptCreate(
            title="Data model sanity check / Revision de modelo de datos",
            category="Architecture",
            tags=[*shared, "data-model", "database", "consistency"],
            rating=5,
            body="""ES:
Revisa este modelo de datos. Busca: invariantes, normalizacion vs pragmatismo, claves/indices, relaciones, borrado/retencion, migraciones, y consultas mas comunes. Devuelve:
1) Lista de riesgos (con severidad)
2) Cambios minimos recomendados
3) Pruebas de integridad a agregar

EN:
Review this data model. Check: invariants, normalization vs pragmatism, keys/indexes, relationships, deletion/retention, migrations, and common queries. Return:
1) Risk list (with severity)
2) Minimal recommended changes
3) Integrity tests to add""",
        ),
        PromptCreate(
            title="Agent tool contract / Contrato de herramienta para agente",
            category="Agents",
            tags=[*shared, "agents", "tools", "contracts"],
            rating=5,
            body="""ES:
Define un contrato para una herramienta que usara un agente. Incluye: nombre, proposito, entradas (schema), salidas (schema), errores, idempotencia, limites (tiempo/tamano), permisos, y ejemplos. Termina con casos borde y pruebas sugeridas.

EN:
Define a contract for a tool an agent will use. Include: name, purpose, inputs (schema), outputs (schema), errors, idempotency, limits (time/size), permissions, and examples. End with edge cases and suggested tests.""",
        ),
        PromptCreate(
            title="Prompt evaluation rubric / Rubrica de evaluacion de prompts",
            category="Prompts for ChatGPT",
            tags=[*shared, "prompting", "evaluation", "quality"],
            rating=5,
            body="""ES:
Evalua este prompt con una rubrica. Puntua 1-5: claridad del objetivo, contexto, restricciones, formato de salida, criterios de exito, testabilidad, seguridad/privacidad, y esfuerzo del usuario. Devuelve:
- Tabla (criterio, puntuacion, por que, mejora concreta)
- Version mejorada del prompt (sin pedir cadena de pensamiento)

EN:
Evaluate this prompt with a rubric. Score 1-5: goal clarity, context, constraints, output format, success criteria, testability, safety/privacy, and user effort. Return:
- Table (criterion, score, why, concrete improvement)
- Improved prompt version (without requesting chain-of-thought)""",
        ),
        PromptCreate(
            title="Codex TDD feature builder / Constructor de feature TDD con Codex",
            category="Prompts for Codex",
            tags=[*shared, "codex", "tdd", "tests"],
            rating=5,
            favorite=True,
            body="""ES:
Implementa esta feature con enfoque TDD. Primero escribe/actualiza pruebas (unit/integration) que fallen por la razon correcta. Luego implementa el minimo para pasar. Itera hasta cubrir bordes. Mantente dentro del repo; no agregues dependencias sin necesidad. Termina con comandos exactos ejecutados y estado de git.

EN:
Implement this feature using TDD. First write/update unit/integration tests that fail for the right reason. Then implement the minimum to pass. Iterate until edges are covered. Stay within the repo; do not add dependencies unless necessary. Finish with exact commands executed and git status.""",
        ),
        PromptCreate(
            title="Claude structured extraction to JSON / Extraccion estructurada a JSON para Claude",
            category="Prompts for Claude",
            tags=[*shared, "claude", "extraction", "json"],
            rating=5,
            body="""ES:
Extrae la informacion solicitada y devuelve SOLO JSON valido (sin markdown). Reglas:
- Usa solo el texto proporcionado
- Si un campo no aparece, usa null o \"no consta\" (segun se pida)
- Incluye un campo \"evidence\" con citas cortas (max 20 palabras) por cada item importante
Si hay ambiguedad critica, pregunta maximo 3 cosas.

EN:
Extract the requested information and return ONLY valid JSON (no markdown). Rules:
- Use only the provided text
- If a field is missing, use null or \"not found\" (as requested)
- Include an \"evidence\" field with short quotes (max 20 words) for key items
If there is critical ambiguity, ask at most 3 questions.""",
        ),
        PromptCreate(
            title="ChatGPT quick decision memo / Memo rapido de decision para ChatGPT",
            category="Prompts for ChatGPT",
            tags=[*shared, "chatgpt", "decision", "tradeoffs"],
            rating=4,
            body="""ES:
Ayudame a tomar esta decision. Devuelve: recomendacion, 2 alternativas, criterios, tradeoffs, riesgos, y plan de reversibilidad. Si faltan datos, declara supuestos y pide maximo 3 preguntas al final.

EN:
Help me make this decision. Return: recommendation, 2 alternatives, criteria, tradeoffs, risks, and reversibility plan. If data is missing, state assumptions and ask at most 3 questions at the end.""",
        ),
        PromptCreate(
            title="Git commit message helper / Ayudante de mensajes de commit",
            category="Productivity",
            tags=[*shared, "git", "commits", "writing"],
            rating=4,
            body="""ES:
Genera un mensaje de commit claro. Entradas: resumen del cambio, impacto, riesgos. Salida:
- 3 opciones (conventional commits si aplica)
- Una opcion recomendada
- Cuerpo opcional con bullets (que cambio, por que, como verificar)

EN:
Generate a clear commit message. Inputs: change summary, impact, risks. Output:
- 3 options (Conventional Commits if applicable)
- One recommended option
- Optional body bullets (what changed, why, how to verify)""",
        ),
        PromptCreate(
            title="Incident status update / Actualizacion de estado de incidente",
            category="Productivity",
            tags=[*shared, "incident", "oncall", "communication"],
            rating=4,
            body="""ES:
Redacta una actualizacion de incidente para stakeholders. Incluye: resumen, impacto, alcance, linea temporal breve, mitigacion aplicada, estado actual, siguientes pasos, riesgos, y ETA si existe (o explica por que no). Mantenerlo honesto es requisito.

EN:
Write an incident update for stakeholders. Include: summary, impact, scope, short timeline, mitigation applied, current status, next steps, risks, and ETA if known (or explain why not). Being honest is a requirement.""",
        ),
        PromptCreate(
            title="Customer interview script / Guion de entrevista a usuarios",
            category="Research",
            tags=[*shared, "research", "interviews", "product"],
            rating=4,
            body="""ES:
Crea un guion de entrevista de 30 minutos para este problema. Incluye: objetivos, preguntas abiertas, probes, preguntas de comportamiento pasado, y como evitar sesgos. Termina con una plantilla para capturar notas (quotes, dolor, soluciones actuales).

EN:
Create a 30-minute customer interview script for this problem. Include: goals, open-ended questions, probes, past-behavior questions, and how to avoid bias. End with a note-taking template (quotes, pain, current solutions).""",
        ),
        PromptCreate(
            title="Competitive teardown / Analisis competitivo profundo",
            category="Research",
            tags=[*shared, "competition", "analysis", "marketing"],
            rating=4,
            body="""ES:
Haz un analisis competitivo profundo. Compara 3-5 alternativas en: publico objetivo, propuesta de valor, pricing (si se conoce), UX, integraciones, barreras de cambio y riesgos. Devuelve una tabla y 3 apuestas estrategicas.

EN:
Do a competitive teardown. Compare 3-5 alternatives on: target audience, value proposition, pricing (if known), UX, integrations, switching costs, and risks. Return a table plus 3 strategic bets.""",
        ),
        PromptCreate(
            title="API error taxonomy / Taxonomia de errores API",
            category="Architecture",
            tags=[*shared, "api", "errors", "contracts"],
            rating=5,
            body="""ES:
Define una taxonomia de errores para esta API. Incluye: codigos, estructura JSON, mensajes para usuario vs logs, trazabilidad (request_id), y reglas de mapeo desde excepciones internas. Devuelve ejemplos de 5 errores comunes y como probarlos.

EN:
Define an error taxonomy for this API. Include: codes, JSON structure, user-facing vs log messages, traceability (request_id), and mapping rules from internal exceptions. Return examples for 5 common errors and how to test them.""",
        ),
        PromptCreate(
            title="Documentation from code / Documentacion desde codigo",
            category="Coding",
            tags=[*shared, "docs", "maintenance", "readme"],
            rating=4,
            body="""ES:
Genera documentacion a partir de este codigo. Produce: descripcion, como ejecutarlo, configuracion, ejemplos, y errores comunes. No inventes flags ni endpoints: si no estan en el codigo, marca como \"no consta\" o pide una aclaracion.

EN:
Generate documentation from this code. Produce: overview, how to run it, configuration, examples, and common errors. Do not invent flags or endpoints: if they are not in the code, mark as \"not found\" or ask for clarification.""",
        ),
        PromptCreate(
            title="Architecture diagram spec / Especificacion de diagrama de arquitectura",
            category="Architecture",
            tags=[*shared, "architecture", "diagram", "documentation"],
            rating=4,
            body="""ES:
Convierte esta arquitectura en una especificacion de diagrama (texto). Incluye: componentes, limites de confianza, flujos principales, dependencias externas, y datos persistidos. Devuelve:
1) Lista de nodos (id, nombre, tipo)
2) Lista de aristas (origen, destino, tipo de flujo, datos)
3) Un diagrama Mermaid (flowchart o sequence) si es posible
No inventes servicios: si falta info, declara supuestos.

EN:
Turn this architecture into a diagram specification (text). Include: components, trust boundaries, main flows, external dependencies, and persisted data. Return:
1) Node list (id, name, type)
2) Edge list (source, target, flow type, data)
3) A Mermaid diagram (flowchart or sequence) if possible
Do not invent services: if info is missing, state assumptions.""",
        ),
    ]
