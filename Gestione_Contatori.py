while True:
    stampa_comandi()
    comando = int(input("Scegli il comando da eseguire: "))
    if comando == 1:
        nome_eliminare = input("inserisci il nome dell'utente da eliminare: ")
        cancella_utente(nome_eliminare)
    elif comando == 2:
        stampa_rubrica()
    elif comando == 3:
        print("Marco Verdi", rubrica['Marco Verdi'])
        print("Mario Rossi", rubrica['Mario Rossi'])
        print("Luca Bianchi", rubrica['Luca Bianchi'])


    elif comando == 4:
        print("Luca Bianchi", rubrica['Luca Bianchi'])
        print("Mario Rossi", rubrica['Mario Rossi'])
        print("Marco Verdi", rubrica['Marco Verdi'])


    elif comando == 5:
        nuovo_contatto()
    elif comando == 6:
        nome = input("inserisci nome")
        lista_dati = ottieni_lista(nome)
        print("scegliere uno dei seguenti dati da modificare:")
        print("via")
        print("CAP")
        print("citta")
        print("telefono")
        print("e_mail")
        print("campo_note")
        dato_da_modificare = input("> ")

        nuovo_dato = input("inserisci il nuovo dato")
        rubrica[nome] = modifica_dati(lista_dati, dato_da_modificare, nuovo_dato)
    elif comando == 0:
        print('Grazie per aver usato la nostra applicazione')
        break

    else:
        print("comando non riconosciuto")