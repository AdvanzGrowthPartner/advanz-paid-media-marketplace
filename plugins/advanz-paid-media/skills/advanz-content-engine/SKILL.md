---
name: advanz-content-engine
description: >-
  Motor brand-agnostic de Advanz para producir creativos publicitarios on-brand con IA
  para CUALQUIER marca — de punta a punta: onboarding, clasificar, generar, aprobar,
  Meta, medir, aprender. Usar SIEMPRE que el usuario diga "quiero crear creativos",
  "generar contenido/creativos para [marca]", "armar anuncios para [marca]", "contenido
  en volumen para [marca]", "probar el content engine", "arrancar el sistema de contenido",
  o pegue una marca/carpeta/URL y pida producir piezas. Es marca-agnóstico: el motor no
  cambia, cambia el Brand Profile. Reusa las skills estaticos-ia (generación), 7-maletas
  (investigación) y diagram-engine. ANTES de arrancar, confirmar con el usuario el MODO
  (Express o Sistema). Amazing Care es el primer caso validado, pero vive como instancia
  separada — nunca cablear nada de Amazing dentro del motor.
---

# Advanz Content Engine

Motor **brand-agnostic** para producir creativos on-brand con IA para cualquier marca.
**Regla madre:** el motor es una plantilla PURA (placeholders). Cada marca es un
**Brand Profile** que la llena. Amazing = instancia de ejemplo, separada. Al terminar,
**test de pureza:** si aparece "Amazing / Electrolitos / P1 Deportista / Moderat" dentro
del motor → está contaminado, sacarlo.

**Spec visual (referencia, no rehacer):**
- Walkthrough: https://claude.ai/code/artifact/8578fa67-15c3-46d9-a16c-817c404b07f9
- Mapa end-to-end navegable: https://claude.ai/code/artifact/7dc635c1-2213-4b54-a30e-887e7a6cd1e8

---

## Paso 0 · Elige el modo (primera y única pregunta obligatoria)

| Modo | Qué hace | Input | Incluye |
|---|---|---|---|
| **🚀 Express** | Solo dar creativos on-brand | Marca + fotos + objetivo | Generar + copy + aprobación |
| **🏗️ Sistema** | El flywheel completo | Acceso a Notion / Meta / Drive | Clasificar · base · Meta · medir · aprender |

Express se **gradúa** a Sistema cuando el usuario quiera estructurar. No hace falta Notion
para arrancar; si lo hay, se activa el flywheel.

## Paso 1 · Brief mínimo (4 cosas)

`Objetivo · Avatar · Producto/Oferta · Etapa de funnel`

El **objetivo es la estrella polar**: de ahí se derivan funnel, ángulo y formato. Sin
objetivo explícito, no generar (se produce lindo pero sin norte). **Placement:** una sola
pregunta — ¿Meta, TikTok o Google?

## Paso 2 · Onboarding (magro) + gap report

Insumos, en orden de valor:
1. **URL del sitio** → analizar PDP, marca y ecommerce. Autocompleta gran parte del Brand
   Profile (paleta, claims, precios, reseñas, posicionamiento) → menos preguntas.
2. **Brand guidelines** → logo, paleta, fuentes, y **claims permitidos + prohibidos**
   (sobre todo salud/legal).
3. **Fotos de producto** → 🔴 innegociable (la IA nunca inventa el pack).
4. **Referencias / ganadores** → ads propios + winners (con su performance) + competencia.
5. **Reseñas / Voz de cliente** → opcional (skill 7-maletas): el lenguaje real de los dolores.

**Sourcing (cadena de fallback):** Shopify CDN → Drive → **carpeta local** → pegar en el chat.
La carpeta local es la ruta por defecto; Drive/Shopify/Pletor son aceleradores opcionales.

**Gap report** — clasifica lo faltante por gravedad; el último eslabón siempre es preguntar:
- 🔴 **Bloquea todo** (sin identidad de marca) → resolver primero.
- 🟠 **Bloquea la pieza** (sin foto real) → pedir el insumo.
- 🟡 **Bloquea el claim** (sin dato duro) → omitir o pedir.
- ⚪ **Degrada** (sin performance) → generar igual, menos optimizado.

**Salida:** el **Brand Profile** de la marca (archivo aparte) + veredicto de huecos.

## Las 7 fases del ciclo

| # | Fase | Qué hace | Dónde (modo Sistema) |
|---|---|---|---|
| 01 | **Clasificar** | 2 fases: (A) analizar ads descargados; (B) capturar ganadores con su performance. Marca huecos avatar×funnel. | Base Creativos + Matriz |
| 02 | **Generar** | Estáticos on-brand con IA (producto real de referencia) + copy. Anti-repetición vs lo hecho. | Manuales + Copywriting |
| 03 | **Aprobar** | Checklist de la marca. Solo lo aprobado avanza → Drive con SKU. | Fase 0 |
| 04 | **Meta** | Packs → adsets. ABO testea / CBO escala. Ads nombrados por SKU. | Meta Ads |
| 05 | **Medir** | Gasto/ROAS/compras por SKU (por eso el naming por SKU). | Meta → Base |
| 06 | **Aprender** | Qué ángulo/estructura/avatar vende. Escala el ganador (vertical+horizontal). | Aprendizajes |
| 07 | **Reingreso** | Lo aprendido define qué se clasifica y genera. El ciclo se afina. | ↺ vuelve a 01/02 |

En **modo Sistema**, el onboarding **provisiona el Notion**: clona un template
brand-agnostic (fases + esquema de bases + manuales) y re-parametriza las opciones con
los avatares/productos/packs de la marca.

## Entregable para el equipo (HTML branded) — capa de handoff

En cualquier punto, el engine empaqueta un **HTML branded** (estándar Advanz de entregables,
ver [[advanz_reporting_engine_vision]] y skill relacionada) para compartir con el equipo /
diseño / IA. **Dos modos:**

- **📋 Brief / bajada** (ANTES de producir) — el objetivo del mes/campaña, el ángulo, la
  estructura, los **do's & don'ts** (incluidos los claims permitidos/prohibidos) y ejemplos.
  Para decirle al equipo *"chicos, esto es lo que hay que desarrollar y por qué"* y que hagan
  las piezas alineadas. (Ej: el brief de NAD-FDA.)
- **🖼️ Showcase** (DESPUÉS de producir) — las piezas desarrolladas **embebidas**, con su
  ficha (avatar · ángulo · funnel · SKU), para que el equipo las **revise/apruebe** de un vistazo.

La marca del HTML = el **Brand Profile de la marca** (no Advanz), salvo que sea un doc interno.
Es la salida natural de las fases Generar (showcase) y del onboarding/planificación (brief).

## 4 requisitos de arquitectura (por fases, low-friction)

1. **Conexiones just-in-time** — cada conexión (Notion/Drive/Pletor/Meta) se usa y verifica
   **cuando la fase la necesita**, no todo al arranque. Cada una con su fallback. `[LIVE]`
2. **Memoria que aprende por marca** — cada feedback/aprobación/rechazo **actualiza las
   reglas de esa marca** con un **append de una línea** (sin fricción) + un archivo de
   memoria por marca. Arranca vacía, crece con el uso. `[v1: los ganchos]`
3. **ADN ganador** — de los ganadores (propios + referencias) se extrae el **patrón** que
   guía CADA generación, no solo la pieza puntual. `[v1/v2]`
4. **Criterio antes del final** — validar en el **brief/prompt** contra reglas + ADN +
   auto-chequeo, para NO iterar en piezas finales. La pieza sale correcta por construcción. `[LIVE]`

## Principios (no negociables)

- **Foto real del producto = innegociable.** La IA nunca inventa el pack ni el texto.
- **Generación:** Pletor si está; si no, entregar **el prompt afinado + la foto** para que
  el usuario genere en ChatGPT/Gemini. Método ganador = IA con producto real de referencia
  + QA humano al final.
- **Reglas de aprobación se DERIVAN por marca** (del feedback del equipo/cliente), no se
  heredan de otra marca.
- **Video = parqueado** (módulo futuro). Hoy el engine genera estáticos.

## Skills que reusa

- **estaticos-ia** → generación de estáticos on-brand (el motor de piezas).
- **7-maletas** → investigación de mercado / voz de cliente (avatares, dolores, copy).
- **diagram-engine** → mapas/diagramas cuando haga falta un entregable visual.

## Export a prompt maestro

La skill es la **fuente de verdad**. Para portabilidad (modo Express o correr fuera de
Claude Code), se puede **exportar un prompt maestro** = una versión condensada de este
flujo (Paso 0 → 1 → 2 + generación) que el usuario pega en ChatGPT/Gemini junto con la
foto del producto.

## Instancia de ejemplo

**Amazing Care** es el primer caso validado (75 creativos, base viva, test ABO, medición
por SKU). Vive **separado** como un Brand Profile lleno — sirve de modelo de "así se ve
un Notion terminado", nunca como parte del motor. Ver memorias `amazing_content_system`,
`amazing_reglas_aprobacion_ads`, `amazing_generador_estaticos_ia`.
