#menampilkan informasi program

print ("Konversi suhu (Farenheit ke Celcius)")

#input suhu dalam farenheit
F = float(input("Masukkan suhu(Farenheit):"))

#melakukan konversi suhu ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil konversi ke layar
print("Farenheit:", F)
print("Celcius:", C)