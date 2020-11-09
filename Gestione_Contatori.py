import os
os.chdir('C:/Users/fabio/Desktop/Code contest project/')
import pymysql

db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     db="ccp")            # name of the data base
cur = db.cursor()

cur.execute('INSERT INTO banche(id_banca, nome_banca, indirizzo_fatturazione) VALUES (001, "Banca di Milano", "Via Verdi 5"),(002, "Banca di Milano", "Via Verdi 5"),(003, "Banca di Milano", "Via Verdi 5")')
cur.execute("SELECT * FROM banche")
db.commit()
for row in cur.fetchall():
    print (row)
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
while False:
    comando = int(input("Scegli il comando da eseguire: "))
    stampa_comandi()
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
    elif comando == 8:
        pass
    elif comando == 0:
        print('Grazie per aver usato la nostra applicazione')
        break
    else:
        print("comando non riconosciuto")
