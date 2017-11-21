# -*- coding: utf-8 -*-
'''
Created on 2017/05/30

@author: 0048005456
'''
#華氏を摂氏に変換する
def fahrenheit_to_celsius():
    fahrenheit = float(input('enter degree in fahrenheit: '))
    print('摂氏 = (華氏-32)*(5/9)')
    celsius = ((fahrenheit - 32) * 5) / 9
    print('華氏{0}度 は、摂氏{1} 度'.format('{0:.2f}'.format(fahrenheit),'{0:.2f}'.format(celsius)))
#摂氏を華氏に変換する
def celsius_to_fahrenheit():
    celsius = float(input('enter degree in celsius: '))
    print('華氏 = (摂氏 * (9/5)) + 32 ')
    fahrenheit = (celsius * 9)/5 + 32
    print('摂氏{0}度 は、華氏{1} 度'.format('{0:.2f}'.format(celsius),'{0:.2f}'.format(fahrenheit)))

if __name__ == '__main__':
# 1.5.3.2 測定単位変換プログラム
    print '1.5.3 測定単位変換プログラム2'
    print '1 華氏を摂氏に変換'
    print '2 摂氏を華氏に変換'
    choice = input('測定単位変換プログラム選択?:')
    if choice == 1: fahrenheit_to_celsius()
    elif choice == 2: celsius_to_fahrenheit()


