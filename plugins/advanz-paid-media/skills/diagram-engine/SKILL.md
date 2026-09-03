---
name: diagram-engine
description: "Genera diagramas interactivos en HTML self-contained, clickeables y publicables — single-file, sin build. Tipos: flujo, arquitectura de sistema, mapa mental, customer journey, funnel, org chart, roadmap, blueprint, mapa de stack y ECOSYSTEM MAP (canvas infinito navegable con zoom/pan, columnas por área, conexiones curvas tipadas, tags de estado LIVE/WIP/PENDING/MANUAL/BLOCKER/FUTURE, leyenda, minimap y filtros). Cada nodo abre un hipervínculo o se expande a detalle. Usa cuando el usuario diga diagrama, mapa visual, ecosystem map, mapa del ecosistema, mapear todo, mapa del sistema, flujo, flowchart, arquitectura, mapa mental, customer journey, funnel, org chart, roadmap, blueprint, diagrama interactivo/clickeable/navegable/con links/con zoom/que se expande, mapa de proceso, mapa con conexiones, visualiza este flujo, haz un mapa de; o cuando pegue pasos/áreas/un sistema y pida verlo como mapa navegable o entregable visual para publicar."
license: MIT
---

# Diagram Engine

Genera **diagramas interactivos en HTML self-contained** que se ven como producto, no como herramienta de developer. El objetivo siempre es el mismo: un mapa visual **live, navegable y publicable** donde el usuario hace click en los nodos para saltar a recursos reales (un doc, un dashboard, una página, otra sección del mismo diagrama).

## Regla de oro

El entregable es **un único archivo `.html`** que abre en cualquier navegador sin servidor, sin build, sin dependencias instaladas. Todo va inline o por CDN. Esto permite: abrir local, subir a un host estático, embeber en otra herramienta, o mandar por link. Nunca entregues un diagrama que requiera `npm install` para verse.

## Flujo de trabajo (no te saltes pasos)

1. **Clasifica el tipo de diagrama.** Lee `references/diagram-types.md` para elegir entre los 10 tipos canónicos. Cada tipo tiene una geometría y layout recomendados.

2. **Decide el motor de render.** Hay dos. Lee `references/engine-decision.md`:
   - **Mermaid** (vía CDN) — cuando la estructura importa más que el pixel-perfect y el diagrama es grande/cambiante. Rápido de escribir, auto-layout. Limitación conocida: los clicks tienen que hacerse con la directiva `click` de Mermaid, NO con `<a>` embebido (Mermaid lo bloquea por CSP en muchos renderers). Detalle resuelto en el reference.
   - **SVG/HTML custom** — cuando el diagrama es la cara visible al usuario final y tiene que verse pulido, con hover states, animaciones y clicks 100% garantizados. Default para entregables.
   - Regla rápida: *interno/borrador rápido → Mermaid. Publicable → SVG custom.* Si dudas, SVG custom.

3. **Carga el diseño base.** Lee `references/design-system.md`. Tokens neutros (dark por defecto), tipografía, glassmorphism. Personalizable: cambiá las CSS variables del `:root` para adaptarlo a cualquier marca.

4. **Implementa los clicks reales.** Lee `references/interactivity.md`. Cada nodo clickeable debe: (a) tener cursor pointer y hover state visible, (b) abrir su URL en `target="_blank"` salvo que sea navegación interna al mismo diagrama, (c) opcionalmente mostrar un panel lateral / tooltip con detalle al hover/click. NUNCA dejes un nodo que parezca clickeable pero no haga nada.

5. **Construye desde template.** Parte de `templates/` (no desde cero):
   - `templates/ecosystem-map.html` — **canvas infinito navegable**: zoom/pan, columnas por área, conexiones curvas tipadas (flujo vs. loop), tags de estado, highlight al click, filtros por área, minimap y panel de detalle. Es el formato para mapear sistemas/operaciones completas. Data-driven: editás 3 arrays (`COLS`, `NODES`, `WIRES`).
   - `templates/svg-interactive.html` — base SVG custom con panel lateral, zoom/pan, leyenda y nodos clickeables. Para diagramas acotados de cara al usuario final.
   - `templates/mermaid-live.html` — base Mermaid con CDN, tema inyectado y clicks vía directiva. Para borradores rápidos / interno.
   Copia el template a tu working dir, NO lo edites in-place.

6. **Verifica antes de entregar.** Checklist en `references/publishing.md`: abre el archivo, confirma que cada link funciona, que el hover responde, que se ve bien en mobile, y que no quedó ningún `href="#"` muerto. Luego entrega con `present_files`.

## Tipos de diagrama soportados

Flujo de proceso · Arquitectura de sistema · Mapa mental · Customer journey · Funnel (conversión) · Org chart · Roadmap temporal · Blueprint de servicio · Mapa de stack tecnológico · **Ecosystem map** (canvas navegable de toda la operación). Detalle y cuándo usar cada uno en `references/diagram-types.md`.

> **Caso de uso central — Ecosystem Map:** que un sistema, negocio u operación completa viva como un **mapa navegable** en vez de páginas y folders sueltos. Un mapa donde cada nodo es una pieza real con su estado (LIVE/WIP/PENDING/…), sus conexiones (qué alimenta a qué, dónde están los loops) y su link al recurso real. El objetivo no es solo ver el sistema, sino **entender cómo se construye cada conexión**. Para esto, default al tipo #10 y al template `ecosystem-map.html`.

## Modos de entrega

- **Standalone** — un `.html` que abres y listo. Default.
- **Embed** — el mismo archivo subido a un host estático y embebido como iframe.
- **Live público** — para links compartibles. Cualquier host estático sirve.

Detalle en `references/publishing.md`.

## Qué NO hacer

- No entregues PNG/imagen estática cuando piden algo navegable. El punto es el click.
- No uses `<form>` dentro de artifacts React (rompe). Para HTML standalone es libre.
- No metas localStorage/sessionStorage en artifacts que corran en sandbox (no soportado) — usa variables JS en memoria.
- No dejes nodos decorativos que simulen ser clickeables.
- Si no tenés la URL de un nodo, déjalo con un placeholder claramente marcado `[pendiente: URL]` y no-clickeable, en vez de un link muerto.
