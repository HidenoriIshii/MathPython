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

if __name__ == '__main__':
# 1.5.3.1 測定単位変換プログラム
    print '1.5.3 測定単位変換プログラム1'
    print '1 キロメートルをマイルに変換'
    print '2 マイルをキロメートルに変換'
    choice = input('測定単位変換プログラム選択?:')
    if choice == 1: km_to_miles()
    elif choice == 2: miles_to_km()


