import random

def cargaLista1():
    list1=[]
    for i in range(random.randint(10, 99)):
        list1.append(random.randint(1000, 9999))
    return list1
def cargaLista2():
    list1 = [random.randint(1000, 9999) for i in range(random.randint(10, 99))]
    return list1

def sumatoria(lista):
    suma=sum(lista)
    return suma

def eliminarElemento(lista, num):
    for element in lista:
        if element == num:
            lista.remove(element)

def capicua(lista):
    if lista == lista[::-1]:
        return True
    else:
        return False


def main():
    '''
    numList2=cargaLista2()
    print(numList2)
    '''

    '''numList=cargaLista1()
    print(numList)
    sumaLista=sumatoria(numList)
    print(sumaLista)
    numAEliminar = int(input("Elegir numero a eliminar: "))
    eliminarElemento(numList, numAEliminar)
    print(numList)'''

    capList=[50,17,91,17,50]
    esCap = capicua(capList)
    print(esCap)

if __name__=="__main__":
    main()