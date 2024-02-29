class ExamException(Exception):
    pass
class CSVTimeSeriesFile:
    def __init__(self, name):

        # Setto il nome del file
        self.name = name

    def get_data(self):

        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r') #funzione open() apre il file e 'r' sta letteralmente per reading (lettura)
            my_file.readline() #readline mi permette di leggere la prima riga del file (fino a \n)(per capire se il file è leggibile)
        except:
            self.can_read = False #nel caso in cui il file non sia leggibile can_Read diventa false (servirà per dopo)


        if not self.can_read: #mi controlla se can_read è di tipo True o False (in questo caso, usando not, controlla se can_read è False)

            # Se ho settato can_read a False vuol dire che
            # il file non poteva essere aperto o era illeggibile
            raise ExamException('Errore, file non aperto, illeggibile o non trovato')


        else:
            #Se entra nell'else significa che il file è aperto ed è leggibile
            # Inizializzo una lista vuota per salvare tutti i dati
            data = []
            #Inizializzo una variabile che mi servirà per controllare
            #che le date siano ordinate
            prev_date = None

            # Apro il file in lettura
            my_file = open(self.name, 'r')

            # Leggo il file linea per linea
            for line in my_file:

                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')

                #Sfrutto questo ciclo for per strippare tutti i campi di ogni riga
                #lo uso per pulire righe del tipo ['1949-01 ', ' 123']
                #che possiedono dati validi, ma a causa dello spazio in più,
                #non passano per il filtro
                for i in range(len(elements)):
                    elements[i] = elements[i].strip()


                # Controllo che ci siano almeno due campi e prendo quelli con data e valore (nel caso ci sia solo un campo, ignoro la riga)
                #Controllo che il formato della riga rispetti il formato della data
                #con 7 cifre (YYYY-MM, non considero altri formati, e do per scontato che l'anno sia sopra il 1000)
                #e al 5 carattere (6 posizione) ci sia "-", inoltre
                #controllo che il valore al secondo campo ci siano delle cifre
                #aggiungo anche il controllo al fatto che i primi quattro valori debbano essere dei numeri, e il sesto e il settimo pure
                #inserisco un ulteriore controllo per prendere solo date che hanno dei mesi esistenti
                if len(elements) >= 2 and \
                len(elements[0]) == 7 and \
                elements[0][4] == "-" and \
                elements[0][:4].isdigit() and \
                elements[0][5:7].isdigit() and \
                elements[1].isdigit() and \
                int(elements[1]) >= 0 and \
                (elements[0][5:7]<="12" and elements[0][5:7]>="01"):
                    if prev_date is None or elements[0] > prev_date:
                        data.append([elements[0], int(elements[1])]) #rendo elements degli interi e non stringe di valori numerici
                        prev_date = elements[0]
                            #se la data è uguale a prev_date (la prima volta sarà sempre impossibile dato che prev_date è none)
                            #ma nel caso, so che prev_date è sempre la data precedente e quindi se fosse uguale alla data attuale (elements[0])
                            #so che esiste una data doppia e alzo un eccezione
                    elif elements[0] == prev_date:
                        raise ExamException('Presenza di date doppie')
                    else:
                            #il controllo iniziale era elements[0]>prev_date
                            #il secondo =, il terzo else entra in gioco solamente
                            #quando la data attuale (elements[0]) è minore della precedente,
                            #in questo caso so che sto controllando delle date non ordinate
                            #e quindi alzo un eccezione
                        raise ExamException('Date non ordinate')
                else:
                    pass






            # Chiudo il file
            my_file.close()

            # Quando ho processato tutte le righe, ritorno i dati
            return data

def find_min_max(time_series):
    result_dict = {}  # Creo il dizionario che conterrà tutti i dati

    dictionary_all = {} #Creo un dizionario contenente tutti i valori, mi servirà per facilitare il controllo del max e min
                        #avrei potuto usare anche una lista? no perché senno sarebbe stato piu complesso controllare tutto
                        #per singolo anno, col dizionario chiamo l'anno interessato come chiave

    for data, valore in time_series:
        anno = data.split('-')[0] #sto prendendo la prima riga e la divido fino a "-", dopo di che, da questa divisione
                                  #prendo solamente il primo valore (che sarebbe l'anno)
        #posso farlo perché do per scontato che il formato delle date sia YYYY-MM
        if anno not in dictionary_all:
            dictionary_all[anno] = [] #controllo se un anno è già utilizzato come chiave del dizionario,
                                      #in caso contrario creo un nuovo elemento che ha come chiave l'anno

        dictionary_all[anno].append(valore) #con append() inserisco in coda il valore

    for row in time_series:

        date_value = row[0].split('-')  #Divido la data in [anno, mese]
        year, month, value = date_value[0], date_value[1], row[1]


        # Inizializza il dizionario per l'anno se non esiste già
        if year not in result_dict:
            result_dict[year] = {"min": [], "max": []}

        # Aggiungo i valori minimo e massimo, sfrutto dictionary_all per trovare il max o il min
        # dell'anno in questione, se value è uguale al min o max, allora inserisce il valore min
        #o max del caso
        if value == min(dictionary_all[year]):
            result_dict[year]["min"].append(month)

        if value == max(dictionary_all[year]):
            result_dict[year]["max"].append(month)

    return result_dict
