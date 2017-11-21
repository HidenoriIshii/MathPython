#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017/07/11

@author: 0048005456
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import *
#日本語を使えるようにする
from matplotlib.font_manager import FontProperties
import math
'''
 generate equally spaced floating point numbers between two given values
 ２つの値の間で等間隔な浮動小数点の生成
'''
'''
    start: 開始時間(s)
    final: 全飛行時間(s)
'''
def frange(start,final,interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers
'''
Draw the trajectory of a body in projectile motion
投射運動物体の軌跡を描く
'''
# draw th graph
def draw_graph(x,y,u):
    plt.plot(x,y,label='{0}(ms)'.format(u))
def set_graph_design(u_list):
    plt.figure(figsize=(15,8))
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    plt.xlabel('x-coordinate(m)')
    plt.ylabel('y-coordinate(m)')
    plt.title(u'Projectile motion of a ball(投射運動物体の軌跡)',fontproperties=fp)
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
    plt.minorticks_on()
    #指定間隔でメモリ表示
#    ax = plt.gca()
#    ax.xaxis.set_major_locator(MultipleLocator(2))  #x軸補助目盛り
#    ax.xaxis.set_minor_locator(MultipleLocator(1))  #x軸主目盛り
#    ax.yaxis.set_major_locator(MultipleLocator(1))  #y軸補助目盛り
#    ax.yaxis.set_minor_locator(MultipleLocator(1)) #y軸主目盛り
def show_plot():
    plt.legend()
    plt.show()

'''
    u:初速度(m/s)
    theta:放射角度θ
'''
def draw_trajectory(u,theta):
    #math.radians()関数を使って度(θ)をラジアンに変換
    theta = math.radians(theta)
    # 重力加速度：9.8 m/s**2
    g = 9.8
#    Time of flight ボール全飛行時間(秒) t_flight = 2*t_peak
#    1: 最高点に到達するまでの時間を求める
#      垂直速度 uy = (u * sinθ) -gt
#      最高到達点の垂直速度：0 m/s = (u * sinθ) -(g * t_peak)
#                                g * t_peak = (u * sinθ)
#                                t_peak = (u * sinθ) / g
#    2: ボール全飛行時間は、 t_flight = 2 * t_peak
#                                     = 2 * { (u * sinθ) / g
    t_flight = 2 * ((u * math.sin(theta)) / g)
    # find time intervals
    intervals = frange(0,t_flight,0.001)
    # list of x and y coordinates
    # x方向水平距離リスト
    x = []
    # y方向水平距離リスト
    y = []
    for  t in intervals:
# 水平距離(Sx) Sx = u * cosθ * t
# 垂直距離(Sy) Sy = u * sinθ * t - 1/2 * (g * (t**2))
        Sx = u * math.cos(theta) * t
        Sy = (u * math.sin(theta) * t) - ((g * (t**2)) * 0.5)
        x.append(Sx)
        y.append(Sy)
    draw_graph(x, y,u)

if __name__ == '__main__':
    while True:
        u_list = []
        try:
            counts = int(input('How many initial velocity datas :'))
        except:
            print 'You entered an invalide input'
        else:
            for i in range(0,counts):
                try:
                    u = float(input('Enter the initial velocity(初速度)(m/s) :'))
                except:
                    print 'You entered an invalide input'
                else:
                    u_list.append(u)
        theta = float(input('Enter the angle of projection(放射角度)(degree) : '))
        set_graph_design(u_list)
        for u in u_list:
            draw_trajectory(u,theta)
        show_plot()
        answer = raw_input('プログラムを継続しますか?(y) for yes : ')
        if answer != 'y': break;
    pass