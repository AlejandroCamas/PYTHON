#aqui vamos a ver los tipos de datos en python
#tipos de datos:
#string este es una cadena de texto
#ejemplo:
my_name = "Alejandro" #esto aqui son nuestras variables 
my_lastname = "Camas"
print("my_name =>", my_name) #aqui estamos indicando que debe imprimir la variable "my_name"

#tipo de dato entero
#int
my_age = 21 
#los numero no necesitan llevar comillas : ("" '')
print("my_age =>", my_age)#lo que tenemos entre comillas es lo que el usuario leera y en azul es la variable

#tenemos tambien la manera de que python nos diga que tipo de dato es el que estamos viendo
#de la siguiente forma #print(type(y nuestra variable que queremos saber))


#ahora tenemos el tipo de datos Booleanos los cuales son solo de Verdad o Falzo
#por ejemplo imaginemos que queremos decir que una persona esta soltera, se haria asi:

#boolean
the_person_is_single = True #importante siempre poner las letras en mayuscula "True" "False"
print("La persona es soltera =>", the_person_is_single)
print(type(the_person_is_single))#usamos esta linea para ver que tipo de dato es.

#inputs
my_age = input("cual es tu edad? ")
print("tu edad es =>", my_age)
#aqui estamos nosotros solicitando al usuario la informacion para poder imprimirla en la consola.