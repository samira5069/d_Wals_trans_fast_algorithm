import math
import random as rand
import numpy as np
import d_Walsh_trans_fast_algorithm as W_alg


n = int(input("Введите размерность:"))
mas = [rand.randint(0, 100) for j in range(2**n)]
print("Исходный массив:\n",mas)
mas=W_alg.fast_algoritm(n, mas)
bit, masd=W_alg.bin_trans_and_bit(n, mas)
a=W_alg.create_cod_mat(n)
A = np.matrix(a)
print("Кодовая матрица:\n",A)
b=W_alg.create_mat_per(n,a)
number=W_alg.number(n,b)
bitI, itog=W_alg.permutation(n,number,masd, bit)
print("Количество бит:\n", bitI,"\nИтоговый результат:\n",itog)