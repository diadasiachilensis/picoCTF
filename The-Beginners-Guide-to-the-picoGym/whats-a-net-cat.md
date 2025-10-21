# picoCTF — What’s a Net Cat? (picoCTF 2019)

## Descripción

**What’s a Net Cat?** es un desafío de picoCTF orientado a familiarizar al jugador con la herramienta **Netcat (nc)**.
El objetivo es conectarse a un servicio remoto usando **Netcat** en un puerto proporcionado para recibir un mensaje que incluye la bandera en formato `picoCTF{...}`.

**Acceso proporcionado en el enunciado:**

* Host: `jupiter.challenges.picoctf.org`
* Puerto: `41120`

---

## Teoría

**Netcat** (a menudo `nc`) es una utilidad de red tipo *Swiss Army knife* que permite abrir conexiones TCP o UDP, escuchar puertos, y transferir datos de forma sencilla. Es extremadamente útil en pruebas de red, debugging y CTFs porque permite:

* Conectarse a servicios remotos y recibir/saludar datos.
* Crear un servidor simple que escuche en un puerto.
* Redirigir entrada/salida entre sockets y archivos o procesos.

Netcat actúa como cliente/servidor de sockets; cuando te conectas como cliente, establece una sesión TCP/UDP con el host/puerto y transmite lo que el servidor envía.

---

### ¿Cómo funciona?

1. **Establecer conexión TCP/UDP:**

   * Ejecutas `nc <host> <port>` y Netcat abre un socket hacia ese destino.
   * Si el servicio en el host escucha en ese puerto, se establece la conexión y comienza el intercambio de datos.

2. **Enviar/Recibir datos:**

   * Por defecto, Netcat conecta la entrada estándar (tu teclado) y la salida estándar (tu terminal) al socket.
   * Cualquier texto que el servidor envíe lo verás en tu terminal; puedes redirigir esa salida a un archivo.

3. **Modo escucha (opcional):**

   * `nc -l -p <port>` hace que Netcat escuche en un puerto y acepte conexiones entrantes (útil para pruebas locales).

---

### Ejemplos de usos comunes

* Conectarse a un servicio remoto:
  `nc host.example.com 1234`

* Guardar la respuesta del servidor en un archivo:
  `nc host.example.com 1234 > salida.txt`

* Escuchar en un puerto y servir un archivo:
  `nc -l -p 8080 < archivo.html`

---

## Resumen del reto

1. Conectarse al host y puerto indicados usando `nc`.
2. Leer el texto que el servicio remoto envía (en él estará la bandera).
3. Copiar la cadena con formato `picoCTF{...}` y subirla como solución.

---

## Solución (paso a paso reproducible)

> **Recomendación:** si no puedes usar una terminal local, usa la webshell o la consola proporcionada por picoCTF.

### 1. Conexión con Netcat

Abre tu terminal y ejecuta:

```bash
nc jupiter.challenges.picoctf.org 41120
```

* `nc` → comando Netcat.
* `jupiter.challenges.picoctf.org` → host del desafío.
* `41120` → puerto indicado.

### 2. Interpretar la respuesta

Al conectarte, deberías ver una salida en tu terminal con un mensaje del servicio y la bandera, por ejemplo:

```
Welcome to Netcat training!
Here is your flag:
picoCTF{ejemplo_de_bandera}
```

### 3. Guardar la salida (opcional)

Si prefieres guardar la respuesta a un archivo para revisarla con calma:

```bash
nc jupiter.challenges.picoctf.org 41120 > respuesta.txt
# luego:
cat respuesta.txt
```

### 4. Copiar y enviar la bandera

Localiza la cadena con formato `picoCTF{...}`, cópiala exactamente y pégala en el formulario del desafío.

---

## Notas y consideraciones

* Netcat no cifra la conexión por sí misma; es una herramienta para probar/transferir datos. Nunca envíes información sensible sin cifrado.
* Si el servicio cierra la conexión inmediatamente, prueba a reconectar; algunas instancias son de corta duración.
* Usa `nc -v` (verbose) para ver información de conexión si necesitas debug:
  `nc -v jupiter.challenges.picoctf.org 41120`
* En sistemas donde `nc` no está instalado, puedes usar `ncat` (Nmap) o instalar netcat con el gestor de paquetes de tu sistema (`apt`, `brew`, etc.).
* No publiques la bandera en repositorios públicos. En tu README público deja un placeholder `FLAG_AQUI` si necesitas mostrar evidencia.

---

## Solución

```
## Solución
Conectarse:
nc jupiter.challenges.picoctf.org 41120

Leer la salida en pantalla:
# recibirás un mensaje que contiene la bandera

Alternativa: guardar salida en archivo:
nc jupiter.challenges.picoctf.org 41120 > respuesta.txt
cat respuesta.txt

-- Bandera encontrada:
picoCTF{TU_BANDERA_AQUI}
```

---

¿Quieres que también te genere una **imagen/diagrama simple** que muestre el flujo (tu máquina ↔ servidor remoto) para incluir en el README? ¿O prefieres que lo deje listo para pegar en tu repo con un pequeño `badge` y el placeholder de la bandera?
