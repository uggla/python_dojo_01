# Backlog – User Stories Coding Dojo Pokémon

## User Story #1 – Acquisition de Pokémon avec points et API mockée (TDD)

### En tant que joueur

Je veux pouvoir utiliser mes 3 points pour obtenir des Pokémon tirés aléatoirement via une API REST,
afin de constituer mon équipe et bénéficier de jets de dés selon les points non utilisés.

#### Règles du jeu

- Le joueur commence avec **3 points**
- Chaque Pokémon coûte **1 point**
- Pour chaque point utilisé :
  - Un Pokémon est tiré au hasard depuis une liste obtenue via une API REST
  - Ses caractéristiques sont récupérées via une seconde requête API
  - Le Pokémon est ajouté à la collection du joueur
- Chaque point non utilisé donne droit à **un jet de dé**

#### Objectifs pédagogiques

- TDD sur la gestion de points, de collection
- Mock d’une API REST
- Transformation JSON → Objet métier
- Introduction d’un `Enum` pour le type de Pokémon

## User Story #2 – Affichage de la collection de Pokémon du joueur (vers l’inversion de dépendance)

### En tant que joueur

Je veux pouvoir afficher ma collection de Pokémon sous différentes formes (texte, HTML, Markdown),
afin de mieux visualiser mon équipe.

#### Règles

- Affichage d’abord en texte simple
- Puis en HTML et Markdown
- Chaque renderer respecte une interface commune

#### Objectifs pédagogiques

- Introduire la séparation présentation / données
- Implémenter plusieurs rendus d’un même objet
- Refactor vers l’inversion de dépendance
  - Injection d’un renderer
  - Interface `CardRenderer`

## User Story #3 – Faire évoluer un Pokémon en échange d’un point (avec appel API REST)

### En tant que joueur

Je veux pouvoir utiliser 1 point pour faire évoluer un Pokémon que je possède déjà,
afin de le rendre plus puissant via ses nouvelles caractéristiques.

#### Règles

- Coût de l’évolution : **1 point**
- L’évolution est déterminée via l’API REST :
  - Espèce → Chaîne d’évolution → Stade suivant
  - Nouveau Pokémon récupéré via l’API
  - Le Pokémon dans la collection est mis à jour ou remplacé

#### Objectifs pédagogiques

- Naviguer dans des ressources liées d’une API
- Réutiliser le parseur de Pokémon
- Mock d’appels REST multiples
- Mutation ou remplacement d’un objet métier existant

## User Story #4 – Combat entre deux joueurs avec score basé sur un dé et une caractéristique

### En tant que joueur

Je veux pouvoir faire combattre un de mes Pokémon contre celui d’un autre joueur,
afin de déterminer un vainqueur avec un système de score.

#### Règles

- Chaque joueur choisit un Pokémon
- Score = caractéristique \* dé (valeur aléatoire entre 1 et 6)
- Le joueur avec le plus gros score gagne
- Chaque point restant permet **une relance de dé**
  - On conserve le **meilleur score**

#### Objectifs pédagogiques

- Calculs aléatoires (mock de `random`)
- Comparaison d’objets / résultats
- Stratégie avec les points restants
- Implémentation d’un processus de combat
