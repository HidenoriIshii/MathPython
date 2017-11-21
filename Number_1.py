# -*- coding: utf-8 -*-
'''
Created on 2017/05/30

@author: 0048005456
'''

# 分数を扱えるようにするためのlibray
from fractions import Fraction
#webブラウザを開くためのlibray
import webbrowser
import fractions

if __name__ == '__main__':
# 1.2 ラベル：変数に数を割り当てる
    print '1.2 ラベル：変数に数を割り当てる '
    a=3
    print 'a=%d' % a
    a= a+1
    print 'a+1=3+1=%d' % a
# 1.3 さまざまな種類の数の型(type)
    print '1.3 さまざまな種類の数の型(type)'
    print type(3)
    print type(3.5)
    print type(3.0)
    print type(-1)

    print 'a=3.8'
    a = int(3.8)
    print 'int(3.8) = %d' %- a
    a = float(3.8)
    print 'float(3.8) = {:.1f}'.format(a)

# 1.3.1 分数
# 式の中が分数だけなら分数を返す
    print '式の中が分数だけなら分数を返す'
    print 'f = Fraction(3,4)'
    f = Fraction(3,4)
    print f
# 式の中が浮動小数点があるとだけなら浮動小数点を返す
    print '式の中が浮動小数点があるとだけなら浮動小数点を返す'
    f = Fraction(3,4)+1+1.5
    print 'Fraction(3,4)+1+1.5 ={:.2f}'.format(f)
