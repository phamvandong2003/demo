import math
import random
print("--------HELLO NHA----------")
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
        x1 = (-(b) + (math.sqrt(denta))) / (2*a)
        x2 = (-(b) - (math.sqrt(denta))) / (2*a)
        print("Nghiem x1 = ",x1)
        print("Nghiem x2 = ",x2)
    elif denta == 0:
        print("Phuong trinh co nghiem kep")
        x = -b / (2*a)
        print("Nghiem pt la ",x)

def taixiu():
    print("KET QUA PHIEN DAU GIA")
    xx1 = random.randint(1,6)
    xx2 = random.randint(1,6)
    xx3 = random.randint(1,6)
    ket_qua = xx1 + xx2 + xx3

    if ket_qua <= 10:
        print(xx1, xx2, xx3)
        print("Ket qua la Xiu",ket_qua)
    else:
        print(xx1, xx2, xx3)
        print("Ket qua la Tai",ket_qua)
taixiu()