import pymysql
db = pymysql.connect(host="localhost",                    # your host, usually localhost
                     user="root",                         # your username
                     db="gestione_contatori")             # name of the data base
cur = db.cursor()

cur.execute('INSERT INTO banche(id_banca, nome_banca, indirizzo_fatturazione) VALUES (001, "Banca di Milano", "Via Verdi 5"),(002, "Banca di Pescara", "Via Verdi 5"),(003, "Banca di Firenze", "Via Rossi 5"),(004, "Banca di Pisa", "Via del Corso 5"),(005, "Banca di Torino", "Via Roma 15"),(006, "Banca di Bari", "Via Sparano 5"), (007, "Banca di Venezia", "Via Capri 7"),(008, "Unicredit Banca", "Via Battisti 21"), (009, "Banca Intesa", "Via Liguria 43"),(010, "Banca di Bologna", "Via Leonida 5")')
cur.execute("SELECT * FROM banche")
db.commit()

cur.execute('INSERT INTO utenti(id_utente, CF, nome, cognome, indirizzo, città, CAP, tipologia_cliente, moroso) VALUES (001, "RSSMRA68S14D643C", "Mario", "Rossi", "Via Campania 9", "Taranto", "74121", "azienda", "NO"),(002, "VRDGLI68S14D643W", "Giulia", "Verdi", "Via Mirabella 33", "Foggia", "71021", "privato", "NO"),(003, "BLLLSN82A01H501P", "Alessandro", "Bellino", "Via Roma 6", "Roma", "00145", "azienda", "NO"),(004, "DPLFNC60R54D643P", "Francesco", "Depaolis", "Via Firenze 10", "Bari", "72987", "privato", "NO"),(005, "BRNCRL74A01F205Z", "Carla", "Bernabei", "Via Castelfidardo 3", "Milano", "20122", "azienda", "NO"),(006, "GRCNGL73R54D643R", "Angela", "Grieco", "Via Cesare Battisti 56", "Roma", "00145", "privato", "SI"), (007, "CNTGNI85A01F205K", "Gina", "Conte", "Via Marconi 50", "Roma", "00147", "azienda", "NO"),(008, "RSSMHL73R54D643T", "Michele", "Rossi", "Via Mazzini 4", "Torino", "10121", "privato", "SI"), (009, "MRZFLV85A01L219V", "Flavio", "Marzocca", "Via Amendola 90", "Firenze", "00354", "azienda", "NO"),(010, "CRDCLD94E45L049W", "Claudia", "Cardella", "Via Veneto 89", "Roma", "00148", "privato", "NO")')
cur.execute("SELECT * FROM utenti")
db.commit()

def rimuovi_cliente(nome_da_eliminare):
    pass
def stampa_clienti():
    pass
def nuovo_cliente():
    pass
def stampa_comandi():
    print("****************")
    print("1 Cancella utente")
    print("2 Stampa elenco clienti")
    print("3 ...")
    print("4 ...")
    print("5 Inserisci nuovo cliente")
    print("6 Modifica contatto")
    print("7 Stampa Comandi")
    print("0 Quit")
    print("*******************")
#___MAIN___
print("Benvenuto nel software di gestione contatori")
while True:
    comando = int(input("Scegli il comando da eseguire: "))
    if comando == 1:
        nome_da_eliminare = input("inserisci il nome dell'utente da eliminare: ")
        rimuovi_cliente(nome_da_eliminare)
    elif comando == 2:
        stampa_clienti()
    elif comando == 3:
        pass
    elif comando == 4:
        pass
    elif comando == 5:
        nuovo_cliente()
    elif comando == 6:
        pass
    elif comando == 7:
        stampa_comandi()
    elif comando == 0:
        print('Grazie per aver usato la nostra applicazione')
        break
    else:
        print("comando non riconosciuto")