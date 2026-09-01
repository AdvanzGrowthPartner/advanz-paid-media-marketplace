# Módulo SEO / GEO — reporte de performance orgánico (EN CONSTRUCCIÓN)

> Estado: **placeholder**. La estructura y las fuentes se definen cuando se arme el primer cierre de SEO.
> Mientras tanto, si el usuario pide "reporte de SEO", avisá que el módulo está en construcción y ofrecé
> armar una primera versión con las fuentes de abajo.

Mismo **estándar común** que el resto (ver `SKILL.md`): tono neutral-growth, español neutro, métricas primero,
conclusiones con color + Advanz/Cliente ejecuta, gráficos con hover, tablas con heatmap, HTML branded Advanz,
entrega local + embed en Notion.

## Estructura prevista (borrador)
1. **Resultados del mes** — tráfico orgánico, clics, impresiones, posición media, conversiones/ventas
   influidas; MoM y YoY.
2. **Cómo venimos** — tendencia de tráfico e ingresos orgánicos últimos meses + año contra año.
3. **Visibilidad clásica (Google)** — keywords en top 3/10, ganadas/perdidas, páginas que traen tráfico,
   share of voice vs. competencia.
4. **GEO (citas en LLMs)** — presencia/citas en ChatGPT/Claude/Gemini/Perplexity, AI Overviews, AI citation
   score (ver skill `advanz-seo-geo-engine`).
5. **Contenido y páginas** — qué entró, qué rankea, oportunidades de cluster/pillar.
6. **Técnico y autoridad** — Core Web Vitals, indexación, schema, backlinks/refdomains.
7. **Próximos pasos & proyección** — bloques ilustrados.

## Fuentes previstas (MCP)
- **Ahrefs** (`site-explorer-*`, `keywords-explorer-*`, `rank-tracker-*`, `site-audit-*`, `brand-radar-*`
  para GEO) — valores monetarios en centavos USD (÷100).
- **Semrush** (`domain_overview`, `organic_research`, `position_tracking`, `backlinks_research`,
  `traffic_overview`).
- **GA4** — sesiones/keyEvents de `sessionDefaultChannelGroup` (orgánico) como proxy mientras no haya Search
  Console por MCP.
- Cruce con **paid** (marca vs genérico) y con el motor `advanz-seo-geo-engine` (framework de 7 capas).

## Reglas
- SEO **influye**, no se suma a la venta total (se solapa con paid/directo).
- Search Console no está por MCP hoy → dejar anotado como pendiente; medir orgánico con GA4 + Ahrefs/Semrush.
- Reutilizar `assets/report_charts.py` para los gráficos.
