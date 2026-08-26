print("=== KALKULATOR BMI ===")


berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))


tinggi_meter = tinggi / 100


bmi = berat / (tinggi_meter ** 2)

print("=== HASIL ===")
print(f"Berat badan : {berat} kg")
print(f"Tinggi badan: {tinggi} cm")
print(f"BMI kamu    : {bmi:.2f}")


if bmi < 18.5:
    print("Kategori   : Kurus")
elif bmi < 25:
    print("Kategori   : Normal")
elif bmi < 30:
    print("Kategori   : Kelebihan")
else:
    print("Kategori   : Kamu Bukan Manusia")