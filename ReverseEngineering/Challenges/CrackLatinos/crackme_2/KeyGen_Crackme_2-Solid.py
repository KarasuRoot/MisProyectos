def serial(usu):  #Defino mi funcion
    conta = 0       #inicializo mi variable para contar en 0
    for letra in usu: #Recorro el string que el usuario indico como 'su usuario'
        valor_hexadecimal = hex(ord(letra))[2:]  # Elimino el prefijo '0x'
        conta += int(valor_hexadecimal, 16)  #suma el contador en hexa
    return conta

usu = (input('Indique su usuario: ')) #Solicita un usuario
resultado = serial(usu) #aplica la funcion previamente definida
print('Su serial es: ', resultado) #imrpimo resultado




