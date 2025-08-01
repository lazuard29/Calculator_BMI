"Program Perhitungan BMI"

print ("PERHITUNGAN BMI (BODY MASS INDEX)")
print ("---------------------------------")
while True:
    berat_badan = input("Masukan berat badan anda (kg): ") #bentuknya str
    berat_badan = float(berat_badan) #diubah
    tinggi_badan = input("masukan tinggi badan anda (m): ")
    tinggi_badan = float(tinggi_badan)

    bmi = berat_badan/(tinggi_badan**2)

    berat_badan_ideal = dict()
    berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
    berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

    if bmi < 18.5:
        kategori = "anda kekurangan berat badan"
    elif bmi < 25:
        kategori = "Nilai BMI anda adalah normal "
    elif bmi < 30:
        kategori = "anda kelebihan berat badan"
    else:
        kategori = "anda mengalami obesitas"
    print ("hasil kalkulator BMI anda adalah:")
    print ("---------------------------------")
    print("\nNilai BMI anda adalah: %1.2f kg/m^2"%(bmi))
    # bisa juga print (f"nilai bmi anda adalah {bmi:.2f} kg/m^2) .2f adalah angka belakang koma yang dibawa
    # bisa juga print ("nilai bmi anda adalah {0} kg/m^2".format(bmi)) 0 berarti bmi index ke-0

    print(kategori)
    print("Berat badan ideal anda adalah dalam rentang %1.2f kg sampai dengan %1.2f kg"%(berat_badan_ideal["bawah"], berat_badan_ideal["atas"]))

    print ("Terima kasih sudah menggunakan program ini :)")