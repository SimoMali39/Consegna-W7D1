def lunghezze_parole():
    # Chiedi all'utente di inserire le parole separate da spazi
    input_utente = input("Inserisci parole separate da spazi: ")
    # Dividi la stringa di input in una lista di parole
    lista_parole = input_utente.split()
    # Calcola le lunghezze delle parole
    lista_lunghezze = [len(parola) for parola in lista_parole]
    return lista_lunghezze

# Esempio di utilizzo:
B = lunghezze_parole()
print(B)