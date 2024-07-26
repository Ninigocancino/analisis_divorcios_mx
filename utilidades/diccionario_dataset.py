def triger(accion):
    if accion == "ver":
        print("Estos son los terminos usandos en el data set")
        shortcuts = ["tipo_divorcio"]
        for i in shortcuts:
            print(i)
            print("")
    else:
        print("Ingrese un valor valido")

triger("ver")