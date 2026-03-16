#PROBLEMA 66

alumnos = [
    ("Ana", 85),
    ("Luis", 55),
    ("María", 70),
    ("Pedro", 40),
    ("Sofía", 95)
]
def reprobados(lista, minimo=70):
    lista_reprobados = []
    for nombre, calificacion in lista:
        if calificacion < minimo:
            lista_reprobados.append(nombre)
    return lista_reprobados

resultado = reprobados(alumnos)
print("Lista de reprobados:", resultado)