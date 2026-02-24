## Système de gestion de médiathèque – Python (POO)

## Description du projet

Application console de gestion de médiathèque en Python, utilisant les principes de la programmation orientée objet (POO).
Le projet gère différents types de documents (Livres et Magazines) et permet l’inscription de membres, l’emprunt et le retour des documents.

## Fonctionnalités principales

Ajouter un document (Livre ou Magazine) au catalogue,
Inscrire un membre à la bibliothèque,
Prêter un document à un membre (avec vérification de disponibilité),
Retourner un document emprunté,
Afficher tous les documents avec leur statut (Disponible / Emprunté),
Afficher tous les membres et les documents qu’ils ont empruntés,

## Concepts POO utilisés

    1. Abstraction : La classe Document est abstraite (ABC) et définit un contrat pour tous les documents via la méthode __str__.

    2. Encapsulation : L’état de disponibilité des documents est privé et manipulé uniquement via les méthodes emprunter et retourner.

    3. Polymorphisme : Les méthodes __str__ de Livre et Magazine sont appelées dynamiquement pour un affichage cohérent dans le catalogue ou les emprunts des membres.

    4. Héritage : Les classes Livre et Magazine héritent de Document et implémentent leurs comportements spécifiques.

## Technologies et modules

Langage : Python 3
Paradigme : Programmation orientée objet
Modules : abc pour l’abstraction
Interface : Application console avec menu interactif (match/case)

## Exécution

Lancer le fichier main.py avec Python 3
Toutes les interactions se font via le menu textuel

## Extensibilité

Nouveau type de document → créer une classe héritant de Document et implémenter __str__
Le reste du système (gestionnaire, menu) fonctionne sans modification