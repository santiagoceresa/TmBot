from enum import Enum
import json
import os

TOKEN = ''
ADMIN = 'SANTIAGO'
file_name = "coinquilini.json"

#gestione resto
class Inquilino:
    def __init__(self, name, punti = 0):
        self.name = name
        self.punti = punti

    def __str__(self):
        return f"{self.name} a {self.punti}"

    def aggiungi_punti(self,guadagno):
        self.punti+=guadagno

# definizione dizionario
coinquilini = {}

#funzioni gestione JSON
def carica_json(file_name):
    if os.path.exists(file_name):
        with open(file_name,'r') as f:
            data = json.load(f)

            #caricamento in dizionario
            for nome, punti in data.items():
                coinquilini[nome] = Inquilino(nome, punti)
            print("Coinquilini caricati correttamente dal JSON.")
    else:
       # json vuoto
        print("File JSON non trovato, avvio con lista vuota.")
        with open(file_name,'w') as f:
            json.dump({}, f, indent=4)

def salva_json(data, file_name):
    with open(file_name, 'w') as f:
        data = {nome: inquilino.punti for nome, inquilino in coinquilini.items()}
        json.dump(data, f, indent = 4)
    print("Return positivo: Situazione attuale salvata sul JSON")

    # devo passare il nome dal main, chiedendolo a video
def aggiungi_coinquilino():
    #ciclico se si vuole aggiungerne più di uno
    nome = input("inserisci il nome del coinquilino da aggiungere").upper()
    if nome in coinquilini:
        print(f"esiste già un coinquilino chiamato {nome}")
        check = input("aggiungerne un altro?")
        if(check == "si"):
            cognome = input("inseriscine il cognome")
            nome_completo = nome + " " + cognome
            coinquilini[nome_completo] = Inquilino(nome_completo)
            print(f"Coinquilino {nome_completo} aggiunto correttamente! ")
        else:
            return
    else:
        coinquilini[nome] = Inquilino(nome)
        print(f"Coinquilino {nome} aggiunto correttamente! ")

def stampa_coinquilini():
    if not coinquilini:
        print("Nessun coinquilino presente.")
    else:
        for nome, coinquilino in coinquilini.items():
            print(coinquilino)

def print_info(self):
    print(f"Ciao {self.tipo.get_name()}! hai {self.punti} punti")

def reset_scores():
    for coinquilino in coinquilini.values():
        coinquilino.punti = 0
    print("Tutti i punteggi sono stati resettati correttamente.")

class settings(Enum):
    STAMPA_COINQUILINI = "STAMPA COINQUILINI",
    AGGIUNGI_COINQUILINI = "AGGIUNGI COINQUILINI",
    RESET_SCORES = "RESET SCORES"

actions = {
    settings.STAMPA_COINQUILINI: stampa_coinquilini,
    settings.AGGIUNGI_COINQUILINI: aggiungi_coinquilino,
    settings.RESET_SCORES: reset_scores
}

def esegui_setting(azione):
    action = actions.get(azione)
    if action:
        action()
    else:
        print("azione non valida")

DICT = {
    "PULITO":{
        "CUCINA": 2,
        "TAVOLO": 1,
        "QUADRI": 1
    },
    "ASPIRATO":{
        "ENTRATA": 2,
        "SALA": 2
    },
    "SVUOTATO":{
        "CESTINI": 1,
        "LAVASTOVIGLIE": 1
    }
}

def main():
    carica_json(file_name)
    # se parto a lista coinquilini vuota

    if not coinquilini:
        scelta = input("la lista dei coinquilina è vuota, aggiungerne uno per continuare? Si/ Esci").upper()
        if(scelta == "SI"):
            aggiungi_coinquilino()
            #deve essere admin

        if(scelta == "ESCI"):
            return

    nome = input ("Ciao! chi sei? ").upper()
    while nome not in coinquilini:
        print(f"Errore! {nome} non è presente nella lista dei coinquilini! ")
        nome = input("Inserisci il tuo nome").upper()
    scan = "SI"
    if nome == ADMIN:
        scelta = input(f"{nome} sei admin! Cosa vuoi fare? settings / aggiungi ").upper() #settings or aggiungi
        if scelta == 'SETTINGS':
            while (scan=="SI"):
                # scorro enum per quale impostazione voglio fare
                for setting in settings:
                    print(f"-{setting.value}")
                azione_input = input("Scegli tra una di queste azioni\n")
                try:
                    azione = settings[azione_input]
                    esegui_setting(azione)
                    scan = input("Vuoi eseguire altre settings? ").upper()
                except KeyError:
                    print("Azione non valida, riprova")
            scan = input(f"{ADMIN} vuoi anche aggiungere faccende eseguite?").upper()
            if scan == "NO":
                return

    continua = True
    moltiplicatore = 1
    guadagnoTot = 0
    while continua:
        for faccenda in DICT:
            print(faccenda)
        faccenda_input = input("Che faccenda di queste hai eseguito? ").upper()
        try:
            print(f"Che cosa hai {faccenda_input} ?")
            for SubAzione in DICT[faccenda_input]:
                print(f"{SubAzione}")

            sottofaccenda_input = input("").upper()
            if (sottofaccenda_input == "Cestini"):
                moltiplicatore = int(input("Quanti cestini hai svuotato? 1,2,3 o 4? "))
                while moltiplicatore>4 or moltiplicatore == 0:
                    moltiplicatore = int(input("Errore! puoi inserire solo numeri compresi tra 1 e 4, inseriscine un altro "))
            # aggiungo punteggio
            valore_sottofaccenda = DICT[faccenda_input][sottofaccenda_input]
            guadagno = moltiplicatore*valore_sottofaccenda
            guadagnoTot += guadagno

            coinquilini[nome].aggiungi_punti(guadagno)
            moltiplicatore = 1
        except KeyError:
            print("Azione non valida")

        scan = input("Hai eseguito altre faccende?").upper()
        if(scan == "NO"):
            continua = False
        print(f"Complimenti {nome}! Hai guadagnato {guadagnoTot} punti in totale ")
        print("continua così!")

    print("Situazione attuale: ")
    for nome, coinquilino in coinquilini.items():
        print(f"{coinquilino.name} a {coinquilino.punti} punti\n")
    salva_json(coinquilini,file_name)

if __name__== "__main__":
    main()
