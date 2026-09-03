# Consultas por área (ShopifyQL + GraphQL)

Set reproducible que corre el motor. ShopifyQL vía `run-analytics-query`; el fallback de
costo por variante vía `graphql_query`. Ventana por defecto: `last_90_days`.

> **Regla:** cada número del reporte sale de una de estas consultas. Si una consulta vuelve
> vacía (típico `gross_profit` sin COGS), se declara "no verificado" — no se rellena.

## 1 · Foto general
```
FROM sales
SHOW total_sales, net_sales, orders, average_order_value
DURING last_90_days
```

## 2 · Margen por producto (el corazón)
```
FROM sales
SHOW net_sales, net_items_sold, gross_profit
GROUP BY product_title
DURING last_90_days
ORDER BY net_items_sold DESC
```
- Margen % = `gross_profit` ÷ `net_sales` por fila.
- Si `gross_profit` viene vacío/0 para TODAS las filas → COGS no cargado (Paso: fallback 2b).

### 2b · Fallback de costo por variante (GraphQL) — cuando falta COGS en ShopifyQL
```graphql
{
  productVariants(first: 100) {
    edges {
      node {
        sku
        displayName
        price
        inventoryItem { unitCost { amount currencyCode } }
      }
    }
  }
}
```
- Si `unitCost` es null en la mayoría → confirmar con el dueño que el costo no está cargado.
  Ese es el **primer hallazgo**: no se puede leer rentabilidad sin costos.

## 3 · Recompra / clientes nuevos vs recurrentes
```
FROM sales
SHOW total_sales, orders
GROUP BY customer_type
DURING last_90_days
```
- `customer_type` = first-time vs returning. % recurrente = ventas returning ÷ total.

## 4 · Descuentos por producto
```
FROM sales
SHOW gross_sales, total_discounts, net_sales
GROUP BY product_title
DURING last_90_days
ORDER BY total_discounts DESC
```
- Descuento % = `total_discounts` ÷ `gross_sales`. Cruzar contra el margen del producto.

## 5 · Tendencia de margen (opcional, salud del negocio)
```
FROM sales
SHOW net_sales, gross_profit
TIMESERIES month
SINCE -6m UNTIL today
```
- Margen % mes a mes: detecta erosión de margen que el ROAS esconde.

## 6 · Concentración / mix
- Reusar la salida de la consulta 2 ordenada por `net_sales DESC`: calcular qué % del margen
  total aporta el top 3 de SKUs (Pareto).

## Notas de compatibilidad
- Campos de la familia `sales`: `total_sales`, `net_sales`, `gross_sales`, `orders`,
  `net_items_sold`, `gross_profit`, `total_discounts`, `average_order_value`. Dimensiones
  útiles: `product_title`, `customer_type`, `sales_channel`, `billing_region`.
- `gross_profit` requiere **cost per item** cargado; refleja el costo al momento de la venta.
- No mezclar la moneda de la tienda con la del gasto de paid: convertir antes de cruzar ROAS.
- Devoluciones: si `returns`/`returned_items` no está disponible en el MCP conectado, marcar
  el bloque de devoluciones como "no verificado".
- Ventanas: `last_90_days`, `last_30_days`, o `SINCE -Nd UNTIL today`. Para tiendas nuevas,
  usar el máximo disponible y declararlo.
