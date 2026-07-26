# **Projet de Thèse : Conception et Évaluation d’un Écosystème d’IA Co-adaptatif pour l’Inclusion Pédagogique Active**

Candidat : Steeve PYTEL  
Statut : Professeur Certifié (PRCE), IUT Le Havre \- Département TC  
Laboratoire d'accueil envisagé : LITIS (Laboratoire d'Informatique, du Traitement de l'Information et des Systèmes), UR 4108  
Directeur de thèse pressenti : Professeur Laurent Heutte

### 

**Projet de Thèse : Conception et Évaluation d’un Écosystème d’IA Co-adaptatif pour l’Inclusion Pédagogique Active	1**

1\. Contexte, Problématique et Positionnement Scientifique	2

2\. Axes de Recherche et Méthodologie	4

3\. Originalité et Contributions Attendues	6

### 

### **1\. Contexte, Problématique et Positionnement Scientifique**

**1.1. Contexte : De l'Inclusion Passive à l'Empowerment Actif**

Le paradigme de l'inclusion scolaire évolue. La simple mise à disposition de ressources adaptées (inclusion passive) montre ses limites. L'enjeu contemporain est de créer un environnement où chaque acteur – élève à besoins éducatifs particuliers (EBEP), Accompagnant d'Élèves en Situation de Handicap (AESH), et enseignant – devient un agent actif de la réussite éducative. Cette thèse postule que l'Intelligence Artificielle, conçue non comme un substitut mais comme un **partenaire co-adaptatif**, peut être le catalyseur de cette transformation.

Le projet s'étend également à une problématique souvent négligée : celle des **enseignants eux-mêmes en situation de handicap**. Comment peuvent-ils préparer et manipuler des supports de cours qui ne leur sont pas nativement accessibles ? Le système envisagé se doit donc de répondre à une double exigence d'accessibilité : en aval pour l'élève, et en amont pour l'enseignant.

**1.2. Problématique Centrale**

Comment concevoir, développer et évaluer un **écosystème socio-technique** fondé sur l'IA, capable de fluidifier la collaboration et de renforcer les compétences du triptyque **élève-AESH-enseignant** en automatisant l'adaptation de contenus pédagogiques, tout en créant une boucle de rétroaction humaine qui améliore continuellement le système et les pratiques ?

**1.3. Positionnement Scientifique et Verrous à Lever**

Ce projet se situe à la confluence de trois domaines, en s'adossant solidement à l'expertise du LITIS :

* **Document Intelligence & IA pour l'Éducation (AIEd) :** Le socle technique repose sur l'expertise historique du LITIS (travaux de L. Heutte, T. Paquet) en analyse de documents.  
  * **Verrou scientifique n°1 (Analyse Sémantique Profonde) :** Aller au-delà de l'OCR et de la segmentation de page. Il s'agit de modéliser l'**intention pédagogique** d'un document (e.g., "ceci est un exercice de définition", "ceci est un exemple illustratif") à partir de sa structure et de son contenu, afin de proposer des adaptations pertinentes.  
* **Interaction Homme-Machine (IHM) & IA Explicable (XAI) :** L'outil doit être plus qu'un simple outil ; il doit être un médiateur.  
  * **Verrou scientifique n°2 (Médiation et Confiance) :** Comment concevoir des interfaces qui ne se contentent pas d'appliquer une adaptation, mais qui **expliquent** le "pourquoi" de la suggestion ("Ce passage a été simplifié car il contient 3 propositions subordonnées complexes") et permettent au couple AESH/enseignant d'ajuster, de valider ou d'infirmer la proposition, générant ainsi des données de haute qualité pour le réentraînement du système ?  
* **Apprentissage par Renforcement avec Rétroaction Humaine (RLHF) en Contexte Pédagogique :** C'est le cœur de l'originalité du projet.  
  * **Verrou scientifique n°3 (Apprentissage Collaboratif) :** Comment formaliser les interactions du trio (élève, AESH, enseignant) avec le système pour qu'elles constituent un signal de récompense pertinent et efficace ? Il s'agit d'appliquer les principes du RLHF, non pas pour aligner un grand modèle de langue, mais pour **aligner un système d'assistance sur les objectifs pédagogiques réels d'une situation de classe**.

### 

### **2\. Axes de Recherche et Méthodologie**

La thèse est structurée en trois axes progressifs et interdépendants.

**Axe 1 : Immersion, Co-conception et Modélisation des Besoins (Année 1\)**

* **Objectif :** Dépasser la simple analyse de besoins pour engager les futurs utilisateurs dans une démarche de co-conception. Modéliser finement les interactions et les points de friction actuels dans la chaîne de l'adaptation pédagogique.  
* **Méthodologie :**  
  1. **Recherche Ethnographique :** Observations participantes en classe (grâce au statut de PRCE) pour cartographier les flux de travail réels, les "bricolages" et les stratégies palliatives des AESH et des enseignants.  
  2. **Entretiens Semi-directifs :** Avec les trois profils d'utilisateurs (incluant des enseignants en situation de handicap) pour identifier les leviers et freins à l'adoption d'un outil d'IA.  
  3. **Ateliers de Co-conception :** Utilisation de techniques de Design Thinking (maquettage papier, scénarios d'usage) pour définir les fonctionnalités clés et les principes d'interaction du système.  
* **Livrable :** Un cahier des charges fonctionnel et ergonomique détaillé, et un modèle formel des interactions du trio.

**Axe 2 : Développement du Prototype d'Écosystème d'IA (Année 1.5 \- 2.5)**

* **Objectif :** Construire un prototype fonctionnel (Proof of Concept) intégrant les modules d'analyse, d'adaptation et de feedback.  
* **Architecture Modulaire :**  
  1. **Module d'Ingestion & d'Analyse (Socle LITIS) :** Pipeline robuste basé sur les derniers modèles de vision et de NLP (e.g., Donut, LayoutLMv3) pour extraire le contenu et sa structure sémantique pédagogique à partir de formats hétérogènes (PDF, scan, image).  
  2. **Module d'Adaptation Multi-modale :**  
     * **Texte :** Simplification (FALC), résumé, génération de questions, traduction (en s'appuyant sur des LLMs fine-tunés).  
     * **Visuel :** Description d'images (Alt-text), simplification de schémas, adaptation des couleurs.  
     * **Structure :** Reformatage pour lecteurs d'écran, réorganisation de la mise en page.  
  3. **Module de Rétroaction (Cœur de l'IHM/XAI) :** Interface web permettant à l'enseignant/AESH de visualiser les adaptations proposées, de les modifier, et de les valider en un clic. Chaque interaction est enregistrée comme une donnée d'apprentissage.  
* **Méthodologie :** Développement Agile avec des sprints et des tests utilisateurs réguliers (enseignants et AESH de l'IUT et du secondaire).

**Axe 3 : Expérimentation, Évaluation et Mesure d'Impact (Année 2.5 \- 3\)**

* **Objectif :** Évaluer l'efficacité, l'efficience et la satisfaction générées par le système en conditions réelles.  
* **Méthodologie :**  
  1. **Protocole Quasi-expérimental :** Déploiement du prototype dans plusieurs classes témoins. Comparaison d'un groupe "avec système" et d'un groupe "sans système".  
  2. **Collecte de Données Mixtes :**  
     * **Quantitatives :** Mesure du temps gagné par les AESH/enseignants, taux d'autonomie des élèves (nombre de sollicitations), performances scolaires sur les supports adaptés.  
     * **Qualitatives :** Questionnaires de satisfaction (e.g., SUS \- System Usability Scale), entretiens post-expérimentation pour évaluer la charge cognitive, le sentiment de compétence et la qualité de la collaboration au sein du trio.  
  3. **Analyse de la Boucle d'Apprentissage :** Mesure de l'amélioration des suggestions de l'IA au fil des validations humaines.  
* **Livrable :** Rapport d'évaluation d'impact, articles scientifiques et préconisations pour un déploiement à plus grande échelle.

### 

### **3\. Originalité et Contributions Attendues**

* **Contribution Scientifique :** Proposition d'un modèle d'IA co-adaptatif pour le domaine de l'éducation, avec une application originale du RLHF à la collaboration homme-machine en classe.  
* **Contribution Technologique :** Développement d'un prototype open-source qui pourra servir de base à de futurs outils pour l'Éducation Nationale.  
* **Contribution Sociale et Pédagogique :** Renforcement concret de l'inclusion scolaire en outillant et en valorisant l'expertise de chaque acteur. Amélioration des conditions de travail des AESH et des enseignants (y compris ceux en situation de handicap).

Ce projet, par son ancrage pragmatique et son ambition scientifique, vise à apporter une contribution significative et directement applicable au champ de l'IA au service d'une éducation plus juste et plus efficace.