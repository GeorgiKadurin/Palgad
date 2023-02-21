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