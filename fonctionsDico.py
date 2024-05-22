
def fabriqueDicoSet(fichier):
    with open(fichier) as f:
        mots = set(f.read().splitlines())
    return mots

def preffixeDico(mot, fichier):
    for i in range(1, len(mot)):
        if mot[:i] in fichier:
            return True
    return False


if __name__=="__main__":
    dico = fabriqueDicoSet("dicoFR.txt")
    dico2 = preffixeDico("poids,",dico)
    print(dico2)





