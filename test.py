import math
print("Hello nha")
print("Hello hello hello hello")
a = 10
b = 8

tong = a + b
print(tong)

def tinhtich():
    a = float(input("Nhap gia tri a = "))
    b = float(input("Nhap gia tri b= "))
    tich = a*b
    print("Tich hai so = ",tich)

def giaiptbac2():
    a = float(input("Nhap he so a = "))
    b = float(input("Nhap he so b = "))
    c = float(input("Nhap gia tri c = "))
    denta = b*b - 4*a*c

    if denta < 0:
        print("Phuong trinh vo nghiem")
    elif denta > 0:
        print("Phuong trinh co 2 nghiem phan biet")
        x1 = (- math.sqrt(denta) + b) / (2*a)
        x2 = (- math.sqrt(denta) - b) / (2*a)
        print("Nghiem x1 = ", x1)
        print("Nghiem x2 = ",x2)
    elif denta == 0:
        print("Phuong trinh co nghiem kep")
        x = -c/a
        print("Nghiem pt la ",x)
tinhtich()
giaiptbac2()