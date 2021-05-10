from math import *
print("Tanlang: \
      \n 1. Uchburchak  \
      \n 2. To'g'ri to'rtburchak \
      \n 3. Parallelogramm \
      \n 4. Trapetsiya \
      \n 5. Kvadrat \
      \n 6. Romb \
      \n 7. Aylana \
      \n 8. Doira")      
ja = int(input("--> "))
if ja == 1:                              # Uchburchak
    print(" 1. Perimetri \
          \n 2. Yuzi")
    ja_u = int(input("--> "))
    if ja_u == 1:                        # Perimetri
        a = float(input("a tomonning uzunligi: "))
        b = float(input("b tomonning uzunligi: "))
        c = float(input("c tomonning uzunligi: "))
        if a+b<=c or a+c<=b or b+c<=a:   # Tekshirish
            print("Buday uchburchak mavjud emas!")
        else:
            P_u = a+b+c
            print(f"Uchburchakning perimetri {P_u} ga teng.")
    elif ja_u == 2:                      # Yuzi 
        print(" 1. Balandligiga ko'ra \
              \n 2. Burchagiga ko'ra \
              \n 3. Geron formulasiga ko'ra \
              \n 4. Medianalariga ko'ra")
        ja_u_yuz = int(input('--> '))
        if ja_u_yuz == 1:
            a = float(input("Asosining uzunligi: "))
            h = float(input("Balandligining uzunligi: "))
            if a <= 0 or h <= 0:
                print("Tomon yoki balandlik noldan kichik yoki teng bo'lmaydi!")
            else:
                S = (1/2)*a*h
                print(f"Uchburchakning yuzi {S} ga teng.")
        elif ja_u_yuz == 2:
            a = float(input("a tomon uzunligi: "))
            b = float(input("b tomon uzunligi: "))
            gamma = float(input("Burchakning kattaligi(radian): "))
            if a <= 0 or b <= 0 or gamma <= 0 or gamma >= 6.28:
                print("Tomonlar noldan katta va burchak (0; 6,28) \
                      oraliqda bo'ladi!")
            else:
                S = (1/2)*a*b*gamma
                print(f"Uchburchak yuzi {S} ga teng.")
        elif ja_u_yuz == 3:
            a = float(input("a tomon uzunligi: "))
            b = float(input("b tomon uzunligi: "))
            c = float(input("c tomon uzunligi: "))
            if a <= 0 or b <= 0 or c <= 0:
                print("Tomon noldan katta bo'lishi shart!")
            else:
                p = (a+b+c)/2
                S = (p*(p-a)*(p-b)*(p-c))**(1/2)
                print(f"Uchburchak yuzi {S} ga teng.")
        elif ja_u_yuz == 4:
            m1 = float(input("Birinchi mediana uzunligi: "))
            m2 = float(input("Ikkinchi mediana uzunligi: "))
            m3 = float(input("Uchinchi mediana uzunligi: "))
            if m1 <= 0 or m2 <= 0 or m3 <= 0:
                print("Mediana uzunligi musbat son bo'ladi.")
            else:
                m = (m1+m2+m3)/2
                S = (4/3)*(m*(m-m1)*(m-m2)*(m-m3))**(1/2)
                print(f"Uchburchak yuzi {S} ga teng.")
        else:
            print("Xatolik")
    else:
        print("Xatolik")
elif ja == 2:              # to'g'ri to'rtburchak
    print(" 1. Perimetri \n 2. Yuzi")
    ja_u = int(input("--> "))
    if ja_u == 1: 
        a = float(input("a tomon uzunligi: "))
        b = float(input("b tomon uzunligi: "))
        if a <= 0 or b <= 0:
            print("Tomonlar uzunligi musbat son bo'ladi!")
        else:
            P = (a+b)*2
            print(f"To'g;ri to'rtburchak perimetri {P} ga teng.")
    elif ja_u == 2:
        a = float(input("a tomon uzunligi: "))
        b = float(input("b tomon uzunligi: "))  
        if a <= 0 or b <= 0:
            print("Tomonlar uzunligi musbat son bo'ladi!")
        else:
            S = a*b
            print(f"To'g'ri to'rtburchak yuzi {S} ga teng.")
    else:
        print("Xatolik!")
elif ja == 3:     # Parallelogramm
    print("1. Perimetri \n2. Yuzi")
    ja_p = int(input("--> "))
    if ja_p == 1:
        a = float(input("a tomon uzunligi: "))
        b = float(input("b tomon uzunligi: "))
        if a <= 0 or b <= 0:
            print("Tomonlar uzunligi musbat son bo'ladi!")
        else:
            P = (a+b)*2
            print(f"Parallellogrammning perimetri {P} ga teng.")
    elif ja_p == 2:
        print("1. Asosi va balandligiga qarab \
              \n2. Tomonlari va burchagiga qarab \
              \n3. Diagonallariga qarab \
              \n4. Balandliklari va ular orasidagi burchagiga qarab")
        j = int(input("--> "))
        if j == 1:
            a = float(input("Asos uzunligi: "))
            h = float(input("Balandlik uzunligi: "))
            if a <= 0 or h <=0:
                print("Tomon yoki balandlik uzunligi musbat son bo'ladi!")
            else:
                S = (1/2)*a*h
                print(f"Parallellogrammning yuzi {S} ga teng.")
        elif j == 2:
            a = float(input("a tomon uzunligi: "))
            b = float(input("b tomon uzunligi: "))
            alfa = int(input("Burchak kattaligi: "))
            if a <= 0 or b <= 0 or alfa <= 0 or alfa >= 3.14159:
                print("Tomonlar uzunligi musbat yoki burchak kattaligi \
                      (0; 3.14) oraliqda bo'ladi!")
            else:
                S = a*b*sin(alfa)
                print(f"Parallelogramm yuzi {S} ga teng.")
        elif j == 3:
            d1 = float(input("Birinchi diagonal uzunligi: "))
            d2 = float(input("Ikkinchi diagonal uzunligi: "))
            b = float(input("Diagonallar orasidagi burchak kattaligi: "))
            if d1 <= 0 or d2 <= 0 or b <= 0 or b >= 3.14159:
                print("Diagonallar uzunligi musbat yoki \
                      ular orasidagi burchak (0; 3,14) oraliqda bo'ladi!")
            else:
                S = (1/2)*d1*d2* sin(b)
                print(f"Parallelogramm yuzi {S} ga teng.")
        elif j == 4:
            h1 = float(input("Birinchi balandlik uzunligi: "))
            h2 = float(input("Ikkinchi balandlik uzunligi: "))
            bu = float(input("Balandliklar orasidagi burchak kattaligi: "))
            if h1 <= 0 or h2 <= 0 or bu <= 0 or bu >=3.14159:
                print("Balandlik musbat yoki burchak kattaligi \
                      (0; 3,14) oraliqda bo'ladi!")
            else:
                S = (h1*h2)/sin(bu)
                print(f"Parallelogramm yuzi {S} ga teng.")
        else:
            print("Xatolik!")
elif ja == 4:                              # Trapetsiya
    print("1. Perimetri \n2. Yuzi")
    ja_t = int(input("--> "))
    if ja_t == 1:
        print("1. Teng yonli trapetsiya \n2. Turli tomonli trapetsiya")
        ja_t_t = int(input("--> "))
        if ja_t_t == 1:
            a = float(input("a asos uzunligi: "))
            b = float(input("b asos uzunligi: "))
            c = float(input("Yon tomon uzunligi: "))
            if a <= 0 or b <= 0 or c <= 0:
                print("Tomonlar uzunligi musbat son bo'ladi!")
            else:
                P = a + b + 2*c
                print(f"Trapetsiyaning perimetri {P} ga teng.") 
        elif ja_t_t == 2:
            print("1. Asoslari va balandligiga qarab \
                  2. O'rta chizig'i va balandligiga qarab")
            ja_d = int(input("--> "))
            if ja_d == 1:
                a = float(input("a asos uzunligi: "))
                b = float(input("b asos uzunligi: "))
                h = float(input("Balandlik uzunligi: "))
                if a <= 0 or b <= 0 or h <= 0:
                    print("Balandlik yoki asos musbat son bo'ladi!")
                else:
                    S = (a+b)*h/2
                    print(f"Trapetsiyaning yuzi {S} ga teng.")
            elif ja_d == 2:
                l = float(input("O'rta chiziq uzunligi: "))
                h = float(input("Balandlik uzunligi: "))
                if l <= 0 or h <= 0:
                    print("O'rta chiziq yoki balandlik \
                          uzunligi musbat son bo'ladi")
                else:
                    S = l*h
                    print(f"Trapetsiyaning yuzi {S} ga teng.")
            else:
                print("Xatolik")
        else:
            print("Xatolik")
elif ja == 5:
    print("1. Perimetri \n2. Yuzi")
    ja_k = int(input("--> "))
    if ja_k == 1:
        a = float(input("Tomon uzunligi: "))
        if a <= 0:
            print(F"Kvadratning tomoni noldan katta bo'ladi!")
        else:
            P = 4*a
            print(f"Kvadratning perimetri {P} ga teng.")
    elif ja_k == 2:
        a = float(input("Tomon uzunligi: "))
        if a <= 0:
            print("Kvadratning tomoni musbat son bo'ladi!")
        else:
            S = a**2
            print(F"Kvadratning yuzi {S} ga teng.")
    else:
        print("Xatolik")
elif ja == 6:
    print("1. Perimetri \
          \n2. Yuzi")
    ja_r = int(input("--> "))
    if ja_r == 1:
        a = float(input("Tomon uzunligi: "))
        if a <= 0:
            print("Rombning tomoni musbat son bo'ladi!")
        else:
            P = 4*a
            print(F"Rombning perimetri {P} ga teng.")
    elif ja_r == 2:
        print("1. Tomoni va balandligiga ko'ra \
              \n2. Tomoni va burchagiga ko'ra \
              \n3. Diagonallariga ko'ra")
        ja_e = int(input("--> "))
        if ja_e == 1:
            a = float(input("Tomon uzunligi: "))
            h = float(input("Balandlik uzunligi: "))
            if a <= 0 or h <= 0:
                print("Tomon yoki balandlik musbat son bo'ladi!")
            else:
                S = (1/2)*a*h
                print(f"Rombning yuzi {S} ga teng.")
        elif ja_e == 2:
            a = float(input("Tomon uzunligi: "))
            alfa = float(input("Burchak kattaligi: "))
            if a <= 0 or alfa <= 0 or alfa >= 3.14159:
                print("Tomon musbat yoki burchak \
                      (0; 3.14) oraliqda bo'ladi!")
            else:
                S = a**2*sin(alfa)
                print(F"Rombning yuzi {S} ga teng.")
        elif ja_e == 3:
            d1 = float(input("Birinchi diagonal uzunligi: "))
            d2 = float(input("Ikkinchi diagonal uzunligi: "))
            if d1 <= 0 or d2 <= 0:
                print("Diagonallar uzunligi musbat son bo'ladi!")
            else:
                S = (1/2)*d1*d2
                print(F"Rombning yuzi {S} ga teng.")
        else:
            print("Xatolik")
    else:
        print("Xatolik")
elif ja == 7:
    print("1. Radiusga ko'ra \
          \n2. Diametrga ko'ra")
    ja_q = int(input("--> "))
    if ja_q == 1:
        r = float(input("Radius uzunligi: "))
        PI = 3.14159
        if r <= 0:
            print("Radius musbat son bo'ladi!")
        else:
            l = 2*r*PI
            print(f"Aylana uzunligi {l} ga teng.")
    elif ja_q == 2:
        d = float(input("Diametr uzunligi: "))
        PI = 3.14159
        if d <= 0:
            print("Aylana diametri nolda kichik bo'la olmaydi!")
        else:
            l = d*PI
            print(f"Aylana uzunligi {l} ga teng.")
    else:
        print("Xatolik")
elif ja == 8:
    print("1. Radiusga ko'ra \n2. Diametrga ko'ra")
    ja_l = int(input("--> "))
    if ja_l == 1:
        r = float(input("Radius uzunligi: "))
        PI = 3.14159
        if r <= 0:
            print("Radius musbat son bo'ladi!")
        else:
            S = r**2*PI
            print(F"Doira yuzi {S} ga teng.")
    elif ja_l == 2:
        d = float(input("Diametr uzunligi: "))
        PI = 3.14159
        if d <= 0:
            print("Diametr uzunligi musbat son bo'ladi!")
        else:
            S = d**2*PI/4
            print(F"Doira yuzi {S} ga teng.")
    else:
        print("Xatolik")
else:
    print("Xatolik") 