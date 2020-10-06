#-*-coding:utf-8-*-
'''
多变量非线性方程求解
'''
from sympy import *
import numpy as np
np.set_printoptions(suppress=True)

n = 20000#控制迭代次数

def Henon(x,y,n):
    for i in range(n):
        x1 = 1 - 1.4 * x ** 2 + y
        y1 = 0.3 * x
        x = x1
        y = y1
    return x,y

def Jacobian():
    count=0
    a = 0.123456789
    b = 0.123456789
    # 使用符号方式求解
    x, y = symbols("x,y")
    f_mat = Matrix([1 - 1.4 * x ** 2 + y, 0.3 * x])
    # 求解雅各比矩阵
    jacobi_mat = f_mat.jacobian([x, y])#带变量的雅各比矩阵形式是固定的
    a,b=Henon(a,b,5001)#先迭代1000次，消除初始影响.以第1001次的值作为初始值
    # 这里为获取初始雅各比矩阵，将第一次放置在循环外
    result = jacobi_mat.subs({x: a, y: b})  # 将变量替换为当前迭代值，得到当前的雅各比矩阵（数字）
    J = result  # 得到初始的雅各比矩阵
    a, b = Henon(a, b, 1)  # 每次迭代一次获取当前的迭代值
    while(count<n-1):
        result = jacobi_mat.subs({x: a, y: b})  # 将变量替换为当前迭代值，得到当前的雅各比矩阵(数字)
        J = J*result  # 计算累积的雅各比矩阵
        a, b = Henon(a, b, 1)  # 每次迭代一次获取当前的迭代值
        count=count+1
    return J

def LE_calculate(J):
    eig_dic = J.eigenvals()#传入一个累积的雅各比矩阵
    eig_list = list(eig_dic)#求累积雅各比矩阵的特征值
    eig_1 = eig_list[0]
    eig_2 = eig_list[1]
    LE1=N(ln(abs(eig_1))/n)
    LE2=N(ln(abs(eig_2))/n)
    print(LE1)
    print(LE2)

if __name__ == '__main__':
    J=Jacobian()
    LE_calculate(J)
