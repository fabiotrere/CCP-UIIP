import pymysql
db = pymysql.connect(host="localhost",                    # your host, usually localhost
                     user="root",                         # your username
                     db="gestione_contatori")             # name of the data base
cur = db.cursor()


cur.execute('INSERT INTO bolletta(Id_bolletta, id_lettura, data_emissione, data_scadenza, totale_consumato, imponibile_IVA, tipologia_contratto, importo_totale, indirizzo_fatturazione_banca, pagata, mora) VALUES (001, 001, "2020-01-04", "2020-01-28", 2700, "150.45",  "azienda", "150.45", "Via Verdi 5", "SI", "NO"),(002, 002, "2020-02-04", "2020-02-28", 2500, "130.45", "privato", "159.15", "NULL", "SI", "NO"),(003, 003, "2020-03-04", "2020-03-28", 1500, "90.45", "azienda", "90.45", "Via Rossi 5", "SI", "NO"),(004, 004, "2020-04-04", "2020-04-28", 2300, "142.45", "privato", "173.79", "Via Sparano 5", "SI", "NO"),(005, 005, "2020-05-04", "2020-06-28", 2500, "130.70", "azienda", "130.70", "Via Capri 7", "SI", "NO"),(006, 006, "2020-06-04", "2020-07-28", 2300, "142.45", "privato", "173.79", "NULL", "NO", "SI"),(007, 001, "2020-07-04", "2020-08-28", 1750, "100.90", "azienda", "100.90", "Via Liguria 43", "SI", "NO"),(008, 008, "2020-08-04", "2020-08-28", 1800, "128.28", "privato", "128.28", "Via Leonida 5", "NO", "SI"),(009, 009, "2020-09-04", "2020-09-28", 2000, "115.45", "azienda", "115.45", "Via Rossi 5", "SI", "NO"),(010, 010, "2020-10-04", "2020-10-28", 1500, "120.45", "privato", "146.95", "NULL", "NO", "SI")')
cur.execute("SELECT * FROM bolletta")
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