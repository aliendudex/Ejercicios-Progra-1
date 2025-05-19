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





'''
numList=cargaLista1()
print(numList)
numList2=cargaLista2()
print(numList2)
sumaLista=sumatoria(numList)
'''



