meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
ceafa=papanasi=guias=0
ceafaTotal=papanasiTotal=guiasTotal=0
totalpret=0
pretmic=[]

#///////////////////////////////////////////// 1
while studenti:
    student=studenti.pop(0)
    comanda=comenzi.pop(0)
    tavi.pop()
    istoric_comenzi.append(comanda)
    print(f"{student} a comandat {comanda}")

# for val in istoric_comenzi:
#     print(val)
#///////////////////////////////////////////// 2
for mancare in istoric_comenzi:
    if ("ceafa" in mancare):
        ceafa+=1
    if ("papanasi" in mancare):
        papanasi += 1
    if ("guias" in mancare):
        guias += 1
print(f"S-au comandat {ceafa} ceafa, {papanasi} papanasi, {guias} guias")
print(f"Mai sunt {len(tavi)} tavi")
for mancare in meniu:
    if ("ceafa" in mancare):ceafaTotal+=1
    if ("papanasi" in mancare):papanasiTotal+=1
    if ("guias" in mancare):guiasTotal+=1
print(f"Mai este ceafa: {not(ceafaTotal==ceafa)}")
print(f"Mai este papanasi: {not(papanasiTotal==papanasi)}")
print(f"Mai este guias: {not(guiasTotal==guias)}")
#///////////////////////////////////////////// 3
for val in istoric_comenzi:
    if val==preturi[0][0]:
        totalpret+=preturi[0][1]
    if val==preturi[1][0]:
        totalpret+=preturi[1][1]
    if val==preturi[2][0]:
        totalpret+=preturi[2][1]
print(f"Cantina a incasat: {totalpret}")

for pret in preturi:
    if(pret[:][1]<=7):pretmic.append(pret)
print(f"Produse care costă cel mult 7 lei:{pretmic}")


