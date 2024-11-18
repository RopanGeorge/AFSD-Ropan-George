def cauta_document(lista_documente, document):
    numar_iteratii = 0
    lungime=len(lista_documente)
    for i in range(lungime):
        numar_iteratii += 1
        if(lista_documente[i]==document):
            print(f"Documentul cu numărul de referință {document} a fost găsit pe poziția {numar_iteratii-1} după {numar_iteratii} documente verificate.")
            return 1
    print(f"Documentul cu numărul de referință {document} nu a fost găsit în dosar. Total documente verificate: {numar_iteratii}.")




cauta_document([101, 202, 303, 404, 505, 606, 707, 808, 909], 404)
