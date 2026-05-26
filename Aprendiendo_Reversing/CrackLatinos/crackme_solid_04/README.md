English

Solving crackme_solid_04.exe

This repository contains the walkthrough and reverse engineering analysis for the `crackme_solid_04.exe` challenge, a 64-bit binary compiled in C++.

## 📊 Analysis Summary

After performing static and dynamic analysis using **IDA Pro**, the following execution phases were identified within the main function (`main`):

1. **User Input:** The program prompts the user to enter a name in the console (e.g., "pepe") and prints a welcoming greeting.
2. **External File Validation:** The binary invokes the Windows API function `CreateFileA` to attempt to open a specific text file named `test.txt` located in the same directory as the executable. If the file is missing, the program terminates with the message: `"falta algo para seguir avanzando..."`.
3. **Content Validation (The Loop):**
   * Upon reading the file via `ReadFile`, the program enters a loop that inspects the buffer content character by character.
   * It compares the hexadecimal value of each character against `5Ah` (which represents the uppercase letter **'Z'** in the ASCII table).
   * If any non-'Z' character is encountered, it immediately jumps to the failure routine displaying a `"Segui participando"` (Keep participating) message boxes.
   * The loop condition checks if a validation threshold has been successfully met (`0x0A`, equivalent to 10 iterations on a zero-based index).

## 🔑 Solution

To trigger the success message box (`"Bien hecho" / "Lo lograste"`), the `test.txt` file must satisfy the following criteria:
* It must contain only consecutive uppercase **'Z'** letters.
* Due to zero-based indexing and the internal size validation mechanics, the file must be filled with exactly **11 'Z' characters** (`ZZZZZZZZZZZ`).

*Note: A Python automation script is provided in this repository to automatically detect the crackme's presence and generate the required `test.txt` file setup.*



------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------


Español:
Resolviendo crackme_solid_04.exe

Este repositorio contiene la solución y el análisis de ingeniería inversa para el reto `crackme_solid_04.exe`, un binario compilado en C++ para arquitecturas de 64 bits.

## 📊 Resumen del Análisis

Tras realizar el análisis estático y dinámico utilizando **IDA Pro**, se identificaron las siguientes fases de ejecución dentro de la función principal (`main`):

1. **Entrada de Usuario:** El programa interactúa solicitando un nombre en la consola (ej. "pepe") e imprime un saludo de bienvenida.
2. **Validación de Archivo Externo:** El binario invoca la API de Windows `CreateFileA` para intentar abrir un archivo de texto llamado obligatoriamente `test.txt` en el mismo directorio que el ejecutable. Si el archivo no existe, el programa termina mostrando el mensaje: `"falta algo para seguir avanzando..."`.
3. **Validación del Contenido (El Bucle):**
   * Al leer el archivo con `ReadFile`, el programa entra en un bucle que inspecciona el contenido del buffer carácter por carácter.
   * Compara el valor numérico en hexadecimal de cada carácter contra `5Ah` (que representa la letra **'Z'** en mayúscula dentro de la tabla ASCII).
   * Si encuentra un carácter diferente, salta inmediatamente a la rutina que muestra el mensaje de fallo (`"Segui participando"`).
   * El contador del bucle comprueba si se ha alcanzado de manera exitosa un límite de validación (`0x0A`, equivalente a 10 iteraciones en base cero).

## 🔑 Solución

Para obtener el mensaje de éxito (`"Bien hecho" / "Lo lograste"`), el archivo `test.txt` debe cumplir estrictamente con las siguientes condiciones:
* Debe contener la letra **'Z'** (mayúscula) de manera consecutiva.
* Debido al comportamiento del índice del bucle basado en cero y las comprobaciones internas de tamaño, se requiere que el archivo contenga exactamente **11 caracteres 'Z'** (`ZZZZZZZZZZZ`).

*Nota: Se incluye en este repositorio un script de automatización en Python que detecta la presencia del crackme y genera el archivo `test.txt` con el contenido requerido de forma automática.*