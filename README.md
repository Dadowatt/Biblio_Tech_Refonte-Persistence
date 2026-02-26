Système de gestion de médiathèque – Python (POO)
Description du projet

Application console de gestion de médiathèque en Python, utilisant les principes de la programmation orientée objet (POO).
Le projet gère différents types de documents (Livres et Magazines) et permet :

l’inscription de membres

l’emprunt et le retour des documents

Fonctionnalités principales

Ajouter un document (Livre ou Magazine) au catalogue

Inscrire un membre à la bibliothèque

Prêter un document à un membre (avec vérification de disponibilité)

Retourner un document emprunté

Afficher tous les documents avec leur statut (Disponible / Emprunté)

Afficher tous les membres et les documents qu’ils ont empruntés

Concepts POO utilisés

Abstraction : La classe Document est abstraite (ABC) et définit un contrat pour tous les documents via la méthode __str__.

Encapsulation : L’état de disponibilité des documents est privé et manipulé uniquement via les méthodes emprunter et retourner.

Polymorphisme : Les méthodes __str__ de Livre et Magazine sont appelées dynamiquement pour un affichage cohérent.

Héritage : Les classes Livre et Magazine héritent de Document et implémentent leurs comportements spécifiques.

Persistence des données

Base de données : MySQL

Les documents, membres et emprunts sont stockés dans une base MySQL.

La couche persistance (persistance.py) gère toutes les interactions avec la base.

Utilisation d’un context manager (@contextmanager) pour gérer automatiquement les connexions et curseurs, garantissant :

Ouverture et fermeture des connexions

Commit automatique des modifications

Sécurité et nettoyage même en cas d’erreur

Tables principales

documents : stocke les livres et magazines

membres : stocke les informations des membres

emprunts : relie les membres aux documents empruntés

Technologies et modules

Langage : Python 3

Paradigme : Programmation orientée objet

Modules :

abc pour l’abstraction

mysql.connector pour la base de données

dotenv pour gérer les variables d’environnement

Interface : Application console avec menu interactif (match/case)

Exécution

Lancer le fichier main.py avec Python 3

Toutes les interactions se font via le menu textuel

Extensibilité

Nouveau type de document → créer une classe héritant de Document et implémenter __str__

La couche persistance et le gestionnaire (Bibliothecaire) gèrent automatiquement le nouveau type sans modification

Notes

Les entrées utilisateur sont validées via des regex pour garantir des noms et titres corrects.

Les commits du projet utilisent un style clair, par exemple :
Refactorisation : utilisation d’un context manager pour la gestion MySQL.
