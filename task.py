while True:
    a = input("введите длину стены ")
    b = input("введите ширину стены ")
    c = input("введите высоту стены ")
    d = input("введите ширину окна ")
    e = input("введите высоту окна ")
    f = input("введите ширину двери ")
    g = input("введите высоту двери ")
    k = input("введите ширину обоев ")
    l = input("введите длину обоев ")

    if a.isnumeric() and b.isnumeric() and c.isnumeric()\
        and d.isnumeric() and e.isnumeric() and f.isnumeric()\
            and g.isnumeric() and k.isnumeric() and l.isnumeric():
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        g = int(g)
        k = int(k)
        l = int(l)
        print("данные верные")
        break
    else:
        print("ошибка ввода данных")
        continue
walls = 2*(c*b+c*a) - (2*d*e+f*g)
wallpaper = k*l
n = round(walls/wallpaper)
if n < walls/wallpaper:
    n += 1

print("количество рулонов для обклейки = ", n)
