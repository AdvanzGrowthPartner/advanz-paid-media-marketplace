# Módulo SEO / GEO — reporte de performance orgánico

Reporte del canal orgánico. Dos frentes que se leen juntos pero se miden distinto: **SEO clásico**
(Google: clics, posiciones, páginas) y **GEO** (presencia y citas en respuestas de IA: ChatGPT, Claude,
Gemini, Perplexity, AI Overviews). Estándar común (tono, diseño, entrega, handoff) en `SKILL.md`.

## Antes de arrancar
1. **Tipo:** cierre de mes o auditoría/lanzamiento de cluster.
2. **Mapa de cuentas del cliente** (ver §Fuentes): dominio, proyecto de rank-tracker, propiedad de Search
   Console conectada en Ahrefs, competidores de referencia.
3. **Método:** el orgánico **influye**, no se suma a la venta total (se solapa con paid/directo). Las ventas
   se reportan como **"influyó en $X"**. Ventana y fuente consistentes (ver §Gotchas).

## Los dos frentes (no mezclar)
- **SEO clásico (Google):** clics/impresiones/posición de Search Console, keywords en top 3/10, páginas que
  traen tráfico, share of voice vs. competencia. Es demanda que ya existe y busca en Google.
- **GEO (citas en LLMs):** cuántas veces la marca aparece **citada** o **mencionada** en respuestas de IA y
  AI Overviews, y con qué share vs. competencia. Es la nueva capa de descubrimiento; se mide con brand-radar.

## Estructura del reporte (8 bloques)
Misma forma accionable que los otros canales: **KPIs primero → caja de tesis → gráficos, no listas →
conclusiones con color + Advanz/Cliente → próximos pasos → proyección al final**.
1. **Resultados del mes** — KPIs (bien espaciados): **clics orgánicos**, impresiones, **posición media**,
   keywords en **top 3 / top 10**, **ventas influidas** (orgánico), y un KPI GEO (**citas en IA** o AI SoV).
   MoM y YoY. Después la **caja de tesis**.
2. **Cómo venimos** — barras de **clics/tráfico orgánico últimos 6–12 meses** (Search Console) + **año contra
   año** (mismo mes). Conclusiones con color + Advanz/Cliente.
3. **Visibilidad clásica (Google)** — **distribución por posición** (top 3 / 4–10 / 11–20 / 20+, barras
   apiladas o cohorte), **keywords ganadas vs. perdidas**, **share of voice vs. competencia** (velocímetro o
   gauge), y **tabla de páginas que traen tráfico** (clics, impresiones, CTR, posición — heatmap sutil `hmt`).
4. **GEO — citas en respuestas de IA** — **share of voice en IA vs. competencia** (velocímetro), tendencia de
   **menciones/citas**, y **tabla de prompts/temas** donde la marca aparece o no (heatmap sutil). Cruzar con
   el motor `advanz-seo-geo-engine` (framework de capas).
5. **Contenido y páginas** — qué rankea, **quick wins** (keywords en **posición 5–15 con volumen**: mover a
   top 3 es el mayor retorno por esfuerzo) en **barras horizontales** (`hbars`), y oportunidades de
   cluster/pillar. Es el equivalente al "qué vendió cada uno" del email: vista de **decisión** por página.
6. **Técnico y autoridad** — **salud del sitio** (site-audit: errores/warnings, Core Web Vitals,
   indexación, schema) y **autoridad** (backlinks / dominios de referencia y su tendencia). Tabla con
   heatmap sutil.
7. **Próximos pasos** — dos columnas **🤝 Cliente** (prioridad comercial, aprobación de contenidos, fichas de
   producto, decisiones de marca) y **🏢 Advanz** (briefs de contenido, on-page, técnico, linkbuilding,
   GEO) + un bloque de **ejecución inmediata Advanz→Cliente** cuyos ítems salen de los gráficos (quick wins,
   páginas que caen, errores técnicos que frenan).
8. **Proyección — AL FINAL, sección propia.** Tráfico/keywords proyectados al capturar los quick wins del
   bloque 5 (base vs. óptimo), con la base del cálculo.

## Taxonomía de keywords/páginas (para categorizar y colorear)
Agrupá la demanda por **intención** (macro-categoría, igual que los tipos de correo en email):
- **Marca** — el nombre del cliente y variantes. Alta conversión, bajo esfuerzo; controlar que se capture ~100%.
- **Categoría / genérico** — términos de producto sin marca (mayor volumen, más competido; ahí está el crecimiento).
- **Informativo / educativo** — preguntas y "cómo/qué es" (TOFU; alimenta GEO y el cluster de contenido).
- **Transaccional / comparativo** — "comprar", "precio", "mejor X" (cierre; alta prioridad comercial).
- **Retail / marketplace** — términos que derivan a Jumbo/MercadoLibre, no a la web (leerlos aparte).

Levantá los grupos reales del cliente desde el rank-tracker; las macro pueden variar, el motor no.

## Fuentes (MCP) — método consistente
| Dato | Herramienta | Notas |
|---|---|---|
| Clics, impresiones, CTR, posición (Google real) | **Ahrefs `gsc-*`** (`gsc-performance-history`, `gsc-keywords`, `gsc-pages`, `gsc-ctr-by-position`, `gsc-performance-by-device`, `gsc-metrics-by-country`) | Search Console vía Ahrefs — es la fuente de verdad del tráfico orgánico. Requiere la propiedad GSC conectada en Ahrefs. |
| Keywords orgánicas, top 3/10, ganadas/perdidas | **Ahrefs `site-explorer-organic-keywords`**, `site-explorer-keywords-history`, `rank-tracker-overview` | Posiciones y evolución. Para el share of voice: `rank-tracker-competitors-*`. |
| Páginas por tráfico | **Ahrefs `site-explorer-top-pages`** / `site-explorer-pages-by-traffic` | Tabla de páginas que traen tráfico. |
| Volumen / dificultad de keyword | **Ahrefs `keywords-explorer-overview`**, `keywords-explorer-matching-terms`, `keywords-explorer-volume-history` | Para dimensionar quick wins y oportunidades. |
| Salud técnica | **Ahrefs `site-audit-issues`**, `site-audit-page-explorer` | Errores/warnings, indexación, schema. Core Web Vitals: site-audit / PageSpeed. |
| Autoridad / backlinks | **Ahrefs `site-explorer-domain-rating`**, `site-explorer-referring-domains`, `site-explorer-refdomains-history`, `site-explorer-backlinks-stats` | DR y dominios de referencia + tendencia. |
| **GEO — citas en IA** | **Ahrefs `brand-radar-*`** (`brand-radar-sov-overview`, `brand-radar-mentions-history`, `brand-radar-citations-overview-entities`, `brand-radar-cited-pages`, `brand-radar-ai-responses`) | Share of voice, menciones y citas en respuestas de IA + AI Overviews. Es el frente GEO. |
| Cruce competitivo / tráfico estimado | **Semrush** (`domain_overview`, `organic_research`, `position_tracking`, `backlinks_research`, `traffic_overview`) | Segunda fuente para SoV y competencia; útil cuando falta GSC. |
| Orgánico → sesiones/keyEvents (proxy) | **GA4** (si está conectado) | `sessionDefaultChannelGroup` = Organic Search, con sessions + keyEvents, para atar orgánico a conversión/venta influida. |

**Monetario en Ahrefs:** los valores vienen en **centavos USD** → dividir por 100; convertir a CLP y avisarlo.

## Métricas y fórmulas
- **CTR** = clics ÷ impresiones. **Posición media** = promedio ponderado por impresiones (Search Console ya lo da).
- **Quick win** = keyword con **volumen relevante** en **posición 5–15**: el mayor retorno por esfuerzo
  (subir de página 2 / pie de página 1 a top 3).
- **Share of voice (clásico)** = tu visibilidad ÷ visibilidad del set competitivo (rank-tracker).
- **AI SoV (GEO)** = citas/menciones de la marca ÷ total del set en respuestas de IA (brand-radar).
- **Ventas influidas** = conversión orgánica de GA4 × ticket, o atribución de la tienda para el canal orgánico.

## Gotchas de medición
- **Orgánico influye, no suma:** presentá "influyó en $X", nunca sumado a la venta total del negocio.
- **GSC vs. Ahrefs/Semrush:** Search Console (vía `gsc-*`) es el dato real de Google del sitio; Ahrefs/Semrush
  estiman. Para el titular usá GSC; Ahrefs/Semrush para competencia y oportunidad. No mezclar en un mismo número.
- **GEO es joven y ruidoso:** las citas en IA varían por prompt y por corrida. Reportá **tendencia y share**,
  no un número absoluto puntual; fijá el set de prompts/temas del mes y mantenelo entre cierres.
- **Estacionalidad:** el orgánico también estaciona (búsquedas de septiembre, eventos). Leé el YoY, no solo el MoM.
- **Ventana consistente:** misma ventana de fechas en GSC, rank-tracker y brand-radar dentro de un mismo número.

## Entrega
Nombre de salida: **`cliente-seo-mes`** (ej. `amazing-seo-agosto.html`). Preview de validación (Artifact),
`-FINAL` local + embed en Notion, y el **sidecar `cliente-seo-mes.acciones.json`** con el handoff
(ver `references/handoff.md`).
