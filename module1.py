def Sorteerimine(inimesed:list,palgad:list):
    v=int(input("palk 1-kahaneb, 2-kasvab?"))
    if v==1:
        n=len(palgad)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if palgad[j] < palgad[k]:
                    abi=palgad[j]
                    palgad[j]=palgad[k]
                    palgad[k]=abi
                    abi=inimesed[j]
                    inimesed[j]=inimesed[k]
                    inimesed[k]=abi
    elif v==2:
         n=len(palgad)
         for j in range(0,n-1):
             for k in range(j+1,n):
                 if palgad[j] > palgad[k]:
                     abi=palgad[j]
                     palgad[j]=palgad[k]
                     palgad[k]=abi
                     abi=inimesed[j]
                     inimesed[j]=inimesed[k]
                     inimesed[k]=abi










def Kustutamine(inimesed:list,palk:list):
    """Kirjendus..
    :parem list inimesed, list palk: Inimesed ja palk järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in inimesed:
        n=inimesed.count(nimi)
        for j in range(n):
            ind=inimesed.index(nimi)
            inimesed.pop(ind)
            palk.pop(ind)








def kop(inim:list, p:str)->str:
    """
    Määrme kop
    :parem logt list, p str:Järjend kop...
    :rtype: str
    """
    n=int(input("Kui palju inimesi: "))
    for i in range(n):
        print()
        log=input("Sisesta nimi: ")
        print()
        j=int(input("Sisesta palk: "))
        inim.append(log)
        p.append(j)
     
    return inim,p











def palg(palgad:list ,inimesed:list):
    """
    Määrme palg 
    :parem palgad, inimesed ,p_min ,tehe ,:Järjend palg 
    :rtype: str
    """
    palga=min(palgad)
    index=palgad.index(palga)
    pp=inimesed[index]
    return palga, pp
        



def spalg(palgad:list ,inimesed:list):
    """
    Määrme palg
    :parem palgad, inimesed ,p_min ,tehe ,:Järjend palg 
    :rtype: str
    """
    palga=max(palgad)
    index=palgad.index(palga)
    pp=inimesed[index]
    return palga, pp
