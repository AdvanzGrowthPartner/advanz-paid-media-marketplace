# Checklist de rentabilidad — cobertura y criterio

Cada área se evalúa **pass / warning / fail** con umbral, no con opinión. El umbral exacto
se calibra por vertical, pero estos son los cortes de referencia. Ninguna área se omite: si
falta el dato, es **"no verificado"** con motivo.

## 1 · Foto general
- [ ] Ventas netas, pedidos y AOV de los últimos 90 días (dato base para todo lo demás).
- [ ] AOV vs. costo de adquisición esperado: si el AOV no cubre CAC × (1/margen), hay techo.
- **fail** si no se puede leer ventas netas (tienda sin ventas en la ventana → decirlo).

## 2 · Margen por producto (el corazón)
- [ ] COGS cargado en todas las variantes con ventas. **Cobertura de COGS = variantes con
  costo / variantes con ventas.** <80% ⇒ warning; 0% ⇒ fail (no hay margen que leer).
- [ ] Margen de contribución % por producto = (ventas netas − COGS) / ventas netas.
- [ ] Ranking de productos por margen $ total y por margen %.
- **warning** si el margen promedio ponderado < 40% (referencia DTC; ajustar por vertical).
- **fail (dato)** si `gross_profit` viene vacío para todo → COGS ausente, no margen 0.

## 3 · Volumen vs margen — el producto-fuga
- [ ] Cruzar ranking de unidades vs ranking de margen %.
- [ ] **Producto-fuga** = está en el top 20% de unidades **y** en el bottom 40% de margen,
  con ventas > umbral relevante (no un SKU marginal). Ese es el hallazgo ancla.
- **fail** (acción) si el producto nº1 en unidades está bajo el margen de equilibrio.

## 4 · ROAS de equilibrio (breakeven)
- [ ] Breakeven de contribución = 1 ÷ margen de contribución %. (margen 40% → 2,5x).
- [ ] MER objetivo = breakeven que además cubre costos fijos + utilidad (típico 3–4x).
- [ ] Cruzar contra el ROAS/MER real de paid (si hay GA4/Meta/Google): cada campaña gana o
  pierde según esté sobre o bajo el breakeven — **no según el número absoluto**.
- **warning** si el ROAS real está en zona gris (±10% del breakeven): cubre variable, no fijo.

## 5 · Recompra / LTV
- [ ] % de ventas de clientes recurrentes vs nuevos (customer_type).
- [ ] Tasa de recompra. En vertical con recompra: <20% ⇒ warning (LTV sin construir).
- [ ] LTV:CAC ≥ 3:1 como north star (solo si hay CAC de paid). Sin CAC → "no verificado".
- Contexto: recompra baja en categoría de compra única (ej. colchón) **no es** un fallo.

## 6 · Descuentos
- [ ] Descuento promedio por producto (total_discounts / ventas brutas por SKU).
- [ ] Producto cuyo descuento promedio se acerca o supera su margen de contribución.
- **fail** si un producto se vende mayormente con descuento > su margen (pierde por diseño).

## 7 · Devoluciones
- [ ] Tasa de devolución por producto (si el dato está en la ventana).
- [ ] Devolución que convierte un margen positivo en negativo neto.
- Si el dato no está disponible por MCP → "no verificado", no se estima.

## 8 · Envío & fulfillment
- [ ] Costo de envío real vs. lo cobrado al cliente.
- [ ] Umbral de envío gratis vs. AOV: si el umbral está bajo el punto donde el envío gratis
  come el margen, hay fuga silenciosa.

## 9 · Mix & concentración
- [ ] Pareto: qué % de las ventas y del margen depende del top 3 de SKUs.
- **warning** si >60% del margen depende de 1 SKU (riesgo de concentración).
- [ ] Detectar productos de alto volumen y margen negativo (loss-leader): marcar y preguntar
  si es intencional antes de reportarlo como problema.

## 10 · Salud de datos (siempre se reporta)
- [ ] Moneda de la tienda (get-shop-info) y si coincide con la del gasto de paid.
- [ ] Cobertura de COGS.
- [ ] Ventana usada y por qué.
- [ ] Fuentes conectadas (Shopify / GA4 / Meta / Google) y qué quedó "no verificado".
