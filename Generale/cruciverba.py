import os
import tkinter 
from tkinter import messagebox

#Postilla nonostante il cruciverba sia un gioco nozionistico e non algoritmico con questo script che in passato 
#l'avevo creato come risoluture dell'impiccato (togliendo una parte del codice che nel caso del cruciverba risultare inutile) si può applicare tale algoritmo pure qui 
#molto probabilmente per renderlo più adatto potrei cercare di dare per ogni parola un gruppo di apparteneza così da fare scremature ancora più ideali 
#ma questo risulterebbe troppo oneroso
#database https://github.com/napolux/paroleitaliane

def Percent(lista,posizione):
    lettere=[]
    out=""
    for x in lista:
        for i,s in enumerate(x):
            if i == posizione:
                lettere.append(s)
                break
    
    totale=len(lettere)
    while len(lettere)!=0:
        lettera=lettere[0]
        tot_lettera=lettere.count(lettera)
        lettere=list(filter(lambda a: a != lettera, lettere))
        out+="la lettera " + lettera + " è presemte per il ben " +str(tot_lettera) + " su " + str(totale)+"\n"

    return out
        



def Impiccato():
    replace=lambda repleace: mistery.pop(Pattern_found-1) and mistery.insert(Pattern_found-1, inserisci_lettera) #replace letter

    print("premi ctrl+c in qualsiasi momento per uscire")
    #liste
    lenna=[]
    mistery=[]
    database=None

    while True:
        database=input("inserisci il nome del file ").replace("\\","\\\\")
        if os.path.exists(database) is False:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("errore","file non trovato")
            root.destroy()
        else:
            break



    while True:
        try:
            lunghezza=int(input("inserisci la lunghezza "))
            if lunghezza>1:
                break
        except ValueError:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("errore","non è un intero")
            root.destroy()




    a_file = open(database)
    lines = a_file.readlines()
    print("welcome to Hagman resolutor \n\nscan " +str(len(lines))+" words")
    for line in lines:
        line=line.strip("\n")
        if len(line) == lunghezza:
            lenna.append(line)

    print("trovate " +str(len(lenna)) + " con la stessa lunhezza")

    for x in range(lunghezza):
        mistery.append("_") #gui per vedere le lettere


    

    while len(lenna)!=1 and len(lenna)!=0:
        elimina=[]
        while True:
            print("la tua parola:  ",mistery)
            try:
                check2="consenti"
                check=False
                inserisci = [int(x) for x in input("inserisci la posizione se vuoi inserire più lettere uguali dividi i numeri con uno spazio\n, 0 per vedere le parole, -2 percentuali delle lettere in una posizione  ").split()]
                for x in range(0,len(inserisci)):
                    if (int(inserisci[x])>lunghezza) or inserisci[x]<=0 or inserisci is None:
                        if inserisci[0] == 0:
                            print(lenna)
                            check=False
                            check2="negato"
                            break
                        
                        if inserisci[0]==-2:
                            try:
                                while True:
                                    posizione=int(input("dammi la posizione "))
                                    if posizione<=lunghezza:
                                        break
                            except:
                                pass

                            print(Percent(lenna,posizione-1))
                            check=False
                            check2="negato"
                            
                        else:
                            root = tkinter.Tk()
                            root.withdraw()
                            messagebox.showwarning("info","numero eliminato")
                            root.destroy()
                            check=False
                            check2="negato"
                            break
                    else:
                        check=True
                if check is True and check2 == "consenti":
                    break
            except ValueError:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("errore","inserito una stringa")
                root.destroy()
                

        
        inserisci_lettera=input("letter ")

        for x in lenna:
            for i in inserisci:
                if x[i-1]!=inserisci_lettera:
                    elimina.append(x)
                    
        elimina=list(dict.fromkeys(elimina))

        
        for x in elimina:
            lenna.remove(x)
            
        for Pattern_found in inserisci:
            replace(mistery)
                
        if len(lenna)<15 and len(lenna)!=0:print("\npossible word "+str(lenna))
        print("still remain " + str(len(lenna)) + " word")
        
    if len(lenna)==0:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showwarning("errore","parola non trovata del database")
        root.destroy()
    else:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("trovata","la parola è " + str(lenna[0]))
        root.destroy()


while True:
    try:
        Impiccato()
    except KeyboardInterrupt:
        pass
    x=input("digita esci per smettere di usare il programma ")
    if x=="esci":
        exit()
    os.system("cls")
