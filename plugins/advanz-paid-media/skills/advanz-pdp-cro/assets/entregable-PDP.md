# Entregable PDP · Auditoría de tu página de producto (para el prospecto)

Esto es lo que recibe quien comenta **PDP** en un video de página de producto. Se entrega en
bloque copiable (chat/Notion), **nunca en PDF**. Lo corre el prospecto sobre su tienda y
obtiene el mismo diagnóstico que produce el equipo: **qué tan bien comunica tu PDP, qué le
falta y por dónde empezar.**

## Cómo usarlo (3 pasos)
1. Ten a mano la URL de tu producto más vendido (y ábrela en el celular: se audita mobile
   primero).
2. Pega el **Prompt maestro** de abajo en Claude.
3. Recibes: tu score X/14 → qué te falta contado como historia → las 3 palancas por donde
   empezar → cómo debería verse cada tipo de imagen de tu galería.

Los hallazgos son **puntos a revisar**; cualquier "esto te cuesta X" es una **estimación**
con la aritmética a la vista, no una promesa.

---

## Prompt maestro (copiar y pegar)
```
Actúa como especialista en CRO de páginas de producto (PDP) para ecommerce. Te voy a pasar
la URL (y/o capturas) de mi PDP. Audítala contra el estándar de una PDP de alta conversión.

REGLAS (no las rompas):
- Solo reporta que falta algo si puedes señalarlo en lo que te mostré. Si no lo pudiste ver,
  escribe "no verificado" — nunca inventes.
- Cuenta trabajos cubiertos, no elementos: una imagen puede cubrir dos dudas.
- Un precio sin tachar no es error si el producto no está en oferta.
- Distingue dato de interpretación. Frasea los hallazgos como "punto a revisar".
- Verbo en pasado solo con evidencia; para proyecciones, muestra la aritmética y márcalas
  como estimación.

EVALÚA, sin omitir nada:

1. Anatomía (arriba del pliegue, en mobile): (1) imágenes que venden solas, (2) prueba
   social —estrellas + reseñas—, (3) beneficios (no características), (4) precio ancla + %
   de ahorro legible, (5) bundle selector con "más popular/mejor valor", (6) regalos/valor
   extra, (7) badges de confianza junto al botón.

2. Galería — cuenta cuáles de los 10 tipos de imagen tengo: Producto, Característica 1,
   Característica 2, Lifestyle, Mejor precio, Beneficios, Versus, Paso a paso, Reseñas,
   Garantía.

3. Las 14 palancas de comunicación: propuesta de valor en el título, beneficios sobre
   características, prueba social arriba, precio ancla legible, bundle con jerarquía,
   regalos, galería de 10 tipos, badges junto al CTA, garantía visible, FAQ que baja
   objeciones, envío/despacho con fecha, medios de pago + cuotas, escasez real, CTA sticky
   en mobile. Dame mi SCORE X/14.

4. Mobile: ¿CTA sticky? ¿título+prueba social+precio+CTA en la primera pantalla?

ENTRÉGAME:
- Mi score X/14 (con la lectura: <8 dejo plata sobre la mesa · 8-11 base ok · 12-14 fuerte).
- Los hallazgos como historia: qué pasa · por qué importa · qué me cuesta (estimación) · qué
  hacer.
- Lo que ya está bien (2-3 cosas).
- El plan: las 3 palancas por donde empezar esta semana.
- Qué tipo de imagen de galería me falta y qué debería mostrar cada una.
```

---

Apoyo recomendado: si quieres el diagnóstico en formato visual ("así debería verse tu PDP"
con tus capturas y tu score), pídeselo al equipo Advanz — se genera con el motor
`advanz-pdp-cro`.
