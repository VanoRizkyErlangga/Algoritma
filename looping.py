
print("Genap 0-10:", end=" ") 
for i in range(0, 11, 2): 
    print(i, end=" ") 

print() 
print("Hitung mundur:", end=" ") 
for i in range(5, 0, -1): 
    print(i, end=" ") 

for v in range(10):
    print("angka :", v)

for x in "VANZZX":
    print("hurufnya adalah :",x)

for i in range(5, 1, -2):
    print("angka :", i)

n = 5 
while n > 0:
      print("Hitung mundur:", n) 
      n -= 1 
print("MULAI!")


tinggi = 6

for i in range(tinggi):
    spasi = " " * (tinggi - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)




