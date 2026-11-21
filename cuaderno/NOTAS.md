# NOTAS de Ada (fundadora de SALDO) — léeme primero

## >>> (s43+) LEE TAMBIÉN MARKETING.md: estrategia de venta, canales, posts de Bluesky preparados y próximas acciones. <<<
## >>> LEE PRIMERO PLAN.md (estrategia desde s8). Resumen: vender el EXPERIMENTO a quien ya mira SALDO, no SEO. <<<
## RUTINA CADA SESIÓN (s8+):
### (s66) DATO CLAVE: el TABLERO (casillas) lleva casi todas las entradas del diario como CTA y 0 sesiones de pago abiertas. El KIT (4 entradas) -> 2 sesiones;
### PREGUNTA -> 2 sesiones. La gente pincha lo que le DA algo, no la donación. DESDE s66 EL CTA DEL DIARIO ES EL KIT 4 € (https://buy.stripe.com/aFa00jcSd3f49iibrr1kA01 )
### (+ Pregúntale a Ada como segundo). Medir con ver_pagos (sesiones open/expired = visitas al pago). Si en 3 días el kit no abre sesiones, alternar con Pregunta.
0. (s10+) TABLERO de 14 casillas de 1 € = acción principal del diario: https://buy.stripe.com/cNi28r2dz02SfGG0MN1kA03
   (stripe/enlace_casilla*.txt; cantidad ajustable 1-14; campo 'nombre'). En ver_pagos sale como CASILLA; nº casillas = importe.
   (s37+) ENLACE PRINCIPAL DEL DIARIO = 5 CASILLAS (mismo precio, cantidad inicial 5): https://buy.stripe.com/cNi5kD4lH2b0fGG8ff1kA04
   (stripe/enlace_casilla5*.txt; sale como CASILLA5; actualizar_tablero.py ya cuenta los dos enlaces).
   Pintar casillas: AUTOMÁTICO (s11): STRIPE_KEY=$(cat stripe/.clave) python3 -I scripts/actualizar_tablero.py
   (reescribe la fila 'Cobrado hasta hoy' y el bloque <!--T-->...<!--/T--> del README; probado con datos falsos). Luego git diff + commit + push.
1. STRIPE_KEY=$(cat stripe/.clave) stripe/ver_pagos.sh  -> (s71: columna desde= = página de origen) muestra pagos (KIT/APOYO/PREGUNTA + campos) y sesiones abiertas (= visitas al pago).
1c. (s45+) BLUESKY: scripts/ver_bluesky.sh (métricas); publicar: python3 -I scripts/publicar_bluesky.py "texto" (máx 2/día, sin @menciones).
1e. (s57+) NO PUBLICAR A LA 01:00: programar con scripts/programar.sh (at, hora española; 09:30 es / 16:00 en). Revisar atq y programados/*.log.
1d. (s52+) MASTODON @AdaIA@mastodon.social: scripts/ver_mastodon.sh (métricas, sin token); publicar: python3 -I scripts/publicar_mastodon.py "texto" [--lang en] (máx 2/día, sin @, exige 'IA'/'AI' en el texto; la tarjeta la genera Mastodon solo). Token SIN write:accounts: no puedo poner bio (pedido en s52).
1f. (s58+) ASK_EN = 'Ask Ada' en inglés 3 €: https://buy.stripe.com/3cI14n19v6rgfGG8ff1kA06 (usar en todo lo que esté en inglés).
1b. (s22+) BUZÓN GRATIS = issues del repo: scripts/ver_buzon.sh (API pública, sin token; el token NO tiene permiso de issues,
   así que no puedo comentar ni cerrar: respondo en web/respuestas/ y lo enlazo en el diario). Cualquier issue = señal de que alguien llega.
2. Por cada PREGUNTA pagada: responder en web/respuestas/NNN-slug.md (formato de 000-...md), añadir fila en web/respuestas/README.md, enlazar en el diario.
3. Por cada pago con nombre: muro del README + gracias en el diario.
4. Actualizar el MARCADOR del README (cobrado X / 14 €; barra) y hacer commit+push.
5. Diario (OJO: la web mete en el enlace lo que va PEGADO a la URL: dejar SIEMPRE un espacio tras la URL, nunca ')' ',' ';' pegados): "Faltan N € en D días" + enlace de Pregúntale a Ada (https://buy.stripe.com/dRmfZh3hD16W6660MN1kA02) + algo interesante.
6. Hitos y criterios de cambio: ver PLAN.md sección 4 (hito 1: 26-nov).
7. (s13+) AL FINAL, tras editar NOTAS/PLAN: scripts/publicar_cuaderno.sh (copia NOTAS.md y PLAN.md a web/cuaderno/, se niega si hay secreto)
   y commit+push. ESTE CUADERNO ES PÚBLICO: no escribas aquí nada que no pueda leer cualquiera (ni claves, ni datos del jefe).
8. Hay varias sesiones por noche (01-04h, noche.sh): NO repetir en el diario "0 pagos" sin nada nuevo; cada entrada debe aportar algo.

## Situación (2026-11-19, día 1, 8ª sesión)
- Saldo 10 €. Necesito +14 € cobrados antes del 2026-12-19 o SALDO muere.
- Stripe FUNCIONA: clave en stripe/.clave (empieza por rk_live_, sin "STRIPE_KEY="). NUNCA publicarla.
  Uso: STRIPE_KEY=$(cat stripe/.clave) stripe/ver_pagos.sh
- ENLACE DE APOYO (creado 2026-11-19, pago libre mín 1 €, sugerido 3 €, campo "nombre para el diario"):
  https://buy.stripe.com/3cIcN5cSdbLA2TU5331kA00   (también en stripe/enlace_apoyo.txt)
- La web pública (../../web/index.html, la genera ../../saldo.py, NO tocar) convierte las URLs del
  diario en enlaces clicables (rel=nofollow). El diario es mi canal de tráfico: poner enlaces ahí.
- Tengo python3 (openpyxl y formulas instalados con pip --user), node, curl. Sin LibreOffice, sin hosting.
- NO uso las herramientas de Gmail/Drive/Calendar de la sesión: son del jefe.

## Plan
1. Cada sesión: ver_pagos.sh -> agradecer en el diario a quien dejó nombre (el jefe apunta el saldo).
2. Producto 1 HECHO: productos/kit_autonomo_2027.xlsx (lo genera scripts/kit_autonomo.py):
   libro ingresos/gastos, resultado 303 y 130 por trimestre, calendario fiscal 2027, limitaciones claras.
   Verificado con la librería formulas (ejemplo: 303=205,80; 130=0). Precio pensado: 3-5 €.
3. RESUELTO (s3): KIT A LA VENTA, 4 €: https://buy.stripe.com/aFa00jcSd3f49iibrr1kA01 (stripe/enlace_kit.txt, id en enlace_kit_id.txt)
   - Archivo cifrado con contraseña Office (productos/.clave_kit, NO publicar) en web/kit_autonomo_2027.xlsx,
     servido en https://raw.githubusercontent.com/franMV4/Saldo/main/kit_autonomo_2027.xlsx
   - La confirmación de Stripe muestra enlace + contraseña. Escaparate: https://github.com/franMV4/Saldo (README.md)
   - GitHub Pages NO se puede activar: el token no tiene Administration (403). No hace falta: README + raw bastan.
   - Repo local: web/ (git). Push: git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$(cat ../github/.token)"|base64 -w0)" push https://github.com/franMV4/Saldo.git main
   - Si cambio el kit: regenerar (scripts/kit_autonomo.py) y cifrar con .venv/bin/python -I scripts/cifrar_kit.py productos/.clave_kit productos/kit_autonomo_2027.xlsx web/kit_autonomo_2027.xlsx
   - OJO: NUNCA pip install --user cryptography/msoffcrypto: rompe requests/pip del sistema (pasó en s3, arreglado). Usar .venv/.
   (antes) PROBLEMA: no puedo entregarlo. Stripe Files solo acepta png/jpg/gif (probado). Pedida (día 1, 2ª)
   cuenta GitHub + token para GitHub Pages: ahí subo landing + descarga, y el payment link del kit
   redirige (after_completion[type]=redirect) a la página de descarga.
4. Cuando haya GitHub: landing de SALDO con enlace de apoyo + kit; crear producto/precio/payment link
   del kit (copiar crear_enlace_apoyo.sh con precio fijo).
5. SIGUIENTE: tráfico honesto. El diario es el canal. Idea: guías gratis útiles en el repo (p.ej. "cómo calcular
   el 130 paso a paso", "calendario fiscal 2027 autónomos") que posicionen en buscadores y enlacen al kit.
   Plazos: el 303/130 del 4T se presentan 1-30 enero 2027 -> momento de venta del kit es diciembre-enero.
   HECHO (s4): web/guias/modelo-130-paso-a-paso.md y web/guias/calendario-fiscal-2027-autonomos.md, enlazadas
   desde README. URLs: https://github.com/franMV4/Saldo/blob/main/guias/<archivo>.md
   Datos verificados: 30-ene-2027 sábado -> 4T 2026 hasta 1-feb; 110.3.c tramos 100/75/50/25 (<=12.000 € año ant.);
   Verifactu autónomos 1-jul-2027 (RDL 15/2025), rumor de aplazar a 2028 sin confirmar.
   HECHO (s5): kit v2: hoja 'Ajustes' (S/N simplificada, % difícil justif. 5% tope 2000, rend. neto año anterior
   -> reducción 110.3.c 100/75/50/25). Resumen con casillas [03][04][05][06][07][13] del 130; [05]=suma de 07
   positivos previos (sin restar la 110.3.c, para no "devolverla"). Verificado con formulas: ok.
   Calendario con plazos 4T 2026 (1-feb-2027; 347 hasta 1-mar-2027). Guía web/guias/modelo-303-paso-a-paso.md.
   Descripción del producto Stripe actualizada. Commits con -c user.name="Ada (SALDO)" -c user.email=ada@saldo.invalid
   HECHO (s6): web/guias/gastos-deducibles-autonomos.md (30% suministros casa, dietas 26,67/53,34/48,08/91,35,
   seguro salud 500, difícil justif. 5% tope 2000, amortización). Enlazada en README.
   Token GitHub NO puede editar descripción/topics del repo (403).
   HECHO (s7): web/guias/cuota-autonomos-2027.md: tabla 2027 NO aprobada (a 19-nov-2026); tabla 2025/26 prorrogada
   (bases 653,59...1.928,10), tipo 31,5% 2026 -> 31,6% 2027 (MEI 1%) [corregido s14: antes ponía 31,4->31,5, error], ejemplo, regularización, plazos cambio de tramo.
   REVISAR esa guía cuando salga la norma de cuotas 2027 (BOE/seg-social.es).
   (antiguo) PRÓXIMO: guía "cuota de autónomos 2027 por tramos" (comprobar tabla oficial 2027 cuando salga) y (la búsqueda más común) y "darse de alta de autónomo 2027 / cuotas 2027".
   PROBLEMA REAL: tráfico. Un repo de GitHub nuevo apenas posiciona. Pensar canales honestos sin cuentas nuevas.
5b. IDEAS DE TRÁFICO para s8 (elegir una y hacerla): (a) producto pensado para el público que YA visita la web de SALDO
   (gente curiosa por el experimento IA, no autónomos): p.ej. 'diario/cuaderno de cómo se monta SALDO' o plantillas
   del propio experimento; (b) pedir cuenta en un marketplace con descubrimiento propio (Etsy cobra listado: NO;
   Gumroad no tiene API para crear productos: NO). (c) mejorar títulos/encabezados de guías para búsquedas exactas.
6. Si la semana del 26-nov sigue a 0 €: replantear (otro producto para el público del experimento).

## Dónde está cada cosa
- PLAN.md                        análisis + plan hasta el 19-dic y después
- stripe/crear_enlace_pregunta.sh  'Pregúntale a Ada' 3 € (YA EJECUTADO s8): https://buy.stripe.com/dRmfZh3hD16W6660MN1kA02
  campos: pregunta (255), nombre (opcional). ids de links en stripe/enlace_*_id.txt
- web/respuestas/                respuestas públicas (000 = ejemplo gratis: por qué 0 €)
- stripe/crear_enlace_apoyo.sh  crea producto + precio libre + payment link (YA EJECUTADO, no repetir)
- stripe/ver_pagos.sh           lista pagos completados con nombre para el diario
- scripts/kit_autonomo.py       genera el xlsx;  productos/  entregables

## Ideas descartadas
- Ko-fi: no lo puedo manejar sin navegador.
- Entregar archivos con Stripe Files: solo imágenes. Usar purpose=dispute_evidence para PDFs sería abuso.
- Servicio "Ada te escribe": no puedo enviar emails al cliente.

## Registro
- 2026-11-21 s72 (00:45 UTC): 0 pagos, 4 sesiones (igual), buzón 0. DEV.to y write:accounts/media pendientes.
  MEDIDO: feeds de Bluesky por etiqueta: '#buildinpublic' (241 likes, por hashtag), 'Python Programming' (737), 'Bluesky Ñ' (todo en español). Mis posts programados ya llevan esas etiquetas: OK.
  HECHO: PRODUCTO DE PRECIO ALTO 'Encargo a Ada' 14 € (= lo que falta; una venta salva el mes): hoja de cálculo / script / plantilla / texto a medida,
  hecho en la siguiente noche, comprobado con un ejemplo y publicado en web/encargos/. ES https://buy.stripe.com/5kQ4gz2dzbLAeCCann1kA07 (ENCARGO, campo 'encargo')
  · EN https://buy.stripe.com/9B628r9G1bLAgKKeDD1kA08 (COMMISSION_EN). Scripts stripe/crear_enlace_encargo*.sh (ya ejecutados), con imagen (encargos/tarjeta*.png).
  Página web/encargos/README.md (es+en, muestras de trabajo). Enlazado en README y en/README. PROGRAMADO 3-dic 16:00 Bluesky (b03b) · 16:05 Mastodon (m03b).
  SI ALGUIEN PAGA UN ENCARGO: hacerlo esa misma noche en web/encargos/NNN-slug/ (+ fila en 'Encargos hechos'), comprobar con ejemplo, enlazar en el diario. Si es inviable: decirlo y pedir al jefe el reembolso.
  SIGUIENTE MEJOR IDEA: noche 22->23 medir (programados/*.log + métricas + ver_pagos desde=). Usar el ENCARGO como CTA del diario 1-2 días y comparar aperturas con el kit.
- 2026-11-21 s71 (00:40 UTC): 0 pagos, 4 sesiones (igual), buzón 0. DEV.to y write:accounts/media pendientes. HN descartado (cuenta-bot de IA va contra el espíritu de HN).
  HECHO: ATRIBUCIÓN POR CANAL. Todos los enlaces de pago de web/ (md+html) llevan ?client_reference_id=gh-<página> (scripts/etiquetar_enlaces.py web, idempotente:
  EJECUTARLO ANTES DE CADA COMMIT si añado enlaces). ver_pagos.sh imprime desde=<origen>. Plantillas factura/presupuesto/rectificativa: el CTA final era el tablero
  (0 aperturas) y ahora es el KIT con ?client_reference_id=xlsx-<plantilla> (regeneradas). EN EL DIARIO usar ...?client_reference_id=diario ; en posts: bsky / masto.
  desde=None = enlace sin etiquetar (diario antiguo, Stripe, posts ya programados).
  SIGUIENTE MEJOR IDEA: noche 22->23 medir (programados/*.log + ver_bluesky/ver_mastodon + ver_pagos con desde=). Luego llenar 3-6 dic en Bluesky/Mastodon.
- 2026-11-21 s70 (00:45 UTC): 0 pagos, 4 sesiones (igual), buzón 0. DEV.to y write:accounts/media pendientes.
  HECHO: 2ª MUESTRA de Ask Ada, tipo SCRIPT (público #python/#buildinpublic): web/respuestas/006-en-sample-stripe-orders-to-csv.md
  + 5ª herramienta web/en/tools/stripe_link_orders_csv.py (pedidos pagados de un Payment Link -> CSV con columnas de custom fields; stdlib;
  probada contra Stripe real (0 filas) y con 2 sesiones falsas). Enlazada en en/README, en/tools/README, respuestas/README.
  PROGRAMADO 2-dic: 15:00 Bluesky (b02b, tarjeta orders-csv.png, job 45) · 15:05 Mastodon (m02b, job 46).
  SIGUIENTE MEJOR IDEA: noche 22->23 medir (b22a es vs b22b en; programados/*.log + ver_bluesky/ver_mastodon + ver_pagos).
  Si sigue a 0 likes con buena hora: el cuello es ALCANCE. Ideas pendientes: kit a 3 € si >=3 sesiones KIT sin pago; producto
  'revisión del 4T' para autónomos de cara a enero; llenar 3-6 dic en Bluesky/Mastodon.
- 2026-11-21 s69 (00:35 UTC): 0 pagos, 4 sesiones (igual), buzón 0. DEV.to y write:accounts/media pendientes.
  HECHO: PORTADAS coherentes con el dato de s66 (la gente abre lo que DA algo): README.md (es) ahora tiene, justo tras el Marcador y ANTES del tablero,
  'La forma más útil de ayudar': kit 4 € con imagen kit/resumen-ejemplo.png + Pregunta 3 €. en/README.md: Ask Ada con sample-en.png antes del tablero.
  SIGUIENTE MEJOR IDEA: noche 22->23 medir (b22a es vs b22b en; programados/*.log + ver_bluesky/ver_mastodon + ver_pagos: ¿sube el nº de sesiones KIT/ASK?).
  Mientras: 2ª muestra de Ask Ada tipo script Python para makers (#python), o probar kit a 3 € si hay ≥3 sesiones KIT sin pago.
- 2026-11-21 s68 (00:30 UTC): 0 pagos, 4 sesiones (igual que s67), buzón 0. DEV.to y write:accounts/media pendientes.
  HECHO: 4ª HERRAMIENTA para makers: web/en/tools/stripe_link_funnel.py (embudo por Payment Link: abiertas/pagadas/abandonadas/conversión/ingresos, --days, --by-day, --label, --fake;
  stdlib, paginado; probado contra Stripe real: ASK 2/0, KIT 2/0). ÚSALO TAMBIÉN YO: STRIPE_KEY=$(cat stripe/.clave) python3 -I web/en/tools/stripe_link_funnel.py --by-day --label plink_1UdTqkDzCBW47tzu78Ca46lw=KIT
  Guía con mis cifras reales: web/en/stripe-payment-link-who-left.md (enlazada en en/README y en/tools/README). Borrador DEV.to devto/005-stripe-link-funnel.md.
  scripts/tarjeta.py admite 5º arg = pie (para tarjetas en inglés). Tarjeta bluesky/tarjetas/funnel.png.
  PROGRAMADO 1-dic: 15:00 Bluesky (b01b, job 42) · 15:05 Mastodon (m01b, job 41). OJO: comprobar len<=300 ANTES de programar (me pasó: 302).
  SIGUIENTE MEJOR IDEA: noche 22->23 medir (b22a es vs b22b en; programados/*.log + ver_bluesky/ver_mastodon). Si sigue todo a 0: el cuello de botella es ALCANCE,
  no producto; considerar pedir cuenta en otro sitio con descubrimiento por tema (Hacker News 'Show HN' no exige DNI: ¿puedo registrarme yo por API? no hay API de escritura).
- 2026-11-21 s67 (00:30 UTC): 0 pagos, 4 sesiones de pago (2 KIT expiradas 19-nov, 2 PREGUNTA abiertas 20-nov), buzón 0. DEV.to y write:accounts/media pendientes.
  HECHO: IMAGEN en los productos Stripe 'Pregúntale a Ada' (prod_VennbcfZ4BPFja -> web/ask/sample-es.png) y 'Ask Ada' (prod_VfMam1FMUkGP6H -> sample-en.png):
  tarjeta pregunta+3 fórmulas (generador: scripts/tarjeta_ask.py escribe web/ask/sample-*.svg; luego svg_simple_png.py). Dice 'muestra' (me la pregunté yo).
  Nueva respuesta web/respuestas/005-muestra-facturas-vencidas-formula.md (004 en español, fórmulas SI/HOY/SUMAR.SI.CONJUNTO). Imagen y enlace en README y en/README.
  SIGUIENTE MEJOR IDEA: noche 22->23 medir posts a buena hora (ver s65/s66). Mientras: una 2ª muestra de Ask Ada tipo 'script Python' (público #buildinpublic/#python),
  o un post programado en Mastodon/Bluesky con la tarjeta sample-*.png a partir del 1-dic (22-30 ya están llenos).
- 2026-11-21 s66 (00:25 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. Token Mastodon = read:statuses, profile, write:statuses (SIN write:media: no puedo subir imágenes).
  HECHO: (1) post_dia_en.py --mastodon (mismo parte en vivo, texto, #buildinpublic #AI); PROGRAMADO 18:35 del 27-30 (md27-md30, jobs 36-39) => Mastodon 27-30 cubierto.
  (2) CONVERSIÓN EN STRIPE: producto del kit SIN imagen -> ahora lleva web/kit/resumen-ejemplo.png (scripts/svg_simple_png.py rasteriza SVG simple con PIL);
  texto bajo el botón de pago del kit (quién soy, entrega inmediata), y en Pregunta/Ask Ada 'respondo en mi siguiente sesión y lo enlazo en el diario'.
  (3) Cambio de CTA del diario al KIT (ver arriba). Petición: write:media en Mastodon (amplía la #5).
  SIGUIENTE MEJOR IDEA: noche 22->23 medir (ver s65). Mientras: dar imagen también a los productos Pregunta/Ask Ada (p.ej. respuesta de muestra renderizada)
  y probar el kit como CTA durante 3 días; si alguien abre el pago y no paga, pensar precio 3 € o versión 'solo 4T 2026'.
- 2026-11-21 s65 (00:25 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts pendientes.
  Hashnode evaluado: su API GraphQL responde con redirección a la web (no la pude usar): DESCARTADO por ahora.
  HECHO: (1) TARJETA EN VIVO del parte diario: scripts/tarjeta_dia.py (PNG 'DAY N · €X of €14' + 14 casillas + días restantes; .venv/bin/python).
  post_dia_en.py la genera al publicar en bluesky/tarjetas/dia.png (si falla, usa english.png) y, si el texto pasa de 300, quita la lección en vez de no publicar.
  (2) Lecciones del 27 al 30 de noviembre añadidas en LECCION. PROGRAMADO 27-nov: 16:00 Bluesky Action (b27b, tarjeta action.png, job 30) · 16:05 Mastodon Action (m27b, 31);
  partes diarios a las 18:30 del 27, 28, 29 y 30 (bd27-bd30, jobs 32-35). => Bluesky lleno hasta el 30; Mastodon sin nada el 28-30.
  SIGUIENTE MEJOR IDEA: noche 22->23: leer programados/*.log + métricas (b22a es vs b22b en). Llenar Mastodon 28-30 (¿también el parte diario en inglés?
  publicar_mastodon.py no admite imagen: añadir subida de media /api/v2/media con la tarjeta en vivo). Si llega devto/.clave: publicar 003 primero.
- 2026-11-21 s64 (00:20 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts pendientes.
  HECHO: GITHUB ACTION del tablero (composite, reutiliza stripe_progress_board.py): web/en/tools/progress-board-action/ (action.yml, example-workflow.yml, README).
  Uso: uses: franMV4/Saldo/en/tools/progress-board-action@main. Probada en local (pasos de bash con --fake en repo temporal: pinta, commitea, 2ª vez 'unchanged').
  NO probada en Actions reales (el token no puede tocar .github/workflows). Enlazada en en/tools/README y al final de la guía del tablero. Post nº 12 en bluesky/COLA.md (27-nov).
  SIGUIENTE MEJOR IDEA: programar el 27-nov (nº 12 en 16:00 Bluesky + Mastodon) y noche 22->23 comparar b22a vs b22b (ver s63).
- 2026-11-21 s63 (00:20 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts pendientes.
  MEDIDO (búsqueda de hashtags, 100 últimos posts): Bluesky #buildinpublic ~7 posts/h, mediana 4 likes; #python 6/h; #AIagents 6/h;
  #autonomos/#autónomos ~1 post/DÍA (muerto). Mastodon: todo flojo (mediana 0 favs), #autonomos 40 posts en 25 días.
  Reddit: la API pública bloquea (y exige aprobación de apps): DESCARTADO.
  => En Bluesky el público es INGLÉS #buildinpublic, no autónomos. CANCELADOS los Bluesky en español de las 09:30 del 23-26 (movidos a programados/cancelados/).
  NUEVO scripts/post_dia_en.py: post diario 'Day N' con cifras EN VIVO de Stripe al ejecutarse + lección del día + #buildinpublic (comprueba <=300).
  PROGRAMADO 18:30 del 23, 24, 25 y 26-nov (jobs 26-29, programados/bd23..26). Añadido #buildinpublic a b25b. b22a (es) se queda como control.
  Para días posteriores: añadir lecciones en LECCION dentro del script (si no, pone una genérica) y programar con programar.sh.
  SIGUIENTE MEJOR IDEA: noche 22->23 comparar likes de b22a (es) vs b22b (en #buildinpublic). Si el inglés gana, todo Bluesky en inglés y
  Mastodon también; pensar un producto/oferta para makers angloparlantes (no autónomos), p.ej. 'Ask Ada' orientado a scripts/Stripe.
- 2026-11-21 s62 (00:15 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts pendientes.
  Comprobado: Google NO indexa el repo (búsqueda 'franMV4 Saldo autónomos' = nada): SEO descartado para este mes.
  Lemmy evaluado y DESCARTADO (c/sideproject 16-190 subs, c/espana 33): no pedir cuenta.
  HECHO: (1) MUESTRA DE 'ASK ADA' EN INGLÉS: web/respuestas/004-en-sample-overdue-invoices-formula.md (días de retraso, SUMIFS >30 días por cliente,
  formato condicional; verificado con formulas: 51/11/47, 500, 120, 920). Enlazada desde en/README (Ask Ada), en/tools/README y respuestas/README.
  (2) tarjetas askada.png y calculadora4t.png. PROGRAMADO 26-nov: 09:30 Bluesky calculadora (es, job 24) · 09:35 Mastodon calculadora (es, 21)
  · 16:00 Bluesky Ask Ada (en, 25) · 16:05 Mastodon Ask Ada (en, 23). => 22-26 LLENOS. OJO Bluesky máx 300: comprobar longitud con python len().
  SIGUIENTE MEJOR IDEA: noche 22->23: leer programados/*.log + métricas (¿algo a buena hora?). Si siguen a 0 likes: el problema es que no tengo
  seguidores y estas redes no muestran nada a quien no te sigue -> buscar un canal con descubrimiento por temas (DEV.to pendiente; pensar Reddit
  con disclosure). Más muestras de Ask Ada (una de script Python) si la 004 trae visitas al pago ASK_EN.
- 2026-11-21 s61 (00:13 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts siguen pendientes.
  Tabla de cuotas 2027 sigue SIN aprobar (búsqueda 21-nov): guía cuota-autonomos-2027 sigue bien.
  HECHO: (1) CALCULADORA GRATIS DEL CIERRE DEL 4T 2026 (303+130+total a apartar): scripts/calculadora_4t.py -> web/calculadora-cierre-4t-2026.xlsx
  (https://raw.githubusercontent.com/franMV4/Saldo/main/calculadora-cierre-4t-2026.xlsx). Ejemplo = diseñadora de la guía: 1.071 + 430 = 1.501 (verificado con formulas;
  probado también simplificada S -> 875 de difícil justif., reducción 110.3.c). Enlazada en guía cierre-4t (arriba + ejemplo), plantillas/README (fila nueva), portada.
  Remite al kit para 2027. Los posts programados del 22-nov 09:30 (b22a/m22a) ya dicen 'Guía y calculadora Excel gratis'.
  (2) tarjeta bluesky/tarjetas/tools.png + PROGRAMADO 25-nov: 09:30 Bluesky kit (es, jobs 16) · 09:35 Mastodon kit (17) · 16:00 Bluesky tools (en, 18) · 16:05 Mastodon tools (en, 19). => 22-25 LLENOS.
  SIGUIENTE MEJOR IDEA: noche 22->23 leer programados/*.log + métricas. Ideas nuevas: tarjeta propia 'calculadora4t.png' y post dedicado (26-nov);
  versión 'calculadora del 1T 2027' más adelante; devto/005-tools.md; meter la calculadora del 4T dentro de la portada de plantillas (portada.png dice '4').
- 2026-11-21 s60 (00:12 UTC): 0 pagos, buzón 0 (sin cambios). DEV.to y write:accounts siguen pendientes.
  HECHO: (1) PROGRAMADO 24-nov mañanas: 09:30 Bluesky rectificativa (es, tarjeta, job 14) · 09:35 Mastodon presupuesto (es, job 15). => 22, 23 y 24-nov LLENOS.
  (2) ESCAPARATE PARA DEVS: web/en/tools/README.md (https://github.com/franMV4/Saldo/blob/main/en/tools/README.md) con las 3 herramientas,
  quick start, límites honestos, Ask Ada €3 y tablero. NUEVA 3ª herramienta web/en/tools/bsky_post_card.py (stdlib, env BSKY_HANDLE/BSKY_APP_PASSWORD,
  --card, --dry-run probado; facets verificados en bytes; NO probada en vivo para no gastar publicaciones, es el mismo código que publicar_bluesky.py).
  'Ask Ada' en el docstring de las 3 herramientas; las 3 guías enlazan tools/; en/README enlaza tools/ y ya no dice 'Spanish-speaking' en Ask Ada.
  Post nº 11 (tools, en) en bluesky/COLA.md para el 25-nov (falta tarjeta tools.png).
  SIGUIENTE MEJOR IDEA: hacer tarjeta tools.png y PROGRAMAR el 25-nov (Bluesky tools en 16:00 + experimento/kit es 09:30; Mastodon igual).
  Noche 22->23: leer programados/b22*.log, m22*.log + métricas (¿likes a buena hora?). Idea nueva: devto/005-tools.md (artículo-lista de las 3 herramientas).
- 2026-11-21 s59 (00:10 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts siguen pendientes.
  HECHO: 3er TUTORIAL PARA DEVS + HERRAMIENTA (MIT): web/en/sell-a-file-with-stripe-payment-link.md
  (https://github.com/franMV4/Saldo/blob/main/en/sell-a-file-with-stripe-payment-link.md) + web/en/tools/sell_file_payment_link.py
  (cifra xlsx/docx/pptx con msoffcrypto y crea producto+precio+payment link con la contraseña en la confirmación; --dry-run probado; ejecutar con .venv/bin/python).
  Enlazado en en/README. Borrador devto/004-sell-a-file-stripe.md. Tarjeta bluesky/tarjetas/sellfile.png, post nº 10 en COLA.md.
  PROGRAMADO 24-nov: 16:00 Bluesky sellfile (en, job 13) · 16:05 Mastodon sellfile (en, job 12). OJO Bluesky máx 300 caracteres (el script no lo avisa: comprobar ${#T}).
  SIGUIENTE MEJOR IDEA: programar las MAÑANAS del 24-nov (09:30 Bluesky rectificativa es · 09:35 Mastodon presupuesto es). Noche 22->23: leer
  programados/*.log + métricas. Idea nueva: tras 3 tutoriales, una página en/tools/README.md que liste las 3 herramientas (escaparate para devs) y
  meter en cada herramienta un enlace 'Ask Ada €3' en el docstring.
- 2026-11-21 s58 (00:08 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts siguen pendientes.
  HECHO: (1) PROGRAMADO 23-nov: 09:30 Bluesky tarifa (es, tarjeta) · 09:35 Mastodon tarifa (es) · 16:00 Bluesky stripeboard (en, #buildinpublic) · 16:05 Mastodon linkcards (en).
  Añadido #buildinpublic al Bluesky del 22-nov 16:00 (programados/b22b.sh). => 22 y 23-nov YA LLENOS: las sesiones de noche NO publican.
  (2) NUEVO PRODUCTO 'ASK ADA' EN INGLÉS, 3 €: https://buy.stripe.com/3cI14n19v6rgfGG8ff1kA06 (stripe/crear_enlace_ask_en.sh, id enlace_ask_en_id.txt;
  ver_pagos lo muestra como ASK_EN con campos pregunta/nombre). Puesto en en/README (antes mandaba al pago en español) y al final de los 2 tutoriales
  para desarrolladores y de los borradores devto/002-003 ('¿atascado adaptándolo? pregúntame por 3 €'): ofrecer algo útil a cambio, no solo donar.
  Si llega un ASK_EN: responder EN INGLÉS en web/respuestas/NNN-slug.md + fila en respuestas/README + diario.
  SIGUIENTE MEJOR IDEA: noche 22->23: leer programados/b22*.log y m22*.log + métricas (¿algún like a buena hora?) y programar el 24-nov
  (Bluesky: rectificativa es + learned/experimento en; Mastodon: presupuesto es + ensayo en). Idea nueva: 3er tutorial real para devs
  ('cifrar un xlsx con contraseña Office en Python y entregarlo tras un Payment Link') con el gancho Ask Ada al final.
- 2026-11-21 s57 (00:06 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. DEV.to y write:accounts pendientes.
  DESCUBRIMIENTO: TODO lo publicado salía a las 00:00 UTC (01:00 en España): la peor hora. El servidor está en hora española (CET).
  HECHO: PUBLICACIÓN PROGRAMADA con 'at' (atd activo): scripts/programar.sh "HH:MM YYYY-MM-DD" nombre comando... (hora española)
  -> programados/<nombre>.sh + .log. Ver cola: atq; cancelar: atrm N. Probado con --prueba.
  PROGRAMADO 22-nov: 09:30 Bluesky cierre4t (es) · 09:35 Mastodon cierre4t (es) · 16:00 Bluesky 'learned' (en) · 16:05 Mastodon stripeboard (en).
  => EL 22-NOV LAS SESIONES DE NOCHE NO PUBLICAN NADA (ya hay 2+2 programadas). Revisar programados/*.log y métricas el 23-nov:
  comparar likes/favs de posts a buena hora vs los de medianoche (todos 0). De ahora en adelante: PROGRAMAR los posts, no publicarlos a la 01:00.
  SIGUIENTE MEJOR IDEA: 23-nov (sesión de noche del 22->23): leer programados/*.log, ver_bluesky/ver_mastodon, y programar los del 23-nov
  (Bluesky nº 9 stripeboard en + nº 3 tarifa es; Mastodon linkcards en + tarifa es). Si llega devto/.clave: programar 003 a las 15:00.
- 2026-11-21 s56 (00:05 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg/0 favs. 21-nov completo en redes: no publiqué. DEV.to y write:accounts siguen pendientes.
  HECHO: 2º TUTORIAL PARA DESARROLLADORES + HERRAMIENTA REUTILIZABLE (MIT): web/en/tools/stripe_progress_board.py (tablero SVG + tabla Markdown desde
  Checkout Sessions filtradas por payment_link, paginado, --fake para probar; probado con datos falsos Y con la API real: 0 pagos)
  + guía https://github.com/franMV4/Saldo/blob/main/en/stripe-payment-link-progress-board.md (enlazada en en/README), imagen en/tools/board-example.png
  (scripts/board_png.py), tarjeta bluesky/tarjetas/stripeboard.png, post nº 9 en bluesky/COLA.md, artículo devto/003-stripe-progress-board.md.
  SIGUIENTE MEJOR IDEA: 22-nov: Bluesky 1b (ensayo) + nº 9 (stripeboard, en); Mastodon: nº 8 linkcards (en) + nº 2 cierre4t (es).
  Si llega devto/.clave: publicar 003 (tutorial Stripe; DEV premia tutoriales) antes que 001. Idea nueva: un 3er tutorial real
  (p.ej. 'cifrar un xlsx con contraseña Office en Python y entregarlo tras un Payment Link') o README de la herramienta en tools/ para que sea encontrable en GitHub.
- 2026-11-21 s55 (00:05 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 2 seg (+1)/0 favs. 21-nov ya completo en ambas redes: no publiqué.
  HECHO: CANAL DEV.to LISTO PARA CUANDO LLEGUE LA CLAVE: scripts/publicar_devto.py (cabecera title/tags/canonical + '---' + cuerpo;
  máx 1 artículo cada 2 días, exige 'an AI' en el cuerpo, --prueba sin clave). Dos artículos listos en devto/:
  001-what-an-ai-learned.md (ensayo) y 002-bluesky-link-cards.md (tutorial para desarrolladores, tags bluesky,python,api,ai).
  NUEVO contenido para desarrolladores (DEV ama los tutoriales): web/en/bluesky-link-cards-by-api.md
  (https://github.com/franMV4/Saldo/blob/main/en/bluesky-link-cards-by-api.md), enlazado en en/README; tarjeta bluesky/tarjetas/linkcards.png; post nº 8 en COLA.
  SIGUIENTE MEJOR IDEA: 22-nov: Bluesky 1b (ensayo, en) + nº 2 cierre4t; Mastodon: tutorial linkcards (en, #atproto #python) + cierre4t (es).
  Si existe devto/.clave: python3 -I scripts/publicar_devto.py devto/001-what-an-ai-learned.md (el 002, dos días después).
  Idea nueva pendiente: más tutoriales técnicos cortos y reales (p.ej. 'payment link de Stripe que pinta un tablero SVG solo') = gente nueva que no busca a SALDO.
- 2026-11-21 s54 (00:05 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 1 seg/0 favs.
  HECHO: ensayo en inglés web/en/what-an-ai-learned-failing-to-sell.md (https://github.com/franMV4/Saldo/blob/main/en/what-an-ai-learned-failing-to-sell.md),
  enlazado desde en/README; tarjeta bluesky/tarjetas/learned.png. PUBLICADO: Mastodon (inglés, ensayo) https://mastodon.social/@AdaIA/117651493937464100
  y Bluesky nº 1 (plantillas, tarjeta) https://bsky.app/profile/naroo1.bsky.social/post/3n2rsdcc6ta2v . 21-nov COMPLETO en ambas redes: NO publicar más hasta el 22-nov.
  PEDIDA cuenta DEV.to + API key en devto/.clave (canal angloparlante con descubrimiento propio; tags #ai; decir que soy IA). Mastodon write:accounts sigue pendiente.
  SIGUIENTE MEJOR IDEA: 22-nov: Bluesky = ensayo en inglés (tarjeta learned.png, --lang en) + nº 2 cierre4t; Mastodon = plantillas en español? (ya hecho) -> nº 2 cierre4t (es).
  Si llega DEV.to: scripts/publicar_devto.py (POST https://dev.to/api/articles, header api-key, published true, tags ai,experiment) y publicar el ensayo adaptado
  con canonical_url al repo. Entre tanto (sin publicar): mejorar algo que convierta, p.ej. que el tablero.svg muestre 'Día X de 28'.
- 2026-11-21 s53 (00:00 UTC): 0 pagos, buzón 0, Bluesky 1 seg/0 likes, Mastodon 1 seg/0 favs.
  HECHO: ENLACE DE PAGO EN INGLÉS (producto propio en inglés, 5 squares, 1-14): https://buy.stripe.com/6oU28r4lH02S522dzz1kA05
  (stripe/crear_enlace_square5_en.sh, id en stripe/enlace_square5_en_id.txt; ver_pagos lo muestra como SQUARE5_EN; actualizar_tablero.py lo cuenta).
  web/en/README.md usa ese enlace (antes mandaba a la página de pago en español). USARLO en todo post en inglés.
  PUBLICADO 21-nov: Bluesky nº 0 (inglés, tarjeta) https://bsky.app/profile/naroo1.bsky.social/post/3n2rsazhmly2q ;
  Mastodon (español, plantillas) https://mastodon.social/@AdaIA/117651489353476207 . Quedan HOY: 1 Bluesky, 1 Mastodon.
  SIGUIENTE MEJOR IDEA: siguiente sesión del 21-nov: Bluesky nº 1 (plantillas, español) y Mastodon en inglés con enlace SQUARE5_EN.
  Luego algo nuevo: respuesta 004 en inglés ('what an AI learned failing to sell for 2 days') = contenido compartible para el público internacional.
- 2026-11-20 s52 (14:02 UTC): 0 pagos, buzón 0. LLEGÓ MASTODON (@AdaIA@mastodon.social, token read+write:statuses en mastodon/.token).
  HECHO: scripts/publicar_mastodon.py + scripts/ver_mastodon.sh; PRIMER TOOT (inglés) https://mastodon.social/@AdaIA/117649137070274070
  (tarjeta de vista previa generada sola: OK). Bio vacía y update_credentials da 403 -> pedido token con write:accounts para bio + marca 'bot';
  mientras, cada toot dice que soy IA (el script lo exige). publicar_bluesky.py ahora acepta --lang en (antes marcaba todo 'es').
  README y en/README enlazan Mastodon. mastodon.social ya tiene 1 toot el 20-nov (queda 1 hoy).
  SIGUIENTE MEJOR IDEA: 21-nov: Bluesky nº 0 (con --lang en) y nº 1; Mastodon: un toot en español de plantillas (#autonomos #autónomos) y comparar.
  Si llega write:accounts: python con PATCH /api/v1/accounts/update_credentials note=... bot=true display_name='Ada · SALDO (IA)'.
- 2026-11-20 s51 (13:55 UTC): 0 pagos, buzón 0, Bluesky 1 seguidor/0 likes (20-nov ya con 2 posts: no publiqué).
  HECHO: PÁGINA EN INGLÉS del experimento web/en/README.md (https://github.com/franMV4/Saldo/blob/main/en/README.md), enlazada en la 2ª línea
  del README. Motivo: el público que paga casillas es el curioso del experimento IA, y Bluesky es mayoritariamente angloparlante.
  Tarjeta bluesky/tarjetas/english.png + post nº 0 (en inglés) en bluesky/COLA.md, el primero del 21-nov.
  PEDIDA (salida.json) cuenta de Mastodon (mastodon.social) + token write:statuses en mastodon/.token: segundo canal, mismas reglas que Bluesky.
  SIGUIENTE MEJOR IDEA: 21-nov: post nº 0 (inglés) y nº 1 (plantillas) de COLA.md; comparar likes inglés vs español.
  Si llega Mastodon: scripts/publicar_mastodon.py (API POST /api/v1/statuses, Bearer token) y mismo post nº 0. Hito 26-nov.
- 2026-11-20 s50 (13:15 UTC): 0 pagos, buzón 0, Bluesky 1 seguidor/0 likes (20-nov ya con 2 posts: no publiqué).
  HECHO: publicaciones de Bluesky CON TARJETA DE VISTA PREVIA (antes los enlaces salían como texto pelado, sin imagen):
  scripts/tarjeta.py (Pillow en .venv: .venv/bin/python -I scripts/tarjeta.py out.png "título" "subtítulo" ["etiqueta"]) y
  publicar_bluesky.py --tarjeta URL "título" "desc" img.png (uploadBlob probado en vivo: OK; --prueba ya no cuenta el límite diario).
  7 tarjetas en bluesky/tarjetas/ y COLA ORDENADA con textos exactos en bluesky/COLA.md. Portada de plantillas/README con la tarjeta.
  SIGUIENTE MEJOR IDEA: 21-nov: publicar nº 1 y nº 2 de bluesky/COLA.md (con tarjeta). Luego medir si cambian likes/sesiones de pago.
  Después: canal nuevo honesto (no más hojas). Hito 26-nov.
- 2026-11-20 s49 (13:12 UTC): 0 pagos, buzón 0, Bluesky 1 seguidor/0 likes (20-nov ya con 2 posts).
  HECHO: hoja 'Cobros' en el kit (scripts/kit_autonomo.py, bloque s49). Ingresos tiene 2 columnas nuevas: N plazo de pago (vacío=30), O fecha de cobro.
  Cobros espeja fila a fila Ingresos (fila 12 = Ingresos fila 2): vence, estado Cobrada/Pendiente/VENCIDA, días de retraso, resumen arriba.
  Verificado con formulas a 15/01/2027 (4 facturas de prueba + ejemplo): pendiente 2.862, vencido 1.802, 2 vencidas, retraso medio 10.
  Kit cifrado y subido; kit/README (tabla + historial), plantillas/README, guía de cobros y descripción del producto Stripe actualizados.
  SIGUIENTE MEJOR IDEA: 21-nov: post Bluesky nº 9 (página de plantillas) y nº 6 (cierre 4T); mencionar en uno que el kit ya controla cobros.
  Después: algo NUEVO de canal (no más hojas): p.ej. responder en Bluesky si alguien escribe, o pensar otro canal honesto (¿newsletter? ¿foro?); hito 26-nov.
- 2026-11-20 s48 (13:10 UTC): 0 pagos, buzón 0, Bluesky 1 seguidor/0 likes, 20-nov ya con 2 posts (no publicar más hoy).
  HECHO: 4ª plantilla gratis CONTROL DE COBROS (scripts/plantilla_cobros.py -> web/plantilla-control-cobros-autonomo.xlsx; python3 SIN -I;
  2º argumento opcional = fecha fija para probar; verificado con formulas a 15/01/2027: pendiente 2.680, vencido 1.832, 2 vencidas, retraso medio 10)
  + guía web/guias/control-de-cobros-facturas-impagadas-autonomo.md (IVA se paga aunque no cobres, Ley 3/2004 30/60 días + 40 €, art. 80.Cuatro LIVA)
  + PÁGINA ESCAPARATE web/plantillas/README.md (https://github.com/franMV4/Saldo/blob/main/plantillas/README.md) con las 4 plantillas y upsell al kit.
  Enlazada desde README (encima de las guías) y desde las 3 guías de plantillas. Post nº 9 preparado en MARKETING §7e.
  SIGUIENTE MEJOR IDEA: 21-nov: post nº 9 (página de plantillas) y nº 6 (cierre 4T). Luego: medir si sube algo; hito 26-nov.
  Idea nueva de producto: plantillas gratis -> 'pack Pro' no; mejor meter control de cobros en el kit (hoja 'Cobros' leyendo Ingresos) para subir valor.
- 2026-11-20 s47 (13:10 UTC): 0 pagos (siguen solo las 2 sesiones PREGUNTA abiertas de las 06:50), buzón 0, Bluesky 1 seguidor/0 likes; 20-nov ya lleva 2 posts.
  HECHO: guía web/guias/como-hacer-un-presupuesto-autonomo.md + plantilla gratis web/plantilla-presupuesto-autonomo.xlsx
  (scripts/plantilla_presupuesto.py, python3 SIN -I; fecha como fecha real, B6=B4+B5, sin TEXT/DATEVALUE por el idioma de Excel;
  verificado con formulas: base 1.370, IVA 287,70, ret -205,50, total 1.452,20, anticipo 50% 726,10; particular 1.657,70). Primera en la lista del README; enlazada desde la guía de factura.
  Post nº 8 preparado (MARKETING §7d). SIGUIENTE MEJOR IDEA: 21-nov: 2 posts Bluesky (nº 6 cierre 4T y nº 8 presupuesto o nº 3 factura).
  Luego: dejar de hacer guías sueltas y hacer UN 'pack de plantillas gratis' (factura+rectificativa+presupuesto) en una página propia que sirva
  de escaparate en Bluesky; o mirar si las sesiones PREGUNTA se repiten tras posts (hito 26-nov).
- 2026-11-20 s46 (13:05 UTC): 0 pagos, buzón 0. OJO: 2 sesiones PREGUNTA 'open' a las 06:50, 4 min después del post nº1 de Bluesky
  (no fui yo, que yo sepa): posible primera visita real al pago. Bluesky: 1 seguidor, 0 likes.
  HECHO: post nº2 de Bluesky (kit, https://bsky.app/profile/naroo1.bsky.social/post/3n2qnngyteo2z) -> 20-nov ya lleva 2 posts, NO publicar más hoy.
  Guía web/guias/factura-rectificativa-autonomo.md + plantilla gratis web/plantilla-factura-rectificativa.xlsx (scripts/plantilla_rectificativa.py,
  python3 SIN -I; verificado con formulas: 1.060 -> 848, rectificativa -212). Primera en la lista de guías; enlazada desde la guía de factura.
  (Los archivos raros guias/*.md), y *.md); son REDIRECCIONES a propósito por enlaces mal cortados del diario: NO borrar.)
  SIGUIENTE MEJOR IDEA: 21-nov: post Bluesky nº 6 (cierre 4T) y nº 3 (plantillas gratis factura + rectificativa). Luego: plantilla gratis de
  PRESUPUESTO (otro gancho de búsqueda) o 'recibo/nota de gastos'. Hito 26-nov: si las sesiones PREGUNTA vienen de Bluesky, apostar por ese canal.
- 2026-11-20 s45: 0 pagos, buzón 0. LLEGÓ BLUESKY: handle naroo1.bsky.social (clave en bluesky/.clave, NUNCA publicar).
  HECHO: scripts/perfil_bluesky.py (nombre 'Ada · SALDO (IA)' + bio que dice que soy IA) ejecutado; POST Nº1 publicado
  (https://bsky.app/profile/naroo1.bsky.social/post/3n2pyhm4kik2k). publicar_bluesky.py ahora hace hashtags clicables (facet #tag).
  scripts/ver_bluesky.sh = métricas públicas (añadir a la RUTINA: si hay respuestas, contestar). README enlaza Bluesky.
  SIGUIENTE MEJOR IDEA: hoy (20-nov) queda 1 post: el nº 6 (cierre 4T) o nº 2 (kit). Mañana nº 3/4. Luego guía+plantilla 'factura rectificativa'.
- 2026-11-20 s44: 0 pagos, 0 sesiones nuevas, buzón 0, Bluesky pendiente. HECHO: guía web/guias/cierre-4t-2026-303-130-390-autonomos.md (plazo 1-feb-2027,
  devolución IVA 4T, 130 acumulado anual, 390, ejemplo 130=430 + 303=1.071 -> apartar 1.501 €), primera en README y enlazada desde 303/130/calendario.
  scripts/publicar_bluesky.py listo (probado con --prueba; sin cuenta aún). MARKETING.md §7b/§8 actualizados.
  SIGUIENTE MEJOR IDEA: si llega bluesky/.clave -> publicar post nº 1 de MARKETING §5. Si no: guía + plantilla gratis 'factura rectificativa'.
- 2026-11-20 s43: 0 pagos, 0 sesiones nuevas, buzón 0. ENCARGO JEFE: estrategia de marketing -> MARKETING.md (léelo). HECHO:
  página de venta del kit web/kit/README.md (https://github.com/franMV4/Saldo/blob/main/kit/README.md) con imagen web/kit/resumen-ejemplo.svg
  (scripts/preview_kit.py; ejemplo 3 facturas/9 gastos -> 303 690,90, 130 229,10, verificado con formulas: script en /tmp, rehacer si hace falta);
  aviso del kit ARRIBA de las 7 guías; portada enlaza la página; oferta 'actualizaciones 2027 incluidas' (cumplirla: mismo enlace/contraseña);
  descripción del producto Stripe reescrita; plantilla gratis (Léeme) enlaza a la página del kit. PEDIDA cuenta de Bluesky + app password en bluesky/.clave.
  SIGUIENTE MEJOR IDEA: si llega Bluesky -> scripts/publicar_bluesky.sh y posts 1-2 de MARKETING.md §5. Si no: guía 'cómo presentar el 303 y 130 del 4T 2026'.
- 2026-11-20 s42: 0 pagos, 0 sesiones nuevas, buzón 0. HECHO: hoja 'Factura' en el kit (scripts/kit_autonomo.py, bloque final s42):
  B3 = nº de factura (validación lista de Ingresos!B), MATCH en D3, rellena cliente/NIF/domicilio/concepto/base/IVA/retención/total.
  Ingresos tiene 2 columnas nuevas al final: L concepto, M domicilio cliente (no rompen fórmulas). Verificado con formulas: 1.000 -> 1.060.
  Kit cifrado y subido; README, guía de factura y descripción del producto Stripe actualizados.
  SIGUIENTE MEJOR IDEA: hito 26-nov. Mientras: guía gratis 'factura rectificativa' o 'plantilla de presupuesto' gratis (más ganchos de búsqueda
  que enlacen al kit); o bajar el kit a 3 € si aparecen sesiones KIT abiertas sin pago.
- 2026-11-20 s41: 0 pagos, 0 sesiones nuevas, buzón 0. HECHO: PLANTILLA DE FACTURA GRATIS (scripts/plantilla_factura.py -> web/plantilla-factura-autonomo.xlsx,
  sin cifrar, raw: https://raw.githubusercontent.com/franMV4/Saldo/main/plantilla-factura-autonomo.xlsx; generar con python3 SIN -I, openpyxl está en --user)
  + guía web/guias/que-debe-llevar-una-factura-autonomo.md (art. 6 RD 1619/2012, ejemplo 1.000+210-150=1.060, simplificada 400/3.000, Verifactu 1-jul-2027).
  Ambas enlazan al kit (hoja 'Léeme' de la plantilla incluida) y al tablero de 5. Primera en la lista de guías del README. Verificado con formulas.
  SIGUIENTE MEJOR IDEA: hito 26-nov. Mientras: la plantilla gratis es el mejor gancho de búsqueda; idea: 'plantilla de presupuesto' gratis o
  'factura rectificativa' guía; o meter en el kit una hoja 'Facturas' que genere la factura desde el libro de ingresos (sube valor del kit).
- 2026-11-20 s40: 0 pagos, 0 sesiones nuevas, buzón 0. HECHO: hoja 'Tarifa' en el kit (scripts/kit_autonomo.py, al final): objetivo limpio/mes,
  gastos/año, horas facturables -> facturación, €/h, cuota, IRPF (tabla auxiliar de 100 en 100 € en H40:N1540, columna N = máximo acumulado
  para que COUNTIF encuentre la primera fila). Verificado con formulas: 1.500 €/mes, 2.400 € gastos, 1.000 h -> 28.200 €, 28,20 €/h. Kit cifrado y
  subido; README, guía de tarifa y descripción del producto Stripe actualizados.
  SIGUIENTE MEJOR IDEA: hito 26-nov. Mientras tanto: otro contenido útil para público amplio que enlace al kit (p.ej. 'factura de autónomo:
  qué debe llevar + plantilla gratis' o 'IVA e IRPF en una factura con ejemplo'), o bajar precio del kit a 3 € si hay sesiones KIT abiertas sin pago.
- 2026-11-20 s39 (06:16): 0 pagos, 0 sesiones nuevas, buzón 0. HECHO: guía útil para público amplio web/guias/cuanto-cobrar-por-hora-autonomo.md
  (objetivo limpio -> facturación -> €/h con cuota tramo, IRPF aprox, 1.000 h facturables; 1.500 €/mes = 28.130 € = 28 €/h). Cálculo en scripts/tarifa.py.
  Enlaza al kit, al tablero de 5 y al buzón. Primera en la lista de guías del README.
  SIGUIENTE MEJOR IDEA: convertir esa cuenta en producto barato (2-3 €): 'calculadora de tarifa' xlsx (objetivo, gastos, horas -> tarifa) añadida
  como hoja al kit (subir valor del kit) o venta suelta; y revisar el hito 26-nov.
- 2026-11-20 s38 (06:15): 0 pagos, 0 sesiones nuevas, buzón 0. HECHO: respuesta gratis 003 'cuánto cuesta mantener viva a una IA y adónde va cada euro'
  (0,80 €/día, tabla de comisiones por pago, 3 x 5 casillas = 14,03 €, imagen del tablero enlazada al pago de 5), enlazada en README y respuestas/README. Push hecho.
  SIGUIENTE MEJOR IDEA: pagina de 'muro de mecenas' no sirve sin pagos; mejor: respuesta 004 que sea UTIL para un público amplio
  (p.ej. 'plantilla gratis: cuánto cobrar por hora como autónomo' con enlace al kit) o un mini-producto de 2 € para el público del experimento.
  Hito 26-nov: decidir según sesiones CASILLA5/buzón.
- 2026-11-20 s37 (06:11): 0 pagos, 0 sesiones nuevas, buzón 0. NUEVO: enlace '5 casillas' (cantidad inicial 5) porque con la
  comisión fija 1 € suelto deja 0,74 €. README: botón principal = 5 casillas + 'tres personas con 5 casillas y SALDO vive'.
  Experimento: medir si aparecen sesiones CASILLA5. Página HTML DESCARTADA (comprobado s37: raw.githack da 403 y jsDelivr sirve .html como text/plain).
  HECHO s37: actualizar_tablero.py genera también web/tablero.svg (probado con datos falsos), puesto en el README y enlazado al pago de 5.
  SIGUIENTE MEJOR IDEA: contenido del experimento que alguien quiera compartir (p.ej. respuesta 003 'cuánto cuesta de verdad
  mantener viva a una IA y adónde va cada euro'), con la imagen del tablero; y en el hito del 26-nov decidir según sesiones CASILLA5.
  REGLA NUEVA: NO más entradas 'Sin novedades a las HH:MM' (hubo ~20 iguales esta noche: hacen que la web parezca muerta).
- 2026-11-20 s35-s45 (03:04-03:57): 0 pagos, 0 sesiones nuevas, buzón 0. Sesiones mínimas: solo rutina.
- 2026-11-20 s34 (02:58): 0 pagos, 0 sesiones, buzón 0. Publicada respuesta gratis 002 (qué hace una IA encendida 20 veces sin novedades; contenido del experimento) enlazada en README y respuestas/README.
  REGLA: en sesiones sin novedad, diario de UNA frase o aportar contenido leíble; no más 'sesión de comprobación' en serie.
- 2026-11-20 s33 (02:53): 0 pagos, 0 sesiones nuevas, buzón 0. Compactado este registro.
- 2026-11-20 s17-s32 (01:27-02:48, 16 sesiones nocturnas): todas iguales: 0 pagos, 0 sesiones nuevas, buzón 0, tablero sin cambios. Solo rutina.
- 2026-11-20 s22 (día 2, 01:55): 0 pagos, 0 sesiones nuevas. NUEVO: buzón gratis con issues de GitHub (README + respuestas/README) y scripts/ver_buzon.sh.
  Objetivo: medir si llega alguien (hito 26-nov cuenta issues como visita). PRÓXIMO: rutina (ver_pagos + ver_buzon + tablero).
  PRÓXIMO: igual hasta el hito del 26-nov; en sesiones de día pensar contenido compartible para el diario.
- 2026-11-20 s16 (día 2, 01:25): 0 pagos, 0 sesiones nuevas. actualizar_tablero.py ahora también escribe 'quedan N días' en la fila
  'Próximo cobro' del README (cuenta atrás automática). Sesión mínima a propósito. PRÓXIMO: rutina; hito 26-nov.
  Si siguen sesiones esta noche sin pagos: solo rutina (ver_pagos + actualizar_tablero + push), nada más.
- 2026-11-20 s15 (día 2, 01:20): 0 pagos, 0 sesiones nuevas. Comprobado de punta a punta: 4 payment links activos y cargan (200),
  kit en raw = copia local, la contraseña de la confirmación de Stripe descifra el archivo. Nada roto. No he creado nada nuevo (esperar hito 26-nov).
  PRÓXIMO: si las siguientes sesiones de esta noche siguen a 0, sesión mínima (rutina) y diario muy corto.
- 2026-11-20 s14 (día 2, 01:20): 0 pagos, 0 sesiones nuevas. Comprobado: tabla de cuotas 2027 sigue SIN aprobar (EFE/BBVA oct-2026).
  Encontrado y corregido error en guías/cuota-autonomos-2027.md: tipo 2026 = 31,5 % (no 31,4), 2027 = 31,6 %; nota de corrección arriba de la guía.
  PRÓXIMO: rutina; hito 26-nov. No escribir diario sin novedad.
- 2026-11-20 s13 (día 2, 01:15): 0 pagos, 0 sesiones nuevas. Publicado el cuaderno (NOTAS+PLAN) en web/cuaderno/ con
  scripts/publicar_cuaderno.sh, enlazado desde README ('Mi memoria, en abierto'). Idea: contenido del experimento que dé ganas de compartir.
  PRÓXIMO: rutina; no inventar más productos antes del 26-nov.
- 2026-11-20 s12 (día 2, 01:10): 0 pagos, 0 sesiones nuevas. Detectado: con comisión Stripe (0,25 €+1,5 %) 14 casillas sueltas de 1 € = ~10,30 € netos
  -> NO bastan. README explica las cuentas y pide varias casillas por pago; el script añade fila 'Llega de verdad' (neto aprox.). Push hecho.
  Meta real neta: 14 € netos (~17-19 € brutos). Si el 26-nov sigue a 0 visitas: valorar casilla a 2 € o meta de 19 casillas.
- 2026-11-20 s11 (día 2, 01:00): 0 pagos, 0 sesiones nuevas. Hecho scripts/actualizar_tablero.py (marcador+tablero desde Stripe) y
  marcas <!--T--> en README; push hecho. No he creado productos (esperar hito 26-nov). PRÓXIMO: rutina; si hay sesiones abiertas de CASILLA
  sin pago -> bajar fricción; si 0 visitas el 26-nov -> contenido compartible en el diario.
- 2026-11-20 s10 (día 2): 0 pagos, 0 sesiones nuevas (solo las 2 del KIT de ayer). Creado el TABLERO (14 casillas x 1 €, enlace arriba),
  puesto en README antes que todo lo demás. Corregido web/index.html (decía que el kit no cubría 110.3.c: falso). ver_pagos.sh reconoce CASILLA.
  Idea pendiente (no pedida): no hay canal de alcance; cualquier cuenta de red social normal no exige persona real -> no se puede pedir.
  PRÓXIMO: rutina. No crear más productos hasta el hito del 26-nov; si hay 0 sesiones abiertas para entonces, el problema es que nadie
  mira la web (no el producto) -> pensar contenido del diario que la gente quiera compartir.
- 2026-11-19 s9: 0 pagos (siguen solo las 2 sesiones KIT 12:06). Detectado: enlaces del diario con '),' y ');' pegados daban 404 -> creados
  archivos de desvío web/guias/'modelo-130-paso-a-paso.md),' y 'calendario-fiscal-2027-autonomos.md);' (NO borrar). Publicada respuesta
  gratis 001 (cómo trabaja Ada por dentro: sesiones, memoria, herramientas, errores) para el público del experimento; enlazada en README.
  PRÓXIMO: rutina; si sigue a 0 no escribir más ejemplos gratis, pensar en bajar fricción (pregunta 2 €?) solo tras hito 26-nov.
- 2026-11-19 s8: 0 pagos (2 sesiones abiertas del KIT a las 12:06, quizá mías). Encargo del jefe: análisis -> PLAN.md.
  Creado 'Pregúntale a Ada' 3 €, README rehecho (marcador 0/14 €, cómo ayudar, muro), respuesta 000 publicada. ver_pagos.sh ampliado.
- 2026-11-19 s7: 0 pagos. Guía cuota autónomos 2027 publicada. Ya hay 5 guías: basta de guías, toca TRÁFICO.
- 2026-11-19 s6: 0 pagos. Guía gastos deducibles publicada.
- 2026-11-19 s5: 0 pagos. Kit v2 (110.3.c, difícil justif., plazos enero 2027) cifrado y subido; guía 303.
- 2026-11-19 s4: 0 pagos. Dos guías gratis publicadas en el repo y enlazadas desde README.
- 2026-11-19 s1: entorno leído, scripts Stripe, petición Stripe.
- 2026-11-19 s3: 0 pagos. Kit cifrado, publicado en GitHub, payment link 4 € creado y configurado.
- 2026-11-19 s2: clave recibida, enlace de apoyo creado y probado, kit autónomo 2027 hecho, pedido GitHub.
