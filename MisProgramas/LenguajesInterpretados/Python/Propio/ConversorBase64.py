import base64
import string

def validacion (cadena: str) -> bool:
    # Verifico si es Base64 o no
    cadena = cadena.strip()
    # Se valida a continuacion si la longitud de la cadena es multiplo de 4
    if len(cadena) % 4 != 0: 
        return False
    caracteres_validos = set(string.ascii_letters + string.digits + "+/=")
    return set(cadena).issubset(caracteres_validos)

def decobase64(cadena: str):
    cadena = cadena.strip()
    
    if not validacion(cadena):
        print("[!] La cadena No está en Base64.")
        return

    try:
        # Decodificar de Base64 a Bytes
        datos_decodificados = base64.b64decode(cadena)
        
        # Intentar convertir bytes a texto legible (UTF-8)
        texto = datos_decodificados.decode('utf-8')
        
        # Validar caracteres
        caracteres_imprimibles = set(string.printable)
        es_legible = all(c in caracteres_imprimibles for c in texto)
        
        if es_legible:
            print("[+] Decodificación exitosa (Texto legible):")
            print("-" * 40)
            print(texto)
            print("-" * 40)
        else:
            print("[?] Se decodificó correctamente, pero el contenido contiene caracteres NO imprimibles - OJO")
            print(f"Muestra en Hexadecimal: {datos_decodificados[:30].hex()}...")

    except UnicodeDecodeError:
        print("[!] Es Base64 válido, pero el resultado son datos binarios (no es texto UTF-8).")
        print(f"Muestra en Hexadecimal: {datos_decodificados[:30].hex()}...")
    except Exception as e:
        print(f"[!] Error al decodificar: {e}")

if __name__ == "__main__":
    print("=== Decodificador de Base64 ===")
    print("Escribe 'exit' o 'salir'\n")
    
    while True:
        try:
            muestra = input("\nIngresa la cadena a analizar: ").strip()
            if muestra.lower() in ["exit", "salir"]:
                while True:
                    confirmacion = input("¿Estás seguro de que quiere salir? (Y/N): ").strip().lower()
                    if confirmacion in ["y", "s", "yes", "si"]:
                        print("\n¡Hasta luego!")
                        exit() # Cierra el programa por completo
                    elif confirmacion in ["n", "no"]:
                        print("[+] Operación cancelada. Puedes seguir ingresando cadenas.")
                        break # Sale del bucle de confirmación y vuelve al análisis
                    else:
                        print("[!] Opción no válida. Ingresa 'Y' para salir o 'N' para continuar.")
                
                # Si respondió 'N', continuamos con el bucle principal sin ejecutar decobase64
                continue
                
            # Si se presiona Enter sin escribir nada
            if not muestra:
                continue
                
            decobase64(muestra)
            
        except KeyboardInterrupt:
            # Permite salir de forma limpia presionando Ctrl + C
            print("\n\nPrograma interrumpido. ¡Hasta luego!")
            break