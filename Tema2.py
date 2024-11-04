articol="Ferrari f80 este o masina rosie, verde sau galbena!  "
lungime=len(articol)
jumatate=int(lungime/2)
partea1=articol[:jumatate]
partea2=articol[jumatate:]
partea1=partea1.upper()
partea1=partea1.strip()

partea2=partea2[::-1]
partea2=partea2.capitalize()
partea2=partea2.replace(",","").replace(".","").replace("?","").replace("!","")

rezultat =partea1+partea2

print(partea1)
print(partea2)
print(rezultat)

