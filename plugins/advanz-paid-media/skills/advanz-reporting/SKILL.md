---
name: advanz-reporting
description: >-
  Genera reportes de performance para clientes de Advanz (ecommerce DTC/B2C) en HTML branded, listos para
  compartir. Es un ROUTER POR CANAL: el usuario dice el canal y la skill arma ese reporte. Canales:
  (1) PAID / Negocio — Meta, Google, Shopify, GA4, competencia (módulo base, references/estructura.md +
  references/datos.md); (2) CORREO / EMAIL — Klaviyo, campañas + flujos, captación (references/email.md);
  (3) SEO / GEO — en construcción (references/seo.md). Usa SIEMPRE que el usuario diga "reporte de paid",
  "reporte de correo/email", "reporte de SEO", "reporte de cierre de mes", "reporte de performance",
  "cierre de [cliente]", "reporte mensual", "reporte de [evento/campaña]", "armá el reporte", "quiero la
  data de paid/correo/seo", o pegue una matriz/planilla y pida un reporte. Cubre cierres mensuales y
  reportes de evento/campaña. SOLO ecommerce DTC/B2C. Es marca-agnóstica: el motor y el estándar no cambian,
  cambia el mapa de cuentas del cliente. Amazing Care (amazingcare.cl) es el primer caso validado.
metadata:
  type: reporting
---

# Advanz Reporting — Reportes de performance por canal

Motor estándar para producir el **reporte de performance que Advanz comparte con el cliente**. Funciona como
**router**: preguntá (o detectá) el canal y andá al módulo. El **estándar de tono, diseño y entrega es común**
a todos los canales; lo que cambia es la data y la estructura de cada uno.

## Paso 0 — Elegí el canal
| Si el usuario pide… | Canal | Módulo |
|---|---|---|
| "reporte de **paid**", "cierre de mes" completo, Meta/Google/Shopify/negocio | **Paid / Negocio** | `references/estructura.md` + `references/datos.md` |
| "reporte de **correo**/email", Klaviyo, campañas, flujos, captación | **Correo / Email** | `references/email.md` |
| "reporte de **SEO**/GEO", orgánico, rankings, citas en LLMs | **SEO / GEO** | `references/seo.md` *(en construcción)* |

Si el cliente no tiene mapa de cuentas aún, levantá los IDs del canal y guardalos en memoria como
`<cliente>_account_map` antes de armar.

## Estándar común (todos los canales)
Antes de escribir una línea, internalizá esto — vale para paid, correo y SEO:

- **Marco neutral-growth.** NUNCA asumir resultados buenos ni malos, NUNCA echar culpas. Cada dato =
  **hecho objetivo + señal + próximo paso**. Prohibido "mejor mes", "fuerte", "rentable", "el problema es".
  Detalle y glosario en `references/tono-voz.md`.
- **Español neutro, sin tecnicismos.** Sin voseo ni chilenismos. Traducí la jerga a negocio (ROAS→"retorno",
  CPA→"costo por venta", CTOR→"clics sobre apertura", etc.). Ver `references/tono-voz.md`.
- **Conclusiones con color + acción bifurcada.** Toda conclusión se presenta como una **caja de color**
  (verde=positivo / rojo=negativo / violeta=neutral) con: *qué pasó* + el ajuste dividido en
  **🏢 Advanz ejecuta …** y **🤝 Cliente ejecuta …**. Máximo 2 líneas por caja; si hay más de una idea,
  separá en cajas. Usá emojis para escanear.
- **Métricas primero, texto en box.** El bloque de apertura son KPIs bien espaciados (positivo/negativo por
  color), y la tesis va en una **caja destacada**, no en prosa suelta.
- **Gráficos, no listas.** El cliente decide mirando gráficos: torta o **barras por tipo** (cuando importa
  el ranking, no sólo el mix), barras de tendencia mes a mes y año contra año (que aparezca el año en curso),
  **cohorte horario** (franja en las filas / día en las columnas, mapa de calor **sutil**), embudo real,
  **velocímetro** de meta (`speedo`, aguja + zona verde). Todo gráfico lleva **números visibles** (en CLP
  completo, no "1366k") y **hover** (tooltip). Las tablas usan **heatmap sutil** (`hmt`): se colorea el
  número (verde=fuerte / rojo=débil), **sin banda de fondo** — la métrica toma relevancia, no el color.
- **Simple y escaneable.** Tesis/titular arriba (5 segundos), datos en tiles/tablas/charts, reads de 1–2
  frases, postura en los próximos pasos. Pirámide invertida.

Regla de proceso: **mostrá el borrador para validación antes de dar por final. Iterá en el chat; recién ahí
guardás.**

## Design system y entrega (común)
- **Marca Advanz:** Poppins (texto) + Space Grotesk (títulos/números); violeta `#7b2ff7`→`#c15dff`, cyan
  `#22d3ee`, fondo `#f6f4fb`. Paleta categórica CVD-safe validada: evento `#7b2ff7`, producto `#0e9bc9`,
  contenido `#e8850c`, retail `#2563eb`, marca `#d83a7d`. Verde/rojo solo para chips de variación.
- **Charts + tooltip + heatmap:** usá `assets/report_charts.py` (gráficos SVG con hover ya hechos: donut,
  barras apiladas, cohorte horario —franja×día—, velocímetro `speedo` y gauge, embudo real de trapecios,
  barras horizontales `hbars`, `hmt` para heatmap sutil de tabla y `heatcell` para grillas densas).
  Base y componentes en `assets/plantilla.html` y `references/design-system.md`.
- **Título:** que se lea el canal en grande (ej. píldora "📧 Email Marketing · Cierre mensual").
- **HTML branded autocontenido:** imágenes embebidas en base64 cuando se pueda; si el sandbox bloquea el
  CDN, referenciá la URL y avisalo (el archivo se ve al abrirlo online). **Nombre de salida: `cliente-canal-mes`**
  (minúsculas, sin fecha; ej. `amazing-email-agosto.html`, `amazing-paid-agosto.html`, `amazing-seo-agosto.html`).
  Guardado **local** en `empresa/clientes/<cliente>/reportes/`, con una copia `-FINAL` al aprobar. **NO**
  publicar como Artifact salvo para preview de validación.
- **Entrega en Notion:** el reporte se **incrusta** en la página de cierre del cliente
  (`Clientes / <cliente> / Reportes Mensuales / <año> / <mes>`), junto al de los otros canales. Se sube el
  `.html` como archivo adjunto (`notion-create-file-upload`); si el entorno no puede subir, se inserta un
  **resumen nativo** con `notion-update-page` y se deja el HTML para adjuntar a mano. Ver `references/email.md`.

## Reglas de datos (común)
- **Método consistente por canal.** No mezclar ventanas de atribución dentro de un mismo número. En correo,
  el estándar del equipo es **send-time** (fecha de envío) con **RPR = ventas ÷ destinatarios** — coincide
  con la grilla de correos. Detalle por canal en su módulo.
- **La matriz manda** para el titular financiero cuando existe (paid). El correo/SEO **"influyen"**, no se
  suman a la venta total (se solapan con otros canales).
- Traé la data en paralelo (MCPs). Qué sale de dónde, por canal, en el módulo correspondiente.

## Gotchas transversales
- Atribución que se solapa (email/SEO) → "influyó en $X", nunca sumado.
- Meta suele estar en USD ≠ CLP; convertir y avisar.
- Search Console hoy no está por MCP → SEO se mide con GA4/Ahrefs/Semrush (ver `references/seo.md`).
- Si un CDN de imágenes está bloqueado por el sandbox, referenciar la URL y dejar el script de embebido para
  correr desde una máquina con acceso.
