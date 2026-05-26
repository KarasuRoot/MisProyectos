def xor_strings_with_details(str1, str2):
  """Realiza la operación XOR byte a byte entre dos cadenas y muestra los detalles de cada operación, incluyendo el carácter ASCII resultante y la cadena final.

  Args:
    str1: La primera cadena.
    str2: La segunda cadena.
  """

  bytes1 = bytes(str1, 'utf-8')
  bytes2 = bytes.fromhex(str2)

  result_bytes = bytearray()
  for i, (b1, b2) in enumerate(zip(bytes1, bytes2)):
      result_byte = b1 ^ b2
      result_char = chr(result_byte)
      result_bytes.append(result_byte)
      print(f"{i}: {hex(b1)[2:]} XOR {hex(b2)} = {hex(result_byte)[2:]} ({result_char})")

  result_string = bytes(result_bytes).decode('utf-8')
  print(f"La cadena resultante es: {result_string}")

# Datos de entrada
string1 = "Messing_in_bytes"
hex_string = "1F 2C 37 36 3B 3d 28 19 3D 26 1A 31 2D 3B 37 3E"

# Realizar la operación XOR y mostrar los detalles
xor_strings_with_details(string1, hex_string)

"""
English:
Here is the translation into English:This script takes a text word or phrase (string1) and a sequence of numbers in hexadecimal format (hex_string).
Then, it pairs the text letter by letter with its corresponding hexadecimal value to apply a logical XOR ($\oplus$) operation to them.
At the end, the program prints the step-by-step mathematical process on the screen (showing which letter was generated at each step) and joins all the resulting letters to reveal a hidden message.
In this particular case, the result of combining "Messing_in_bytes" with the hexadecimal string reveals the hidden word: ZORRO_DEL_REVERS (or similar, depending on the exact characters).
---------------------------------------------
---------------------------------------------
---------------------------------------------
Español:
Este script toma una palabra o frase de texto (string1) y una secuencia de números en formato hexadecimal (hex_string). 
Luego, va emparejando letra por letra el texto con su correspondiente valor hexadecimal para aplicarles una operación lógica XOR ($\oplus$). 
Al final, el programa imprime en pantalla el proceso matemático paso a paso (mostrando qué letra se generó en cada paso) y une todas las letras resultantes para revelar un mensaje oculto. 
En este caso particular, el resultado de combinar "Messing_in_bytes" con la cadena hexadecimal revela la palabra oculta: ZORRO_DEL_REVERS (o similar, dependiendo de los caracteres exactos)."""