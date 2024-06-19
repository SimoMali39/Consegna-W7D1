import random
import string

def genera_password(complessa=False):
    if complessa:
        lunghezza = 20
        caratteri = string.ascii_letters + string.digits + string.punctuation
    else:
        lunghezza = 8
        caratteri = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password

# Input dell'utente per la scelta del tipo di password
while True:
    scelta = input("Vuoi una password semplice (digita 's') o complessa (digita 'c')? ").lower()
    if scelta == 's':
        password = genera_password(complessa=False)
        break
    elif scelta == 'c':
        password = genera_password(complessa=True)
        break
    else:
        print("Scelta non valida. Per favore, digita 's' per una password semplice o 'c' per una password complessa.")

print(f"La tua password generata è: {password}")