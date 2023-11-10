def contar_articulos(archivo):
    # Crear una lista para almacenar el orden de aparición de los artículos
    orden_aparicion = []

    # Crear un diccionario para almacenar el conteo de cada artículo
    conteo_articulos = {}

    # Abrir el archivo y leer línea por línea
    with open(archivo, 'r') as file:
        for linea in file:
            # Eliminar espacios en blanco y convertir a minúsculas para evitar diferencias de mayúsculas y minúsculas
            articulos = linea.strip().lower().split()

            # Iterar sobre cada artículo en la línea
            for articulo in articulos:
                # Si el artículo no está en la lista de orden de aparición, agrégalo
                if articulo not in orden_aparicion:
                    orden_aparicion.append(articulo)

                # Si el artículo ya está en el diccionario, incrementar el contador
                if articulo in conteo_articulos:
                    conteo_articulos[articulo] += 1
                else:
                    # Si el artículo no está en el diccionario, agregarlo con un contador inicial de 1
                    conteo_articulos[articulo] = 1

    # Crear la cadena de salida en el formato deseado
    resultado = ''.join([f"{articulo}{conteo_articulos[articulo]}" for articulo in orden_aparicion])

    return resultado



# Ejemplo de uso
archivo = 'message_01.txt'  # Reemplaza 'tu_archivo.txt' con el nombre de tu archivo
resultado = contar_articulos(archivo)
print(resultado)