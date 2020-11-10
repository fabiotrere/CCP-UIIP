import pymysql
db = pymysql.connect(host="localhost",                    # your host, usually localhost
                     user="root",                         # your username
                     db="gestione_contatori")             # name of the data base
cur = db.cursor()

cur.execute('INSERT INTO guasto(id_Contatore, data_segnalazione, tecnico_assegnato, data_primo_intervento, data_risoluzione) VALUES (001, "2020/05/20", "Rossi Alberto", "2020/05/22", "2020/05/23"),(002, "2020/07/11", "Ferrari Giuseppe", "2020/07/15", "2020/07/16"),(003, "2020/07/15", "Laurino Aldo", "2020/07/20", "2020/07/20"),(004, "2020/08/27", "Verdi Filippo", "2020/09/01", "2020/09/02"),(005, "2020/09/14", "Gallo Angelo", "2020/09/17", "2020/09/18"),(006, "2020/09/17", "Russo Roberto", "2020/09/20", "2020/09/20"),(007, "2020/10/05", "Costa Mattia", "2020/10/10", "2020/10/10"),(008, "2020/10/20", "De Luca Stefano", "2020/10/17", "2020/10/18"),(009, "2020/10/20", "Romano Luca", "2020/10/21", "2020/10/21"),(010, "2020/11/03", "Fontana Enrico", "2020/11/06", "2020/11/07")')
cur.execute("SELECT * FROM guasto")
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