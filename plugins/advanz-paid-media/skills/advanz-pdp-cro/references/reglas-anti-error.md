# Reglas anti-falso-positivo · PDP

Un falso positivo —decir que falta algo que sí está, o que algo está mal cuando está bien—
es el único error irreversible. Destruye la confianza del dueño en el diagnóstico completo.
**Ante la duda, NO se reporta: se marca "no verificado".**

## Las heurísticas

1. **Cuenta trabajos, no elementos.** Una galería de 6 imágenes bien elegidas puede cubrir
   los 10 trabajos (una foto puede ser producto + característica). No cuentes fotos: cuenta
   qué dudas resuelve.

2. **Precio sin tachar ≠ error.** Si el producto no está en oferta, no tener precio ancla no
   es un fail. La palanca es "precio legible", no "siempre en descuento".

3. **No viste ≠ no existe.** Si no pudiste comprobar mobile, el sticky CTA o el FAQ (p. ej.
   está en un acordeón que no abriste), es "no verificado", no "ausente".

4. **Bundle no aplica a todo.** Productos de compra única o de ticket alto pueden no tener
   sentido de bundle. Marca "no aplica", no "fail".

5. **Escasez real vs. falsa.** No recomiendes urgencia inventada (contador falso). Si no hay
   escasez real, la palanca queda como "opcional", no como carencia obligatoria.

6. **Prueba social presente pero abajo = warning, no fail.** Existe, mal ubicada. Distinto de
   no tenerla.

7. **Distingue dato de interpretación.** "La galería tiene 3 imágenes" es dato. "La galería
   es pobre" es interpretación — frásea el hallazgo como punto a revisar.

8. **Proyecciones = estimación, siempre.** Cualquier "esto te cuesta X" lleva la aritmética a
   la vista y la palabra estimación. Nunca presentes una proyección como algo que ocurrió.

9. **Anonimato por defecto.** Si el diagnóstico alimenta contenido, tapa marca/dominio del
   cliente salvo OK por escrito.

## Antes de entregar, checea
- [ ] ¿Cada hallazgo tiene el elemento real (o su ausencia) citable en una captura?
- [ ] ¿Marqué "no verificado" lo que no pude comprobar, en vez de asumir?
- [ ] ¿Separé dato de interpretación?
- [ ] ¿Las cifras proyectadas están marcadas como estimación con su aritmética?
