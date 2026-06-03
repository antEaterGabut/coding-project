#pembuatan file struk
with open("struk-pembeli.txt", "w") as file:
    file.write("list pelanggan hari ini")

#daftar menu
def menu():
    print("====list menu===")
    print("1. ayam bakar")
    print("2. mie ayam")
    print("3. ayam pop")

#sistem memilih
def pilih():
    isi = input("menu nomor berapa?: ")
    
    if isi == "3":
        with open("struk-pembeli.txt", "a") as file:
            file.write(isi + /n)


while True:
    menu()
    pilih()

    fungsiSelesai = input(" ")
    if fungsiSelesai == "selesai":
        break
