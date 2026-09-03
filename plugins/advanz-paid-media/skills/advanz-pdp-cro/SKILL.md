---
name: advanz-pdp-cro
description: "Motor de auditoría CRO de la PDP (página de producto) que corre el equipo Advanz para diagnosticar por qué una tienda recibe tráfico y no vende. Evalúa la PDP contra el estándar Advanz —los 7 bloques de anatomía arriba del pliegue, las 14 palancas de comunicación y los 10 tipos de imagen de una galería de alta conversión— con criterio real (umbrales pass/warning/fail) y reglas anti-falso-positivo. Entrega el resultado en NARRATIVA para dueño (qué pasa · por qué · qué te cuesta · qué hacer) y genera un ENTREGABLE VISUAL en HTML branded (así debería verse tu PDP + tu score X/14 + tus capturas marcadas). Dos capas: motor interno del equipo y el entregable PDP que corre el propio prospecto. Brand-agnostic: sirve para cualquier ecommerce. Úsala cuando digan: auditar PDP, revisar mi página de producto, por qué no convierte mi PDP, llega gente y no compra, mejorar la PDP, anatomía de PDP, galería de producto, así debería verse tu PDP, PDP para vender más, o al pegar una URL de producto de Shopify pidiendo feedback de conversión. Para landing/home genérica usar page-cro; para carrito/checkout usar el SOP de Carrito; esta es específica de la PÁGINA DE PRODUCTO."
user-invokable: true
metadata:
  version: 1.0.0
---

# Auditoría CRO de PDP (método Advanz · motor visual)

Este es el motor que usa Advanz para diagnosticar por qué una tienda **recibe tráfico y no
vende**. Casi nunca es el tráfico: es que la PDP no comunica lo que tiene que comunicar, en
el orden correcto. No es un checklist que se lee: **se mira la PDP real, se evalúa contra el
estándar y se devuelve una historia** que cualquier dueño entiende — más un entregable
visual que muestra "así debería verse".

## Principio rector (no negociable)
Nada se inventa. Cada hallazgo se **deriva** de lo que la PDP real muestra o no muestra
(bloque presente/ausente citable, con captura). La IA estructura y acelera, **nunca
origina**. Un falso positivo —decir que falta algo que sí está, o que algo está mal cuando
está bien— es el único error irreversible: **ante la duda, NO se reporta.** Lee
`references/reglas-anti-error.md` antes de reportar.

## Cobertura: la auditoría es 100% o no es
Se evalúan TODAS las áreas. Ninguna se omite en silencio; si no se puede ver un elemento
(p. ej. no hay acceso a mobile), se marca **"no verificado"** y se dice por qué.

| Bloque | Qué cubre |
|---|---|
| Anatomía (7 bloques) | Imágenes, prueba social arriba del pliegue, beneficios (no características), precio ancla, bundle selector, regalos/valor extra, badges de confianza |
| Galería (10 tipos) | Producto · Característica 1 · Característica 2 · Lifestyle · Mejor precio · Beneficios · Versus · Paso a paso · Reseñas · Garantía |
| 14 palancas | Propuesta de valor, beneficios>características, prueba social, precio ancla legible, bundle con jerarquía, regalos, galería completa, badges junto al CTA, garantía, FAQ, envío/despacho con fecha, medios de pago+cuotas, escasez/urgencia real, CTA sticky en mobile |
| Mobile | CTA sticky, jerarquía en 1 pantalla, peso de imágenes, tap targets |
| Confianza | Garantía explícita, política de cambios, medios de pago locales, reseñas verificadas |
| Oferta legible | Descuento visible (ancla + % ahorro), no depender solo de precio tachado (ver SOP oferta legible) |

El detalle de cada check (qué es pass/warning/fail, severidad, quick win) vive en
`references/checklist-completo.md`. **Úsalo como criterio, no lo reinventes.**

## Paso 0 · Elegir capa
- **Motor interno (default):** auditoría completa para el equipo Advanz. Alimenta
  consultoría, propuesta al cliente y la máquina de contenido (deja un hallazgo grabable).
- **Entregable prospecto:** entrega `assets/entregable-PDP.md` para que el propio prospecto
  la corra sobre su tienda (el "comenta PDP y te lo mando").

## Paso 1 · Pre-flight (input)
1. **URL de la PDP (obligatorio):** el producto a auditar. Si hay varias, elegir la de más
   tráfico/venta.
2. **Vista mobile primero:** la mayoría del tráfico es mobile; se audita mobile y luego
   desktop. Anota cuál pudiste ver.
3. **Capturas:** consigue las capturas reales de la PDP (hero, galería completa, bundle,
   badges). Son la evidencia y alimentan el entregable visual. **Sin capturas no hay
   entregable visual** (igual que el gate del Contenido SOP).
4. **Contexto de marca (si existe):** lee `.agents/product-marketing-context.md` o el brand
   kit del cliente para no pedir lo ya sabido (categoría, ticket, avatar).

## Paso 2 · Recolección
Recorre la PDP y registra, elemento por elemento, **presente / ausente / parcial**:
- Los 7 bloques de anatomía (¿están arriba del pliegue?).
- Los 10 tipos de imagen de la galería (¿cuáles hay, cuáles faltan?).
- Las 14 palancas de comunicación.
Si tienes browser/fetch, entra a la URL; si no, trabaja sobre las capturas que te pasen.
No asumas que algo falta solo porque no lo viste: si no lo pudiste comprobar, es "no
verificado", no "ausente".

## Paso 3 · Evaluación con criterio
Evalúa cada área contra el checklist (pass/warning/fail). Distingue **lo que la PDP muestra**
de **tu interpretación**. Aplica las heurísticas anti-falso-positivo (ej.: una galería de 6
imágenes bien elegidas puede cubrir los 10 trabajos — cuenta trabajos cubiertos, no fotos;
un precio sin tachar no es un error si el producto no está en oferta). Calcula el **score
X/14 palancas**.

## Paso 4 · Priorizar por impacto en conversión
Ordena los hallazgos por impacto probable en la conversión de la PDP, no por orden de lista.
Nombra **las 3 palancas que más mueven la aguja** para esta tienda (el "empieza por acá").
Si proyectas plata perdida, muestra la aritmética a la vista (visitas × conversión actual vs.
esperada) y márcala como **estimación**, nunca como logro.

## Paso 5 · Output en NARRATIVA (para el dueño)
Arma la salida siguiendo `references/narrativa-output.md`: titular en lenguaje de dueño →
resumen en 30 segundos → score X/14 → hallazgos contados como historia (qué pasa · por qué ·
qué te cuesta · qué hacer) → lo que ya está bien → el plan (empieza por estas 3) → anexo con
el checklist completo. La historia arriba; lo técnico, disponible pero sin pesar.

## Paso 6 · Entregable VISUAL (el diferencial)
Genera el HTML branded a partir de `assets/plantilla-pdp.html`. Es una **plantilla del design
system Advanz** con partes fijas (la anatomía nativa, la grilla de 10 tipos, el checklist de
14) y partes que rellenas por marca:
- `{{MARCA}}` · `{{SCORE}}` (X/14) · las capturas de ESTA tienda en los slots de "ejemplos".
- Las palancas que le faltan quedan marcadas en rojo; las que tiene, en verde.
Reglas del HTML: **self-contained** (imágenes en base64), responsive real (thumbnails de
altura fija + lightbox, sin scroll interno), sin scroll horizontal. El proceso de armado y
optimización de imágenes está en `references/checklist-completo.md` (sección "Armar el
entregable visual"). El resultado es la misma pieza del Contenido SOP, personalizada.

## Paso 7 · Cierre (según capa)
- **Motor interno:** entrega narrativa + HTML + ofrece empaquetar el hallazgo principal en
  ficha de contenido (formato lean del Contenido SOP).
- **Entregable prospecto:** entrega `assets/entregable-PDP.md` en bloque copiable. **Nunca
  PDF.**

## Voz e idioma
- Español neutro (tú). Primera persona plural del método Advanz ("Así revisamos…", "Lo
  primero que miramos…").
- El héroe es el **método** y el **hallazgo**, no la herramienta. Nombres claros, sin jerga
  en inglés sin explicar.
- Anonimizar la marca del cliente por defecto en cualquier salida pública (Contenido SOP).
