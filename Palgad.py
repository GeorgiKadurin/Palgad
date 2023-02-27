from module1 import *

#4 Kes ja kui palju saab kõige väiksemat palka.

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

spin1=Sorteerimine(inimesed,palgad)
print(palgad)
print(inimesed)




spin= Kustutamine(inimesed,palgad)
print(palgad)
print(inimesed)


while True:

     inimesed, palgad=kop(inimesed,palgad)
     print(palgad)
     print(inimesed)
     break

   
log,palk=palg(palgad, inimesed)
print(f"Väike palk saab {palk}, palk {log}")

 
log,palk=spalg(palgad, inimesed)
print(f"Suur palk saab {palk}, palk {log}")
