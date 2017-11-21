# -*- coding: utf-8 -*-
'''
Created on 2017/05/30

@author: 0048005456
'''
#webブラウザを開くためのlibray
from __builtin__ import True
#1.5 数学プログラム
def is_factor(x,y):
    if y % x == 0: return True
    return False

if __name__ == '__main__':
# 1.5整数プログラム
# 整数の因数について
    print '1.5 数学プログラム'
    print '1.5.1 整数の因数計算プログラム'
    print '因数チェック関数 is_factor(a,b)'
    print '0出ない整数aで他の整数bを割った余りが0なら、aをbの因数(factor)と言う'
    try:
        a = input('Input an integer a: ')
        a = float(a)
    except ValueError:
        print 'You entered an invalide number'
    try:
        b = input('Input an integer b: ')
    except ValueError:
        print 'You entered an invalide number'
    b = float(b)
    if b > 0 and b.is_integer():
        if is_factor(a,int(b)) == True:
            print'{0}は{1}の因数です'.format(a,b)
        else:
            print str(a)+'は'+str(b)+'の因数でない'
    else :print('Please enter a positive integer')


# 0でない整数の因数を見つける
    print '任意の整数の因数を見つける'
    try:
        c = input('Input an integer c: ')
    except ValueError:
        print 'You entered an invalide number'

    print 'c:'+str(c)+'の因数を見つける'
    c = float(c)
    if c > 0 and c.is_integer():
        for i in range(1,int(c)):
            if is_factor(i,int(c)) == True: print 'bの因数:'+str(i)
    else :print('Please enter a positive integer')

