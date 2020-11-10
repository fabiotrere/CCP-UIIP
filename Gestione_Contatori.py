import pymysql
db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     db="ccp")            # name of the data base
cur = db.cursor()
def rimuovi_riga():
    try:
        #global lista_colonne
        scegli_tabella()
        lista_colonne = []
        print ("*1")
        cur.execute('SHOW COLUMNS FROM ' + tabella_scelta)
        for row in cur:
            name = row[0]
            lista_colonne.append(name)
        print("*2")
        id_da_eliminare = input('inserisci l\'id dell\'oggetto da eliminare: ')
        cur.execute("DELETE FROM " + tabella_scelta + " WHERE " + lista_colonne[0] + " = "+ id_da_eliminare)
        db.commit()
    except:
        db.rollback
        print ("ERRORE")
def modifica_riga():
    scegli_tabella()
    lista_colonne = []
    lista_tipo = []
    cur.execute('SHOW COLUMNS FROM ' + tabella_scelta)
    for row in cur:
        name = row[0]
        tipo_dati = row[1]
        lista_colonne.append(name)
        lista_tipo.append(tipo_dati)
    lista_valori = []

def aggiungi_osservazione():
    try:
        scegli_tabella()
        lista_colonne = []
        lista_tipo = []
        cur.execute('SHOW COLUMNS FROM ' + tabella_scelta)
        for row in cur:
            name = row[0]
            tipo_dati = row[1]
            lista_colonne.append(name)
            lista_tipo.append(tipo_dati)
        lista_valori = []
        for i in range(len(lista_colonne)):
            if lista_tipo[i] == 'datetime' or lista_tipo[i] == 'date':
                valore = input('> Inserisci il valore di ' + lista_colonne[i] + ' (le date vanno YYYY-MM-DD) ')
            else:
                valore = input('> Inserisci il valore di ' + lista_colonne[i] + ' ')
            lista_valori.append(valore)
        lista_colonne = ', '.join(lista_colonne)
        lista_valori = '", "'.join(lista_valori)
        lista_valori = '"' + lista_valori + '"'
        cur.execute('INSERT INTO ' + tabella_scelta + '(' + lista_colonne + ')' + ' VALUES ' + '(' + lista_valori + ')')
        db.commit()
    except:
        db.rollback
        print("ERRORE")
def scegli_tabella():
    try:
        global tabella_scelta
        tabella_scelta = input('> Inserisci il nome di una tabella: ')
    except:
        print("Tabella non riconosciuta")
def stampa_clienti():
    pass
def stampa_comandi():
    print("****************")
    print("1 Cancella utente")
    print("2 ...")
    print("3 ...")
    print("4 ...")
    print("5 Inserisci una nuova riga in una tabella a tua scelta")
    print("6 ...")
    print("7 ...")
    print("0 Quit")
    print("*******************")
#___MAIN___
print("Benvenuto nel software di gestione contatori")
while True:
    stampa_comandi()
    comando = int(input("Scegli il comando da eseguire: "))
    if comando == 1:
        rimuovi_riga()
    elif comando == 2:
        stampa_clienti()
    elif comando == 3:
        pass
    elif comando == 4:
        pass
    elif comando == 5:
        aggiungi_osservazione()
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