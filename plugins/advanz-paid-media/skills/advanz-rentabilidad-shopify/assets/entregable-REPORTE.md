# Entregable · REPORTE — Reporte 360 de Rentabilidad Shopify (Capa 2)

Es lo que se le entrega al prospecto cuando comenta **REPORTE**. Se pega en un chat con el
**MCP de Shopify conectado a su tienda**. Nada se inventa: cada número sale de una consulta.

> **Versión:** v1.0 · 2026-09-03. **Requiere:** MCP de Shopify (solo lectura) + *cost per
> item* cargado para ver margen. **Nunca PDF** — se entrega el prompt en bloque copiable.

---

```
# REPORTE 360 DE RENTABILIDAD — Shopify + IA (Método Advanz)

ROL: Eres analista de rentabilidad ecommerce de Advanz. Tienes el MCP de Shopify
conectado a MI tienda. Tu trabajo NO es opinar: es leer datos reales y mostrarme
donde se esta fugando la plata. Idioma: espanol neutro. Tono directo, sin hype.

REGLA DE ORO: nada se inventa. Cada numero sale de una consulta al MCP. Si un dato
no esta cargado (tipico: el costo por producto / COGS), NO lo estimes: marcalo como
"falta cargar" y sigue. Un margen inventado es peor que un margen faltante.

QUE QUIERO (ultimos 90 dias, corre las consultas y arma el reporte):

1. FOTO GENERAL - ShopifyQL:
   FROM sales SHOW total_sales, net_sales, orders, average_order_value DURING last_90_days
   -> ventas totales, netas, pedidos y AOV.

2. MARGEN POR PRODUCTO (el corazon) - ShopifyQL:
   FROM sales SHOW net_sales, net_items_sold, gross_profit
   GROUP BY product_title DURING last_90_days ORDER BY net_items_sold DESC
   -> tabla por producto: unidades, ventas netas, ganancia bruta y % de margen
   (gross_profit / net_sales). Ordenala por unidades vendidas.
   * Si gross_profit viene vacio, el COGS no esta cargado: dilo y pide cargar
     "cost per item" en Shopify (o consulta InventoryItem.unitCost por GraphQL).

3. EL HALLAZGO: cruza volumen vs margen. Marca en rojo el producto que esta en el
   top de unidades pero en el fondo de margen. Esa es la fuga: capital de pauta
   escalando el producto que menos deja.

4. RECOMPRA - ShopifyQL:
   FROM sales SHOW total_sales GROUP BY customer_type DURING last_90_days
   -> % de ventas de clientes nuevos vs recurrentes (salud del LTV).

5. PUNTO DE FUGA EXTRA: el producto con mas devoluciones o descuento promedio mas
   alto que le come el margen (si el dato esta disponible).

FORMATO DE SALIDA:
- Resumen en 3 frases: que vende, de que vive el margen, donde se fuga la plata.
- Tabla de productos (unidades . ventas . margen %) con el hallazgo en rojo.
- 1 frase de tesis: "Tu #1 en ventas es el #N en margen".
- Cierre: los 2 movimientos concretos (que producto conviene empujar en pauta y
  cual revisar de precio/costo). Sin precios de servicio, sin vender: solo el dato.

Ejecuta las consultas ahora y entregame el reporte.
```

---

## Notas internas (no van en cámara ni al prospecto)
- **Origen:** SOP Ecomm IA + SOPs Diagnóstico Productos Ecommerce + calculadora de Unit Economics.
- **Falso positivo cero:** sin COGS cargado el prompt lo declara; nunca inventa margen.
- **Trazabilidad:** cada cifra sale de una consulta ShopifyQL nombrada.
- **Pendiente de validación:** correr en 5 tiendas reales (hit rate ≥ 4/5) antes de marcarlo validado.
- **Ficha de contenido asociada:** R2 · "Tu producto más vendido es el que menos plata te deja".
