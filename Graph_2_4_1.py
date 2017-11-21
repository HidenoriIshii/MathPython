#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017/07/11

@author: 0048005456
'''
'''
 The relationship between gravitational force and distance between two bodies
 2物体間の万有引力と距離の関係
 F = (G x m1 x m2) / r**2
   G:重力定数-> 6.674 x 10**-11(Nm**-2 kg**-2)
   m1:物体1の質量(kg)、m2:物体2の質量(kg)
   r: 物体間の距離(m)
      100m-1000mまで50m単位で刻み19点の距離ついて計算する
'''
import matplotlib.pyplot as plt
from matplotlib.ticker import *
# draw th graph
def draw_graph(dist_list,F_list,m1,m2):
    # x:dist_list y:F_list
    plt.figure(figsize=(15,8))
    plt.plot(dist_list,F_list,marker='o')
    plt.xlabel('Distance in meters(m)')
    plt.ylabel('Gravitational force in newtons(N)')
    plt.title('Gravitational force and distance: m1:{0} kg, m2:{1} kg'.format(m1,m2))
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
    plt.minorticks_on()
    #指定間隔でメモリ表示
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(1))    #x軸主目盛り
#    ax.xaxis.set_major_locator(MultipleLocator(1))  #x軸補助目盛り
    plt.show()
def generate_F_r(m1,m2):
    # generate value for r
    r = range(100,1001,50)
    # empty list to store the calculated values of F(Fの計算値を格納するリスト)
    F = []
    # constant,G 定数G
    G = 6.674 * (10**-11)
    # calculate Force and add it to the list,F 引力を計算しリストFに加える
    for dist in r :
        force = G*(m1*m2) / (dist**2)
        F.append(force)
    # call the draw_graph function draw_graph関数呼び出し
    draw_graph(r, F,m1,m2)

if __name__ == '__main__':
    while True:
        try:
            m1 = input('物体1の質量(kg): ')
            m2= input('物体2の質量(kg): ')
        except:
            print 'You entered an invalide imput'
        else:
            generate_F_r(m1,m2)
            answer = raw_input('プログラムを継続しますか?(y) for yes : ')
            if answer != 'y': break;
    pass