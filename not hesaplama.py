yazılı1=int( input('1. yazılı'))
yazılı2=int( input('2. yazılı'))
sozlu=int (input('sozlu gir'))
ortalama=(yazılı1+yazılı2+sozlu)/3
print('sonuç',ortalama)
if ortalama>90:                 
  print('süper')
elif ortalama>75:
    print('iyi')
elif ortalama>49:
    print('geçtin')
else :print('kaldın')