# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
#from pylab import plot,show,title,xlabel,ylabel,legend,xlim,ylim
import matplotlib.pyplot as plt
from matplotlib.ticker import *
#日本語を使えるようにする
from matplotlib.font_manager import FontProperties

def annualy_tokyo_average_temperature(annualy_aveg_temp):
    #年平均気温取得
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/annually_s.php?'
                 'prec_no=44&block_no=47662&year=2016&month=7&day=6&view=')
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
        if i >= 3761:
            #例外：2014年のデータ構造が他と異なるため為、2015年のデータ先頭は、3761から始まる
            if (i-3761) % 27 == 6:
                year = 2015 + (i-3761)  / 27
                if year <= 2016:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
        elif i >= 3603:
            #例外：2008年のデータ数が26個しかないため異なる為、2009年のデータ先頭は、3555から始まる
            if (i-3603) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                if i == 3744: aveg_temp = 16.6
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 3578:
            #例外：2007年のデータ数が26個しかないため異なる為、2008年のデータ先頭は、3578から始まる
            if (i-3578) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 3555:
            #例外：2006年のデータ数が26個しかないため異なる為、2007年のデータ先頭は、3555から始まる
            if (i-3555) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 3044:
            #例外：1987年のデータ数が26個しかないため異なる為、1988年のデータ先頭は、3044から始まる
            if (i-3044) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 2721:
            #例外：1975年のデータ数が26個しかないため異なる為、1976年のデータ先頭は、2721から始まる
            if (i-2721) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 2641:
            #例外：1972年のデータ数が26個しかないため異なる為、1973年のデータ先頭は、2641から始まる
            if (i-2641) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 2426:
            #例外：1964年のデータ数が26個しかないため異なる為、1965年のデータ先頭は、2426から始まる
            if (i-2426) % 27 == 6:
                year = 1965 + (i-2426)  / 27
                if year >= 1967:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
'''
        elif i >= 2049:
            #例外：1950年のデータ数が26個しかないため異なる為、1951年のデータ先頭は、2049から始まる
            if (i-2049) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 1375:
            #例外：1925年のデータ数が26個しかないため異なる為、1926年のデータ先頭は、1375から始まる
            if (i-1375) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i % 27 == 6:
            aveg_temp = pq(item).text()
            aveg_temp = aveg_temp.replace(' ]','')
            annualy_aveg_temp.append(aveg_temp)
'''
def annualy_yokohama_average_temperature(annualy_aveg_temp):
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
            if (i-3039) % 27 == 6:
                year = 2009 + (i-3039)  / 27
                if year <= 2016:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
        elif i >= 3014:
            #例外：2007年のデータ数が26個しかないため異なる為、2008年のデータ先頭は、3014から始まる
            if (i-3014) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 2989:
            #例外：2006年のデータ数が26個しかないため異なる為、2007年のデータ先頭は、2989から始まる
            if (i-2989) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 2478:
            #例外：1987年のデータ数が26個しかないため異なる為、1976年のデータ先頭は、2478から始まる
            if (i-2478) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 2155:
            #例外：1975年のデータ数が26個しかないため異なる為、1976年のデータ先頭は、2155から始まる
            if (i-2155) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 1482:
            #例外：1950年のデータ数が26個しかないため異なる為、1951年のデータ先頭は、1482から始まる
            if (i-1482) % 27 == 6:
                year = 1951 + (i-1482)  / 27
                if year >= 1967:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
        elif i >= 808:
            #例外：1925年のデータ数が26個しかないため異なる為、1926年のデータ先頭は、808から始まる
            if (i-808) % 27 == 6:
                year = 1926 + (i-808)  / 27
                if year >= 1967:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
        elif i % 27 == 6:
            year = 1896 + i / 27
            if year >= 1967:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)

def annualy_antarctic_average_temperature(annualy_aveg_temp):
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
#                print('{0}年の平均気温 {1} ℃'.format('{:02d}'.format(year), aveg_temp))
        if i >= 1613:
            #例外：2016年のデータ数が26個しかないため異なる為、2017年のデータ先頭は、1613から始まる
            if (i-1613) % 27 == 6:
                year = 2017 + (i-1613)  / 27
                if year <= 2016:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
        elif i >= 1373:
            #例外：2007年のデータ数が26個しかないため異なる為、2008年のデータ先頭は、1373から始まる
            if (i-1373) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 862:
            #例外：1988年のデータ数が26個しかないため異なる為、1989年のデータ先頭は、862から始まる
            if (i-862) % 27 == 6:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
        elif i >= 269:
            #例外：1966年のデータ数が26個しかないため異なる為、1967年のデータ先頭は、269から始まる
            if (i-269) % 27 == 6:
                year = 1967 + (i-269) / 27
                if year >= 1967:
                    aveg_temp = pq(item).text()
                    aveg_temp = aveg_temp.replace(' ]','')
                    annualy_aveg_temp.append(aveg_temp)
'''
        elif i % 27 == 6:
            #1967年-1988年まで
            year = 1957 + i / 27
            if year >= 1967:
                aveg_temp = pq(item).text()
                aveg_temp = aveg_temp.replace(' ]','')
                annualy_aveg_temp.append(aveg_temp)
'''
def annualy_average_temperature():
    fp = FontProperties(fname=r'C:\Windows\Fonts\HGRGM.TTC', size=14)
    years = []
    annualy_aveg_temp_tokyo = []
    annualy_aveg_temp_yokohama = []
    annualy_aveg_temp_antarctic = []
    # 気象庁 年平均気温(1967年-2016年)を取得する
    # 1967年から2016年まで
    for num in range(1967,2017):
        years.append(str(num))

    annualy_tokyo_average_temperature(annualy_aveg_temp_tokyo)
    annualy_yokohama_average_temperature(annualy_aveg_temp_yokohama)
    annualy_antarctic_average_temperature(annualy_aveg_temp_antarctic)

    #キャンバスサイズ
    plt.figure(figsize=(20,8))
#    plt.plot(years,annualy_aveg_temp_antarctic,years,annualy_aveg_temp_tokyo,years,annualy_aveg_temp_yokohama,marker='o')
    plt.plot(years,annualy_aveg_temp_antarctic,marker='o')
    plt.plot(years,annualy_aveg_temp_tokyo,marker='o')
    plt.plot(years,annualy_aveg_temp_yokohama,marker='o')

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
気象庁 東京 任意の年の月平均気温を取得する
'''
def monthly_average_temperature(y):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthly_aveg_temp_tokyo = []
    monthly_aveg_temp_yokohama = []
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
        # 27:気象庁データ表の項目数 6:平均気温項目index
        if i % 27 == 6:
            aveg_temp = pq(item).text()
            monthly_aveg_temp_tokyo.append(aveg_temp)
#気象データ取得：横浜
    #  pyquery
    query = pq(url_yokohama, parser='html')
    # 月毎を取得(データクラス：data_0_0)
    monthly = query('.data_0_0')
    for i, item in enumerate(monthly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 27:気象庁データ表の項目数 6:平均気温項目index
        if i % 27 == 6:
            aveg_temp = pq(item).text()
            monthly_aveg_temp_yokohama.append(aveg_temp)
#            print('{0}月の平均気温 {1} ℃'.format('{:02d}'.format(month), aveg_temp))
    #キャンバスサイズ
    plt.figure(figsize=(10,8))
    plt.plot(months,monthly_aveg_temp_tokyo,months,monthly_aveg_temp_yokohama,marker='o')
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
気象庁 東京 任意の年と月を指定してその月の平均気温を取得する
'''
def daily_average_temperature(y,m):
    days = []
    dayly_aveg_temp_tokyo = []
    dayly_aveg_temp_yokohama = []
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
        if i % 20 == 5:
            day = i / 20 + 1
            aveg_temp = pq(item).text()
            days.append(day)
            dayly_aveg_temp_tokyo.append(aveg_temp)
#気象データ取得：横浜
    #  pyquery
    query = pq(url_yokohama, parser='html')
    # 日毎を取得(データクラス：data_0_0)
    dayly = query('.data_0_0')
    for i, item in enumerate(dayly):
        # 気象データ配列から1個づつ参照して平均気温データかどうかを判別する
        # i:総気象庁データのindex
        # 20:気象庁データ表の項目数 5:平均気温項目index
        if i % 20 == 5:
            aveg_temp = pq(item).text()
            dayly_aveg_temp_yokohama.append(aveg_temp)
#            print('{0}日の平均気温 {1} ℃'.format('{:02d}'.format(day), aveg_temp))
#    plot(days,dayly_aveg_temp_tokyo,marker='o')
#    title_str =
#    title(title_str.text())
#    xlabel('Days')
#    xlim(1,31)
#    ylabel('Temperature')
#    show()
    plt.figure(figsize=(15,8))
    plt.plot(days,dayly_aveg_temp_tokyo,days,dayly_aveg_temp_yokohama,marker='o')
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

if __name__ == '__main__':
    while True:
        # 2.3.2-2.3.5 気温情報取得プログラム
        print '東京の気温データ取得プログラム'
        print '1 月平均気温'
        print '2 日平均気温'
        print '3 年平均気温(1967年-2016年)'
        choice = input('気温データ取得プログラム選択?:')
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
        answer = raw_input('プログラムを継続しますか?(y) for yes : ')
        if answer != 'y': break;
    pass