# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

def verificare(lit,sir):
    if lit in sir:
        return True
    return False

castigator=0
print(cuvant_de_ghicit)

#////////////////////////////////////////////////////////////1
print(progres)
#////////////////////////////////////////////////////////////2
while(incercari_ramase and castigator==0):
    litera=input()

    if(litera.isalpha() and len(litera)==1):

        if(litera in litere_incercate):
                incercari_ramase = incercari_ramase - 1
                print(f"Litera este valida, dar a mai fost introdusa, mai aveti {incercari_ramase} incercari")
                continue
        litere_incercate.append(litera)
        if(verificare(litera,cuvant_de_ghicit)):
            lungime=len(cuvant_de_ghicit)
            for i in range(lungime):
                if(litera==cuvant_de_ghicit[i]):
                    progres[i]=cuvant_de_ghicit[i]
            print(*progres)
            if verificare("_",progres)==False:
                castigator=1;
        else:
            incercari_ramase=incercari_ramase-1
            print(f"Litera nu se afla in cuvant, mai aveti {incercari_ramase} incercari")

    else:
        print("Caracter invalid sau prea multe caractere")
if(castigator==1):
    print(f"Felicitări! Ai ghicit cuvântul! {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut, cuvantul era {cuvant_de_ghicit}")