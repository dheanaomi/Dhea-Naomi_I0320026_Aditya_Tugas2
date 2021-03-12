
def persegi_panjang():
    print ("==Masukkan panjang persegi panjang==")
    p = float(input("Panjang :"))
    print ("==Masukkan lebar persegi panjang==")
    l = float(input("Lebar :"))
    print ("Luas persegi panjang adalah",p*l)
def luas_lingkaran():
    print ("==Masukkan Jari-jari lingkaran==")
    r=float(input("Jari-jari :"))
    phi = 3.14
    print("Luas lingkaran adalah", phi*(r**2))
def luas_permukaan_kubus():
    print("==Masukkan sisi kubus==")
    sisi=float(input("Sisi :"))
    print("Luas permukaan kubus adalah",6*sisi*sisi)
def celciuskefarenheit():
    print("==Masukkan suhu dalam celcius==")
    c=float(input("Suhu(Celcius) :"))
    f=((9/5)*c)+32
    print("Suhu Farenheit adalah", f)
def reamurkekelvin():
    print ("==Masukkan suhu dalam reamur==")
    r=float(input("Suhu(Reamur) :"))
    k=((5/4)*r)+273
    print("Suhu Kelvin adalah", k)
def menu():
    print("Pilih fungsi dalam program ini")
    print("1.Menghitung Luas Persegi Panjang")
    print("2.Menghitung Luas Lingkaran")
    print("3.Menghitung Luas Permukaan Kubus")
    print("4.Menghitung Suhu Celcius ke Farenheit")
    print("5.Menghitung Suhu Reamur ke Kelvin")
    pilihan = int(input("Pilihan : "))
    select(pilihan)
def select(pilih):
    if pilih == 1:
        persegi_panjang()
    elif pilih == 2:
        luas_lingkaran()
    elif pilih == 3:
        luas_permukaan_kubus()
    elif pilih == 4:
        celciuskefarenheit()
    elif pilih == 5:
        reamurkekelvin()
    else:
        print ("tidak tersedia")
    menu()
menu()


