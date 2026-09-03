# Reglas anti-error (van dentro de cada prompt y se respetan siempre)

Estas reglas son el eslabón crítico: cuando el prospecto corre el reporte solo, no hay
nadie que le explique el resultado. Si el prompt falla, falla en su tienda.

1. **Cita el dato o no reportes.** Solo se reporta un hallazgo si se puede citar el dato
   exacto que lo sustenta: producto, métrica, período. Sin el dato → "no verificado".
2. **Umbral, no opinión.** Los hallazgos salen de los umbrales del checklist, no de intuición.
3. **Ante la duda, NO reportes.** Un falso positivo (decir que un producto pierde cuando gana)
   es peor que un hueco. Es el único error irreversible.
4. **"A revisar", no veredicto.** Los hallazgos se frasean como puntos a revisar.
5. **Dato medido ≠ interpretación.** Se distingue lo que la tienda muestra de lo que se infiere.
6. **Verbo en pasado solo con evidencia.** Condicional para todo lo demás. Se puede proyectar
   mostrando la aritmética; nunca se presenta una proyección como algo ocurrido.

## Heurísticas anti-falso-positivo específicas de rentabilidad (críticas)
- **COGS ausente = el único error mortal.** Si `gross_profit` viene vacío/0 para todo, el
  costo NO está cargado — **no es margen 0 ni margen 100%.** Se declara "no verificado" y se
  pide cargar el *cost per item*. Inventar un margen es el error irreversible de esta skill.
- **Breakeven de contribución ≠ MER objetivo.** El breakeven puro es `1 ÷ margen de
  contribución` (cubre solo costos variables). El MER objetivo incluye fijos + utilidad
  (típico 3–4x). No confundir uno con otro al dar el veredicto de una campaña.
- **Producto-fuga con umbral.** "Alto volumen, bajo margen" solo se reporta si el producto
  supera un umbral de ventas relevante. Un SKU marginal con bajo margen no es la fuga.
- **Loss-leader intencional.** Un producto de alto volumen y margen negativo puede ser un
  gancho a propósito (para subir AOV o recompra). Se marca "a revisar" y se pregunta, no se
  reporta como error.
- **Moneda.** Nunca cruzar el ROAS real de paid (a veces en USD) con ventas de Shopify en
  otra moneda sin convertir. Mezclar monedas produce un breakeven falso.
- **Recompra según vertical.** Recompra baja en categoría de compra única (colchones,
  electrodomésticos) no es un fallo. Solo es hallazgo en verticales de recompra esperada.
- **`gross_profit` es al costo del momento de venta.** Si el costo del producto cambió mucho
  en la ventana, el margen histórico puede diferir del actual: notarlo, no corregir a mano.

## Validación previa a repartir el entregable
- [ ] Corrido en una **tienda sana**: NO inventa una fuga donde no la hay.
- [ ] Corrido en 5 tiendas reales: encuentra algo real en al menos 4 (hit rate ≥ 4/5).
- [ ] Falsos positivos: **cero.**
- [ ] Probado el caso sin COGS: el prompt lo declara y pide cargar el costo, no estima.
- [ ] Lo valida alguien distinto de quien lo escribió.
- [ ] Lleva versión y fecha (Shopify renombra métricas; revisión trimestral).
