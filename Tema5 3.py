numar_iteratii = 0

def cautare_binara(arr, start, stop, val):
    global numar_iteratii
    if stop>=start:
        mid=(start+stop)//2

        if arr[mid]==val:
            return mid
        elif arr[mid]>val:
            numar_iteratii += 1
            return cautare_binara(arr, start, mid-1, val)
        else:
            numar_iteratii += 1
            return cautare_binara(arr, mid+1, stop, val)
    else:
        return -1


def cauta_pacient(pacienti, id_pacient):
    global numar_iteratii
    n=len(pacienti)
    start=0
    stop=n-1
    rezultat=cautare_binara(pacienti, start, stop, id_pacient)
    if rezultat>=0:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția {rezultat} după {numar_iteratii} pași de căutare.")
    else:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} nu a fost găsit. Total pași efectuați: {numar_iteratii}.")

    # continuati restul functiei

cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1000)
