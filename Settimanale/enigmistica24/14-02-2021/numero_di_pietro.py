#un numero di pietro è un numero di 4 cifre tale che il prodotto delle prime due
#è uguale alla somma delle ultime 2. trovare il numero di pietro maggiore

massimo=0

for x in range(1000,9999):
    x=str(x)
    if int(x[0]) * int(x[1]) == int(x[2]) + int(x[3]):
        x=int(x)
        if x>massimo:
            massimo=x


print("il numero di pietro massimo è ",massimo)
input("premi un tasto per terminare")

