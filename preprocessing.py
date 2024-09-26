# Imports: XML parsing library, evtl. Pandas oder so
import xml.etree.ElementTree as ET
import os

# Lade alle Daten 
def load_all_SMS_from_corpus(path_to_dir):

    # Lade die XML-Datei
    tree = ET.parse(path_to_dir)
    root = tree.getroot()

    # Informationen extrahieren
    messages = []

    for text in root.findall('text'):
        # Jede Nachricht hat eine ID, Autor, Datum und Uhrzeit Attribut
        message_id = text.get('id')
        author = text.get('author')
        date = text.get('date')
        time = text.get('time')

        # Tatsächlichen Text extrahieren (nur linke Spalte)
        content = []
        full_text = text.text  # Gesamter Text im <text>-Element
        
        if full_text:
            # Text zeilenweise splitten
            lines = full_text.strip().split('\n')
            for line in lines:
                if line.split() != []:
                    word = line.split()[0]  # Nimmt nur das erste Element (das Wort)
                    content.append(word)

        # Füge die Nachricht und ihren Text als String hinzu
        messages.append({
            'id': message_id,
            'author': author,
            'date': date,
            'time': time,
            'content': ' '.join(content)  # Verbindet alle Wörter zu einem String
        })
    
    return messages

def get_dataframe(directory):
    df = []
    for output in os.listdir(directory):
        batch_list = load_all_SMS_from_corpus(directory + output)
        for datapoint in batch_list:
            df.append(datapoint)
    return df
