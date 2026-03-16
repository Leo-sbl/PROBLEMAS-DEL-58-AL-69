#PROBLEMA 67
numeros = [10, 5, 8, 20, 3 ,89 ,6 ]
def ordena_creciente(lista):
    return sorted(lista)

def ordena_decreciente(lista):
    return sorted(lista, reverse=True)

def por_indice(lista, indice):
    if 0 <= indice < len(lista):
        return lista.pop(indice)
    else:
        return None  # índice inválido

def por_dato(lista, dato):
    try:
        lista.remove(dato)
    except ValueError:
        print(f"El dato {dato} no está en la lista")
    return lista

def calcula_estadisticas(lista):
    if len(lista) == 0:
        return None, None, None
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return promedio, maximo, minimo


print("Lista original:", numeros)
print("Orden creciente:", ordena_creciente(numeros))
print("Orden decreciente:", ordena_decreciente(numeros))
valor_eliminado = por_indice(numeros, 2)
print("Valor eliminado en índice 2:", valor_eliminado)
print("Lista después de eliminar por índice:", numeros)
print("Lista después de eliminar el dato 20:", por_dato(numeros, 20))
prom, maxi, mini = calcula_estadisticas(numeros)
print(f"Promedio: {prom:.2f}, Máximo: {maxi}, Mínimo: {mini}")
