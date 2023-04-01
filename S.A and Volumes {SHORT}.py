# Surface Area & Volumes of 2-D and 3-D Figures

while True:

    import math

    print('''...............OPERATIONS...............

    For 2-D Figures :-

    Type 1 to Perform Operations on Square.
    Type 2 to Perform Operations on Rectangle.
    Type 3 to Perform Operations on Circle.
    Type 4 to Perform Operations on Triangle.
    Type 5 to Perform Operations on Ellipse.

    For 3-D Figures :-

    Type 6 to Perform Operations on Cuboid.
    Type 7 to Perform Operations on Cube.
    Type 8 to Perform Operations on Cylinder.
    Type 9 to Perform Operations on Cone.
    Type 10 to Perform Operations on Sphere.
    Type 11 to Perform Operations on Hemi-Sphere.
    
    Type 12 for Exit.''')

    opr = int(input("Enter a number to perform operation : "))

    if opr == 12:
        break
    else:
        print(".....INVALID OPERATION.....")

    # For 2-D Figures

    if opr == 1:
        side = float(input("Enter Side : "))
        peri = 4 * side
        print("Area of square is : ", peri)
        area = side * side
        print("Total area of the square is : ", area)

    if opr == 2:
        length = float(input("Enter Length : "))
        breath = float(input("Enter Breath : "))
        peri = 2 * (length + breath)
        print("Perimeter of Rectangle is : ", peri)
        tsa = length * breath
        print("T.S.A of Rectangle is : ", tsa)

    if opr == 3:
        pi = 3.14
        rad = float(input("Enter Radius : "))
        peri = 2 * pi * rad
        print("Perimeter of the Circle is : ",peri)
        tsa = pi * rad ** 2
        print("T.S.A of the Circle is : ",tsa)

    if opr == 4:
        s1 = float(input("Enter First Side : "))
        s2 = float(input("Enter Second Side : "))
        s3 = float(input("Enter Third Side : "))
        peri = s1 + s2 + s3
        print("Perimeter of the Triangle is : ",peri)
        half = 0.5
        sq = s2 ** 2
        base = (s3/2) ** 2
        h = sq - base
        final = math.sqrt(h)
        tsa = half * s3 * final
        print("T.S.A of the Triamgle is : ",tsa)

    if opr == 5:
        a = float(input("Enter Semi-Major Axis : "))
        b = float(input("Enter Semi-Minor Axis : "))
        pi = 2 * 3.14
        half = (a ** 2 + b ** 2)/2
        final = math.sqrt(half)
        peri = pi * final
        print("Perimeter of the Ellipse is : ",peri)
        pi = 3.14
        tsa = pi * a * b
        print("T.S.A of the Ellipse is : ",tsa)

    # For 3-D Figures

    if opr == 6:
        l = float(input("Enter Length : "))
        b = float(input("Enter Breath : "))
        h = float(input("Enter Height : "))
        peri = 4 * (l + b + h)
        print("Perimeter of the Cuboid is : ",peri)
        tsa = 2 * (l*b + b*h + h*l)
        print("T.S.A of the Cuboid is : ",tsa)
        csa = 2 * h * (l + b)
        print("C.S.A of the Cuboid is : ",csa)
        vol = l * b * h
        print("Volume of the Cuboid is : ",vol)

    if opr == 7:
        a = float(input("Enter Side : "))
        peri = 6 * a
        print("Perimeter of the Cube is : ",peri)
        tsa = 6 * a ** 2
        print("T.S.A of the Cube is : ",tsa)
        csa = 4 * a ** 2
        print("C.S.A of the Cube is : ",csa)
        vol = a ** 3
        print("Volume of the Cube is : ",vol)

    if opr == 8:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        tsa = 2 * 3.14 * r * (r + h)
        print("T.S.A of the Cylinder is : ",tsa)
        csa = 2 * 3.14 * r * h
        print("C.S.A of the Cylinder is : ",csa)
        vol = 3.14 * h * r ** 2
        print("Volume of the Cylinder is : ",vol)

    if opr == 9:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        sh = r ** 2 + h ** 2
        l = math.sqrt(sh)
        tsa = 3.14 * r * (r + l)
        print("T.S.A of the Cone is : ",tsa)
        sh = r ** 2 + h ** 2
        l = math.sqrt(sh)
        csa = 3.14 * r * l
        print("C.S.A of the Cone is : ",csa)
        vol = (3.14 * h * r ** 2) / 3
        print("Volume of the Cone is : ")

    if opr == 10:
        r = float(input("Enter Radius : "))
        tsa = 4 * 3.14 * r ** 2
        print("T.S.A of the Sphere is : ",tsa)
        csa = 4 * 3.14 * r ** 2
        print("C.S.A of the Sphere is : ",csa)
        vol = val * 3.14 * r ** 3
        print("Volume of the Sphere is : ",vol)

    if opr == 11:
        r = float(input("Enter Radius : "))
        tsa = 3 * 3.14 * r ** 2
        print("T.S.A of the Hemi-Sphere is : ",tsa)
        csa = 2 * 3.14 * r ** 2
        print("C.S.A of the Hemi-Sphere is : ",csa)
        val = 2 / 3
        vol = val * 3.14 * r ** 3
        print("Volume of the Hemi-Sphere is : ",vol)
