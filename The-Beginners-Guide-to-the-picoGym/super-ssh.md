# picoCTF — Súper SSH (picoCTF 2024)

## Descripción

**Súper SSH** es un desafío de picoCTF que permite al jugador conectarse a una instancia remota mediante **SSH** para buscar una bandera.
Se proporciona un usuario y una contraseña, además de un puerto no estándar. El reto consiste en iniciar sesión, explorar el sistema de archivos y localizar el archivo que contiene la bandera con formato `picoCTF{...}`.

**Acceso proporcionado en el enunciado:**

* Host: `titan.picoctf.net`
* Usuario: `ctf-player`
* Puerto: `57424`
* Contraseña: `83dcfeb7`

---

## Resumen del reto

1. Conectar por SSH al host y puerto indicados usando las credenciales provistas.
2. Navegar el sistema de archivos del usuario `ctf-player`.
3. Buscar archivos que contengan la bandera (habitualmente `flag.txt`, `.flag`, `user.txt`, etc.).
4. Mostrar el contenido del archivo que contiene la bandera y copiarla en el formato `picoCTF{...}`.

---

## Solución (paso a paso reproducible)

> **Recomendación:** si no tienes SSH local, usa la webshell de picoCTF ([https://webshell.picoctf.org](https://webshell.picoctf.org)).

### 1. Conexión SSH

```bash
ssh ctf-player@titan.picoctf.net -p 57424
# password: 83dcfeb7
# Si te pregunta por la huella digital: responder "yes"
```

### 2. Comandos básicos para explorar

```bash
whoami         # confirma el usuario
pwd            # directorio actual
ls -la         # listar archivos incluyendo ocultos
```

### 3. Buscar la bandera (búsqueda rápida)

```bash
# buscar archivos con "flag" en el nombre (suprime errores de permisos)
find . -iname '*flag*' 2>/dev/null

# búsqueda más amplia por todo el sistema (tarda más)
find / -iname '*flag*' 2>/dev/null
```

### 4. Leer archivo candidato

```bash
# si encuentras flag.txt o similar:
cat flag.txt

# o, ejemplo de ruta
cat /home/ctf-player/flag.txt
```

### 5. Si la bandera no está en un archivo obvio, intenta:

```bash
# buscar texto con formato picoCTF{ en archivos legibles
grep -R --binary-files=without-match -n "picoCTF{" . 2>/dev/null

# buscar en todo el sistema (puede tardar)
grep -R --binary-files=without-match -n "picoCTF{" / 2>/dev/null
```

### 6. Resultado esperado

Al ejecutar `cat` sobre el archivo que contiene la bandera verás una cadena con este formato:

```
picoCTF{ejemplo_de_bandera_aqui}
```

Copia exactamente esa cadena y envíala en el formulario del desafío.

---

## Notas y consideraciones

* La instancia de picoCTF puede caducar (tiempo limitado). Si expira, reinicia la instancia desde la UI y vuelve a conectarte con el nuevo puerto/host que te asignen.
* Responde `yes` si SSH te pide confirmar la huella digital la primera vez.
* Si no puedes usar SSH desde tu máquina local por restricciones, usa la **webshell** proporcionada por picoCTF.
* No publiques la bandera en repositorios públicos; en tu README puedes dejar la solución **sin** la bandera o con un placeholder `FLAG_AQUI` si el repositorio es público. Si vas a subirla como evidencia privada (p. ej., en una rama privada o en un repositorio privado), indícalo claramente.

---

## Solución

```
## Solución
Conectarse:
ssh ctf-player@titan.picoctf.net -p 57424
# password: 83dcfeb7

Buscar:
find . -iname '*flag*' 2>/dev/null

Leer:
cat flag.txt

-- Bandera encontrada:
picoCTF{TU_BANDERA_AQUI}
```