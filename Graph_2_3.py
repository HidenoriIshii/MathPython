# -*- coding: utf-8 -*-
'''
Created on 2017/07/06

@author: 0048005456
'''
from pylab import plot,show
# matplotlibでグラフを作る
if __name__ == '__main__':
    x_list = [1,2,3]
    y_list = [2,4,6]
    print('グラフを作る')
#    plot(x_list,y_list)
#    print('グラフに点と線をつける')
#    plot(x_list,y_list,marker='o')
    print('グラフに点のみにする')
    plot(x_list,y_list,'o')
    print('グラフを表示させる')
    show()
    pass