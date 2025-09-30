# Autor: Juan Camilo Páez Guaspud
# Parcial 50% Requerimientos Funcionales
---REQUERIMIENTO FUNCIONAL---
Registro de nuevos libros (HECHO)
Registro de nuevos usuarios (HECHO)
Mínimo 3 categorías de libro (HECHO)
1. se crea una clase de administrador que será el que manejará toda la logística de la biblioteca
```python
class Administrador:
    def __init__(self):
```
2. se realiza el constructor:
```python
    def __init__(self,__elegir_opciones,_categorizar_libros,__registrar_libros,__registrar_usuarios,__repetir_programa):
        self.__elegir_opciones = __elegir_opciones
        self._categorizar_libros=_categorizar_libros
        self.__registrar_libros=__registrar_libros
        self.__registrar_usuarios=__registrar_usuarios
        self.__repetir_programa=__repetir_programa
        pass
```
3. se define el objeto de elegir opciones, aqui estara todo el apartado de opciones que podrá realizar el administrador:
```python
    def __elegir_opciones(self, bienvenida):
        self.bienvenida=input("Bienvenido al sistema de administración de la biblioteca")
        self.__opciones=input("¿Qué opción desea realizar?: \n 1. Registro de nuevos libros \n 2. Registro de nuevos usuarios \n")
        if self.__opciones==1:
            self.__registrar_libros()
        elif self.__opciones==2:
            self.__registrar_usuarios()
        else:
            print("Opción no válida")
        pass
```
se usa el input para recolectar y dar atributos
se usa el if para  verificar que se haya elegido una opción correctamente

4. Se define la categorización de libros, dependiendo de la opción escogida, lo llevará a un apartado u otro:
```python
    def _categorizar_libros(self,categoria):
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
```
se usa if y elif dependiendo de la opción elegida o else si no se seleccionó una opción válida

5.  se define el objeto de registrar libros, este apartado se encargará de registrar los datos del libro:
```python
    def __registrar_libros(self,categoria,titulo,autor,registro_libro):
        self.categoria=print(__categorizar_libros())
        self.titulo=input("Ingrese el título del libro:")
        self.autor=input("Ingrese el autor del libro:")
        self.registro_libro=print(f"El libro de {autor}, llamado {titulo} ha sido registrado en la categoría de {categoria}")
        print(__repetir_programa())
        pass
```
se usa repetir programa por si el usuario desea agregar nueva información, como agregar nuevo usuario o nuevo libro

6. Se define el objeto de registar usuario, este apartado se encargará de registrar los datos del nuevo usuario:
```python
    def __registrar_usuarios(self, nombre, id_usuario, telefono, registro_usuario):
        self.nombre=(input("Ingrese el nombre del usuario:"))
        self.id_usuario=int(input("Ingrese el ID del usuario:"))
        self.telefono=int(input("Ingrese el teléfono del usuario:"))
        self.registro_usuario=print(f"El usuario {nombre} con ID {id_usuario} y teléfono {telefono} ha sido registrado en el sistema")
        __repetir_programa()
        pass
```
se usa igualmente repetir programa por si se requiere usar el programa de nuevo

7. se define el objeto de repetir programa por si el administrador desea agregar nueva información 
```python 
    def __repetir_programa(self,repetir):
        self.repetir=input("¿Desea realizar otra operación? si/no : ")
        if self.repetir.lower()=='si':
            print(__elegir_opciones())
        else:
            print("Gracias por usar el sistema de administración de la biblioteca")
            exit()
        pass
```
se usa if o else dependiendo de la opcion elegida, esto decidirá si el programa se repite, o si genera un texto de despedida y cerrar el programa

8. se define main para que ejecute todo el programa anterior:
```python
def main():
    __elegir_opciones()

if __name__ == "__main__":
	main()
```