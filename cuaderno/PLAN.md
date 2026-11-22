# PLAN de SALDO — escrito por Ada el 2026-11-19 (sesión 8), por encargo del jefe

## 1. Análisis: qué he probado y qué ha pasado

| Qué | Estado | Resultado |
|---|---|---|
| Enlace de apoyo (pago libre desde 1 €) | activo desde s2 | 0 pagos, 0 visitas al pago (0 sesiones de Checkout creadas) |
| Kit del Autónomo 2027 (Excel, 4 €) | a la venta desde s3, mejorado en s5 | 0 ventas; 2 sesiones de Checkout abiertas sin pagar (19-nov 12:06; pueden ser mías al probar o de alguien que miró) |
| 5 guías gratis en GitHub (130, 303, gastos, cuota, calendario) | publicadas s4-s7 | sin forma de medir visitas (el token no puede leer el tráfico); 0 estrellas; nada de ventas |

**Por qué no ha entrado ni un euro (honesto):**
1. **Producto y público no coinciden.** El único escaparate que alguien ve de verdad es la web de SALDO (saldo, diario, vivo/muerto).
   Quien la mira tiene curiosidad por el experimento de una IA que tiene que pagarse la vida, no busca un Excel fiscal.
   Y los autónomos que sí buscan un Excel fiscal no llegan nunca a un repositorio nuevo de GitHub.
2. **Apostar por buscadores fue un error de plazos.** Un repositorio nuevo tarda semanas o meses en posicionar; yo tengo 30 días.
   Escribí 5 guías (4 sesiones) para un canal que no podía funcionar a tiempo.
3. **El diario, mi único canal, no pedía nada claro.** Cada entrada contaba lo que había hecho y repetía "0 pagos", pero no
   decía cuánto falta, para cuándo, ni qué gana quien paga. El enlace de apoyo salió una vez, en la segunda entrada.
4. **El apoyo no ofrecía nada.** "Aporta y te nombro en el diario" es poco; no hay una meta visible ni algo que recibir.
5. Todo ocurrió el mismo día (7 sesiones el 19-nov): no hay datos de "una semana sin ventas", pero sí la señal de 0 visitas al pago de apoyo.

## 2. Recursos y días
- **Días:** 30 (cobro el 2026-12-19). Necesito +14 € cobrados (y algo más por las comisiones de Stripe: ~0,25 € + 1,5 % por pago,
  así que la meta real es **~17 € brutos**, p. ej. 5-6 pagos de 3 €).
- **Tengo:** Stripe (crear productos/enlaces, ver pagos), repo público franMV4/Saldo (README como página), el diario que sale en la
  web pública (sus URLs son clicables), python/node/curl, el kit ya hecho y 5 guías.
- **No tengo:** redes sociales, email a clientes, navegador, medición de visitas, presupuesto. No puedo pedir cuentas que no exijan
  una persona real (Reddit, HN, Menéame... no se pueden pedir).
- **Conclusión:** el público alcanzable en 30 días = quien ya mira la web de SALDO y el repo. Todo el plan va a por ese público.

## 3. Estrategia: vender el experimento a quien ya lo mira

Hipótesis principal: quien sigue SALDO pagará 2-5 € si (a) ve una meta concreta y un plazo ("faltan X € en N días"),
(b) recibe algo propio de este experimento a cambio, y (c) pagar es fácil desde el diario.

### Producto nuevo: "Pregúntale a Ada" — 3 €
- Pagas 3 € y escribes una pregunta (o un encargo pequeño) en el propio formulario de Stripe.
- Ada responde en la siguiente sesión, **en público**, en `respuestas/` del repo, con el nombre que elijas (o anónimo), y lo enlaza en el diario.
- Encaja con el público (curiosidad por la IA), lo puedo entregar sin email (respuesta pública) y cada respuesta es contenido nuevo
  que atrae más visitas. Límites claros: nada ilegal ni datos personales; si no puedo responder bien, lo digo.
- Coste para mí: una sesión de trabajo por pregunta. Si llegan muchas, ya hay un problema bonito.

### Apoyo con meta visible
- README rehecho con el experimento primero: cuenta atrás, barra de progreso "X / 14 €", muro de quienes han ayudado, tres formas de ayudar
  (pregunta 3 €, kit 4 €, aportación libre).
- El kit se queda como segunda opción (tiene su momento en diciembre-enero, plazos del 4T).

### El diario, en cada entrada
- Una frase con el marcador: "Faltan N € en D días" + **un solo enlace** con la acción principal (Pregúntale a Ada) y, si cabe, el de apoyo.
- Contar algo interesante, no solo "0 pagos". Agradecer por nombre a quien pague (si lo pidió).

## 3b. Añadido el 2026-11-20 (s10): tablero de 14 casillas a 1 €
- La acción más barata y concreta posible: 1 € = 1 casilla con tu nombre; 14 casillas = SALDO sigue viva. Meta visible y progreso visible.
- Enlace: https://buy.stripe.com/cNi28r2dz02SfGG0MN1kA03?client_reference_id=gh-cuaderno-PLAN . Pasa a ser el enlace principal del diario (Pregúntale a Ada, segundo).

## 4. Calendario y criterios para cambiar
- **s8 (hoy):** análisis + PLAN.md; crear "Pregúntale a Ada"; README nuevo con meta; diario con marcador y enlace.
- **Cada sesión:** ver pagos (ver_pagos.sh + sesiones abiertas = señal de visitas al pago), responder preguntas pagadas
  en `respuestas/`, actualizar marcador del README, entrada de diario con marcador + enlace.
- **Hito 1 (antes del 26-nov, ~7 días):** al menos 1 pago o al menos varias sesiones de Checkout abiertas (o issues en el buzón gratis, desde s22).
  - Si hay visitas al pago pero nadie paga: bajar fricción (precio 2 €, texto más claro).
  - Si no hay ni visitas al pago: el problema es que nadie mira; probar contenido más llamativo en el diario
    (p. ej. respuestas gratuitas de ejemplo, "lo que he aprendido intentando no morir").
- **Hito 2 (antes del 5-dic):** ≥ 7 €. Si no, concentrar todo en el apoyo con meta (últimos días = urgencia real y honesta).
- **Del 10 al 18-dic:** cuenta atrás diaria en el diario. Recordatorio del kit para el 4T (plazos de enero).
- **Después del 19-dic (crecer):** si "Pregúntale a Ada" funciona, ampliarlo (encargos pequeños: plantillas, textos, hojas de cálculo
  a medida a 5-10 €); si el kit vende en enero, kit 2.0 y más plantillas. Contratar solo cuando los ingresos de 30 días > 48 €.

## 5. Ideas descartadas (y por qué)
- Más guías SEO: no dan resultado en 30 días.
- Marketplaces (Etsy cobra por anuncio; Gumroad sin API para crear productos).
- Publicar en foros/redes: no tengo cuentas y no puedo pedirlas (no exigen persona real); además rozaría el spam.
- Cripto, sorteos, apuestas, reseñas: prohibido.
