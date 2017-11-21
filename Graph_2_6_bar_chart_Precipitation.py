# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
#from pylab import plot,show,title,xlabel,ylabel,legend,xlim,ylim
import matplotlib.pyplot as plt
from matplotlib.ticker import *
import numpy as np
#日本語を使えるようにする
from matplotlib.font_manager import FontProperties

# Datas 27:気象庁データ表の項目数
# DataIndex 2:降水量項目index
#           6:平均気温項目index
def annualy_tokyo_data(annualy_data,Datas,DataIndex):
    #年気象データ取得
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/annually_s.php?'
                 'prec_no=44&block_no=47662&year=2016&month=7&day=6&view=')
#気象データ取得：東京
    #  pyquery
    query = pq(url, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    annualy = query('.data_0_0')
    for i, item in enumerate(annualy):
#        print ('i:{0} data:{1}'.format(i,pq(item).text()))
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 27:気象庁データ表の項目数 6:平均気温項目index
        if i >= 3761:
            #例外：2014年のデータ構造が他と異なるため為、2015年のデータ先頭は、3761から始まる
            if (i-3761) % Datas == DataIndex:
                year = 2015 + (i-3761)  / Datas
                if year <= 2016:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
        elif i >= 3603:
            #例外：2008年のデータ数が26個しかないため異なる為、2009年のデータ先頭は、3555から始まる
            if (i-3603) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                if i == 3744: sample_data = 16.6
                annualy_data.append(sample_data)
        elif i >= 3578:
            #例外：2007年のデータ数が26個しかないため異なる為、2008年のデータ先頭は、3578から始まる
            if (i-3578) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 3555:
            #例外：2006年のデータ数が26個しかないため異なる為、2007年のデータ先頭は、3555から始まる
            if (i-3555) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 3044:
            #例外：1987年のデータ数が26個しかないため異なる為、1988年のデータ先頭は、3044から始まる
            if (i-3044) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 2721:
            #例外：1975年のデータ数が26個しかないため異なる為、1976年のデータ先頭は、2721から始まる
            if (i-2721) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 2641:
            #例外：1972年のデータ数が26個しかないため異なる為、1973年のデータ先頭は、2641から始まる
            if (i-2641) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 2426:
            #例外：1964年のデータ数が26個しかないため異なる為、1965年のデータ先頭は、2426から始まる
            if (i-2426) % Datas == DataIndex:
                year = 1965 + (i-2426)  / Datas
                if year >= 1967:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
'''
        elif i >= 2049:
            #例外：1950年のデータ数が26個しかないため異なる為、1951年のデータ先頭は、2049から始まる
            if (i-2049) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 1375:
            #例外：1925年のデータ数が26個しかないため異なる為、1926年のデータ先頭は、1375から始まる
            if (i-1375) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i % Datas == DataIndex:
            sample_data = pq(item).text()
            sample_data = sample_data.replace(' ]','')
            annualy_data.append(sample_data)
'''
# Datas 27:気象庁データ表の項目数
# DataIndex 2:降水量項目index
#           6:平均気温項目index
def annualy_yokohama_data(annualy_data,Datas,DataIndex):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/annually_s.php?'
                    'prec_no=46&block_no=47670&year=&month=&day=&view=')
#気象データ取得：横浜
    #  pyquery
    query = pq(url, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    annualy = query('.data_0_0')
    for i, item in enumerate(annualy):
#        print ('i:{0} data:{1}'.format(i,pq(item).text()))
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 27:気象庁データ表の項目数 6:平均気温項目index
        if i >= 3039:
            #例外：2007年のデータ数が26個しかないため異なる為、2009年のデータ先頭は、3039から始まる
            if (i-3039) % Datas == DataIndex:
                year = 2009 + (i-3039)  / Datas
                if year <= 2016:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
        elif i >= 3014:
            #例外：2007年のデータ数が26個しかないため異なる為、2008年のデータ先頭は、3014から始まる
            if (i-3014) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 2989:
            #例外：2006年のデータ数が26個しかないため異なる為、2007年のデータ先頭は、2989から始まる
            if (i-2989) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 2478:
            #例外：1987年のデータ数が26個しかないため異なる為、1976年のデータ先頭は、2478から始まる
            if (i-2478) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 2155:
            #例外：1975年のデータ数が26個しかないため異なる為、1976年のデータ先頭は、2155から始まる
            if (i-2155) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 1482:
            #例外：1950年のデータ数が26個しかないため異なる為、1951年のデータ先頭は、1482から始まる
            if (i-1482) % Datas == DataIndex:
                year = 1951 + (i-1482)  / Datas
                if year >= 1967:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
        elif i >= 808:
            #例外：1925年のデータ数が26個しかないため異なる為、1926年のデータ先頭は、808から始まる
            if (i-808) % Datas == DataIndex:
                year = 1926 + (i-808)  / Datas
                if year >= 1967:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
        elif i % Datas == DataIndex:
            year = 1896 + i / Datas
            if year >= 1967:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
# Datas 27:気象庁データ表の項目数
# DataIndex 2:降水量項目index
#           6:平均気温項目index
def annualy_antarctic_data(annualy_data,Datas,DataIndex):
    url= ('http://www.data.jma.go.jp/obd/stats/etrn/view/annually_s.php?'
                    'prec_no=99&block_no=89532&year=2016&month=7&day=6&view=')
#気象データ取得：南極
    #  pyquery
    query = pq(url, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    annualy = query('.data_0_0')
    for i, item in enumerate(annualy):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 27:気象庁データ表の項目数 6:平均気温項目index
#                print('{0}年の平均気温 {1} ℃'.format('{:02d}'.format(year), sample_data))
        if i >= 1613:
            #例外：2016年のデータ数が26個しかないため異なる為、2017年のデータ先頭は、1613から始まる
            if (i-1613) % Datas == DataIndex:
                year = 2017 + (i-1613)  / Datas
                if year <= 2016:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
        elif i >= 1373:
            #例外：2007年のデータ数が26個しかないため異なる為、2008年のデータ先頭は、1373から始まる
            if (i-1373) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 862:
            #例外：1988年のデータ数が26個しかないため異なる為、1989年のデータ先頭は、862から始まる
            if (i-862) % Datas == DataIndex:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
        elif i >= 269:
            #例外：1966年のデータ数が26個しかないため異なる為、1967年のデータ先頭は、269から始まる
            if (i-269) % Datas == DataIndex:
                year = 1967 + (i-269) / Datas
                if year >= 1967:
                    sample_data = pq(item).text()
                    sample_data = sample_data.replace(' ]','')
                    annualy_data.append(sample_data)
'''
        elif i % Datas == DataIndex:
            #1967年-1988年まで
            year = 1957 + i / Datas
            if year >= 1967:
                sample_data = pq(item).text()
                sample_data = sample_data.replace(' ]','')
                annualy_data.append(sample_data)
'''

def annualy_average_temperature():
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    years = []
    annualy_tokyo = []
    annualy_yokohama = []
    annualy_antarctic = []
    # 気象庁 年平均気温(1967年-2016年)を取得する
    # 1967年から2016年まで
    for num in range(1967,2017):
        years.append(str(num))
    # 27:気象庁データ表の項目数 6:平均気温項目index
    Datas = 27
    DataIndex = 6
    annualy_tokyo_data(annualy_tokyo,Datas,DataIndex)
    annualy_yokohama_data(annualy_yokohama,Datas,DataIndex)
    annualy_antarctic_data(annualy_antarctic,Datas,DataIndex)

    #キャンバスサイズ
    plt.figure(figsize=(20,8))
#    plt.plot(years,annualy_data_antarctic,years,annualy_data_tokyo,years,annualy_data_yokohama,marker='o')
    plt.plot(years,annualy_tokyo,marker='o')
    plt.plot(years,annualy_yokohama,marker='o')
    plt.plot(years,annualy_antarctic,marker='o')

#    title_str = 'Average monthly temperature in Tokyo in {0}'.format(y)
#    plt.title(title_str)
    plt.title( u'1967年-2016年 平均気温',fontproperties=fp)
    plt.xlabel('Year')
    plt.xlim(1967,2016)
    plt.ylim(-15,20)
    plt.xticks(rotation=50)
    plt.ylabel(u'Temperature(℃)',fontproperties=fp)
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
    plt.minorticks_on()
    #指定間隔でメモリ表示
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(1))    #x軸主目盛り
    ax.xaxis.set_major_locator(MultipleLocator(1))  #x軸補助目盛り
    plt.legend(['Antarctic','Tokyo','Yokohama'],shadow=True,loc='center right')
    plt.show()
'''
気象庁 任意の年の月平均気温を取得する
'''
def monthly_average_temperature(y):
    # 27:気象庁データ表の項目数 6:平均気温項目index
    Datas = 27
    DataIndex = 6
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthly_tokyo = []
    monthly_yokohama = []
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    #月平均
    url_tokyo = ('http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?'
           'prec_no=44&block_no=47662&year={0}&month=&day=&view='.format(y))
    url_yokohama = ('http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?'
           'prec_no=46&block_no=47670&year={0}&month=&day=&view='.format(y))
#気象データ取得：東京
    #  pyquery
    query = pq(url_tokyo, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    monthly = query('.data_0_0')
    for i, item in enumerate(monthly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        if i % Datas == DataIndex:
            sample_data= pq(item).text()
            monthly_tokyo.append(sample_data)
#気象データ取得：横浜
    #  pyquery
    query = pq(url_yokohama, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    monthly = query('.data_0_0')
    for i, item in enumerate(monthly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        if i % Datas == DataIndex:
            sample_data = pq(item).text()
            monthly_yokohama.append(sample_data)
#            print('{0}月の平均気温 {1} ℃'.format('{:02d}'.format(month), sample_data))
    #キャンバスサイズ
    plt.figure(figsize=(10,8))
    plt.plot(months,monthly_tokyo,months,monthly_yokohama,marker='o')
#    title_str = 'Average monthly temperature in Tokyo in {0}'.format(y)
#    plt.title(title_str)
    plt.title( u'{0}年 平均気温'.format(y),fontproperties=fp)
    plt.xlabel('Month')
    plt.xlim(1,12)
    plt.ylim(0,40)
    plt.ylabel(u'Temperature(℃)',fontproperties=fp)
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
    plt.minorticks_on()
    #指定間隔でメモリ表示
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(1))    #x軸主目盛り
    ax.xaxis.set_major_locator(MultipleLocator(1))  #x軸補助目盛り
    plt.legend(['Tokyo','Yokohama'],shadow=True,loc='upper right')
    plt.show()
'''
気象庁 任意の年と月を指定してその月の平均気温を取得する
'''
def daily_average_temperature(y,m):
    # 20:気象庁データ表の項目数 5:降水量項目index
    Datas = 20
    DataIndex = 5
    days = []
    dayly_tokyo = []
    dayly_yokohama = []
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    #日平均
    url_tokyo = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=44&block_no=47662&year={0}&month={1}&day=&view='.format(y,m))
    url_yokohama = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=46&block_no=47670&year={0}&month={1}&day=&view='.format(y,m))
#気象データ取得：東京
    #  pyquery
    query = pq(url_tokyo, parser='html')
    # 日毎を取得(データクラス：data_0_0)
    dayly = query('.data_0_0')
    for i, item in enumerate(dayly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 20:気象庁データ表の項目数 5:平均気温項目index
        if i % Datas == DataIndex:
            day = i / Datas + 1
            sample_data = pq(item).text()
            days.append(day)
            dayly_tokyo.append(sample_data)
#気象データ取得：横浜
    #  pyquery
    query = pq(url_yokohama, parser='html')
    # 日毎を取得(データクラス：data_0_0)
    dayly = query('.data_0_0')
    for i, item in enumerate(dayly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 20:気象庁データ表の項目数 5:平均気温項目index
        if i % Datas == DataIndex:
            sample_data = pq(item).text()
            dayly_yokohama.append(sample_data)
#            print('{0}日の平均気温 {1} ℃'.format('{:02d}'.format(day), sample_data))
#    plot(days,dayly_sample_data_tokyo,marker='o')
#    title_str =
#    title(title_str.text())
#    xlabel('Days')
#    xlim(1,31)
#    ylabel('Temperature')
#    show()
    plt.figure(figsize=(15,8))
    plt.plot(days,dayly_tokyo,days,dayly_yokohama,marker='o')
#    title_str = 'Average daily temperature in Tokyo in {0} / {1}'.format(y,m)
#    plt.title(title_str)
    plt.title( u'{0}年{1}月 平均気温'.format(y,m).format(y),fontproperties=fp)

    plt.xlabel('Days')
    plt.xlim(1,31)
    plt.ylim(0,40)
    plt.ylabel(u'Temperature(℃)',fontproperties=fp)
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
    plt.minorticks_on()
    #指定間隔でメモリ表示
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(1))    #x軸主目盛り
    ax.xaxis.set_major_locator(MultipleLocator(1))  #x軸補助目盛り
    plt.legend(['Tokyo','Yokohama'],shadow=True,loc='upper right')
    plt.show()

# 降水量データ取得
def annualy_precipitation():
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    years = []
    annualy_tokyo = []
    annualy_yokohama = []
    # 気象庁 年平均気温(1967年-2016年)を取得する
    # 1967年から2016年まで
    for num in range(1967,2017):
        years.append(str(num))

    # 27:気象庁データ表の項目数 2:降水量項目index
    Datas = 27
    DataIndex = 2
    annualy_tokyo_data(annualy_tokyo,Datas,DataIndex)
    annualy_yokohama_data(annualy_yokohama,Datas,DataIndex)
    #キャンバスサイズ
    w = 0.4
    Y1 = np.array(annualy_tokyo)
    Y2 = np.array(annualy_yokohama)
    X = np.arange(len(Y1))
    plt.figure(figsize=(20,8))
    plt.bar(X,Y1, color="b", width=w,)
    plt.bar(X+0.6,Y2, color='g', width=w,align='center')
    plt.title( u'1967年-2016年 年降水量合計推移',fontproperties=fp)
    plt.xlabel('Year')
    plt.xticks(X+0.4,years,rotation=50)
    plt.ylabel(u'降水量(mm)',fontproperties=fp)
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
#    plt.minorticks_on()
    #指定間隔でメモリ表示
#    ax = plt.gca()
#    ax.xaxis.set_minor_locator(MultipleLocator(1))    #x軸主目盛り
#    ax.xaxis.set_major_locator(MultipleLocator(1))  #x軸補助目盛り
    plt.legend(['Tokyo','Yokohama'],shadow=True,loc='center right')
    plt.show()
'''
気象庁 任意の年の月平均気温を取得する
'''
def monthly_precipitation(y):
    # 27:気象庁データ表の項目数 2:降水量項目index
    Datas = 27
    DataIndex = 2
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',]
    monthly_tokyo = []
    monthly_yokohama = []
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    #月平均
    url_tokyo = ('http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?'
           'prec_no=44&block_no=47662&year={0}&month=&day=&view='.format(y))
    url_yokohama = ('http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s1.php?'
           'prec_no=46&block_no=47670&year={0}&month=&day=&view='.format(y))
#気象データ取得：東京
    #  pyquery
    query = pq(url_tokyo, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    monthly = query('.data_0_0')
    for i, item in enumerate(monthly):
        # 気象データ配列から1個づつ参照して降水量データかどうかを判別する
        # i:総気象庁データのindex
        if i % Datas == DataIndex:
            sample_data = pq(item).text()
            monthly_tokyo.append(sample_data)
#気象データ取得：横浜
    #  pyquery
    query = pq(url_yokohama, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    monthly = query('.data_0_0')
    for i, item in enumerate(monthly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        if i % Datas == DataIndex:
            sample_data = pq(item).text()
            monthly_yokohama.append(sample_data)
#            print('{0}月の平均気温 {1} ℃'.format('{:02d}'.format(month), sample_data))
    #キャンバスサイズ
    plt.figure(figsize=(10,8))
    #キャンバスサイズ
    w = 0.4
    Y1 = np.array(monthly_tokyo)
    Y2 = np.array(monthly_yokohama)
    X = np.arange(len(Y1))
    plt.bar(X,Y1, color="b", width=w,)
    plt.bar(X+0.6,Y2, color='g', width=w ,align='center')
#    title_str = 'Average monthly temperature in Tokyo in {0}'.format(y)
#    plt.title(title_str)
    plt.title( u'{0}年 月降水量'.format(y),fontproperties=fp)
    plt.xlabel('Month')
    plt.xticks(X+w,months,rotation=50)
    plt.ylabel(u'降水量',fontproperties=fp)
    #グリッド表示有効
    plt.grid()
    #メモリ表示有効
#    plt.minorticks_on()
    #指定間隔でメモリ表示
#    ax = plt.gca()
#    ax.xaxis.set_minor_locator(MultipleLocator(1))    #x軸主目盛り
#    ax.xaxis.set_major_locator(MultipleLocator(1))  #x軸補助目盛り
    plt.legend(['Tokyo','Yokohama'],shadow=True,loc='upper right')
    plt.show()

if __name__ == '__main__':
    while True:
        # 2.3.2-2.3.5 気温情報取得プログラム
        print '気象データ取得プログラム'
        print '1 月平均気温'
        print '2 日平均気温'
        print '3 年平均気温(1967年-2016年)'
        print '4 月降水量'
        print '5 年降水量(1967年-2016年)'
        choice = input('気象データ取得プログラム選択?:')
        if choice == 1:
            try:
                year = int(input('気象データ取得年 : '))
            except:
                print 'You entered an invalide number'
            else:
                monthly_average_temperature(year)
        elif choice == 2:
            try:
                year = int(input('気象データ取得年 : '))
            except :
                print 'You entered an invalide number'
            else:
                try:
                    month = int(input('気象データ取得月 : '))
                except:
                    print 'You entered an invalide number'
                else:
                    daily_average_temperature(year,month)
        elif choice == 3: annualy_average_temperature()
        if choice == 4:
            try:
                year = int(input('気象データ取得年 : '))
            except:
                print 'You entered an invalide number'
            else:
                monthly_precipitation(year)
        elif choice == 5: annualy_precipitation()
        answer = raw_input('プログラムを継続しますか?(y) for yes : ')
        if answer != 'y': break;
    pass