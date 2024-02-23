def decimal_a_binario_recursivo(numero):
    if numero == 0:
        return '' 
    else:
        return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)


numero_decimal = 23
print(decimal_a_binario_recursivo(numero_decimal))
