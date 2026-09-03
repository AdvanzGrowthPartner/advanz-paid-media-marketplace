# Conectar el MCP de Shopify (+ fuentes de paid opcionales)

## Shopify (obligatorio)
1. En Claude (escritorio / Code): **Configuración → Conectores → Shopify** (o `claude mcp add shopify`).
2. Autorizar con la cuenta **dueña de la tienda**. Permisos de **solo lectura**: pedidos,
   productos, analytics.
3. Confirmar la conexión: `get-shop-info` → devuelve nombre, dominio `.myshopify.com`,
   **moneda** y timezone. Anotar la moneda (se usa para no mezclarla con el gasto de paid).

## COGS — requisito para leer margen
- El margen real necesita el **cost per item** cargado en Shopify (Productos → variante →
  campo **Costo**). Con eso, `gross_profit` de ShopifyQL trae la ganancia bruta.
- Sin costo cargado, el reporte sale **sin margen y lo avisa**. No se estima. Ese es, de
  hecho, el primer hallazgo del diagnóstico: no se puede leer rentabilidad sin costos.
- Verificación rápida del costo por variante: `graphql_query` →
  `productVariants { ... inventoryItem { unitCost { amount } } }`.

## Fuentes de paid (opcionales — para cruzar el ROAS de equilibrio)
- **Meta Ads / Google Ads / GA4** por sus MCP respectivos: dan el ROAS/MER real que se cruza
  contra el breakeven calculado desde el margen. Sin ellas, se entrega el ROAS de equilibrio
  y se pide el ROAS real al dueño.
- Regla de moneda: convertir el gasto de paid a la moneda de la tienda antes de cruzar.

## Salud de los datos (se reporta siempre)
Registrar qué quedó conectado (Shopify / GA4 / Meta / Google), la cobertura de COGS y la
ventana usada. Todo lo que no se pudo leer va como **"no verificado"**, con el motivo.
