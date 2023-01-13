n=int(input("Entrer le nombre d'etudiants"))
notes=[]
som=0
for i in range (n):
    note=int(input("Entrer un la note de l'ètudiant"))
    notes.append(note)
    som+=note
    while note < 0 or note > 20 :
     note=int(input("Entrer une note valide"))
for i in range(n):
 print("Note etudiant {} : {}" .format(i, notes[i]))

moy= som/n
print("la moyenne de la classe est {}" .format(moy))
ecarts=[]
print("numero de l'etudiant  | note | ecart à la moyenne ")
for note in notes :
    ecart=note-moy
    ecarts.append(ecart)
for i in range (n):
    print("{} | {} | {} ".format(i, notes[i], ecarts[i]))

