import math
def cauta_container(containere, numar_identificare):
    n=len(containere)
    cont =1
    salt = int(math.sqrt(n))
    st=1
    if(numar_identificare<containere[0] or numar_identificare>containere[n-1]):
        print(f"Containerul cu numărul {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {cont}.")
        return 0
    for i in range(0,n,salt):
        if containere[i] < numar_identificare:
            st=i
            cont+=1
        elif containere[i] == numar_identificare:
            print(f"Containerul cu numărul {numar_identificare} a fost găsit pe pozitia {i} după {cont} pași.")
            return 1
        else:
            break
    for i in range(st,st+salt):
        cont+=1
        if(containere[i]==numar_identificare):
            print(f"Containerul cu numărul {numar_identificare} a fost găsit pe pozitia {i} după {cont} pași.")
            return 1
    print(f"Containerul cu numărul {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {cont}.")


cauta_container([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)
cauta_container([1050, 1075, 1100, 1125, 1150, 1175, 1200], 1300)
cauta_container([1005, 1010, 1015, 1020, 1025], 1005)

cauta_container(range(0, 150000, 5), 10120)
cauta_container(range(0,150000,3), 10121)