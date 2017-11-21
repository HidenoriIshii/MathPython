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
# 1.3.2 複素数
#キーワード：複素数、実数、虚数i
# 補足情報：リンク先提示
# http://atarimae.biz/archives/500
    a = 2 + 3j
    print type(a)
    print 'a=2+3jのaは、複素数型\n'
    print '複素数の四則演算'

    a = complex(2,3)
    b = complex(3,3)
    print 'a = complex(2,3):{0}'.format(a)
    print 'b = complex(3,3):{0}'.format(b)
    c = a + b
    print 'c = a + b:{0}'.format(c)

    d = a - b
    print 'd = a - b:{0}'.format(d)

    e = a * b
    print '虚数は2乗したら-1になる'
    print 'e = a * b:{0}'.format(e)

    f = a / b
    print 'f = a / b:{0}'.format(f)

    print '剰余（%）、整除（//）除算は複素数に使えない'
    print '複素数の実部と虚部は、属性realとimagを使って次のように取り出す'
    print 'a = complex(2,3)'
    print '実部:{0}'.format(a.real)
    print '虚部:{0}'.format(a.imag)
#共役複素数とは
    print '複素数 a+bi(a,bは実数)に対してa-biを共役複素数と言う'

    a = 2 + 3j
    print 'a=2+3jのaは、共役複素数(conjugate)'
    print a.conjugate()
#複素数の大きさ
    print '複素数の大きさ(magnitude)'
    print ' (a.real**2 +a.imag**2)**0.5 = '
    print (a.real**2 +a.imag**2)**0.5
