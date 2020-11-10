import pymysql
db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     db="ccp")            # name of the data base
cur = db.cursor()
def rimuovi_riga():
    try:
        lista_colonne = seleziona_lista_colonne()
        id_da_eliminare = input('inserisci l\'id dell\'oggetto da eliminare: ')
        cur.execute("DELETE FROM " + tabella_scelta + " WHERE " + lista_colonne[0] + " = "+ id_da_eliminare)
        db.commit()
    except:
        db.rollback
        print ("ERRORE")
def seleziona_lista_colonne():
    scegli_tabella()
    lista_colonne = []
    cur.execute('SHOW COLUMNS FROM ' + tabella_scelta)
    for row in cur:
        name = row[0]
        lista_colonne.append(name)
    return lista_colonne
def modifica_riga():
    lista_colonne = seleziona_lista_colonne()
    print(lista_colonne)
    selezione_campo = input("inserisci il campo da modificare: ")
    selezione_nuovo_campo = input("inserisci il nuovo valore del campo: ")
    selezione_id = input("inserisci l'id della riga da modificare: ")
    cur.execute('UPDATE ' + tabella_scelta + ' SET ' + selezione_campo + ' = ' + '"' + selezione_nuovo_campo + '"' + ' WHERE ' + tabella_scelta + '.'+ lista_colonne[0] + ' = ' + selezione_id)
    db.commit()
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
def seleziona_id():
    global id_scelto
    id_scelto =  input('Inserire id dell\'elemento > ')
def leggi_tabella():
    seleziona_id()
    lista_colonne = seleziona_lista_colonne()
    cur.execute('SELECT * FROM ' + tabella_scelta + ' WHERE ' + lista_colonne[0] + '=' + id_scelto)
    for row in cur:
        print(row)
def stampa_clienti():
    pass
def stampa_comandi():
    print("****************")
    print("1 Cancella utente")
    print("2 ...")
    print("3 Modifica Riga")
    print("4 Leggi una riga di una tabella")
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
        modifica_riga()
    elif comando == 4:
        leggi_tabella()
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