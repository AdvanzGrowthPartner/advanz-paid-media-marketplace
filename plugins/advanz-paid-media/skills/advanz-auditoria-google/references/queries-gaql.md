# Set de consultas GAQL (recolección reproducible por área)

Corre estas contra el MCP de Google Ads (`search_search`). Una corrida = una auditoría.
Ventanas: performance ≥30d; términos de búsqueda `LAST_30_DAYS`; producto/PMax ≥60–90d.
Costos vienen en **micros** → dividir por 1.000.000. Respetar `../ads/references/gaql-notes.md`.

> Validado en cuenta real (2026-09). Ajustar nombres de campos si la API cambia; usar
> `metadata_get_resource_metadata` ante duda, nunca adivinar campos.

## 1 · Estructura + performance por campaña
- resource: `campaign`
- fields: campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type,
  campaign.bidding_strategy_type, metrics.cost_micros, metrics.conversions,
  metrics.conversions_value, metrics.clicks, metrics.impressions, metrics.average_cpc, metrics.ctr
- conditions: `segments.date DURING LAST_30_DAYS`, `campaign.status != 'REMOVED'`
- order: metrics.cost_micros DESC

## 2 · Impression share (solo Search, query aparte — incompatibilidades)
- resource: `campaign`
- fields: campaign.name, metrics.search_impression_share,
  metrics.search_budget_lost_impression_share, metrics.search_rank_lost_impression_share, metrics.cost_micros
- conditions: `segments.date DURING LAST_30_DAYS`, `campaign.advertising_channel_type = 'SEARCH'`,
  `campaign.status = 'ENABLED'`

## 3 · Términos de búsqueda (wasted spend)
- resource: `search_term_view`
- fields: search_term_view.search_term, campaign.name, metrics.cost_micros,
  metrics.conversions, metrics.clicks, metrics.conversions_value
- conditions: `segments.date DURING LAST_30_DAYS`, `metrics.cost_micros > 0`
- order: metrics.cost_micros DESC · limit 100
- **Nota:** `search_term_view` NO admite `campaign.status`/`ad_group.status` → filtrar en app.
  "Wasted" solo si >umbral de gasto y 0 conv (ver anti-error).

## 4 · Keywords + Quality Score
- resource: `keyword_view`
- fields: ad_group_criterion.keyword.text, ad_group_criterion.keyword.match_type,
  ad_group_criterion.quality_info.quality_score,
  ad_group_criterion.quality_info.creative_quality_score,
  ad_group_criterion.quality_info.post_click_quality_score,
  ad_group_criterion.quality_info.search_predicted_ctr,
  campaign.name, ad_group.name, metrics.cost_micros, metrics.conversions, metrics.impressions, metrics.clicks
- conditions: `segments.date DURING LAST_30_DAYS`, `campaign.status = 'ENABLED'`, `ad_group.status = 'ENABLED'`
- **Dedup** por (ad_group + texto + match_type); agregar métricas.

## 5 · Anuncios (RSA: ad strength, tipo, estado)
- resource: `ad_group_ad`
- fields: campaign.name, ad_group.name, ad_group_ad.ad.type, ad_group_ad.ad_strength, ad_group_ad.status
- conditions: `campaign.status = 'ENABLED'`, `ad_group_ad.status = 'ENABLED'`
- Para contar titulares/descripciones: ad_group_ad.ad.responsive_search_ad.headlines / .descriptions

## 6 · Extensiones / assets a nivel campaña
- resource: `campaign_asset`
- fields: campaign.name, campaign_asset.field_type, asset.type, campaign_asset.status
- conditions: `campaign.status = 'ENABLED'`, `campaign_asset.status = 'ENABLED'`
- (contar sitelinks, callouts, structured snippets, imágenes por campaña)

## 7 · PMax asset groups (densidad de assets)
- resource: `asset_group`  → fields: asset_group.name, asset_group.status, campaign.name, asset_group.ad_strength
- resource: `asset_group_asset` → fields: asset_group.name, asset_group_asset.field_type, asset.type
  (contar imágenes/logos/videos por grupo)

## 8 · Presupuestos
- resource: `campaign_budget`
- fields: campaign_budget.name, campaign_budget.amount_micros,
  campaign_budget.has_recommended_budget, campaign_budget.recommended_budget_amount_micros

## 9 · Conversiones (tracking)
- resource: `conversion_action`
- fields: conversion_action.name, conversion_action.category, conversion_action.status,
  conversion_action.type, conversion_action.primary_for_goal, conversion_action.counting_type
- conditions: `conversion_action.status = 'ENABLED'`
- (chequear: 1 primaria macro; no doble conteo de PURCHASE; ATC/micro como secundarias)

## 10 · Productos / feed (PMax + Shopping)
- resource: `shopping_performance_view`
- fields: segments.product_title, segments.product_item_id, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value, metrics.clicks
- conditions: `segments.date DURING LAST_30_DAYS` (idealmente 60–90d), `metrics.cost_micros > 0`
- order: metrics.cost_micros DESC · limit 50
- **Nota:** a 30d la atribución por producto viene fraccionada → marcar "a revisar".

## Fuera del MCP de Google Ads (marcar "no verificado" si no hay fuente)
- **Enhanced conversions / consent mode:** requiere auditoría de tag/GTM.
- **GMC diagnósticos y desaprobaciones de feed:** requiere Merchant Center (o Shopify MCP).
- **Discrepancia Google vs GA4 vs Shopify:** requiere analytics-mcp (GA4) y/o Shopify MCP.
- **Landing (velocidad/relevancia):** requiere acceso a la URL (`../ads/scripts/analyze_landing.py`).
