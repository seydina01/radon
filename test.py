from dicoFR import dico as dFR
from dicoAN import dico as dAN
import fonctionsDico
mc= dFR & dAN

mcSorted=sorted(mc)
if __name__=="__main__":
    france = fonctionsDico.fabriqueDicoSet("dicoFR.txt")
    angleterre = fonctionsDico.fabriqueDicoSet("dicoAN.txt")
    liste=[]
    # for mot in france:
    #     if mot.startswith('x') and mot.endswith('e'):
    #         liste.append(mot)

    liste2= [ mot for mot in france if mot.startswith('x') and mot.endswith('e')]

    nbrAng= len(angleterre)
    nbrFr= len(france)

    sommeAng=0
    for mot in angleterre:
        if not fonctionsDico.preffixeDico(mot,angleterre):
         sommeAng=sommeAng + 1

    sommeFr = 0
    for mot in france:
        if not fonctionsDico.preffixeDico(mot, france):
            sommeFr = sommeFr + 1
    print(sommeAng,sommeFr)

    angPourcentage =(sommeAng * 100)/nbrAng
    frPourcentage =(sommeFr * 100)/nbrFr

    print(f"france:{frPourcentage}%")
    print(f"angleterre:{angPourcentage}%")



