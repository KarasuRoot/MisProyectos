# Solución de Crackme CruShead1999 (por CruShead)

English:
This repository houses the in-depth technical walkthrough and the functional Keygen implementation for the classic **CruShead1999 Crackme**. The objective of this analysis is to reverse-engineer its internal validation algorithms to derive a valid key for any given username without modifying the original compiled binary instructions (*No patching*).

## 📊 Challenge Overview
* **Crackme Author:** CruShead
* **Analyst:** KarasuRØØT 
* **Analysis Date:** 08/14/2024 
* **Rules:** No patching allowed. A working keygen must be built.
* **Tools Used:** OllyDbg (or x32dbg), Programmer's Calculator, Python 3.

---

## 🔍 Technical Analysis

When launching the binary and navigating to `Help -> Register`, a legacy registration window prompts the analyst to input a **Name** and a **Serial**.

### Phase 1: Data Capture (Windows API)
By setting a strategic breakpoint at the core Windows dialog interaction module:
* `GetDlgItemTextA`

The software captures the user string entered into the input buffer and maps it to a memory address to begin its validation routines.

### Phase 2: License Validation Algorithm
The crackme implements a character loop that safely inspects the string array and calculates the key parameters as follows:

1.  **ASCII Filter & Capitalization:** * The code consumes a character from the username byte array.
    * It checks if the character is lowercase; if so, it subtracts `20` in hexadecimal (`SUB AL, 20`), effectively modifying the character into its corresponding **uppercase** representation.
2.  **Cumulative Checksum:**
    * Once filtered, the uppercase ASCII integer value is added sequentially into an accumulation CPU register (`EDI`).
    * *Example:* The input name `karasu` is treated internally as `KARASU`. Adding their hexadecimal ASCII values together (`4B + 41 + 52 + 41 + 53 + 55`) yields the target checksum **`1C7`**.
3.  **First Bitwise Operation (XOR with Username Checksum):**
    * Right after exiting the loop, the application performs an XOR operation between the accumulated total (`EDI`) and the static hex key `5678`.
    * `1C7` XOR `5678` = **`57BF`**.
4.  **Second Bitwise Operation (XOR with Serial Input):**
    * Concurrently, the user-supplied numerical serial key undergoes a secondary verification path involving an XOR calculation against the static hex key `1234`.
    * To produce a successful flag, both cross-calculations must mirror each other in the processor registers.

By extracting the reverse equation using standard bitwise math principles, we establish:
$$\text{Final Serial} = (\text{Uppercase ASCII Checksum} \oplus \text{0x5678}) \oplus \text{0x1234}$$

---

## 🛠️ Case Study Walkthrough (Example)

Given the test user `karasu`:
* **Uppercase Conversion:** `KARASU`
* **Hex Checksum Total:** `1C7`
* **Step 1:** `1C7` XOR `5678` = `57BF`
* **Step 2 (Deduction):** `57BF` XOR `1234` = **`458B`**
* **Base-10 Conversion:** `458B` in Hex translates directly to **`17803`** in standard Decimal notation.

Providing the user `karasu` alongside the calculated serial integer `17803` satisfies the conditional jump check, showing the successful registration string: *"Great work, mate! Now try the next CrackMe!"

----------------------------------------------------
----------------------------------------------------
----------------------------------------------------


Español:

Este repositorio contiene el análisis detallado y el desarrollo de un generador de claves (Keygen) para el clásico **Crackme CruShead1999**. El análisis se centra en realizar ingeniería inversa al algoritmo de validación para lograr el registro con cualquier nombre sin alterar las instrucciones del binario original (*No patching*).

## 📊 Información del Desafío
* **Autor del Crackme:** CruShead
* **Analista:** KarasuRØØT
* **Fecha de Análisis:** 14/08/2024
* **Reglas:** No parchear el binario. Se requiere crear un keygen funcional.
* **Herramientas Utilizadas:** OllyDbg (o x32dbg), Calculadora de Programador, Python 3.

---

## 🔍 Análisis Técnico

Al interactuar con el binario y acceder a la opción `Help -> Register`, el programa despliega una ventana de registro clásica que solicita un **Name** (Nombre) y un **Serial** (Número de serie).

### Fase 1: Captura de Datos (API de Windows)
Estableciendo un breakpoint en la API de lectura de diálogos de Windows:
* `GetDlgItemTextA`

El programa captura la cadena de texto ingresada en el campo de usuario y la almacena en memoria para iniciar las rutinas de validación.

### Fase 2: El Algoritmo de Validación de la Licencia
El crackme utiliza un bucle que inspecciona cada uno de los caracteres del nombre ingresado y procesa la clave de la siguiente forma:

1.  **Conversión y Filtro ASCII:** * El programa toma un carácter de la cadena. 
    * Evalúa si es una letra minúscula y, si se encuentra dentro del rango correspondiente, le resta `20` en hexadecimal (`SUB AL, 20`), lo cual transforma automáticamente la letra a **mayúscula**.
2.  **Sumatoria Acumulativa (Checksum):**
    * Una vez procesado el carácter, su valor ASCII en mayúscula se añade secuencialmente a un registro acumulador (`EDI`).
    * *Ejemplo:* Si el nombre ingresado es `karasu`, el bucle lo transforma internamente en `KARASU`. La sumatoria de sus valores hexadecimales (`4B + 41 + 52 + 41 + 53 + 55`) da como resultado final **`1C7`**.
3.  **Primera Operación Bitwise (XOR con el Nombre):**
    * Tras finalizar el recorrido del nombre, el programa realiza una operación XOR entre el acumulador (`EDI`) y la constante fija `5678` en hexadecimal.
    * `1C7` XOR `5678` = **`57BF`**.
4.  **Segunda Operación Bitwise (XOR con el Serial):**
    * Posteriormente, el binario toma el número de serie numérico ingresado por el usuario y realiza una segunda operación XOR con la constante fija `1234` en hexadecimal.
    * Para que el registro sea exitoso, ambos cálculos cruzados deben coincidir en los registros del procesador.

Despejando la ecuación matemática mediante las propiedades del XOR:
$$\text{Serial final} = (\text{Suma ASCII del nombre en Mayúsculas} \oplus \text{0x5678}) \oplus \text{0x1234}$$

---

## 🛠️ Caso de Estudio (Ejemplo)

Para el usuario `karasu`:
* **Nombre en Mayúsculas:** `KARASU`
* **Suma ASCII (Hex):** `1C7`
* **Operación 1:** `1C7` XOR `5678` = `57BF`
* **Operación 2 (Despeje):** `57BF` XOR `1234` = **`458B`**
* **Conversión a Decimal:** `458B` en base hexadecimal equivale a **`17803`** en base decimal.

Al introducir el usuario `karasu` junto con el serial calculado `17803`, el programa valida la clave correctamente y muestra el mensaje de felicitación: *"Great work, mate! Now try the next CrackMe!"*.

