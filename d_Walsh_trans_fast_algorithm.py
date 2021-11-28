import math
import random as rand
import numpy as np

#Реализация быстрых алгоритмов
def fast_algoritm(n, mas):
    masf=[0 for i in range(2**n)]
    for i in range(n):
        for k in range(0,2**n,2**(i+1)):
            for j in range (k,k+2**i):
                masf[j]=mas[j]+mas[j+2**i]
                masf[j+2**i]=mas[j]-mas[j+2**i]
        mas=masf.copy()
    return mas
#Алгоритм вычисления количества бит и перевод в двоичный код
def bin_trans_and_bit(n, mas):
    bit=[0 for i in range(2**n)]
    masd=['' for i in range(2**n)]
    for i in range(2**n):
        k=0
        while mas[i]!=0:
            masd[i]=str(abs(mas[i])%2)+masd[i]
            mas[i]=abs(mas[i])//2
            k=k+1
        if mas[i]<0:
            k=k+1
            masd[i]=str(0)+masd[i]
        bit[i]=k
    return bit, masd
#Создание кодовой матрицы
def create_cod_mat(n):
    d=0
    while d==0 or d>1 or d<-1:
        a = [[rand.randint(0, 1) for j in range(n)] for i in range(n)]
        d = np.linalg.det(a)
    return a
#Создание матрицы перестановок
def create_mat_per(n, a):
    k = 0
    b=[[0 for j in range(n)] for i in range(2**n)]
    for i in range(1,2**n):
        if i == 2**k:
            for j in range(n):
                b[i][j]=a[k][j]
            k=k+1
        else:
            for j in range(n):    
                b[i][j]=(b[i-2**(k-1)][j] + b[2**(k-1)][j])%2
    return b
#Вычисление места для перестановки
def number(n, b):
    number=[0 for j in range(2**n)]
    for i in range(2**n):
        k=n-1
        for j in range (n):
            number[i]=number[i]+b[i][j]*(2**k)
            k=k-1
    return number
#Выполнение перестановки и получение итогапше
def permutation(n, number, masd, bit):
    bitI=[0 for i in range(2**n)]
    masp=['' for j in range(2**n)]
    for i in range(2**n):
        for k in range(2**n):
            if number[k]==i:
                masp[k]=masd[i]
                bitI[k]=bit[i]
    itog=''
    for i in range(2**n):
        itog=itog+masp[i]
    return bitI, itog