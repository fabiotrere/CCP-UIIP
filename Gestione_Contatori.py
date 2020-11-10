import pymysql
db = pymysql.connect(host="localhost",                    # your host, usually localhost
                     user="root",                         # your username
                     db="gestione_contatori")             # name of the data base
cur = db.cursor()



cur.execute('INSERT INTO letture_contatore(id_lettura, id_contatore, mese_lettura, fascia_energia1, fascia_energia2, fascia_energia3) VALUES (001, 001, "2020-01-01", 500, 700, 1500),(002, 002, "2020-02-01", 300, 700, 1500),(003, 003, "2020-03-01", 300, 500, 700),(004, 004, "2020-04-01", 500, 800, 1000),(005, 005, "2020-05-01", 300, 700, 1500),(006, 006, "2020-06-01", 300, 500, 1500),(007, 001, "2020-07-01", 250, 500, 1000), (008, 008, "2020-08-01", 400, 600, 800),(009, 009, "2020-09-01", 500, 600, 900),(010, 010, "2020-10-01", 300, 500, 700)')
cur.execute("SELECT * FROM letture_contatore")
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