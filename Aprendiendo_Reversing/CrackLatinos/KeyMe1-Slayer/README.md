English:

This repository contains the comprehensive technical analysis and solution for **KeyMe #1**, authored by Slayer. It is a reverse engineering challenge focused on software validation analysis through Keygenning without modifying the original binary (*No patching allowed*).

## 📊 Challenge Overview
* **Crackme Author:** Slayer
* **Analyst:** KarasuRØØT
* **Analysis Date:** 09/19/2024
* **Rules:** Do not patch the binary. A keygen must be created.
* **Tools Used:** x64dbg (x32dbg), Notepad++, Python 3.

---

## 🔍 Technical Analysis

When executing the binary, the user interface shows three available buttons (`About`, `Check`, `Exit`) and a disabled/grayed-out **`Register`** button. The initial objective is to activate the registration phase and then successfully pass the key validation logic.

### Phase 1: Enabling the "Register" Button
By tracing the execution workflow using **x32dbg**, key Windows API calls were discovered:
* `OpenClipboard`
* `GetClipboardData`

The program directly evaluates the Windows clipboard content. 
* **Condition:** The clipboard must contain the exact, uppercase **Hostname** of the local machine where the crackme is currently running (e.g., `REVERW10`).
* Clicking **Check** while the Hostname is copied into the clipboard will trigger the binary to enable the **`-> Register <-`** button.

### Phase 2: `reg.key` File Validation
Once the registration button is active, the program triggers a `CreateFileA` routine seeking a specific license file named **`reg.key`** within its execution directory. This file must contain an exact size of **8 bytes of data**, structured in **Little Endian** format.

The internal validation algorithm operates as follows:
1.  **Hostname Checksum:** The program iterates through each character of the Hostname, calculating the hexadecimal sum of their ASCII values.
    * *Example:* For `REVERW10`, the hex sum (`52+45+56+45+52+57+31+30`) yields **`23C`**.
2.  **Bitwise Operation (XOR):** The crackme splits the 8 bytes retrieved from `reg.key` into two 4-byte registry chunks (`EAX` and `EDX`).
3.  **Final Comparison:** It executes an `XOR` operation between `EAX` and `EDX`. The mathematical output must precisely match the checksum value calculated from your Hostname (e.g., `23C`).

Using the mathematical property of the XOR operation ($A \oplus B = C \implies A \oplus C = B$), we can supply a fixed arbitrary constant for one block (such as decimal `1234` / hex `4D2`), allowing us to easily solve for our unknown variable to match target value `23C`.

---

## 🛠️ `reg.key` File Structure (Example)

For the Hostname `REVERW10` (Checksum = `23C`), using the decimal constant `1234` as our static base value, the required program calculation outputs `4D26EE`. Padding the remaining missing bytes up to the mandatory 8 bytes and applying **Little Endian** formatting, the exact hex bytes inside `reg.key` must look like this:

```text
EE 06 00 00 D2 04 00 00

---------------------------------------------------
---------------------------------------------------
---------------------------------------------------

Español:
Este repositorio contiene el análisis detallado y la solución para el **KeyMe #1** desarrollado por Slayer. Es un desafío de ingeniería inversa enfocado en la validación mediante generación de claves (Keygenning) sin modificar el binario original (*No patching*).

## 📊 Información del Desafío
* **Autor del Crackme:** Slayer
* **Analista:** KarasuRØØT
* **Fecha de Análisis:** 19/09/2024
* **Reglas:** No parchear el binario. Se requiere crear un keygen.
* **Herramientas Utilizadas:** x64dbg (x32dbg), Notepad++, Python 3.

---

## 🔍 Análisis Técnico

Al ejecutar el binario, la interfaz muestra tres botones (`About`, `Check`, `Exit`) y un botón deshabilitado o grisáceo (`Register`). El objetivo inicial es habilitar la fase de registro y, posteriormente, validar la licencia correctamente.

### Fase 1: Habilitar el Botón "Register"
A través del rastreo de la ejecución del programa con **x32dbg**, se identificaron las siguientes llamadas clave de la API de Windows:
* `OpenClipboard`
* `GetClipboardData`

El programa inspecciona de manera activa el portapapeles de Windows. 
* **Condición:** Es obligatorio que el portapapeles contenga exactamente el **nombre de host (Hostname)** de la máquina en la que se está ejecutando el crackme (en mayúsculas, ej. `REVERW10`).
* Al hacer clic en `Check` con el Hostname copiado en el portapapeles, el binario habilita con éxito el botón **`-> Register <-`**.

### Fase 2: Validación del archivo `reg.key`
Una vez habilitado el botón de registro, el programa invoca a `CreateFileA` buscando un archivo de licencia llamado obligatoriamente **`reg.key`** en el mismo directorio de ejecución. El archivo debe contener exactamente **8 bytes de datos** estructurados internamente en formato **Little Endian**.

La lógica algorítmica de validación interna se resume de la siguiente manera:
1.  **Suma del Hostname:** El programa recorre el nombre del equipo y calcula la sumatoria hexadecimal de cada uno de sus caracteres en código ASCII. 
    * *Ejemplo:* Para `REVERW10`, la suma hexadecimal (`52+45+56+45+52+57+31+30`) es igual a **`23C`**.
2.  **Operación Bitwise (XOR):** El crackme fragmenta los 8 bytes leídos desde `reg.key` en dos bloques de 4 bytes (`EAX` y `EDX`).
3.  **Cálculo Final:** Realiza una operación `XOR` entre `EAX` y `EDX`. El resultado matemático resultante debe ser exactamente igual al valor de la sumatoria de tu Hostname (en el ejemplo, `23C`).

Aprovechando las propiedades algebraicas del XOR ($A \oplus B = C \implies C \oplus B = A$), si elegimos una constante arbitraria para uno de los bloques (por ejemplo, `1234` en decimal / `4D2` en hexadecimal), podemos despejar nuestra incógnita fácilmente para alcanzar el valor clave deseado (`23C`).

---

## 🛠️ Estructura del Archivo `reg.key` (Ejemplo)

Para el Hostname `REVERW10` (Suma = `23C`), utilizando el valor decimal `1234` como base fija, el valor calculado que requiere el programa es **`4D26EE`**. Rellenando con ceros hasta completar los 8 bytes obligatorios y aplicando la codificación en **Little Endian**, el contenido exacto en formato hexadecimal dentro de `reg.key` debe ser:

```text
EE 06 00 00 D2 04 00 00