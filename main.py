import math
import random as rand
import numpy as np
import d_Wals_trans_fast_algorithm


n = int(input("Введите размерность:"))
mas = [rand.randint(0, 100) for j in range(2**n)]
print("Исходный массив:\n",mas)
mas=d_Wals_trans_fast_algorithm.fast_algoritm(n, mas)
bit, masd=d_Wals_trans_fast_algorithm.bin_trans_and_bit(n, mas)
a=d_Wals_trans_fast_algorithm.create_cod_mat(n)
A = np.matrix(a)
print("Кодовая матрица:\n",A)
b=d_Wals_trans_fast_algorithm.create_mat_per(n,a)
B=np.matrix(b)
number=d_Wals_trans_fast_algorithm.number(n,b)
bitI, itog=d_Wals_trans_fast_algorithm.permutation(n,number,masd, bit)
print("Количество бит:\n", bitI,"\nИтоговый результат:\n",itog)