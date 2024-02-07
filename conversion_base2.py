def convertir_letra_binario(x):
    a = ord(x)

    binario = ''
    while a > 0:
        residuo = a % 2
        binario = str(residuo) + binario
        a = a // 2
    temp = 8 - len(binario)

    retorno = ''
    for i in range(temp):
        retorno = retorno + '0'
    retorno = retorno + binario
    return retorno

def convertir_binario_letra(x):
    valor_decimal = 0

    for i in range(8):
        valor_decimal += int(x[i]) * (2 ** (len(x) - i - 1))


    letra = chr(valor_decimal)
    return letra

def codificar_binario(x):
    retorno = ""
    for i in x:
        retorno += convertir_letra_binario(i)
    return retorno

def decodificar_binario(x):
    retorno = ""
    for i in range(0, len(x), 8):
        retorno += convertir_binario_letra(x[i:i+8])
    return retorno

resbinario = codificar_binario('Hola mundo como estas amigi')
print(resbinario)
desbinario = decodificar_binario(resbinario)
print(desbinario)


def codificar_base64(x):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binarios = ""
    for i in x:
        binarios += convertir_letra_binario(i)

    temp = []
    for i in range(0, len(binarios), 6):
        segmento = binarios[i:i+6]
        if len(segmento) < 6:
            resultado_temp = 6 - len(segmento)
            retorno = ''
            for i in range(resultado_temp):
                retorno = retorno + '0'
            retorno = retorno + segmento
            segmento = retorno
        temp.append(segmento)

    resultado = [base64[int(seg, 2)] for seg in temp]
    return ''.join(resultado)

def decodificar_base64(x):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binarios = ""
    for i in x:
        if i in base64_chars:
            valor_decimal = base64_chars.index(i)
            binario = bin(valor_decimal)[2:]
            while len(binario) < 6:
                binario = '0' + binario
            binarios += binario

    texto = ""
    for i in range(0, len(binarios), 8):
        segmento = binarios[i:i+8]
        if len(segmento) == 8:
            valor_decimal = int(segmento, 2)
            texto += chr(valor_decimal)

    return texto

resbase64 = codificar_base64('Hola mundo como estas')
desbase64 = decodificar_base64(resbase64)
print(resbase64)
print(desbase64)