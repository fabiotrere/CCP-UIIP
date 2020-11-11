import pymysql
import pandas as pd
import numpy as np
db = pymysql.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     db="ccp")            # name of the data base
cur = db.cursor()
def stampa_morosi_gravi():
    count = 0
    cur.execute('SELECT u.nome, u.cognome, u.id_utente, COUNT(b.pagata) as tot_non_pagate FROM (bollette b JOIN contatori c ON c.id_contatore = b.id_contatore) JOIN utenti u ON u.id_utente = c.id_utente WHERE pagata="NO" GROUP BY u.id_utente HAVING COUNT(*) > 1')
    lista_nomi_colonne = [i[0] for i in cur.description]
    for row in cur:
        for i in range(len(row)):
            count += 1
            print(lista_nomi_colonne[i], ':', str(row[i]))
        print()
    if count == 0:
        print('Nessun Guasto')
    else:
        pass
def stampa_nomi_tabelle():
    print("(banche, bollette, contatori, guasti, letture_contatori, utenti)")
def calcolo_bolletta():
    sql = ('SELECT b.id_bolletta, u.id_utente, u.tipologia_cliente, c.id_contatore, l.data_lettura as periodo_bolletta, SUM(l.fascia_energia1) as tot_fascia1, SUM(l.fascia_energia2) as tot_fascia2, SUM(l.fascia_energia3) as tot_fascia3, SUM(l.fascia_energia1 + l.fascia_energia2 + l.fascia_energia3) as tot_energia_mensile FROM ((letture_contatore l JOIN contatori c ON c.id_contatore = l.id_contatore) JOIN utenti u ON u.id_utente = c.id_utente) JOIN bollette b ON b.id_bolletta = l.id_bolletta GROUP BY b.Id_bolletta')
    global dataframe
    dataframe = pd.read_sql(sql, db)
    dataframe['aliquota_iva'] = np.where(dataframe['tipologia_cliente']!= 'azienda', "0", "0.22")
    dataframe['prezzo_unitario'] = np.where(dataframe['tot_energia_mensile'] < 1600, "0.10", "0.20")
    dataframe['importo_totale'] = ((dataframe['prezzo_unitario'].astype(float)*dataframe['tot_fascia1'].astype(float)*0.8
    + (dataframe['prezzo_unitario'].astype(float)*dataframe['tot_fascia2'].astype(float)*0.9)
    + (dataframe['prezzo_unitario'].astype(float)*dataframe['tot_fascia3'].astype(float)*1))
    * (1 + (dataframe['aliquota_iva'].astype(float))))
    print(dataframe)
    for i in range(dataframe.shape[0]):
        cur.execute('UPDATE bollette SET importo_totale =' + str(dataframe.iloc[i, dataframe.columns.get_loc('importo_totale')]) + 'WHERE id_bolletta =' + str(dataframe.iloc[i, dataframe.columns.get_loc('id_bolletta')]))
        db.commit()
def aggiornamento_morosità():
    lista_id = []
    cur.execute('SELECT u.id_utente, u.nome, u.cognome FROM (bollette b JOIN contatori c ON b.id_contatore=c.id_contatore) JOIN utenti u on c.id_utente=u.id_utente WHERE b.pagata="NO"')
    for row in cur:
        id = row[0]
        lista_id.append(id)
    lista_id = str(lista_id)
    lista_id = lista_id.replace("[", "")
    lista_id = lista_id.replace("]","")
    print(lista_id)
    cur.execute('UPDATE utenti SET moroso="SI" WHERE id_utente IN( ' + lista_id + ')')
    db.commit()
def consumo_per_data():
    giorno = input('inserisci il giorno >  ')
    mese = input ('inserisci il mese >  ')
    anno = input('inserisci l\'anno >  ')
    count = 0
    cur.execute('SELECT l.data_lettura , SUM(l.fascia_energia1) AS Consumo_F1, SUM(l.fascia_energia2) AS Consumo_F2, SUM(l.fascia_energia3) AS Consumo_F3, \
    (SUM(l.fascia_energia1) + SUM(l.fascia_energia2) + SUM(l.fascia_energia3)) AS Consumo_Totale FROM letture_contatore l \
    WHERE l.data_lettura =' + '"' + anno + '-' + mese + '-' + giorno + '"' + '\
    GROUP BY l.data_lettura ')
    lista_nomi_colonne = ['Data_lettura','Consumo_F1','Consumo_F2', 'Consumo_F3', 'Consumo_Totale']
    print(lista_nomi_colonne)
    for row in cur:
        for i in range(len(row)):
            count += 1
            print(lista_nomi_colonne[i], str(row[i]))
    if count == 0:
        print("Non ci sono rilevazioni in questa data")
    else: pass
def segnala_guasti():
    count = 0
    cur.execute('SELECT g.data_segnalazione, c.id_contatore, c.indirizzo, c.id_utente, u.nome, u.cognome, DATEDIFF(now(),g.data_segnalazione) AS giorni_durata_guasto FROM (guasti g JOIN contatori c on g.id_contatore=c.id_contatore) JOIN utenti u on c.id_utente=u.id_utente WHERE g.data_risoluzione IS NULL ORDER BY g.data_segnalazione ')
    lista_nomi_colonne = [i[0] for i in cur.description]
    new_row = []
    for row in cur:
        for i in range(len(row)):
            count += 1
            print(lista_nomi_colonne[i], ':', str(row[i]))
        print()
    if count == 0:
        print('Nessun Guasto')
    else:
        pass
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
        stampa_nomi_tabelle()
        tabella_scelta = input('> Inserisci il nome di una tabella tra quelli elencati sopra: ')
    except:
        print("Tabella non riconosciuta")
def seleziona_id():
    global id_scelto
    id_scelto =  input('Inserire id dell\'elemento > ')
def leggi_riga_tabella():
    scegli_tabella()
    seleziona_id()
    id_name = []
    cur.execute('SHOW COLUMNS FROM ' + tabella_scelta)
    for row in cur:
        id = row[0]
        id_name.append(id)
    id_name = id_name[0]
    cur.execute('SELECT * FROM ' + tabella_scelta + ' WHERE ' + id_name + '=' + id_scelto)
    for row in cur:
        row = list(row)
        for i in range(len(row)):
            row[i] = str(row[i])
    print(row)
def scrittura_bolletta():
    pass
def stampa_comandi():
    print("****************")
    print("1 Cancella utente")
    print("2 Stampa consumi per data")
    print("3 Modifica riga")
    print("4 Leggi una riga di una tabella in base all\'id dell\'elemento")
    print("5 Inserisci una nuova riga in una tabella a tua scelta")
    print("6 Segnala Guasti")
    print("7 Aggiornamento Morosità")
    print("8 Calcolo Bolletta")
    print("9 Stampa morosi gravi")
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
        consumo_per_data()
    elif comando == 3:
        modifica_riga()
    elif comando == 4:
        leggi_riga_tabella()
    elif comando == 5:
        aggiungi_osservazione()
    elif comando == 6:
        segnala_guasti()
    elif comando == 7:
        aggiornamento_morosità()
    elif comando == 8:
        calcolo_bolletta()
    elif comando == 9:
        stampa_morosi_gravi()
    elif comando == 0:
        print('Grazie per aver usato la nostra applicazione')
        break
    else:
        print("comando non riconosciuto")