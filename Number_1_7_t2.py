# -*- coding: utf-8 -*-
'''
Created on 2017/05/30

@author: 0048005456
'''
#乗算表生成器拡張プログラム
def is_multi_table(x,y):
    for i in range(1,(y+1)):
        # 小数点以下の桁数の指定'{0:.af}'.format(b)
        # aには桁数を入れる。bは表示する値
        print('{0} × {1} = {2}'.format(x,i,'{0:.2f}'.format(x*i)))


if __name__ == '__main__':
# 1.5.2 乗算表の生成プログラム（#乗算表生成器拡張プログラム）
    print '1.5.2 乗算表の生成プログラム'
    while True:
        print '整数aの倍数をb番目まで求める'
        try:
            a = input('Input an integer a: ')
        except ValueError:
            print 'You entered an invalide number'
        try:
            b = input('Input an integer b: ')
        except ValueError:
            print 'You entered an invalide number'

        is_multi_table(a, b)
        answer = raw_input('プログラムを継続しますか?(y) for yes : ')
        if answer != 'y': break;