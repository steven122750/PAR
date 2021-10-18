
from Infraestructura import Persistencia
import os

saver = Persistencia()

def guardarPreguntas():

    pregunta1=["Cual es la abreviatura de kilometro","A: kl","B: klm","C: km","D: kmt"]
    pregunta2=["Quien salio de la lampara de Aladino","A: Un genio","B: Un principe","C: Una bruja","D: Un sapo"]
    pregunta3=["La antena de radio sirve para","A: Adornar el radio","B: Mejorar la senial",
               "C: Regular la corriente","D: Eliminar el ruido"]
    pregunta4=["Cual es el simbolo quimico del aluminio","A: Ao","B: Am","C: Lm","D: Al",4,"imagenes/pregunta4.ogg"]
    pregunta5=["Las gotas heladas que caen en algunas tormentas se les llama","A: Granizo","B: Nieve","C: Lluvia",
               "D: Rocio"]
    pregunta6=["De que color es una senial de Pare","A: verde y azul","B: rojo y blanco","C: amarillo y negro",
               "D: rosa y verde"]
    pregunta7=["Cual de estos animales es un reptil","A: Cocodrilos","B: Serpientes","C: Lagartos","D: Todos"]
    pregunta8=["Cual de estas piedras es de color verde","A: Rubi","B: Topacio","C: Zafiro","D: Esmaraldas"]
    pregunta9=["Para que el pan se fermente o crezca debe llevar","A: Levadura","B: Agua","C: Uvas","D: Amor"]
    pregunta10=["Este perro es el mas alto de todos ellos. Tiene un pelaje delgado.","A: Lobero Irlandes",
                "B: Gran danes","C: Deerhound Escoces","D: San Bernardo"]
    pregunta11=["El protagonita de este espectaculo tiene un abuelo llamado Lou","A: Los padrinos magicos","B: Doug",
                "C: Rugrats","D: Clarissa lo explica todo"]
    pregunta12=["Cual es el continente mas grande del mundo","A: Asia","B: Europa","C: Africa","D: America"]
    pregunta13=["Cual es la forma completa de la abreviatura GMT","A: Greenwich Mean Time","B: Greenland Mean time",
                "C: German Mean Time","D: Gippsland Mean Time"]
    pregunta14=["Cual es el oceano en el que llega el caudal del rio amazonas","A: El Artico","B: El indio",
                "C: El Atlantico","D: El Pacifico"]
    pregunta15=["Cual es el aparato que facilita la refrigeracion en una nevera","A: Congelador",
                "B: Barillas metalicas","C: Tener la puerta cerrada","D: Compresor"]
    pregunta16=["Cuantos jugadores conforman un equipo de voleibol en la cancha","A: 10","B: 5","C: 6","D: 4"]
    pregunta17=["En matematicas, diez milimetros son...","A: Un poquito","B: Un metro","C: Un decimetro",
                "D: Un centimetro"]
    pregunta18=["Cuantos segundos tiene un minuto y medio","A: 45","B: 90","C: 60","D: 75"]
    pregunta19=["Los delfines son animales de sangre...","A: Caliente","B: Fria","C: Azul","D: Gris"]

    lista=[pregunta1,pregunta2,pregunta3,pregunta4,pregunta5,pregunta6,pregunta7,pregunta8,pregunta9,pregunta10,
           pregunta11,pregunta12,pregunta13,pregunta14,pregunta15,pregunta16,pregunta17,pregunta18,pregunta19]


    saver.save_json(lista)

#Si en files no esta el archivo .json, llamar al metodo guardarPreguntas()



def cargarPreguntas():
    for file in os.listdir("files") :
        if '.json' in file:
           return Persistencia.load_json(file)

def ganancia() :
    lista=[100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000]
    return lista


print("BIENVENIDO A QUIEN QUIERE SER MILLONARIO")
print("Antes de jugar recuerda que debes responder con letras minusculas")

n=0
score=0
opcion=0

for i in cargarPreguntas():

    print(cargarPreguntas()[n])

    if n == 0 :
        res=str(input("Tu respuesta --> "))
        if res == "c" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1

        else :
            print("Fallaste")
            exit()

    elif n == 1 :
        res=str(input("Tu respuesta --> "))
        if res == "a" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()
    elif n == 2 :
        res=str(input("Tu respuesta --> "))
        if res == "b" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()
    elif n == 3 :
        res=str(input("Tu respuesta --> "))
        if res == "d" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()
    elif n == 4 :
        res=str(input("Tu respuesta --> "))
        if res == "a" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 5:

        ayuda = "Tienes una ayuda! elige: 1. 50:50, 2. Ayuda del publico, 3. LLamada a un amigo"
        print(ayuda)

        opcion = int(input("Elige con el numero --> "))

        if opcion == 1:
            print("Se descartan las preguntas a y c")
        elif opcion == 2:
            print("El publico te ayudara, la mayoria de votos apuntan a la opcion b ")
        elif opcion == 3:
            print("Tu amigo dice que la respuesta correcta es la b")

        res=str(input("Tu respuesta --> "))

        if res == "b" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n = n + 1
        else:
            print("Fallaste")
            exit()

    elif n == 6 :


        res=str(input("Tu respuesta --> "))

        if res == "d" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 7:

        res=str(input("Tu respuesta --> "))

        if res == "d" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 8 :
        res=str(input("Tu respuesta --> "))
        if res == "a" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 9 :
        res=str(input("Tu respuesta --> "))
        if res == "b" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 10 :

        if opcion == 1 :
            print("Tienes una ayuda! elige: 2. Ayuda del publico, 3.LLamada a un amigo")
            opcion=int(input("Elige con el numero --> "))
            if opcion == 2 :
                print("El publico te ayudara, la mayoria de votos apuntan a la opcion c ")
            elif opcion == 3 :
                print("Tu amigo dice que la respuesta correcta es la c")

        elif opcion == 2 :
            print("Tienes una ayuda! elige: 1. 50:50, 3.LLamada a un amigo")
            opcion=int(input("Elige con el numero --> "))
            if opcion == 1 :
                print("Se descartan las opciones b y d")
            elif opcion == 3 :
                print("Tu amigo dice que la respuesta correcta es la c")

        elif opcion == 3 :
            print("Tienes una ayuda! elige: 1. 50:50, 2. Ayuda del publico")
            opcion=int(input("Elige con el numero --> "))
            if opcion == 1 :
                print("Se descartan las opciones b y d")
            elif opcion == 2 :
                print("El publico te ayudara, la mayoria de votos apuntan a la opcion c")

        res=str(input("Tu respuesta --> "))

        if res == "c" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else:
            print("Fallaste")
            exit()

    elif n == 11 :
        res=str(input("Tu respuesta --> "))
        if res == "a" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 12 :
        res=str(input("Tu respuesta --> "))
        if res == "a" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 13 :
        res=str(input("Tu respuesta --> "))
        if res == "c" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 14 :
        res=str(input("Tu respuesta --> "))
        if res == "d" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 15 :

        if opcion == 1 or opcion == 2 :
            print("Tienes una ayuda! elige: 3. LLamada a un amigo")
            opcion=int(input("Elige con el numero --> "))
            if opcion == 3 :
                print("Tu amigo dice que la respuesta correcta es la c")
        elif opcion == 3 or opcion == 2:
            print("Tienes una ayuda! elige: 1. 50:50")
            opcion=int(input("Elige con el numero --> "))
            if opcion == 1 :
                print("Se descartan las opciones a y b")
        elif opcion == 1 or opcion == 3:
            print("Tienes una ayuda! elige: 2. Ayuda del publico")
            opcion=int(input("Elige con el numero --> "))
            if opcion == 2:
                print("El publico te ayudara, la mayoria de votos apuntan a la opcion c ")


        res=str(input("Tu respuesta --> "))
        if res == "c" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 16 :
        res=str(input("Tu respuesta --> "))
        if res == "d" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 17 :
        res=str(input("Tu respuesta --> "))
        if res == "b" :
            print("acertaste")
            score=ganancia() [n]
            print("Tu puntaje: " + str(score))
            n=n + 1
        else :
            print("Fallaste")
            exit()

    elif n == 18 :
        res=str(input("Tu respuesta --> "))
        if res == "a" :
            print("acertaste")
            score=ganancia() [n-1]
            print("Tu puntaje: " + str(score))
            n=n + 1
            print("FELICIDADES! HAS GANADO EL JUEGO")
        else :
            print("Fallaste")
            exit()
