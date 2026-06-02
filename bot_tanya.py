def aku():
  who = input("siapa kamu? ")
  print(f"halo {who}")
  
  kelas = int(input(f"{who} kelas berapa? "))
  if kelas < 12:
    print("semangat terus, perjalanmu masih panjang!")
  elif kelas == 12:
    print("jangan lupa persiapkan masa depan mu ya!")
  else:
    print("semoga masa depanmu indah dan bahagia!")
    
  yearsAge = int(input(f"{who} kelahiran tahun berapa? "))
  realAge = 2026 - yearsAge
  if yearsAge >= 1997 and yearsAge <= 2012 :
    print(f"wih gen z nih, berarti umurmu sekarang adalah {realAge} tahun")
  elif yearsAge > 2012:
    print(f"keren ada anak muda nih, umurmu pasti {realAge} tahun")
  else:
    print(f"ana gak tau gen apa -_- tapi pasti umurmu {realAge}")
  
  hobby = input(f"apa hobi {who}? ")
  print(f"keren punya hobi {hobby} kembangin terus ya! jangan denger kata-kata negatif orang yang penting hobimu itu positif ok")
  
  print("terimakasih atas partisipasinya, mau akhiri sesi ini?")
  
while True:
  aku()
