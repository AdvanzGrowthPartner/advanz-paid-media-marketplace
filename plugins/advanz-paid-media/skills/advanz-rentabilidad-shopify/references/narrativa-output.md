# El output en narrativa (el entregable que ve el dueño)

El objetivo: un dueño de ecommerce abre esto y **en 30 segundos entiende de qué vive su
margen, qué le cuesta la fuga y qué hacer.** Lo técnico pesado queda disponible, fuera del
camino. Referencia de estilo: la auditoría de Clarity — mega-visual, accionable, cero relleno.

## Dos formas de entregar (misma historia)
1. **Narrativa en chat** — para uso interno rápido del equipo.
2. **Reporte visual HTML branded (default para dueño/prospecto)** — se construye con el
   design system de Advanz: `../advanz-reporting/references/design-system.md` +
   `../advanz-reporting/assets/plantilla.html` (Poppins + Space Grotesk, violeta+cyan,
   autocontenido, imágenes en base64, **guardado local, nunca Artifact**). Plantilla de
   referencia de esta skill: `../assets/plantilla-reporte.html`. Es un tipo de reporte nuevo
   dentro del estándar visual: "Rentabilidad de Shopify".

## Componentes visuales del dashboard (estándar congelado)
El reporte se arma como **dashboard**, no como documento. Componentes, en orden, todos con
tokens de marca Advanz (violeta `#c15dff`, cyan `#00ddfc`, Poppins + Space Grotesk):

1. **Hero** — titular con la frase clave en degradado + anillo de score de rentabilidad
   (0–100) + fila de 4 stat-cards (ventas netas, margen promedio ponderado, ROAS de
   equilibrio, plata en juego / margen dejado en la mesa).
2. **Semáforo de áreas** — tiles con punto de color (🟢 sólido · 🟡 a revisar · 🔴 acción ·
   ⚪ sin verificar): margen, mix, recompra, descuentos, envío, datos.
3. **Tabla de productos por margen** — el centro: producto · unidades · ventas · margen % ,
   ordenada por unidades, con el **producto-fuga en rojo** (top ventas / bajo margen).
4. **Cruce volumen vs margen** — barras o scatter: dónde está el producto que se escala y no
   deja. Carga el hallazgo ancla ("tu #1 en ventas es el #N en margen").
5. **Medidor ROAS real vs equilibrio** — por campaña/canal si hay paid: capturado sobre/bajo
   el breakeven. Traduce el número absoluto en "gana / zona gris / pierde".
6. **Dona "¿de dónde viene tu margen?"** — concentración del margen por producto (Pareto).
7. **Tarjetas de hallazgo** — cada una: icono + título + **número de impacto grande a la
   derecha** + filas condensadas (Qué pasa · Por qué · Qué te cuesta · Qué hacer). Borde rojo
   si es acción. Ordenadas por plata en juego.
8. **Fortalezas** — tiles verdes (los productos y palancas que sí dejan margen).
9. **Plan · 3 movimientos** — pasos numerados con chip "quick win" donde aplique.
10. **Anexo técnico** (colapsable) — tabla completa de productos con COGS, margen $/%, descuentos.
11. **Salud de los datos** — moneda, cobertura de COGS, ventana, fuentes y qué quedó "no verificado".

Regla de diseño: **cada visual carga un insight.** Nada decorativo. Self-contained (CSS/SVG
inline, sin librerías), guardado local, nunca Artifact.

## La estructura (arco narrativo, de mayor a menor jerarquía)
1. **Titular / veredicto (una línea, lenguaje de dueño).** De qué vive el margen + el número
   que más importa. Ej.: "Tu tienda factura bien, pero tu producto estrella deja 12% y estás
   poniendo la pauta ahí."
2. **Salud de rentabilidad.** Score 0–100 + la plata en juego (margen dejado en la mesa).
3. **El resumen en 30 segundos.** 3–4 bullets, en plata.
4. **Los hallazgos, contados como historia.** Ordenados por plata en juego. Cada uno, SIEMPRE
   los cuatro bloques, en lenguaje simple:
   - **Qué está pasando** — el hecho, sin jerga.
   - **Por qué pasa** — la causa, traducida.
   - **Qué te está costando** — plata en juego, con la aritmética a la vista, marcado como
     estimación. Nunca una proyección presentada como algo ocurrido.
   - **Qué hacer** — la acción concreta (y si es Quick Win, decirlo).
5. **Lo que está bien.** Reconocer los productos/palancas sanos da credibilidad (regla Tipo B).
6. **El plan — 3 movimientos.** Priorizados (esta semana / este mes), con impacto estimado.
7. **Anexo técnico (colapsable).** La tabla completa de productos y márgenes, datos crudos.
8. **Salud de los datos.** Moneda, COGS, ventana, fuentes, y qué quedó "no verificado" y por qué.

## Reglas de traducción (jerga → negocio)
- ROAS → "retorno" · margen de contribución → "lo que te queda después de costo, envío y comisión"
- breakeven / ROAS de equilibrio → "el retorno mínimo para no perder en cada venta"
- MER → "retorno de todo tu negocio, no de una campaña"
- COGS → "lo que te cuesta el producto" · AOV → "ticket promedio"
- gross_profit → "ganancia bruta" · customer_type → "clientes nuevos vs. que ya te compraron"
- LTV:CAC → "cuánto te deja un cliente vs. cuánto te cuesta traerlo"

## Tono
Español neutro (tú). Primera persona plural del método Advanz. La IA/MCP es el cómo, nunca el
titular. Marco honesto: se dice lo que el dato sostiene, ni más ni menos.

---

## Ejemplo (mini, con datos de ejemplo del framework)

**Titular:** "Tu tienda vende, pero el margen vive de 2 productos — y el que más vende deja
12%. Ahí está yendo tu pauta."

**Hallazgo 1 — Tu producto estrella es el que menos te deja**
- *Qué pasa:* el Pack Familiar es tu nº1 en unidades (512) y está último en margen (12%).
- *Por qué:* su costo y descuento promedio se comen la contribución; el Refill, que vende
  1/5, deja 58%.
- *Qué te cuesta:* cada peso de pauta que empuja el Pack rinde ~5x menos margen que empujar
  el Refill (aritmética a la vista, estimación sobre la ventana de 90d).
- *Qué hacer:* mover presupuesto de pauta al Refill / Kit Individual y revisar precio o costo
  del Pack antes de seguir escalándolo. (Quick win: bundle Pack+Refill para subir el margen mezclado.)

*(…hallazgos 2–4 en el mismo formato, ordenados por plata en juego. El detalle —tabla de
COGS por SKU, descuentos, breakeven por producto— va en el anexo colapsable.)*
