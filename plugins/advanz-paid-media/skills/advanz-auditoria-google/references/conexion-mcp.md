# Conectar las fuentes al MCP (multi-fuente)

La auditoría rinde más mientras más fuentes estén conectadas. Google Ads es obligatorio;
el resto es "si está, mejor" — y lo que falte se marca "no verificado".

> **Nota interna (validar):** el setup real del equipo Advanz corre el MCP de Google Ads
> desde un venv fijo. Confirmar el comando exacto contra ese setup antes de publicar la
> guía como entregable al prospecto.

## 1 · Google Ads (obligatorio)
- MCP de Google Ads conectado (OAuth + developer token + login-customer-id / MCC).
- Verificar con `customers_list_accessible_customers` y elegir el customer ID (10 dígitos).
- Nivel lectura basta para auditar.

## 2 · GA4 (analytics-mcp · opcional, recomendado)
- Da comportamiento y la discrepancia de conversiones Google vs GA4.
- Gotcha conocido: algunas cuentas rebotan `ACCESS_TOKEN_SCOPE_INSUFFICIENT`; si pasa,
  marcar la discrepancia GA4 como "no verificado" y seguir.

## 3 · Merchant Center / Shopify (opcional)
- Para estado del feed, desaprobaciones, precios y oferta legible.
- Sin GMC MCP dedicado: usar lo que expone la API de Ads (shopping_performance_view,
  estado de producto) + Shopify MCP para precios; lo demás → "no verificado".

## Reglas de lectura del resultado
- **"No verificado"** = hueco de acceso, no un problema.
- Los hallazgos son **"puntos a revisar"**, priorizados por plata en juego.
- El gasto recuperable es **estimación** con aritmética a la vista, no un resultado.
