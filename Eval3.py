tab = []
note,nbrNote,sommeNote,moyenne = 0 ,0 ,0 ,0
while note>=0 and note<=20:
    note=float(input("Saisir la note "+str(int(nbrNote+1))+" : "))
    if note>=0 and note<=20:
        nbrNote+=1
        sommeNote+=note
        tab.append(note)
print("Nombre des notes saisie est:",nbrNote)
for j in tab:
    print('%0.2f' % j,end=' ')
print()
moyenne = (sommeNote/nbrNote)
print("Moyenne des notes saisies est:",'%0.2f' %moyenne)

li=[note]
max=li[0]
for i in range(0,len(li))
    if li[i]>max
        max=li[i]
print("Notes la plus haute:"max)

li=[note]
min=li[0]
for i in range(0,len(li))
    if li[i]=min
        min=li[i]
print("Notes la plus haute:"min)