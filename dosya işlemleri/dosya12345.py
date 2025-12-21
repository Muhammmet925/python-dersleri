import os
import sys

# Bazı sistemlerde OpenCV yüklü olmayabilir, hata almamak için kontrol ekleyelim
try:
    import cv2
except ImportError:
    cv2 = None

# --- Sınıf Tanımlama ---
class Ogrenci:
    def __init__(self, adi, numara):
        self.ad = adi
        self.nu = numara  # Girinti hatası düzeltildi

# --- Fonksiyonlar ---

def rehber_kayit():
    print("\n--- KAYIT EKRANI ---")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    nu = input("Okul No: ")
    tel = input("Telefon: ")

    # 'a' modu: Ekleme yapar. Encoding utf8 Türkçe karakterler için önemlidir.
    with open("rehber.dat", "a", encoding="utf8") as dosya:
        dosya.write(f"{ad} {soyad}#{nu}#{tel}\n")
    print("Kayıt başarıyla eklendi.")

def rehber_listele():
    print("\n--- KAYIT LİSTESİ ---")
    print(f"{'Ad Soyad':<20} | {'No':<10} | {'Telefon':<15}")
    print("-" * 50)
    
    if not os.path.exists("rehber.dat"):
        print("Henüz bir kayıt bulunamadı.")
        return

    try:
        with open("rehber.dat", "r", encoding="utf8") as dosya:
            for satir in dosya:
                satir = satir.strip()
                if not satir or "#" not in satir:
                    continue
                
                veriler = satir.split("#")
                
                # Veri bütünlüğünü kontrol et (Ad-Soyad, No, Tel olmalı)
                if len(veriler) >= 3:
                    print(f"{veriler[0]:<20} | {veriler[1]:<10} | {veriler[2]:<15}")
                else:
                    print(f"Hatalı formatlı satır atlandı: {satir}")
    except Exception as hata:
        print(f"Listeleme sırasında bir hata oluştu: {hata}")

def konsol_tasarimi():
    # ANSI renk kodları: 32 Yeşil, 31 Kırmızı
    print("\033[1;32;40m")
    print("╔════════════════════════════════════╗")
    print("║\033[1;31;40m         PROGRAM BAŞLATILDI         \033[1;32;40m║")
    print("╚════════════════════════════════════╝")
    print("\033[0m")

def resim_goster(dosya_yolu):
    if cv2 is None:
        print("OpenCV kütüphanesi yüklü değil. 'pip install opencv-python' komutunu kullanın.")
        return

    try:
        img = cv2.imread(dosya_yolu)
        if img is not None:
            cv2.imshow("Resim Penceresi", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print(f"Resim dosyası bulunamadı: {dosya_yolu}")
    except Exception as e:
        print(f"Resim açılırken hata oluştu: {e}")

# --- ANA AKIŞ ---
if __name__ == "__main__":
    # Temel Değişkenler
    ad_orn = "Efekan"
    tc_orn = 20222241528
    ogrenciler_liste = ["Hüseyin", "Emre", "Bartu"]

    konsol_tasarimi()
    
    # Nesne örneği
    ogrenci1 = Ogrenci("Ahmet", 666)
    print(f"Sistem Kaydı: {ogrenci1.ad}, No: {ogrenci1.nu}")

    # Önce listele, sonra yeni kayıt al
    rehber_listele()
    
    secim = input("\nYeni kayıt eklemek ister misiniz? (e/h): ").lower()
    if secim == 'e':
        rehber_kayit()
        rehber_listele()

    # Dosya oluşturma örneği
    for i in range(3):
        with open(f"deneme{i}.txt", "w") as f:
            pass # Boş dosyalar oluşturuldu

        # resim okumak için
# pip install opencv-python
import cv2
d = cv2.imread("h5_1 dosya islemleri+proje1destek/pythonlogo.png")
print(d)
cv2.imshow("resim", d)
cv2.waitKey(0)

# ör1: klasör konumunu alma
import os # operating sistem
print("Klsör:",os.getcwd()) # current working directory/çalışılan klasör.

# klasör konumunu belirleme
import os
print(os.getcwd()) # current working directory/çalışılan klasör
yol = os.getcwd().split("\\")


print("Dosya yolu",len(yol),"parçadan oluşur.")
print("Bulunduğun sürücü:",yol[0])
print("Çalıştığın klasör:",yol[len(yol)-1])
print("Bir öncek klsör  :",yol[len(yol)-2])


print("Birleşik hali    :",'\\'.join(yol[0:len(yol)-1])) # birleştir

# mevcut konumdaki dosya/dizin listesini alma
import os
# print(os.listdir())
liste = os.listdir()
print(*liste,sep="\n")

# mevcut konumdaki dosya/dizin listesini alma
import os
liste = os.listdir()


for a in liste:
    print("dosya" if os.path.isfile(a) else "klasör",end="")
    print("\t",a)


dosyaSayisi = 0
for a in liste:
    if os.path.isfile(a): dosyaSayisi +=1


print(len(os.listdir()),"adet dosya ve klasör var.")
print(dosyaSayisi,"adet dosya,",len(os.listdir())-dosyaSayisi,"adet klasör var.")
