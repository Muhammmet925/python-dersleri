print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   VEKTOREL APP  \033[1;32;40m    ║")
print("║                     ║")
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-çarpma           ║")
print("║  4-bölme            ║")
print("║  5-ortalama         ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")

# 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
secim=int(input("Seçiminiz: "))
sayı1=int( input('birinci sayı gir: '))
sayı2=int( input('ikinci sayı gir: '))      

if secim==1:        
    print('sonuç',sayı1+sayı2)
elif secim==2:
    print('sonuç',sayı1-sayı2)
elif secim==3:
    print('sonuç',sayı1*sayı2)
elif secim==4:
    print('sonuç',sayı1/sayı2)
elif secim==5:  
    print('sonuç',(sayı1+sayı2)/2)
else:
    print("Geçersiz işlem seçtiniz.")                                                       
input()
sayı1=int( input('birinci sayı gir'))
sayı2=int( input('ikinci sayı gir'))                                                                                                                                            
print('sonuç',sayı1+sayı2)
input()