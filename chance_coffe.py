while True:
  print("====pilihan kopi====")
  print("1. Americano: code(amr)")
  print("2. Tubruk: code(tbr)")
  print("3. Espreso: code(esp)")
  
  jenisKopi = input("Kode Kopi: ")
  
  amr = 20
  tbr = 35
  esp = 45
  
  if jenisKopi == "x":
     break
  
  jumlahPesanan = int(input("pesan berapa?: "))
  
  if jenisKopi == "amr":
   print("total bayar americano", amr * jumlahPesanan, "rb")
  elif jenisKopi == "tbr":
    print("total bayar tubruk", tbr * jumlahPesanan, "rb")
  elif jenisKopi == "esp":
    print("total bayar espreso", esp * jumlahPesanan, "rb")
