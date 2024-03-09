def inverter_string(s):
    # Converte a string para uma lista de caracteres
    lista_caracteres = list(s)

    # Obtém o tamanho da string
    tamanho = len(lista_caracteres)

    # Inverte a lista de caracteres
    for i in range(tamanho // 2):
        # Troca os caracteres simétricos em relação ao centro da string
        temp = lista_caracteres[i]
        lista_caracteres[i] = lista_caracteres[tamanho - 1 - i]
        lista_caracteres[tamanho - 1 - i] = temp

    # Converte a lista de caracteres de volta para uma string
    string_invertida = ''.join(lista_caracteres)

    return string_invertida

# Exemplo de uso:
entrada_usuario = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada_usuario)
print("String invertida:", resultado)