
# Methode, die für eine gegebene Query das Vorkommen im Datensatz zählt
def count_input_in_dataframe(query, dataframe, lower_case=True):

    # Initialisiere Zählvariablen:
    # message_counter zählt in wie vielen Nachrichten die Query vorkommt,
    # occurrence_counter zählt das insgesamte Vorkommen einer Query (mehrmaliges Vorkommen in einer Nachricht möglich)
    message_counter = 0
    occurrence_counter = 0

    # Iteriere durch alle Datenpunkte im Datensatz
    for data_point in dataframe:
        
        # Greife auf den Nachrichteninhalt im Datenpunkt zu
        message = data_point['content'].lower() if lower_case else data_point['content']
        if lower_case:
            query = query.lower() 

        # Wenn die Query in der Nachricht enthalten ist:
        if query in message:
            message_counter += 1 # Erhöhe den message_counter um 1 
            occurrence_counter += message.count(query) # Erhöhe den Vorkommenscounter um die Anzahl der Vorkommen in der Nachricht

    # Gib das Ergebnis auf der Konsole aus
    print(f'Query {query} found in {message_counter} messages. Total count of occurences: {occurrence_counter}')
    return message_counter, occurrence_counter

def count_inputs_for_list(query_list, dataframe):
    message_counter = 0
    occurence_counter = 0 
    for element in query_list: 
        element_msg_counter, element_occ_counter = count_input_in_dataframe(query=element, dataframe=dataframe, lower_case=False)
        message_counter += element_msg_counter
        occurence_counter += element_occ_counter

    print(f'Query elements found in {message_counter} messages. Total count of occurences of all queries: {occurence_counter}')

