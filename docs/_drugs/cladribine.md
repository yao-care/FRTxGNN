---
layout: default
title: Cladribine
parent: Prédiction du modèle uniquement (L5)
nav_order: 176
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Cladribine : De la leucémie à tricholeucocytes au rhabdomyosarcome embryonnaire paraméningé

## Résumé en Une Phrase

Cladribine est un analogue nucléosidique de la purine, initialement utilisé pour traiter la leucémie à tricholeucocytes (et sa variante) ainsi que la sclérose en plaques récurrente-rémittente.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **rhabdomyosarcome embryonnaire paraméningé**, mais **aucun essai clinique** et **aucune publication pertinente** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie à tricholeucocytes, variante de la leucémie à tricholeucocytes, sclérose en plaques récurrente-rémittente (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas disponible) |
| Nouvelle Indication Prédite | Rhabdomyosarcome embryonnaire paraméningé |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, la cladribine est un analogue de la purine résistant à l'adénosine désaminase. Elle s'accumule sous forme de triphosphate dans les cellules ayant un rapport élevé désoxycytidine kinase / 5'-nucléotidase, ce qui provoque des cassures de l'ADN et l'apoptose.

Ce rapport enzymatique est caractéristique des cellules lymphoïdes, ce qui explique son efficacité dans la leucémie à tricholeucocytes et son intérêt dans la sclérose en plaques. Il n'est pas caractéristique du rhabdomyosarcome, une tumeur solide mésenchymateuse. Le lien mécanistique est donc faible et non étayé par les données récupérées.

Le score élevé du modèle reflète probablement la proximité des différents types de rhabdomyosarcome dans le graphe de connaissances (six prédictions très corrélées, qui ne sont pas des signaux indépendants) plutôt qu'une justification biologique spécifique. Avant toute considération clinique, il faudrait des données précliniques, par exemple la sensibilité de lignées cellulaires et l'expression de la désoxycytidine kinase. Les traitements standards du rhabdomyosarcome reposent sur la vincristine, l'actinomycine D et le cyclophosphamide ; aucune donnée sur la cladribine n'a été identifiée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le rhabdomyosarcome embryonnaire paraméningé.

À noter : une seule publication a été retrouvée pour une autre prédiction du même médicament (sarcome du foie, rang 7). Il s'agit d'un rapport de cas de 2004 sur la cladribine dans la mastocytose systémique indolente (PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/)). Elle ne concerne pas le sarcome hépatique et n'est pas une preuve pertinente.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 60427957 | LITAK 2 mg/ml, solution injectable | Solution injectable | Non disponible | Annulée |
| 65820786 | MAVENCLAD 10 mg, comprimé | Comprimé | Non disponible | Annulée |
| 60522572 | LEUSTATINE 1 mg/ml, solution pour perfusion | Solution pour perfusion | Non disponible | Annulée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (analogue nucléosidique de la purine) |
| Risque de Myélosuppression | Élevé : les contre-indications du graphe de connaissances incluent la neutropénie, la thrombocytopénie, l'agranulocytose et l'anémie |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec formule, fonction rénale, fonction hépatique, surveillance neurologique (neuropathie périphérique) |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications (graphe de connaissances, et non texte de la notice)** : maladie rénale, pyourétère, thrombocytopénie, neutropénie, agranulocytose, anémie, anémie macrocytaire, maladie du système nerveux périphérique, neuropathie périphérique, hyperuricémie.
- **Interactions médicamenteuses** : 100 interactions recensées, dont les principales sont de niveau majeur :
  - Corticoïdes : hydrocortisone, triamcinolone (y compris ophtalmique), dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone.
  - Radiopharmaceutiques : ibritumomab tiuxétan, iobenguane (I-131), tositumomab (avec ou sans I-131), samarium (153Sm) lexidronam, chlorure de strontium Sr-89.
  - Autres : défériprone.
  - Interactions de niveau modéré : palifermine, dipyridamole, cilostazol, eltrombopag.
  - L'interaction avec l'acide acétylsalicylique est de niveau inconnu.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente. Le lien mécanistique est faible, car la sélectivité de la cladribine pour les cellules lymphoïdes ne s'applique pas clairement à ce sarcome. Le profil de myélosuppression est lourd et aucune AMM française n'est actuellement valide.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Des données précliniques : sensibilité de lignées de rhabdomyosarcome à la cladribine et expression de la désoxycytidine kinase par rapport à la 5'-nucléotidase.
- Une revue de la littérature ciblée sur la cladribine dans les sarcomes pédiatriques, ainsi qu'une recherche d'essais enregistrés.
- Une évaluation du rapport bénéfice/risque comparée aux schémas standards (vincristine, actinomycine D, cyclophosphamide).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

