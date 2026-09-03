# El output en narrativa (el entregable que ve el dueño)

El objetivo: alguien que no le dedica el día a Google Ads —un dueño de ecommerce— abre
esto y **en 30 segundos entiende qué pasa, qué le cuesta y qué hacer.** Lo técnico pesado
queda disponible, pero fuera del camino. Referencia de estilo: la auditoría de Clarity —
mega-visual, accionable, cero relleno.

## Dos formas de entregar (misma historia)
1. **Narrativa en chat** — para uso interno rápido del equipo.
2. **Reporte visual HTML branded (default para dueño/prospecto)** — se construye con el
   design system de Advanz: `../advanz-reporting/references/design-system.md` +
   `../advanz-reporting/assets/plantilla.html` (Poppins + Space Grotesk, violeta+cyan,
   autocontenido, imágenes en base64, **guardado local, nunca Artifact**). Es un tipo de
   reporte nuevo dentro del estándar visual: "Auditoría de Google Ads".

## Componentes visuales del dashboard (estándar congelado · v3)
Plantilla de referencia lista para reproducir: `../assets/plantilla-reporte.html` (validada
con datos reales). El reporte se arma como **dashboard**, no como documento. Componentes,
en orden, todos con tokens de marca Advanz (violeta `#7b2ff7`→`#c15dff`, cyan `#22d3ee`,
Poppins + Space Grotesk, fondo `#f4f1fb`):

1. **Hero** — titular con la frase clave en degradado + anillo de score (0–100, conic-gradient
   con tramos rojo/ámbar/violeta) + fila de 4 stat-cards (inversión, retorno, gasto en revisión, áreas verificadas).
2. **Semáforo de áreas** — grid de tiles con punto de color (🟢 sólido · 🟡 a revisar · 🔴 acción ·
   ⚪ sin verificar). Salud de un vistazo, arriba, no en el anexo.
3. **Dona "¿de quién es el retorno?"** — marca vs captación (conic-gradient), con ROAS de cada lado.
4. **Barra "¿a dónde va tu plata?"** — gasto por campaña (stacked) + desglose del gasto en revisión.
5. **Medidores de impression share** — barras apiladas por campaña: capturado / perdido por ranking / perdido por presupuesto.
6. **Quality Score** — pills de color (verde/ámbar/rojo) por keyword clave, con barra.
7. **Tarjetas de hallazgo** — cada una: icono + título + **número de impacto grande a la derecha** +
   filas condensadas (Qué pasa · Por qué · Qué hacer). Borde rojo si es acción. Ordenadas por plata en juego.
8. **Fortalezas** — tiles verdes (lo que está bien, para credibilidad).
9. **Plan · 3 movimientos** — pasos numerados con chip de "quick win" donde aplique.
10. **Anexo técnico** (colapsable) — tabla de estado por área + tabla de campañas.
11. **Salud de los datos** — qué se conectó y qué quedó "no verificado".

Regla de diseño: **cada visual carga un insight.** No agregar gráficos decorativos — restan
credibilidad ante un dueño. Self-contained (CSS/SVG inline, sin librerías), guardado local, nunca Artifact.

## La estructura (arco narrativo, de mayor a menor jerarquía)

1. **Titular / veredicto (una línea, lenguaje de dueño).** El estado de la cuenta + el
   número que más importa. Ej.: "Tu Google trae ventas, pero más de la mitad son de gente
   que ya te buscaba — y hay ~$X/mes en revisión."
2. **Salud de la cuenta.** Un score 0–100 (usar `../ads/references/scoring-system.md`) +
   la plata en juego total. Tiles grandes, escaneables.
3. **El resumen en 30 segundos.** 3–4 bullets: lo que está pasando, en plata.
4. **Los hallazgos, contados como historia.** Ordenados por plata en juego. Cada uno,
   SIEMPRE los cuatro bloques, en lenguaje simple:
   - **Qué está pasando** — el hecho, sin jerga.
   - **Por qué pasa** — la causa técnica, traducida.
   - **Qué te está costando** — plata en juego, con la aritmética a la vista, marcado como
     estimación. Nunca una proyección presentada como algo ocurrido.
   - **Qué hacer** — la acción concreta (y si es Quick Win, decirlo).
5. **Lo que está bien.** Para no ser solo diagnóstico (regla del Tipo B): reconocer lo
   sano da credibilidad. Mínimo lo que de verdad esté en verde, citado.
6. **El plan — 3 movimientos.** Priorizados (esta semana / este mes), con impacto estimado.
   Postura, no "hay una señal de que podría convenir".
7. **Anexo técnico (colapsable).** Los 80+ checks con su estado, tablas y datos crudos —
   para el que quiera bajar al detalle. Va abajo, colapsado, no estorba la historia.
8. **Salud de los datos.** Qué fuentes se conectaron (Google Ads / GA4 / Merchant /
   Shopify) y qué quedó **"no verificado"** y por qué. Honestidad, nunca hueco silencioso.

## Reglas de traducción (jerga → negocio)
Reusar el glosario de `../advanz-reporting/references/tono-voz.md`. En corto:
- ROAS → "retorno" · CPA → "costo por venta" · AOV → "ticket promedio"
- impression share → "cuánto de la búsqueda capturamos"
- search terms → "lo que la gente realmente escribió"
- negativas → "búsquedas que le decimos a Google que ignore"
- enhanced conversions / CAPI → "cuánta de tu data real le llega a Google"
- marca vs no-marca → "gente que ya te buscaba vs. gente nueva"

## Tono
Español neutro (tú). Primera persona plural del método Advanz. La IA/MCP es el cómo,
nunca el titular. Marco honesto: se dice lo que el dato sostiene, ni más ni menos.

---

## Ejemplo (mini, con datos reales anonimizados)

**Titular:** "Tu Google trae retorno, pero más de la mitad viene de gente que ya te
buscaba — y hay ~$116k/mes en revisión."

**Hallazgo 1 — El retorno lo sostiene tu propia marca**
- *Qué pasa:* de cada 10 ventas que Google se anota, ~5 vienen de gente que ya buscaba tu
  nombre. La captación de clientes nuevos rinde mucho menos.
- *Por qué:* la campaña de marca retorna 9,4x; la de categoría (clientes nuevos), 1,25x.
- *Qué te cuesta:* no es plata perdida, pero infla el retorno general (3,4x) y esconde que
  la captación real casi no rinde.
- *Qué hacer:* separar la lectura marca vs. no-marca antes de decidir cuánto escalar, y
  liberar el presupuesto que la marca está dejando sin capturar (pierde ~19% por tope).

*(…hallazgos 2–5 en el mismo formato, ordenados por plata en juego. El detalle técnico —
IS 47,6% rank lost en categoría, cola 0-conv $29k, SKUs sub-0,6 ROAS $87k— va en el anexo
colapsable, no en la historia.)*
