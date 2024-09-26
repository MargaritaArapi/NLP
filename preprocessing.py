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
        # Jede Nachricht hat einen ID, Autor, Datum und Uhrzeit Attribut
        message_id = text.get('id')
        author = text.get('author')
        date = text.get('date')
        time = text.get('time')

    # Textinhalte innerhalb der Nachricht
    content = []
    for element in text:
        word = element.text
        pos_tag = element.get('POS')
        lemma = element.get('LEMMA')
        content.append((word, pos_tag, lemma))
    
    # Füge die Nachricht und ihre Details zur Liste hinzu
    messages.append({
        'id': message_id,
        'content': content
    })
    
    return messages

def get_dataframe(directory):
    df = []
    for output in os.listdir(directory):
        datapoints = load_all_SMS_from_corpus(directory + output)
        df.append(datapoints)
    return

current_dir = os.getcwd()
path_to_whatsapp = current_dir + '/corpora/whatsapp/'
print(path_to_whatsapp)
df = get_dataframe(path_to_whatsapp)
