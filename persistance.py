from database import get_connection
from membre import Membre
from livre import Livre
from magazine import Magazine

def charger_documents():
    catalogue = []
    conn = get_connection()
    curseur = conn.cursor(dictionary=True)
    curseur.execute("SELECT * FROM documents")
    for row in curseur.fetchall():
        if row['type_doc'] == 'livre':
            doc = Livre(row['titre'], row['auteur'], id=row['id'])
        else:
            doc = Magazine(row['titre'], row['numero'], id=row['id'])
        if not row['disponible']:
            doc.emprunter()
        catalogue.append(doc)
    curseur.close()
    conn.close()
    return catalogue

def sauvegarder_document(document):
    conn = get_connection()
    curseur = conn.cursor()
    if isinstance(document, Livre):
        curseur.execute(
            "INSERT INTO documents (titre, type_doc, auteur, numero, disponible) VALUES (%s, %s, %s, %s, %s)",
            (document.titre, "livre", document.auteur, None, int(document.disponible)))
    elif isinstance(document, Magazine):
        curseur.execute(
            "INSERT INTO documents (titre, type_doc, auteur, numero, disponible) VALUES (%s, %s, %s, %s, %s)",
            (document.titre, "magazine", None, document.numero, int(document.disponible)))
    conn.commit()
    document.id = curseur.lastrowid
    curseur.close()
    conn.close()

def charger_membres():
    membres = []
    conn = get_connection()
    curseur = conn.cursor(dictionary=True)
    curseur.execute("SELECT * FROM membres")
    for row in curseur.fetchall():
        membres.append(Membre(row['nom'], id=row['id']))
    curseur.close()
    conn.close()
    return membres

def sauvegarder_membre(membre):
    conn = get_connection()
    curseur = conn.cursor()
    curseur.execute("INSERT INTO membres (nom) VALUES (%s)", (membre.nom,))
    conn.commit()
    membre.id = curseur.lastrowid
    curseur.close()
    conn.close()

def charger_emprunts(membres, catalogue):
    conn = get_connection()
    curseur = conn.cursor(dictionary=True)
    curseur.execute("SELECT e.membre_id, e.document_id FROM emprunts e")
    for row in curseur.fetchall():
        membre = next((m for m in membres if m.id == row['membre_id']), None)
        document = next((d for d in catalogue if d.id == row['document_id']), None)
        if membre and document and document not in membre.liste_emprunts:
            membre.liste_emprunts.append(document)
    curseur.close()
    conn.close()

def sauvegarder_emprunt(membre, document):
    conn = get_connection()
    curseur = conn.cursor()
    curseur.execute(
        "INSERT INTO emprunts (membre_id, document_id) VALUES (%s, %s)", (membre.id, document.id))
    curseur.execute("UPDATE documents SET disponible = 0 WHERE id = %s", (document.id,))
    conn.commit()
    curseur.close()
    conn.close()

def supprimer_emprunt(membre, document):
    conn = get_connection()
    curseur = conn.cursor()
    curseur.execute(
        "DELETE FROM emprunts WHERE membre_id = %s AND document_id = %s", (membre.id, document.id))
    curseur.execute("UPDATE documents SET disponible = 1 WHERE id = %s", (document.id,))
    conn.commit()
    curseur.close()
    conn.close()