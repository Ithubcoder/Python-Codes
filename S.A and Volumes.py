# Surface Area & Volumes of 2-D and 3-D Figures

while True:

    import math

    print('''...............OPERATIONS...............

    For 2-D Figures :-

    Type 1 for Perimeter of Square.
    Type 2 for T.S.A of Square.

    Type 3 for Perimeter of Rectangle.
    Type 4 for T.S.A of Rectangle.

    Type 5 for Perimeter of Circle.
    Type 6 for T.S.A of Circle.

    Type 7 for Perimeter of Triangle.
    Type 8 for T.S.A of Triangle.

    Type 9 for Perimater of Ellipse.
    Type 10 for T.S.A of Ellipse.    

    For 3-D Figures :-

    Type 11 for Perimeter of Cuboid.
    Type 12 for T.S.A of Cuboid.
    Type 13 for C.S.A of Cuboid.
    Type 14 for Volume of Cuboid.

    Type 15 for Perimeter of Cube.
    Type 16 for T.S.A of Cube.
    Type 17 for C.S.A of Cube.
    Type 18 for Volume of Cube.

    Type 19 for T.S.A of Cylinder.
    Type 20 for C.S.A of Cylinder.
    Type 21 for Volume of Cylinder.

    Type 22 for T.S.A of Cone.
    Type 23 for C.S.A of Cone.
    Type 24 for Volume of Cone.
    
    Type 25 for T.S.A of Sphere.
    Type 26 for C.S.A of Sphere.
    Type 27 for Volume of Sphere.

    Type 28 for T.S.A of Hemi-Sphere.
    Type 29 for C.S.A of Hemi-Sphere.
    Type 30 for Volume of Hemi-Sphere.
    
    Type 31 for Exit.''')

    opr = int(input("Enter a number to perform operation : "))

    if opr == 31:
        break
    else:
        print(".....INVALID OPERATION.....")

    # For 2-D Figures

    if opr == 1:
        side = float(input("Enter Side : "))
        peri = 4 * side
        print("Area of square is : ", peri)

    if opr == 2:
        side = float(input("Enter Side : "))
        area = side * side
        print("Total area of the square is : ", area)

    if opr == 3:
        length = float(input("Enter Length : "))
        breath = float(input("Enter Breath : "))
        peri = 2*(length + breath)
        print("Perimeter of Rectangle is : ", peri)

    if opr == 4:
        length = float(input("Enter Length : "))
        breath = float(input("Enter Breath : "))
        tsa = length * breath
        print("T.S.A of Rectangle is : ", tsa)

    if opr == 5:
        pi = 3.14
        rad = float(input("Enter Radius : "))
        peri = 2 * pi * rad
        print("Perimeter of the Circle is : ",peri)

    if opr == 6:
        pi = 3.14
        rad = float(input("Enter Radius : "))
        tsa = pi * rad ** 2
        print("T.S.A of the Circle is : ",tsa)

    if opr == 7:
        s1 = float(input("Enter First Side : "))
        s2 = float(input("Enter Second Side : "))
        s3 = float(input("Enter Third Side : "))
        peri = s1 + s2 + s3
        print("Perimeter of the Triangle is : ",peri)

    if opr == 8:
        s1 = float(input("Enter First Side : "))
        s2 = float(input("Enter Second Side : "))
        s3 = float(input("Enter Third Side : "))
        half = 0.5
        sq = s2 ** 2
        base = (s3/2) ** 2
        h = sq - base
        final = math.sqrt(h)
        tsa = half * s3 * final
        print("T.S.A of the Triamgle is : ",tsa)
    
    if opr == 9:
        a = float(input("Enter Semi-Major Axis : "))
        b = float(input("Enter Semi-Minor Axis : "))
        pi = 2 * 3.14
        half = (a ** 2 + b ** 2)/2
        final = math.sqrt(half)
        peri = pi * final
        print("Perimeter of the Ellipse is : ",peri)

    if opr == 10:
        a = float(input("Enter Semi-Major Axis : "))
        b = float(input("Enter Semi-Minor Axis : "))
        pi = 3.14
        tsa = pi * a * b
        print("T.S.A of the Ellipse is : ",tsa)

    # For 3-D Figures

    if opr == 11:
        l = float(input("Enter Length : "))
        b = float(input("Enter Breath : "))
        h = float(input("Enter Height : "))
        peri = 4 * (l + b + h)
        print("Perimeter of the Cuboid is : ",peri)

    if opr == 12:
        l = float(input("Enter Length : "))
        b = float(input("Enter Breath : "))
        h = float(input("Enter Height : "))
        tsa = 2 * (l*b + b*h + h*l)
        print("T.S.A of the Cuboid is : ",tsa)

    if opr == 13:
        l = float(input("Enter Length : "))
        b = float(input("Enter Breath : "))
        h = float(input("Enter Height : "))
        csa = 2 * h * (l + b)
        print("C.S.A of the Cuboid is : ",csa)

    if opr == 14:
        l = float(input("Enter Length : "))
        b = float(input("Enter Breath : "))
        h = float(input("Enter Height : "))
        vol = l * b * h
        print("Volume of the Cuboid is : ",vol)

    if opr == 15:
        a = float(input("Enter Side : "))
        peri = 6 * a
        print("Perimeter of the Cube is : ",peri)

    if opr == 16:
        a = float(input("Enter Side : "))
        tsa = 6 * a ** 2
        print("T.S.A of the Cube is : ",tsa)

    if opr == 17:
        a = float(input("Enter Side : "))
        csa = 4 * a ** 2
        print("C.S.A of the Cube is : ",csa)

    if opr == 18:
        a = float(input("Enter Side : "))
        vol = a ** 3
        print("Volume of the Cube is : ",vol)

    if opr == 19:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        tsa = 2 * 3.14 * r * (r + h)
        print("T.S.A of the Cylinder is : ",tsa)

    if opr == 20:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        csa = 2 * 3.14 * r * h
        print("C.S.A of the Cylinder is : ",csa)

    if opr == 21:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        vol = 3.14 * h * r ** 2
        print("Volume of the Cylinder is : ",vol)

    if opr == 22:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        sh = r ** 2 + h ** 2
        l = math.sqrt(sh)
        tsa = 3.14 * r * (r + l)
        print("T.S.A of the Cone is : ",tsa)

    if opr == 23:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        sh = r ** 2 + h ** 2
        l = math.sqrt(sh)
        csa = 3.14 * r * l
        print("C.S.A of the Cone is : ",csa)

    if opr == 24:
        r = float(input("Enter Radius : "))
        h = float(input("Enter Height : "))
        vol = (3.14 * h * r ** 2) / 3
        print("Volume of the Cone is : ")

    if opr == 25:
        r = float(input("Enter Radius : "))
        tsa = 4 * 3.14 * r ** 2
        print("T.S.A of the Sphere is : ",tsa)

    if opr == 26:
        r = float(input("Enter Radius : "))
        csa = 4 * 3.14 * r ** 2
        print("C.S.A of the Sphere is : ",csa)

    if opr == 27:
        r = float(input("Enter Radius : "))
        val = 4 / 3
        vol = val * 3.14 * r ** 3
        print("Volume of the Sphere is : ",vol)

    if opr == 28:
        r = float(input("Enter Radius : "))
        tsa = 3 * 3.14 * r ** 2
        print("T.S.A of the Hemi-Sphere is : ",tsa)

    if opr == 29:
        r = float(input("Enter Radius : "))
        csa = 2 * 3.14 * r ** 2
        print("C.S.A of the Hemi-Sphere is : ",csa)

    if opr == 30:
        r = float(input("Enter Radius : "))
        val = 2 / 3
        vol = val * 3.14 * r ** 3
        print("Volume of the Hemi-Sphere is : ",vol)
