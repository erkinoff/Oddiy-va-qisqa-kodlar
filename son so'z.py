
a = input('Enter the required number (0 to 1,000,000 ):')
b = ' '
if a.isdigit():
    a = int(a)
    if a < 1000000:

        A = a % 10
        B = a % 100
        C = a % 1000
        D = a % 10000
        E = a % 100000
        G = a % 1000000
        F = a % 10000000

        if F > 1000000 and F < 2000000:
            b += 'bir mln'
        elif F >= 2000000 and F < 3000000:
            b += ' ikki mln'
        elif F >= 3000000 and F < 4000000:
            b += ' uc mln'
        elif F >= 4000000 and F < 5000000:
            b += ' tort mln'
        elif F >= 5000000 and F < 6000000:
            b += ' bew mln'
        elif F >= 6000000 and F < 7000000:
            b += ' olti mln'
        elif F >= 7000000 and F < 8000000:
            b += ' yetti mln'
        elif F >= 8000000 and F < 9000000:
            b += ' sakkiz mln'
        elif F >= 90000000 and F < 10000000:
            b += ' toqqiz mln'

        if G > 100000 and G < 200000:
            b += ' bir yuz '
        elif G > 200000 and G < 300000:
            b += ' ikki yuz'
        elif G > 300000 and G < 400000:
            b += ' uc yuz'
        elif G > 400000 and G < 500000:
            b += ' tort yuz '
        elif G > 500000 and G < 600000:
            b += ' bew yuz '
        elif G > 600000 and G < 700000:
            b += ' olti yuz'
        elif G > 700000 and G < 800000:
            b += ' yetti yuz '
        elif G > 800000 and G < 900000:
            b += ' sakkiz yuz '
        elif G > 900000 and G < 100000:
            b += ' toqqiz yuz '

        if G == 100000:
            b += ' yuz ming'
        elif G == 200000:
            b += ' ikki yuz ming'
        elif G == 300000:
            b += '  uc yuz ming'
        elif G == 400000:
            b += ' tort yuz ming'
        elif G == 500000:
            b += ' bew yuz ming'
        elif G == 600000:
            b += ' olti yuz ming'
        elif G == 700000:
            b += ' yetti yuz ming'
        elif G == 80000:
            b += ' sakkiz yuz ming'
        elif G == 90000:
            b += ' toqqiz yuz ming'

        if E == 10000:
            b = +' on ming'

        elif E == 20000:
            b += ' yigirma ming'
        elif E == 30000:
            b += ' ottiz ming'
        elif E == 40000:
            b += ' qirq ming'
        elif E == 50000:
            b += ' ellik ming'
        elif E == 60000:
            b += ' oltmiw ming'
        elif E == 70000:
            b += ' yetmiw ming'
        elif E == 80000:
            b += ' sakson ming'
        elif E == 90000:
            b += ' toqson ming'


if E > 10000 and E < 20000:
    b += ' on '
elif E > 20000 and E < 30000:
    b += ' yigirma '
elif E > 30000 and E < 40000:
    b += ' ottiz'
elif E > 40000 and E < 50000:
    b += ' qirq'
elif E > 50000 and E < 60000:
    b += ' ellik'
elif E > 60000 and E < 70000:
    b += ' oltmiw'
elif E > 70000 and E < 80000:
    b += ' yetmiw'
elif E > 80000 and E < 90000:
    b += ' sakson'
elif E > 90000 and E < 100000:
    b += ' toqson'

if D > 1000 and D < 2000:
    b += ' bir ming'
elif D >= 2000 and D < 3000:
    b += '   ikki ming'
elif D >= 3000 and D < 4000:
    b += ' uc ming'
elif D >= 4000 and D < 5000:
    b += ' tort ming'
elif D >= 5000 and D < 6000:
    b += ' bew ming'
elif D >= 6000 and D < 7000:
    b += ' olti ming'
elif D >= 7000 and D < 8000:
    b += ' yetti  ming'
elif D >= 8000 and D < 9000:
    b += ' sakkiz ming'
elif D >= 9000 and D < 10000:
    b += ' toqqiz ming'

if C > 100 and C < 200:
    b += 'bir yuz'
elif C >= 200 and C < 300:
    b += '   ikki yuz'
elif C >= 300 and C < 400:
    b += ' uc yuz'
elif C >= 400 and C < 500:
    b += ' tort yuz'
elif C >= 500 and C < 600:
    b += ' bew yuz'
elif C >= 600 and C < 700:
    b += ' olti yuz'
elif C >= 700 and C < 800:
    b += ' yetti  yuz'
elif C >= 800 and C < 900:
    b += ' sakkiz yuz'
elif C >= 900 and C < 1000:
    b += ' toqqiz yuz'

if B > 10 and B < 19:
    b += ' on'
elif B >= 20 and B < 29:
    b += ' yigirma'
elif B >= 30 and B < 40:
    b += ' ottiz'
elif B >= 40 and B < 50:
    b += ' qirq'
elif B >= 50 and B < 60:
    b += ' ellik'
elif B >= 60 and B < 70:
    b += ' oltmiw'
elif B >= 70 and B < 80:
    b += ' yetmiw'
elif B >= 80 and B < 90:
    b += ' sakson'
elif B >= 90 and B < 100:
    b += ' toqson'

if A == 1:
    b += ' bir'
elif A == 2:
    b += ' ikki'
elif A == 3:
    b += ' uc'
elif A == 4:
    b += ' tort'
elif A == 5:
    b += ' bew'
elif A == 6:
    b += ' olti'
elif A == 7:
    b += ' yetti'
elif A == 8:
    b += ' sakkiz'
elif A == 9:
    b += ' toqqiz'

print(b)