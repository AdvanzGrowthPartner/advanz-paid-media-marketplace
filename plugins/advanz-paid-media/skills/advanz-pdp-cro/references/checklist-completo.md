# Checklist canónico · PDP CRO (criterio Advanz)

Criterio pass / warning / fail por área. **Cuenta trabajos cubiertos, no elementos.** Ante
la duda, "no verificado", no "fail".

## A · Anatomía — los 7 bloques arriba del pliegue
Todo lo crítico debe verse antes del primer scroll en mobile.

| # | Bloque | Pass | Warning | Fail |
|---|---|---|---|---|
| 1 | Imágenes | Galería que explica el producto sin leer (ver sección C) | Fotos ok pero incompletas | 1-2 fotos genéricas |
| 2 | Prueba social | Estrellas + nº reseñas verificadas, arriba del pliegue | Reseñas pero abajo | Sin prueba social |
| 3 | Beneficios | 4 bullets de lo que gana el cliente, escaneables | Mezcla beneficio/spec | Solo características técnicas |
| 4 | Precio ancla | Precio actual + tachado + % ahorro legible | Tachado sin % | Precio suelto sin contexto |
| 5 | Bundle selector | 2-4 packs con "Más popular"/"Mejor valor" marcados | Packs sin jerarquía | Sin opción de volumen |
| 6 | Regalos / valor extra | Incentivo que empuja al pack mayor | Mencionado, no visible | Ausente |
| 7 | Badges de confianza | Garantía+envío+despacho+pago junto al CTA | Algunos, dispersos | Ausentes |

## B · Las 14 palancas de comunicación (score X/14)
1. Propuesta de valor en el título (1 línea, no el nombre SKU)
2. Beneficios sobre características
3. Prueba social arriba del pliegue
4. Precio ancla + ahorro legible
5. Bundle selector con jerarquía
6. Regalos / valor extra
7. Galería de 10 tipos completa (ver C)
8. Badges de confianza junto al CTA
9. Garantía explícita y visible
10. FAQ que baja objeciones
11. Envío y despacho con fecha concreta
12. Medios de pago + cuotas
13. Escasez / urgencia real (no falsa)
14. CTA sticky en mobile

**Score:** cuenta cuántas cumplen (pass). Lectura: <8/14 = la PDP está dejando plata sobre
la mesa; 8-11 = base ok, faltan cierres; 12-14 = fuerte, optimizar detalle.

## C · Los 10 tipos de imagen de una galería de alta conversión
Cada tipo es un **trabajo distinto**, uno por cada duda del cliente:
1. **Producto** — la foto limpia, qué es sin ruido
2. **Característica 1** — el atributo estrella, señalado
3. **Característica 2** — el segundo diferencial duro (tabla, spec clave)
4. **Lifestyle** — el producto usado en contexto real
5. **Mejor precio** — elige tu pack / ahorro por volumen
6. **Beneficios** — lo que gana el cliente, anotado
7. **Versus** — tu producto vs. la alternativa común
8. **Paso a paso** — cómo se usa, fácil en N pasos
9. **Reseñas** — lo que dicen los clientes, con cara
10. **Garantía** — compra con total tranquilidad

Pass = ≥8 trabajos cubiertos. Warning = 5-7. Fail = ≤4.

## D · Mobile (se audita primero)
- CTA sticky visible al hacer scroll · pass/fail
- Jerarquía: título + prueba social + precio + CTA en la 1ª pantalla
- Peso de imágenes (no bloquea el render)
- Tap targets del selector de variantes/bundle

## E · Confianza y oferta legible
- Garantía y política de cambios explícitas
- Medios de pago locales visibles (según mercado: WebPay/Mercado Pago/Flow en CL)
- Reseñas verificadas (no genéricas)
- Oferta legible: el descuento se ve como ahorro (ancla + %), no depende solo del tachado.
  Ver el SOP de oferta legible del Contenido SOP.

---

## Armar el entregable visual (HTML)
1. Junta las capturas reales de la tienda (hero, galería, bundle, badges) en una carpeta.
2. Optimízalas a web: máx ~1100px de ancho, JPEG calidad ~80 (evita el HTML de >5 MB).
3. Rellena `assets/plantilla-pdp.html`: `{{MARCA}}`, `{{SCORE}}` (X/14), incrusta las
   capturas en base64 en los slots de "ejemplos"; marca en rojo las palancas ausentes y en
   verde las presentes.
4. Verifica: sin scroll horizontal, thumbnails de altura fija + lightbox (sin scroll
   interno), abre self-contained.
5. Entrega el `.html` local (nunca PDF, no publicar como Artifact salvo que lo pidan).
