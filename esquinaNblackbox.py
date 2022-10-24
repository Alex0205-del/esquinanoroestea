
"""generamos nuestras matricez/listas sin darle un valor alguno"""

primermatriz = []
segundamatriz = []

"""pedimos al usuario que ingrese el tamaño del que desea
que sean sus tabla y le agregamos una. que sera la de demanda 
y oferta segun sea el caso"""
filas = int (input("\t\t--INGRESE EL NUMERO DE FILAS EN LA TABLA -->  ")) +1
columnas = int(input("\t\t--INGRESE EL NUMERO DE COLUMNAS EN LA TABLA -->  ")) +1

"""generamos las dos tablas, multiplicando las filas por las columnas
la primer matriz nos servira para guardar los datos
y la segunda para los movimientos que se vayan a realizar"""
for i in range (filas):
    primermatriz.append([0]*columnas)
    segundamatriz.append([0]*columnas)

"""pedimos al usuario que ingrese las ofertas y demandas"""

print("\n\t\tINGRESE LAS OFERTAS Y LAS DEMANDAS\n")

"""inicializamos en 0 las variables"""

sumadefilas, sumadecolumnas =0,0

"""generamos el ciclo while para introducir las ofertas y demandas"""

while(True):
    sumadefilas, sumadecolumnas =0,0

    """generamos otro ciclo en el rango de filas introducidas por el usuario para ingresar la orferta"""

    for f in range(filas-1):
        primermatriz[f][columnas-1]= int(input("Ingrese la oferta  [%d] :  -->  "%(f+1)))
        segundamatriz[f][columnas-1] = primermatriz[f][columnas-1]
        sumadefilas += primermatriz[f][columnas-1]

        """inicializamos otro ciclo para las demandas"""

    for c in range (columnas-1):
        primermatriz[filas-1][c]= int(input("Ingrese la demanda  [%d] :  -->  "%(c+1)))
        segundamatriz[filas-1][c] = primermatriz[filas-1][c]
        sumadecolumnas += primermatriz[filas-1][c]
    if (sumadefilas == sumadecolumnas):
        break
    else:
        """si la suma de los valores introducidos no es la misma, el programa pedira que se vuelvan a ingresar los valores"""
        print("\nINGRESE NUEVAMENTE LOS VALORES\nLA SUMA DEBE LA OFERTA DEBE SER IGUAL A LA SUMA DE LA DEMANDA")


"""pedimos al usuario que ingrese los valores del inventario con un ciclo anidado"""

print("\n\t\tINGRESE LOS VALORES DEL INVENTARIO\n")

for f in range (filas-1):
    for c in range(columnas-1):
        primermatriz[f][c] = int(input("Ingrese el elemento de la fila [%d] en la columnda [%d]:\t-->"%(f,c)))

print("\nMostrando movimientos\n")

"""calculamos los movimientos usando estas variables inicializandolas en cero"""

posicionfilas, poscicioncolumnas = 0,0
valordesalida, valordeentrada = 0,0
funcionobjetivo,menor, igual = 0,0,0
sumadefilas, sumadecolumnas =0,0

"""agregamos el ciclo while para el calculo de movimientos"""

while(True):
    sumadefilas, sumadecolumnas =0,0
    for f in range (filas-1):
        sumadefilas += segundamatriz[f][poscicioncolumnas]
    for c in range (columnas -1):
        sumadecolumnas += segundamatriz[posicionfilas][c]

    """asignamos el valor de los valores de salida y entrada ligados a la primer matriz y a la salida"""

    valordesalida = primermatriz [filas-1][poscicioncolumnas] - sumadefilas
    valordeentrada = primermatriz [posicionfilas][columnas-1] - sumadecolumnas

    if(valordesalida<valordeentrada):
        menor = valordesalida
        segundamatriz[posicionfilas][poscicioncolumnas] = menor
        funcionobjetivo+= segundamatriz[posicionfilas][poscicioncolumnas]*primermatriz[posicionfilas][poscicioncolumnas]
        poscicioncolumnas +=1
    elif(valordeentrada<valordesalida):
        menor = valordeentrada
        segundamatriz[posicionfilas][poscicioncolumnas] = menor
        funcionobjetivo+= segundamatriz[posicionfilas][poscicioncolumnas]*primermatriz[posicionfilas][poscicioncolumnas]

        posicionfilas +=1
    elif(valordesalida == valordeentrada):
        igual = (valordesalida+valordeentrada)//2
        segundamatriz[posicionfilas][poscicioncolumnas] = igual
        funcionobjetivo+= segundamatriz[posicionfilas][poscicioncolumnas]*primermatriz[posicionfilas][poscicioncolumnas]

        posicionfilas += 1
        poscicioncolumnas += 1
    
    if(posicionfilas == filas-1 or poscicioncolumnas == columnas -1):
        break

"""mostramos la primer matriz"""

print("\n\t\t--MATRIZ INVENTARIOS--")
for p in range(filas):
    print(primermatriz[p])

"""mostramos la segunda matriz para que muestre los movimientos"""

print ("\n\t\t--MATRIZ MOVIMIENTOS-- ")
for p in range(filas):
    print(segundamatriz[p])

"""agregamos el gasto total"""

print("\n\t\tEL TOTAL DEL GASTO ES DE:\t-->",funcionobjetivo)