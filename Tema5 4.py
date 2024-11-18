def gaseste_cnp(cnpuri, data_nașterii):
    contor=0
    for cnp in cnpuri:
        if data_nașterii in cnp:
            print(f"Primul CNP găsit pentru data de naștere {data_nașterii} este {cnp}.")
            contor+=1
            break
    if contor==0:
        print (f"Nu s-a găsit niciun CNP pentru data de naștere {data_nașterii}.")




gaseste_cnp(["1001001223456", "1980050523456", "1990050523456", "2000010123456"], "001001")
