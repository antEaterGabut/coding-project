def pembukaan():
    print("selamat datang")
    namaPembeli = input("siapa namamu? ")

    print(f"halo {namaPembeli} silahkan pilih menu")

def menu():
    print("===menu makananan resto baru===")
    
    menuResto = [
        "1. sate madura 17rb", 
        "2. nasi padang 10rb", 
        "3. nasi kebuli 26rb",
        "4. rawon sapi 25rb",
        "5. soto betawi 12rb",
    ]

    for menu in menuResto:
        print(menu)

    pilihMenu = int(input("pilih menu (1/2/3/4/5): "))
    totalPorsi = int(input("berapa porsi: "))

    if pilihMenu == 1:

        totalBayar = 17 * totalPorsi
        print(f"bayar {totalBayar}.000")

    elif pilihMenu == 2:

        totalBayar = 10 * totalPorsi
        print(f"bayar {totalBayar}.000")

    elif pilihMenu == 3:

        totalBayar = 26 * totalPorsi
        print(f"bayar {totalBayar}.000")

    elif pilihMenu == 4:

        totalBayar = 25 * totalPorsi
        print(f"bayar {totalBayar}.000")

    elif pilihMenu == 5:

        totalBayar = 12 * totalPorsi
        print(f"bayar {totalBayar}.000")

    else:

        print("harap isi dengan benar")
        return

def penutup():
    print("apakah pesanan telah diambil?")
    pilihan = input("y/n ")

    if pilihan == "y":
        print("terimakasih")
        return
    else:
        print("mohon tunggu")

while True:
    pembukaan()
    menu()
    penutup()

    
