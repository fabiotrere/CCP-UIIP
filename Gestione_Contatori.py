import pymysql
db = pymysql.connect(host="localhost",                    # your host, usually localhost
                     user="root",                         # your username
                     db="gestione_contatori")             # name of the data base
cur = db.cursor()

cur.execute('INSERT INTO contatori(id_contatore, id_utente, indirizzo, tecnico_assegnato, data_attivazione) VALUES (001, "001", "Via XVIII agosto n° 12", "010", "2015/05/21"), (002, "002", "Via Parigi n°1", "011", "2017/10/15"), (003, "003", "Via Cavour n° 22", "020", "2018/07/20"), (004, "004", "Via Mazzini n° 30", "015", "2018/04/02"), (005, "005", "Via Marconi n° 16", "012", "2019/03/18"), (006, "006", "Via Vespucci n° 30", "022", "2019/05/19"), (008, "008", "Via Venezia n° 5", "025", "2019/06/20"), (009, "009", "Via Dante n° 11", "020", "2019/07/16"), (010, "010", "Via Crispi 31", "025", "2019/10/01")')
cur.execute("SELECT * FROM contatori")
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