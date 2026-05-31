print("siapa anda?")
print("pembeli/owner/pekerja")

#input data awal
who = str(input("aku adalah: "))
#logika untuk login
if who == "pembeli":
  print("apakah anda member?")
  print("ya/tidak")

  member = str(input(""))
  
  if member == "ya":
    print("silahkan pilih kopi, dan anda mendapat potongan harga")
    print("silahkan masukkan kode member")
    
    sandiMember = int(input("masukkan angka empat digit: "))
    if sandiMember == int(1425):
      print("selamat menikmati potongan harga")
    else:
      print("jangan berbohong-_-")
      
else:
  print("selamat datang")
  
#pilihan kopi untuk pembeli

