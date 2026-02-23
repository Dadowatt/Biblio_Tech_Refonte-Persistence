## Système de gestion de médiathèque – Python (POO)
## 1. Présentation du projet
Ce projet a pour objectif de concevoir une application console de gestion de médiathèque en Python, en s’appuyant sur les principes fondamentaux de la programmation orientée objet. Il vise à fournir une solution modulaire, robuste et évolutive permettant la gestion de différents types de documents au sein d’un catalogue unique.
Initialement limitée à la gestion des livres, l’application a été repensée afin de permettre l’intégration de nouveaux supports, tels que les magazines, sans nécessiter de modifications du gestionnaire principal. Cette approche garantit une meilleure maintenabilité du code et une extensibilité à long terme.

## 2. Objectifs et enjeux
L’objectif principal du projet est de mettre en œuvre une architecture orientée objet basée sur l’abstraction et le polymorphisme. Chaque type de document doit respecter une interface commune tout en implémentant ses propres règles métier.
Un enjeu majeur du projet réside également dans la protection des données sensibles, notamment l’état de disponibilité des documents, afin d’éviter toute modification directe et non contrôlée.

## 3. Architecture et conception

L’architecture repose sur une classe abstraite Document, définie à l’aide du module abc, qui impose une structure commune à l’ensemble des supports. Les classes concrètes Livre et Magazine héritent de cette classe et implémentent les comportements spécifiques liés à l’emprunt et au retour.
Le gestionnaire Bibliothecaire agit comme un point central de coordination. Il manipule les documents de manière polymorphe, sans dépendre de leur type concret, ce qui garantit une faible dépendance entre les composants et une meilleure évolutivité du système.
L’encapsulation est utilisée pour masquer l’état interne des objets et s’assurer que toute modification de l’état de disponibilité passe exclusivement par des méthodes dédiées.

## 4. Fonctionnalités principales

L’application permet la gestion complète d’un catalogue de documents, incluant l’ajout de nouveaux supports et l’inscription de membres. Elle offre également des fonctionnalités d’emprunt et de retour, avec une recherche des documents effectuée exclusivement par leur titre.
Les règles métier sont strictement appliquées et toute tentative d’emprunt d’un document indisponible ou de manipulation invalide génère une erreur explicite.

## 5. Sécurité et intégrité des données

La protection des données sensibles constitue un axe central du projet. L’état de disponibilité des documents est encapsulé et inaccessible en modification directe depuis l’extérieur de l’objet. Cette approche garantit l’intégrité des données et empêche toute altération non conforme aux règles métier définies.

## 6. Extensibilité et maintenabilité

L’architecture adoptée permet l’ajout de nouveaux types de documents sans remise en cause du code existant. L’introduction d’un nouveau support se limite à la création d’une nouvelle classe héritant de la classe abstraite Document, respectant ainsi le principe ouvert/fermé (Open/Closed Principle).

## 7. Environnement technique

Langage : Python 3
Paradigme : Programmation orientée objet
Modules utilisés : abc
Interface : Application console avec menu interactif (match/case)

## 8. Exécution du projet

Le projet est fourni sous la forme d’un script Python unique. Il peut être exécuté directement depuis un terminal disposant de Python 3. L’ensemble des interactions avec l’utilisateur se fait via un menu textuel intuitif.

## 9. Contexte pédagogique

Ce projet a été réalisé dans un cadre pédagogique, en travail collaboratif, avec pour objectif de consolider les notions d’abstraction, d’encapsulation, de polymorphisme et de gestion des exceptions. Il respecte les standards de nommage et les bonnes pratiques de développement en Python.
