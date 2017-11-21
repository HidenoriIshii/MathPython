# -*- coding: utf-8 -*-
'''
Created on 2017/05/30

@author: 0048005456
'''
#キロメートルをマイルに変換する
def km_to_miles():
    km = float(input('enter distance in kilometers: '))
    miles = km / 1.609
    print('{0} kmは、{1} miles'.format('{0:.3f}'.format(km),'{0:.3f}'.format(miles)))
#マイルをキロメートルに変換する
def miles_to_km():
    miles = float(input('enter distance in miles: '))
    km = miles * 1.609
    print('{0} milesは、{1} km'.format('{0:.3f}'.format(miles),'{0:.3f}'.format(km)))
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

#ポンドをキログラムに変換する
def pound_to_kg():
    pound = float(input('enter weight in pound: '))
    print('kg = pound * 0.453592 ')
    kg = pound * 0.453592
    print('{0}ポンド は、{1}kg'.format('{0:.3f}'.format(pound),'{0:.3f}'.format(kg)))
#キログラムをポンドに変換する
def kg_to_pound():
    kg = float(input('enter weight in kg: '))
    print('pound = kg * 2.20462 ')
    pound = kg * 2.20462
    print('{0}kg は、{1}ポンド'.format('{0:.3f}'.format(kg),'{0:.3f}'.format(pound)))

if __name__ == '__main__':
# 1.7.3. 測定単位変換プログラムの拡張
    print '1.7.3. 測定単位変換プログラムの拡張'
    while True:
        print ' 1 キロメートルをマイルに変換'
        print ' 2 マイルをキロメートルに変換'
        print ' 3 華氏を摂氏に変換'
        print ' 4 摂氏を華氏に変換'
        print ' 5 ポンドをキログラムに変換'
        print ' 6 キログラムをポンドに変換'
        choice = input('測定単位変換プログラム選択?:')
        if choice == 1: km_to_miles()
        elif choice == 2: miles_to_km()
        elif choice == 3: fahrenheit_to_celsius()
        elif choice == 4: celsius_to_fahrenheit()
        elif choice == 5: pound_to_kg()
        elif choice == 6: kg_to_pound()
        answer = raw_input('プログラムを継続しますか?(y) for yes : ')
        if answer != 'y': break;