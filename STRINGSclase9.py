#primero vamos a declarar nuestras variables:
name = "Alejandro"
last_name = "Camas"
print(name)
print(last_name)
#indicamos que imprima nuestros strings

full_name = name + " " + last_name
print(full_name)
#aqui indicamos que imprima nuestras variables iniciales pero concatenadas.
#el signo  mas (+) en los strings significa que queremos hacer la union de 2 o mas strins.
#usamos ese string vacio para poder tener un espacio entre los strings o de lo contrario quedaria pegado.

#uso correcto de las comillas:

comillas_simples = "i'm Alejandro" #usamos las dobles comillas para que python solo interprete que la comilla simple es parte del sting

comillas_dobles = ' dice "ser muy pro"' #usamos las comillas dobles ya que usamos las dobles para hacer mencion de lo que alguien dijo.

#ahora haremos la concatenacion de las variables para poder generar un texto:
#forma 1
concatenacion = "hola mi nombre es " + name + " " + "y  mi apellido es" + " " + last_name
print("forma 1", concatenacion)

#forma 2
concatenacion = "hola mi nombre es {} y mi apellido {}".format(name, last_name)
print("forma 2", concatenacion)

#forrma 3
concatenacion = f"hola mi nombre es {name} y mi apellido es {last_name}"
print("v3", concatenacion)

#como vemos son diferentes en codigo pero las tres hacen exacatamente lo mismo.