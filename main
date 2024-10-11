from enum import Enum
import json
import os

TOKEN = 'inserisco token'
ADMIN = 'SANTIAGO'
file_name = "coinquilini.json"

#gestione JSON
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


# salvo il JSON
def salva_json(data, file_name):
    data = {nome: inquilino.punti for nome, inquilino in coinquilini.items()}
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    print("Coinquilini salvati su JSON.")

def inizializza_diario(file_name):
    return carica_json(file_name)

#gestione resto
class Inquilino:
    def __init__(self, name, punti = 0):
        self.name = name
        self.punti = punti

    def __str__(self):
        return f"{self.name} ha {self.punti}"
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
    print("Situazione attuale salvata sul JSON")

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

class SottoFaccenda(Enum):
    CESTINI = ("Cestini", 1)
    LAVASTOVIGLIE = ("Lavastoviglie", 2)
    SALA = ("Sala", 4)
    ENTRATA = ("Entrata", 4)
    CUCINA = ("Cucina", 4)
    QUADRI = ("Quadri e battiscopa", 2)
    TAVOLO = ("Tavolo", 2)

    def __init__(self, descrizione, valore):
        self._descrizione = descrizione  # Uso di un nome diverso (con _)
        self._valore = valore

    @property
    def descrizione(self):
        return self._descrizione  # Ritorna l'attributo privato

    @property
    def valore(self):
        return self._valore  # Ritorna l'attributo privato

class Faccende(Enum):
    PULITO = ("Pulito", [SottoFaccenda.SALA, SottoFaccenda.ENTRATA])
    SVUOTATO = ("Svuotato", [SottoFaccenda.CESTINI, SottoFaccenda.LAVASTOVIGLIE])
    ASPIRATO = ("Aspirato", [SottoFaccenda.CUCINA, SottoFaccenda.QUADRI, SottoFaccenda.TAVOLO])

    @property
    def descrizione(self):
        return self.value[0]

    @property
    def sottofaccende(self):
        return self.value[1]

def main():
    carica_json(file_name)
    inizializza_diario(file_name)
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

    if nome == ADMIN:
        scelta = input(f"{nome} sei admin! Cosa vuoi fare? settings / aggiungi ").upper() #settings or aggiungi
        if scelta == 'SETTINGS':
            # scorro enum per quale impostazione voglio fare
            for setting in settings:
                print(f"-{setting.value}")
            azione_input = input("Scegli tra una di queste azioni").upper()
            try:
                azione = settings[azione_input]
                esegui_setting(azione)
            except KeyError:
                print("Azione non valida, riprova")
            scan = input("vuoi anche aggiungere faccende eseguite?").upper()
            if scan == "NO":
                return

    continua = True
    moltiplicatore = 1
    while continua:
        for faccenda in Faccende:
            print(f"-{faccenda.descrizione}")
        faccenda_input = input("Che faccenda di queste hai eseguito? ").upper()
        try:
            azione = Faccende[faccenda_input.upper()]
            print(f"Che cosa hai {azione.descrizione} ?")
            for sotto in azione.sottofaccende:
                print(f"-{sotto.descrizione}")
            sottofaccenda_input = input("").upper()
            if (sottofaccenda_input == "Cestini"):
                moltiplicatore = int(input("Quanti cestini hai svuotato? 1,2,3 o 4? "))
                while moltiplicatore>4 or moltiplicatore == 0:
                    moltiplicatore = int(input("Errore! puoi inserire solo numeri compresi tra 1 e 4, inseriscine un altro"))
            # aggiungo punteggio
            sottofaccenda = SottoFaccenda[sottofaccenda_input].valore
            guadagno = moltiplicatore*sottofaccenda.valore

            coinquilini[nome].aggiungi_punti(guadagno)
            moltiplicatore = 1
        except KeyError:
            print("Azione non valida")
        scan = input("Hai eseguito altre faccende?").upper()
        if(scan == "NO"):
            continua = False
    salva_json(coinquilini,file_name)

if __name__== "__main__":
    main()
