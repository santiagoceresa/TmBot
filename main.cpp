#include <iostream>
#include <cctype>
#include <algorithm>
#include <string>
#include <list>
#include <map>

using namespace std;

list<pair<string, int>> coinquilini;
const string admin = "SANTIAGO";
map<string, map<string, int>> DICT = {
    {"PULITO", {
        {"CUCINA", 2},
        {"TAVOLO", 1},
        {"QUADRI", 1}
    }},
    {"ASPIRATO", {
        {"ENTRATA", 2},
        {"SALA", 2}
    }},
    {"SVUOTATO", {
        {"CESTINI", 1},
        {"LAVASTOVIGLIE", 1}
    }}
};

void aggiungi_coinquilino() {
    string nome;
    string scelta;
    string cognome;
    cout << "Inserisci il nome del nuovo coinquilino da inserire " << endl;
    cin >> nome;
    bool trovato = false;

    // Scorro la lista dei coinquilini
    for (const auto& coinquilino : coinquilini) {
        if (nome == coinquilino.first) trovato = true;
    }

    if (trovato) {
        cout << "Questo nome è già presente, inserire un altro " << nome << "?" << endl;
        cin >> scelta;
        if (scelta == "SI") {
            cout << "Allora inserire anche il cognome" << endl;
            cin >> cognome;
        } else return;

        nome = nome + " " + cognome; // Combinazione nome e cognome
    }
    coinquilini.push_back(make_pair(nome, 0)); // Inserisco il nome nella lista
}

enum Settings {
    RESET_SCORES,
    STAMPA_COINQUILINI,
    AGGIUNGI_COINQUILINO
};

void reset_scores() {
    // Logica per resettare i punteggi
}

void stampa_coinquilini() {
    for (const auto& coinquilino : coinquilini) {
        cout << coinquilino.first << endl;
    }
}

void eseguiSettings(enum Settings setting) {
    switch (setting) {
        case RESET_SCORES:
            reset_scores();
            break;
        case STAMPA_COINQUILINI:
            stampa_coinquilini();
            break;
        case AGGIUNGI_COINQUILINO:
            aggiungi_coinquilino();
            break;
    }
}

int main() {
    // carica_json(); // Presupponendo che questa funzione sia definita altrove
    // if vuoto
    string nome;
    if (carica_json == false) {
        string scelta;
        cout << "La lista dei coinquilini è vuota, inserire un nome da aggiungere?" << endl;
        cin >> scelta;
        if (scelta == "SI") aggiungi_coinquilino();
    }
    if (nome == admin) {
        string scelta;
        cout << "Ciao " << admin << ", sei admin, cosa vuoi fare? settings/ aggiungi" << endl;
        cin >> scelta;
        transform(scelta.begin(), scelta.end(), scelta.begin(), ::toupper);

        Settings setting;
        if(scelta== "SETTINGS") eseguiSettings(setting);
        else if(scelta == "aggiungi")   aggiungi_coinquilino();

        cout<< "vuoi anche eseguire azioni fatte da te? "<<endl;
        cin>>scelta;

        if(scelta == "no")  return 0;
    }

    bool continua = true;
    int guadagno = 0;
    
    while (continua) {
        string sceltaI, sceltaII;
        cout << "Che azione hai eseguito tra queste? " << endl;
        for (const auto& faccenda : DICT) {
            cout << faccenda.first << endl;
        }
        cin >> sceltaI;
        
        for (const auto& sottoFaccenda : DICT[sceltaI]) {
            cout << "Quale di queste sottofaccende hai eseguito? " << endl;
            cout << sottoFaccenda.first << endl;
        }
        cin >>sceltaII;

        guadagno +=  DICT[sceltaI][sceltaII];
    }
    cout << "complimenti "<<nome<< " hai guadagnato "<<guadagno<<" punti, continua così! "<<endl;
    
        
    
    cout << "Situazione attuale: " << endl;
    for (const auto& coinquilino : coinquilini) {
        cout << coinquilino.first << " a " << coinquilino.second << " punti " << endl;
    }
    
    return 0;
}