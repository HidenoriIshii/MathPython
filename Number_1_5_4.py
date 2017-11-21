# -*- coding: utf-8 -*-
'''
Created on 2017/05/30

@author: 0048005456
'''
#二次方程式の解を求める
def roots(a,b,c):
    D = (b**2 - 4*a*c)**0.5
    print 'D:{0}'.format(D)
    print ' x_1: x_1=(−b+D) / 2a'
    x_1= ((-b + D) / (2*a))
    print(' x_1:{0}'.format(x_1))

    print ' x_2: x_2=(−b-D) / 2a'
    x_2= ((-b - D) / (2*a))
    print(' x_2:{0}'.format(x_2))

if __name__ == '__main__':
# 1.5.4 二次方程式の解を求めるプログラム
    print '1.5.4 二次方程式の解を求めるプログラム'
    print 'ax2+bx +c'
    print '解の公式: x={−b±√(b2−4ac)} / 2a'
    print ' x_1: x_1={−b+√(b2−4ac)} / 2a'
    print ' x_2: x_2={−b-√(b2−4ac)} / 2a'
    print '  b2は、bの2乗を指す'
    print '公式の分解'
    print ' D: √(b2−4ac)'
    print '  (b2−4ac)の平方根を指数0.5の累乗で計算する'
    print ' -> D = (b**2 - 4*a*c)**0.5'
    print ' x2は、xの2乗を指す'
    try:
        a = input('Input an integer a: ')
        b = input('Input an integer b: ')
        c = input('Input an integer c: ')
        print '2次方程式：{0}x2乗+{1}x+{2}'.format(a,b,c)
    except ValueError:
        print 'You entered an invalide number'


    roots(a,b,c)

