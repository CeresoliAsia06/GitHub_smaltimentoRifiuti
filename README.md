# GitHub_smaltimentoRifiuti
INFORMAZIONI SUL PROGETTO (relazione tecnica)
nome_partecipanti = Ceresoli Asia, Gonzalez Federico L., Naoni Lorenzo

# Introduzione
Creazione del progetto "SmaltimentoRifiuti" con l'aiuto della piattaforma collaborativa cloud Git-Hub con l'utilizzo del sistema di controllo Git.
Il progetto tratta dello smaltimento di rifiuti secondo la normativa del commercio e del riciclo delle apparecchiature elettriche ed elettroniche (AEE) e i relativi rifiuti (RAEE).

# Cenni Teorici
La piattaforma utilizzata denominata Git-Hub è una piattaforma cloud che semplifica il processo di collaborazione ai progetti e fornisce un sito web.
GitHub opera come il "repository remoto". L'Agenda 2030 per lo Sviluppo Sostenibile è un programma d'azione sottoscritto nel 2015 e tiene conto della sostenibilità dell'ambiente e dello smaltimento dei rifiuti. I RAEE vengono smaltiti in cinque macro-categorie:

    R1-Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, congelatori, condizionatori
    R2-Grande bianco non freddo -grandi elettrodomestici come lavatrici, lavastoviglie
    R3-TV Monitor a tubo catodico
    R4-Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici
    R5-Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte.

# Scopo
Lo scopo del progetto è quello di creare un software che permetta il corretto smaltimento dei rifiuti salvando tutti gli smaltimenti, segnandoli su un file a parte con descrizione.

# Procedimento
Ogni membro del gruppo si è suddiviso le parti essenziali del progetto, eseguendo poi delle commit da Git-Hub in modo da unire i propri rami (branch) lavorativi con un unico ramo main.
Il nostro software (basato su una programmazione in linguaggio Python) prevede la presenza di un primo menu generale che permette la chiusura del programma, la stampa a video di tutti i rifiuti smaltiti con le caratteristiche inserite e la possibilità di inserire un nuovo oggetto da smaltire.
Se si sceglie di smaltire un rifiuto, il programma permette di scegliere se si sa già in precedenza la categoria dove smaltire il rifiuto, in modo da permettere alle aziende pubbliche che si servono di aziende apposite di velocizzare il processo di smaltimento.
Se è già conosciuta la categoria o si pensa di saperla, il programma mostrerà tutte le categorie disponibili e chiederà di quale rifiuto si tratti. Il programma controllerà se effettivamente l'oggetto inserito si trova in quella categoria: se è verificato, chiederà di inserirne il peso; se il rifiuto non si trova in quella categoria, stamperà a video tutti gli oggetti di quella categoria e darà un'altra scelta all'utente (inserire nuovamente il rifiuto se effettivamente fa parte di quella categoria ma era stato scritto male in precedenza oppure la possibilità di uscire da quella categoria).
Il programma, una volta selezionato exit, cercherà di aiutare l'utente indirizzandolo lui stesso alla categoria riferita al rifiuto scelto.
Se invece si pensa di non conoscerne la categoria, il programma chiederà di inserire l'oggetto da smaltire e lo cercherà tra le varie liste di rifiuti suddivise in categorie. Se lo trova, consiglierà la categoria da scegliere; se non lo trova stamperà errore e reindirizzerà al menu principale (questo per evitare errori di battitura o inserimento di oggetti inesistenti).
Una volta conclusa una delle due possibilità (sapere dove smaltire o non sapere dove smaltire), l'utente verrà reindirizzato al menu principale. È possibile uscire dal programma selezionando l'opzione di exit.
Il tutto creando un'interfaccia grafica utilizzando la libreria tkinter

# Conclusione
In conclusione il progetto è stato svolto usando la piattaforma di Visual Studio Code con l’estensione di GitHub permettendo la collaborazione fra gli sviluppatori. 

Il progetto è stato suddiviso in due ma svolge le stesse funzioni, perché il primo progetto consiste di fare il codice su Visual Studio Code, con i comandi che venivano scritti nella CMD, e il secondo consiste di farlo con la parte grafica usando la libreria tkinter. 