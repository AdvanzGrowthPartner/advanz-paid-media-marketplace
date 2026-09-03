# Reglas anti-error (van dentro de cada prompt y se respetan siempre)

Estas reglas son el eslabón crítico: cuando el prospecto corre la auditoría solo, no hay
nadie que le explique el resultado. Si el prompt falla, falla en su cuenta.

1. **Cita el dato o no reportes.** Solo se reporta un hallazgo si se puede citar el dato
   exacto que lo sustenta: campaña, métrica, período. Sin el dato → "no verificado".
   Nunca se inventa.
2. **Umbral, no opinión.** Los hallazgos salen de umbrales definidos, no de intuición.
3. **Ante la duda, NO reportes.** Un falso positivo (decir que algo está mal cuando está
   bien) es peor que un hueco. Es el único error irreversible.
4. **"A revisar", no veredicto.** Los hallazgos se frasean como puntos a revisar, no como
   sentencias absolutas.
5. **Dato medido ≠ interpretación.** Se distingue siempre lo que la cuenta muestra de lo
   que se interpreta.
6. **Verbo en pasado solo con evidencia.** Condicional para todo lo demás. Se puede
   proyectar mostrando la aritmética; nunca se presenta una proyección como algo ocurrido.

## Heurísticas anti-falso-positivo específicas de Google (críticas)
- **BROAD + Manual CPC = BMM legacy**, no un error. Solo revisar BROAD en Smart Bidding.
- **Término "wasted"** solo si supera el umbral de gasto Y tiene 0 conversiones. La cola
  larga con <umbral y 1 clic es exploración normal, no desperdicio.
- **Atribución modelada/fraccionada** (valores de conversión repartidos, decimales
  idénticos entre productos): marcar "a revisar" y pedir ventana ≥60–90d, nunca veredicto.
- **Negativas:** contar negativas de campaña Y listas compartidas antes de decir "faltan".
- **Marca:** derivar los tokens de marca del nombre del negocio y escanear el texto real de
  keywords; no confiar solo en el naming de campañas.
- Detalle completo en `../ads/references/gaql-notes.md`.

## Validación previa a repartir el entregable
- [ ] Corrido en una **cuenta sana**: NO inventa un problema donde no lo hay.
- [ ] Corrido en 5 cuentas reales: encuentra algo real en al menos 4.
- [ ] Falsos positivos: **cero**.
- [ ] Lo valida alguien distinto de quien lo escribió.
- [ ] Lleva versión y fecha (las plataformas renombran métricas; revisión trimestral).
