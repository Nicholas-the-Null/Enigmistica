from collections import namedtuple
from itertools import product
import re
import os

Direction = namedtuple('Direction', 'di dj name')

DIRECTIONS = [
    Direction(-1, -1, "up and to the left"),
    Direction(-1,  0, "up"),
    Direction(-1, +1, "up and to the right"),
    Direction( 0, -1, "left"),
    Direction( 0, +1, "right"),
    Direction(+1, -1, "down and to the left"),
    Direction(+1,  0, "down"),
    Direction(+1, +1, "down and to the right"),
]

def leggi_griglia(filename):
    """
   Leggi le parole.
    """
    with open(filename) as f:
        return [re.findall('[A-Z]', line.upper()) for line in f]

def extract(grid, i, j, dir, length):
    """
    estrai le lettere della matrice
    """
    if ( 0 <= i + (length - 1) * dir.di < len(grid) and
         0 <= j + (length - 1) * dir.dj < len(grid[i]) ):
        return ''.join(
            grid[i + n * dir.di][j + n * dir.dj] for n in range(length))
    return None

def search(grid, word):
    """
    Cerca le parole nelle specifiche direzioni
    """
    word_len = len(word)
    for i, j, dir in product(range(len(grid)), range(len(grid[0])), DIRECTIONS):
        if word == extract(grid, i, j, dir, word_len):
            return i, j, dir
    return None

def main(filename, word):
    grid = leggi_griglia(filename)
    match = search(grid, word.upper())
    if match is None:
        print("non è stato possibile trovare la parola "+str(word)+"\n")
    else:
        i, j, dir = match
        print("alla linea {0}, nella colonna {1} nella direzione {2} per {3}".format(
                i + 1, j + 1, dir.name, word)+"\n")

if __name__ == '__main__':
    while True:
        try:
            scelta=int(input("""benvenuto nella scelta del menu\n1-creare un file con le parole da trovare\n2-creare un file con le lettere dello schema
3-trova una parola\n4-trova file\n5-esci\n"""))
            
            if scelta<0 or scelta>6:
                print("comando non trovato")

            elif scelta==5:
                input("premi un qualunque pulsante per uscire")
                break

            elif scelta==4:
                while True:
                    file=input("inserire nome del file con le lettere (senza estensione) ")
                    file+=".txt"
                    if os.path.exists(file) is True:
                        print("ok file valido")
                        break
                while True:
                    file_parole=input("inserire nome del file con le parole (senza estensione) ")
                    file_parole+=".txt"
                    if os.path.exists(file_parole) is True:
                        print("ok file valido")
                        break
                apri=open(file_parole,"r")
                lista_parole=apri.readlines()
                apri.close()
                for x in lista_parole:
                    main(file,x.strip())

                input("premi un pulsante per pulire lo schermo")
                os.system("cls")

            elif scelta==3:
                while True:
                    file=input("inserire nome del file con le lettere (senza estensione) ")
                    file+=".txt"
                    if os.path.exists(file) is True:
                        print("ok file valido")
                        break
                parola=input("dammi la parola ")
                main(file,parola)
                input("premi un pulsante per pulire lo schermo")
                os.system("cls")

            elif scelta==2:
                print("inseire le lettere separate da ',' per dividerle e metti . per andare a capo\n")
                nome=input("nome del file (senza estensione) ")
                x=input("inserire ").replace(","," ").replace(".","\n").upper()
                scrivi=open(nome+".txt","w+")
                scrivi.write(x)
                scrivi.close()
                print("fatto")
                input("premi un pulsante per pulire lo schermo")
                os.system("cls")

            elif scelta==1:
                nome=input("nome del file (senza estensione) ")
                x=input("parole separate da una virgola ").replace(",","\n").upper()
                scrivi=open(nome+".txt","w+")
                scrivi.write(x)
                scrivi.close()
                input("premi un pulsante per pulire lo schermo")
                os.system("cls")
                input("premi un pulsante per pulire lo schermo")
                os.system("cls")

        except Exception:
            print("errore")

