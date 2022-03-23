longitud = input("Ingrese la longitud de la palabra: ")

ruta = "C:\\Users\\robin\\OneDrive\\Escritorio\\Python\\Proyectos\\BUSCAPALABRA\\diccionario-espanol-txt-master\\diccionario-espanol-txt-master\\length\\0"+longitud+".txt"
f = open (ruta,'r', encoding="utf8")

texto = f.readlines()
texto = [x.strip() for x in texto]
f.close()

diccionario = []
diccionario1 = []
buscar = ""

while True:

    print("Ingrese las letras que no contiene ademas de: ", buscar)
    buscar = input("Ingrese las letras que no contiene: ")

    for _ in range(10):
        for palabra in texto:
            for letras in palabra:
                for i in range(len(buscar)):
                    if letras == buscar[i]:
                        try:
                            texto.remove(palabra)
                        except: pass

    print(texto,len(texto))

    sitiene = input("Ingrese las letras que contiene en cualquier orden: ")
    bandera = 0

    for palabra in texto:
        for i in range(len(sitiene)):
            if palabra.count(sitiene[i])>0:
                bandera = bandera + 1
            else: 
                bandera = 0
        if bandera >= len(sitiene):
            try: 
                diccionario1.index(palabra)
            except:
                diccionario1.append(palabra)
            bandera = 0

    texto.clear()
    texto = diccionario1.copy()
    diccionario1.clear()
    print(texto,len(texto))

    c="s"
    while c == "s":

        letra = input("Ingrese 1 letra que contenga: ")
        if len(letra) != 0:
            posicion = int(input("Ingrese la posicion: ")) - 1
            pos_dicci = 0

            for palabra in texto:
                for letras in palabra:
                    if letras == letra and pos_dicci == posicion:
                        diccionario.append(palabra)
                    pos_dicci = pos_dicci + 1
                pos_dicci = 0

            texto = diccionario.copy()
            diccionario.clear()
            print(texto,len(texto))
            c = input("Continuar? s/n: ")

        else:
            c="n"