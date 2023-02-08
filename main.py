def funkcija(sk1,sk2,sk3):
  sar1 = [sk1,sk2,sk3]
  return max(sar1)
sk1 = int(input("Ievadi 1.sk:"))
sk2 = int(input("Ievadi 2.sk:"))
sk3 = int(input("Ievadi 3.sk:"))
print("Lielakais skaitlis = ", funkcija(sk1,sk2,sk3))