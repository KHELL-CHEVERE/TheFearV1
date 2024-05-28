# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Prota")
define n = Character("")


# The game starts here.

label start:
    screen sta():
        frame:
            ypos 400 xpos 1098
            add "sta2.png"
    screen fear1():
        image("fear normal.png"):
            ypos 280 xpos 1150
            #add

    screen stamina():
        default n=3
        frame:
            xpos 1100
            ypos 250
            ysize 150
            vbar value AnimatedValue(n, 3, 0.5): #bar_invert True
            #vbar value StaticValue(n, 3): #bar_invert True
                right_bar Frame("verde.png", 10, 0)
                left_bar Frame("transparente.png", 10, 0)
    screen stamina2():
        default n=2
        frame:
            xpos 950
            ypos 450
            ysize 200
            vbar value AnimatedValue(n, 3, 0.5):
                bar_invert True
                right_bar Frame("transparente.png", 10, 0)
                left_bar Frame("rojo.png", 10, 0)



    $ barvariable = 50
    screen thebar:
        vbar value StaticValue(barvariable, 100):
            #xalign 0.0 yalign 0.0
            xpos 300
            ypos 300
            #xmaximum 400
            #ymaximum 15
            ysize 200
            left_bar Frame("rojo.png", 10, 0)
            right_bar Frame("amarillo.png", 10, 0)
            #thumb "naranja.png"
            thumb None
            thumb_shadow None
    #show screen thebar

    show screen stamina
    show screen sta
    show screen fear1

    #show screen stamina2


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    scene bg entrada
    # Acá definimos variables
    $ puertaEntrando = 0
    $ CUARTOactual = 0
    #$ SALIDA = [[[6,2],["verde","azul"]],[[1,7,3],["azul","marrón","amarillo"]],[[2,4],["amarillo","rojo"]],[[3,5],["morado","rojo"]],[[4,6],["morado","naranja"]],[[7,1,5],["amarillo"]],[[2,6],["marron","amarillo"]]]
    $ SALIDA = [[5,1],[0,6,2],[1,3],[4,2],[3,5],[6,0,4],[1,5]]
    $ PUERTAS = [["verde","azul"],["azul","marrón","amarillo"],["amarillo","rojo"],["morado","rojo"],["morado","naranja"],["amarillo","verde","naranja"],["marron","amarillo"]]
    $ ENTRADAS = [[],[],[],[],[],[],[]]  #Haciendo estooooooo
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ SALIDAS = 0

    show cara chica2 at right
    show prota entradaparada

    #n "hola"
    call jugar
    # FIN DEL JUEGO
    return


    #FUNCIONES
    label jugar :
        label paradaEnCuarto :
        #MOVERSE / llama a funcion MOVERSE
        call moverse
        jump paradaEnCuarto
        return

    label moverse :
        n "Estas en cuarto [CUARTOactual], ahora muevete"


        $ SALIDAS = len(PUERTAS[CUARTOactual])
        if (SALIDAS == 2):
            $ puerta0 = PUERTAS[CUARTOactual][0]
            $ puerta1 = PUERTAS[CUARTOactual][1]
            menu:
                "Voy el camino color [puerta0]":
                    call cruzaPuerta(0)
                    jump finmenu
                "Voy el camino color [puerta1]":
                    call cruzaPuerta(1)
                    jump finmenu
        if (SALIDAS == 3):
            $ puerta0 = PUERTAS[CUARTOactual][0]
            $ puerta1 = PUERTAS[CUARTOactual][1]
            $ puerta2 = PUERTAS[CUARTOactual][2]
            menu:
                "Voy el camino color [puerta0]":
                    call cruzaPuerta(0)
                    jump finmenu
                "Voy el camino color [puerta1]":
                    call cruzaPuerta(1)
                    jump finmenu
                "Voy el camino color [puerta2]":
                    call cruzaPuerta(2)
                    jump finmenu
        label finmenu:
        #n "salidas [SALIDAS]"
        return

    label cruzaPuerta (puertaDestino = 0):
        # $ puertaEntrando
        call entraPorPuerta (CUARTOactual,puertaDestino)
        $ CUARTOactual = SALIDA[CUARTOactual][puertaDestino]
        call cambiaFondo
        return


        #lo llamo desde cruzaPuerta
        #cambia el bg al nuevo
    label cambiaFondo :
        if (CUARTOactual == 0):
            show bg entrada
        if (CUARTOactual == 1):
            show bg recepcion
        if (CUARTOactual == 2):
            show bg oficina
        if (CUARTOactual == 3):
            show bg sala
        if (CUARTOactual == 4):
            show bg comedor
        if (CUARTOactual == 5):
            show bg simulador
        if (CUARTOactual == 6):
            show bg datacenter


        return

    #Hacer funcion f(cuartoactual,puertaDestino) = puerta en cuarto sgte
    label entraPorPuerta (cuartoOrigen = 0, puertaDeCuartoOrigen = 0) :
        if (CUARTOactual == 0):
            show bg entrada
        if (CUARTOactual == 1):
            show bg recepcion
        if (CUARTOactual == 2):
            show bg oficina
        if (CUARTOactual == 3):
            show bg sala
        if (CUARTOactual == 4):
            show bg comedor
        if (CUARTOactual == 5):
            show bg simulador
        if (CUARTOactual == 6):
            show bg datacenter
        label finEntraPorPuerta:

        return
