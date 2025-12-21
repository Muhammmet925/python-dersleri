print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m     Kayıt Ekranı   \033[1;32;40m ║")
print("║   AD                ║")
print("║   Soyad             ║")
print("║   veli              ║")
print("║   tel               ║")
print("║   kimlik            ║")
print("║                     ║")
print("║                     ║")
print("║                     ║")
print("╚═════════════════════╝")
 # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
# dosyadan verileri okuma
dosya = open("rehber.dat") #dosya modu yazılmazsa r (read) modunda açar
print(" KAYIT LİSTESİ ")
print("===============")
okunan = dosya.read()
print(okunan)


# GÖREV:
#

# dosyadan verileri satır satır okuma
dosya = open("rehber.dat") #dosya modu yazılmazsa r (read) modunda açar
print(" KAYIT LİSTESİ ")
print("===============")
print("Adı\t\tTelefonu")
# okunan = dosya.read()
okunan = dosya.readlines()
for a in okunan:
    # satir = a.split("#")
    satir = a.strip().split("#") # strip ile alt satır karakterleri vs silinir.
    print(satir[0],"\t",satir[1])


