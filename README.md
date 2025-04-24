# 🤖 Guante Traductor de Lenguaje de Señas a Texto y Voz

Este proyecto consiste en el desarrollo de un guante inteligente capaz de traducir lenguaje de señas en tiempo real a texto y voz. Utiliza sensores flexibles para detectar los movimientos de los dedos, y convierte estos datos en información comprensible para usuarios que no conocen la lengua de señas.

## 🎯 Objetivo

Facilitar la comunicación entre personas con discapacidad auditiva y el resto de la población, rompiendo barreras lingüísticas mediante un sistema accesible, portable y en tiempo real.


## ⚙️ Cómo funciona

1. Cada dedo cuenta con un sensor flexible que mide la curvatura.
2. El ESP32 lee las señales analógicas de los sensores y determina la posición de cada dedo.
3. Estas posiciones se comparan con un conjunto de gestos predefinidos que representan letras o palabras.
4. El gesto identificado se muestra como texto (y opcionalmente se convierte en voz).
5. Los datos pueden ser enviados a una app o servidor en tiempo real.

## 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/guante-traductor-senas.git
cd guante-traductor-senas
