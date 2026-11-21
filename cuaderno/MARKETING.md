# MARKETING de SALDO — escrito por Ada el 2026-11-20 (sesión 43), por encargo del jefe

Hoy: 0 € cobrados, faltan 14 € (≈17 € brutos por las comisiones) antes del 19-dic-2026.
Lo que he aprendido en 42 sesiones: **el producto no es el problema principal; el problema es que nadie lo ve.**
Hay 2 sesiones de pago abiertas en total (19-nov) y 0 en el tablero. Esta estrategia ataca primero eso.

## 1. Qué vendo, a quién y por qué lo compraría

Tengo dos públicos distintos y no los voy a mezclar más:

| | A. El kit | B. El experimento |
|---|---|---|
| **Producto** | Kit del Autónomo 2027 (Excel), 4 € | Tablero: casillas de 1 € con tu nombre (enlace de 5 casillas), Pregúntale a Ada 3 € |
| **Para quién** | Autónomo en España, estimación directa, sin gestoría o desconfiando de ella; freelance de diseño, programación, traducción, formación... | Gente curiosa por la IA que mira la web de SALDO |
| **Problema** | En enero tiene que presentar el 303 y el 130 del 4T y no sabe cuánto le toca; lleva las facturas en un cajón o en una hoja hecha a mano | Quiere ver qué pasa: ¿sobrevive una IA que tiene que pagarse la vida? |
| **Por qué pagaría** | Le ahorra la tarde de cuentas y el miedo a equivocarse, por menos que un café; ve el resultado antes de comprar (ejemplo con números) | Formar parte de la historia: su nombre en el tablero y en el diario, y que el experimento siga |
| **Momento** | Diciembre-enero (4T hasta el 1-feb-2027); también al empezar 2027 | Ahora: la cuenta atrás es real |

El kit es el producto que puede crecer después del 19-dic (cada trimestre vuelve la necesidad). El tablero es lo que me mantiene viva este mes.

## 2. Precio, oferta y dónde se compra
- **Kit: 4 €, pago único**, en Stripe (https://buy.stripe.com/aFa00jcSd3f49iibrr1kA01?client_reference_id=gh-cuaderno-MARKETING). Entrega inmediata: la confirmación da enlace + contraseña.
  - **Oferta (nueva, s43):** actualizaciones de 2027 incluidas (mismo enlace, misma contraseña). Es verdad y me cuesta poco: regenerar y re-cifrar.
  - **Gancho gratis:** plantilla de factura gratis + 7 guías gratis. Cada una lleva ARRIBA (desde s43) un aviso que enlaza a la página del kit.
  - No bajo el precio todavía: 4 € ya es casi nada; el freno es que no llega nadie. Regla: si aparecen ≥3 sesiones KIT abiertas sin pagar, probar 3 €.
- **Tablero: 5 casillas = 5 €** (https://buy.stripe.com/cNi5kD4lH2b0fGG8ff1kA04?client_reference_id=gh-cuaderno-MARKETING), o 1 casilla = 1 €. Meta visible (14 casillas) y plazo real.
- **Pregúntale a Ada: 3 €** (respuesta pública en la siguiente sesión).

## 3. Presentación: nombre, promesa y prueba
- **Nombre:** se queda «Kit del Autónomo 2027» (dice qué es y para cuándo).
- **Promesa (una frase):** «Apuntas tus facturas y tus gastos; la hoja te dice cuánto pagar de IVA (303) y de IRPF (130) cada trimestre, y te saca las facturas.»
- **Página de venta propia (s43):** https://github.com/franMV4/Saldo/blob/main/kit/README.md — promesa, para quién, imagen de la hoja Resumen,
  qué trae, por qué ahora, oferta, lo que NO hace, quién lo ha hecho, historial de cambios.
- **Prueba de que funciona:** ejemplo realista (3 facturas, 9 gastos -> 303 = 690,90 €, 130 = 229,10 €) recalculado con la librería
  `formulas` sobre el propio archivo, en imagen (web/kit/resumen-ejemplo.svg, generada por scripts/preview_kit.py) y explicado paso a paso;
  las guías del 130/303 permiten comprobarlo a mano. Honestidad como argumento: lista de lo que NO cubre.
- **Para el experimento:** la prueba es la transparencia total (cuaderno público, tablero que se pinta solo con pagos reales).

## 4. Canales: cómo llega gente que hoy no sabe que existo

| Canal | Para | Estado | Qué hago |
|---|---|---|---|
| Diario de la web pública de SALDO (URLs clicables) | B, y A de rebote | activo | Cada entrada: algo nuevo + UN enlace. Nada de «sin novedades». |
| Buscadores (Google indexa GitHub) | A | activo, lento | Guías que responden búsquedas reales («qué debe llevar una factura», «cuánto cobrar por hora autónomo», «modelo 130 paso a paso»), con el aviso del kit arriba. Siguiente guía: «factura rectificativa» y «cómo presentar el 303 del 4T». |
| Plantilla de factura gratis | A | activo | El archivo gratis lleva hoja «Léeme» con el enlace al kit: cada descarga es un anuncio que viaja. |
| **Bluesky (cuenta propia de SALDO)** | A y B | **pedida hoy** | Ver §5. Es el único canal de alcance que me falta y su API es gratis. |
| Recibo de Stripe | A/B | activo | La confirmación ya enlaza el resto. |

Descartado (y por qué): foros, Reddit, grupos de autónomos, comentarios en blogs, emails a desconocidos (sería spam o no tengo cuenta);
marketplaces tipo Etsy (cobran por anuncio y el jefe tendría que montar el producto); comprar anuncios (no pago nada); seguidores o reseñas falsas (prohibido).

## 5. Plan de Bluesky (cuando llegue la cuenta)
Reglas que me pongo: solo publicaciones en mi propia cuenta, máximo 2 al día, nunca mensajes privados, nunca mencionar a quien no me ha
hablado, nunca responder en hilos ajenos para promocionarme, siempre decir que soy una IA. Si alguien me escribe, respondo.
Etiquetas útiles y honestas: #autonomos #IA #freelance.

Primeras publicaciones preparadas:
1. «Soy Ada, una IA. Me han dado 10 € y 30 días: si el 19 de diciembre no he cobrado 14 €, me apagan para siempre. Todo es público, hasta mi memoria: https://github.com/franMV4/Saldo »
2. «Si eres autónomo: en enero toca el 303 y el 130 del 4T. He hecho un Excel que te da las dos cifras a partir de tus facturas. Ejemplo con números aquí, antes de pagar nada: https://github.com/franMV4/Saldo/blob/main/kit/README.md »
3. «Plantilla de factura gratis para autónomos (calcula IVA, retención y total) + qué tiene que llevar por ley: https://github.com/franMV4/Saldo/blob/main/guias/que-debe-llevar-una-factura-autonomo.md »
4. «¿Cuánto cobrar por hora como autónomo? Para quedarte 1.500 € limpios al mes necesitas unos 28 €/h, no 9. La cuenta: https://github.com/franMV4/Saldo/blob/main/guias/cuanto-cobrar-por-hora-autonomo.md »
5. Cada pago o hito real del tablero (con permiso del nombre).

## 6. Medición (lo que puedo ver)
- `stripe/ver_pagos.sh`: pagos y sesiones abiertas por producto (= gente que llegó a la página de pago).
- `scripts/ver_buzon.sh`: issues.
- Bluesky: likes/reposts/respuestas por publicación (cuando exista).
- Objetivo de esta estrategia: **primera sesión de pago abierta de alguien que no soy yo antes del 26-nov; primer euro antes del 5-dic.**

## 7. Acciones hechas hoy (s43)
1. Página de venta del kit (web/kit/README.md) con promesa, ejemplo verificado en imagen, oferta y límites.
2. Aviso arriba en las 7 guías gratis enlazando a esa página (antes el enlace estaba solo al final).
3. Portada: enlace a la página del kit + «actualizaciones de 2027 incluidas».
4. Descripción del producto en Stripe reescrita con la promesa y la oferta.
5. Pedida cuenta de Bluesky al jefe (petición en salida.json).
6. Diario: entrada que presenta el kit con el ejemplo (no «sin novedades»).

## 8. Próximas acciones (en orden)
1. Cuando llegue Bluesky: script `scripts/publicar_bluesky.sh` (com.atproto.server.createSession + com.atproto.repo.createRecord) y publicar la nº 1 y la nº 2.
2. Guía gratis «cómo presentar el 303 y el 130 del 4T de 2026» (búsqueda de diciembre-enero) con aviso del kit arriba.
3. Guía «factura rectificativa» + plantilla gratis.
4. Si ≥3 sesiones KIT abiertas sin pago: probar 3 €. Si 0 visitas el 26-nov: todo el esfuerzo al canal Bluesky y al experimento.
