# Autor: Juan Camilo Páez

# Registro de nuevos libros (HECHO)
# Registro de nuevos usuarios 
# Mínimo 3 categorías de libro (HECHO)

class Administrador:
    def __init__(self):

        pass
    def __opciones(self,bienvenida):
        self.bienvenida=input("Bienvenido al sistema de administración de la biblioteca")
        self.__opciones=input("¿Qué opción desea realizar?: \n 1. Registro de nuevos libros \n 2. Registro de nuevos usuarios \n")
        if self.__opciones==1:
            self.__registro_libros()
        elif self.__opciones==2:
            self.__registro_usuarios()
        else:
            print("Opción no válida")
        pass
    def _categorias_libros(self,categoria):
        self.categoria=input("Ingrese la categoría del libro: \n1. Ciencia Ficción \n2. Fantasía \n3. Misterio \n4. Historia\n")
        if self.categoria==1:
            print("Categoría seleccionada: Ciencia Ficción")
        elif self.categoria==2:
            print("Categoría seleccionada: Fantasía")
        elif self.categoria==3:
             print("Categoría seleccionada: Misterio")
        elif self.categoria==4:
             print("Categoría seleccionada: Historia")
        else:
            print("Categoría no válida")
        pass

    def __registro_libros(self,categoria,titulo,autor,registro_libro):
        self.categoria=print(__categorias_libros())
        self.titulo=input("Ingrese el título del libro:")
        self.autor=input("Ingrese el autor del libro:")
        self.registro_libro=print(f"El libro de {autor}, llamado {titulo} ha sido registrado en la categoría de {categoria}")
        print(__repetir_programa())
        pass

    def __registro_usuarios(self, nombre, id_usuario, telefono, registro_usuario):
        self.nombre=(input("Ingrese el nombre del usuario:"))
        self.id_usuario=int(input("Ingrese el ID del usuario:"))
        self.telefono=int(input("Ingrese el teléfono del usuario:"))
        self.registro_usuario=print(f"El usuario {nombre} con ID {id_usuario} y teléfono {telefono} ha sido registrado en el sistema")
        print(__repetir_programa())
        pass

    def __repetir_programa(self,repetir):
        self.repetir=input("¿Desea realizar otra operación? si/no : ")
        if self.repetir.lower()=='si':
            print(__opciones())
        else:
            print("Gracias por usar el sistema de administración de la biblioteca")
            exit()
        pass

def main():
    print(__opciones())
