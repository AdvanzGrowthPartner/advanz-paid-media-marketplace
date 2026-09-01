# Fuentes de datos, cómo cruzarlas y gotchas

## Qué sale de dónde
| Dato | Fuente (MCP) | Notas |
|---|---|---|
| Inversión y **conversiones por canal**, venta neta, ticket, CAC, ROAS/aMer | **Matriz** (la pasa el cliente/Matias) | Fuente de verdad del titular financiero. No armar sin ella. |
| Ventas, funnel, productos, nuevos vs recurrentes, códigos de descuento | **Shopify** (`run-analytics-query` ShopifyQL; `graphql_query` para fotos de producto) | Tienda. Last-click. |
| Email: campañas + flujos + KPIs | **Klaviyo** | `get_campaign_report` (campañas), `query_metric_aggregates` por `$attributed_channel`/`$attributed_flow` (total email / flujos). Métrica compra = "Placed Order". |
| Orgánico / canales / intención (proxy SEO) | **GA4** (`analytics-mcp run_report`) | `sessionDefaultChannelGroup` con sessions + keyEvents. |
| Campañas, impression share, CPC, RSAs | **Google Ads** (`search_search`) | `campaign` con metrics.* + `metrics.search_impression_share`. cost_micros ÷ 1e6. |
| Alcance, frecuencia, CTR, CPC, video, ROAS por campaña/anuncio, miniaturas | **Meta Ads** (`ads_get_ad_entities`, `ads_get_creatives`) | Verificá campos con `ads_get_field_context`. Requiere `client_conversation_id` (20 chars). |
| Volumen de anuncios activos vs. competencia | **Meta Ad Library** (`ads_library_search`) | Para la sección de fatiga/volumen. |

Traé todo en paralelo. Ver también memorias: [[amazing_account_map]], [[meta_ads_mcp]], [[google_ads_mcp_setup]],
[[ga4_mcp_setup]], [[meta_ads_mcp]].

## Cómo cruzar (regla de oro)
- **Conversiones Google/Meta = matriz.** El resto de KPIs (ROAS/CTR/CPC/alcance/impression share por campaña
  y anuncio) = lo que indiquen las plataformas.
- **Venta neta / órdenes / ticket = matriz** para el titular. Shopify solo para el detalle operativo.
- Si matriz y Shopify divergen, la matriz manda y se anota la diferencia; no se esconde ni se fuerza a cuadrar.

## Gotchas de medición (validar SIEMPRE)
- **Matriz vs Shopify divergen**: Shopify es last-click; la matriz está reconciliada por el equipo. Números
  distintos es normal — usar matriz para lo financiero.
- **Email (Klaviyo) se solapa**: su atribución cuenta compras que también pueden estar en paid/orgánico.
  Presentar como **"influyó en $X"**, nunca sumado a la venta total.
- **Meta suele estar en USD** (≠ CLP de la tienda). Convertir a CLP (FX ≈ 1.000 salvo dato mejor) y avisarlo.
- **Meta in-platform ≠ matriz**: las compras que reporta Meta (pixel, ventana propia) son más que la
  atribución last-click. En creativos/campañas usar métricas de plataforma y aclarar "in-platform".
- **Search Console**: hoy no disponible por MCP → SEO se mide con GA4 (orgánico); dejarlo como pendiente.
- **Campaña de alcance/awareness** (objetivo reach): no aparece en el ROAS de conversión por diseño; su
  impacto es de marca/retail, no de venta web. Leerla aparte.
- **Cálculos que se derivan** (para chequear una lectura de matriz): CPA canal = inversión ÷ conversiones;
  ticket = venta neta ÷ órdenes; CAC = inversión total ÷ órdenes. Sirve para validar la matriz si la imagen
  no se lee bien.

## Mapa de cuentas — Amazing Care (caso validado)
- **Shopify**: amazingcare.cl (`25trtw-d5.myshopify.com`), CLP.
- **Meta Ads DTC**: `2911300959169889` (USD). Mayorista: `3131920510317594` (CLP).
- **Google Ads DTC**: `8800950215` (CLP). MCC Advanz: `5816304092`.
- **GA4**: property `354353475` (en USD por decisión; usar para share/canales, no revenue en CLP).
- **Klaviyo**: métrica "Placed Order" id `RP5iQ9`.
- Competidor de referencia (Ad Library / SEO): **Extra Life**.

Para un cliente nuevo: levantar estos IDs, guardarlos en memoria como `<cliente>_account_map`, y recién armar.
