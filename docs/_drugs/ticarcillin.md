---
layout: default
title: Ticarcillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ticarcillin : nouvelle indication prédite, Maladie du péritoine (la première prédiction du classement est le myo… (niveau de preuve L5). Indication d'origine : Infections bactériennes (infection urin…"
---

# Ticarcillin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Ticarcilline : Des Infections Bactériennes à la Maladie du Péritoine

## Résumé en Une Phrase

La ticarcilline est un antibiotique de la famille des bêta-lactamines (pénicillines), initialement utilisé pour traiter les infections urinaires, les pneumonies bactériennes et les infections à staphylocoque ou à *Escherichia coli*.
Le modèle TxGNN la prédit comme potentiellement efficace pour la **maladie du péritoine**, mais seule la littérature, ancienne et peu concluante, soutient cette direction : **aucun essai clinique** n'est enregistré et **20 publications** ont été identifiées, dont seule une minorité concerne directement la ticarcilline dans les péritonites et les infections intra-abdominales.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (infection urinaire, pneumonie bactérienne, infection à staphylocoque, etc.). Le texte d'indication des AMM n'est pas renseigné ; l'information provient de la base de connaissances du modèle |
| Nouvelle Indication Prédite | Maladie du péritoine (la première prédiction du classement est le myofibroblastome palissadique ganglionnaire, sans aucune preuve ; voir ci-dessous) |
| Score de Prédiction TxGNN | 99,81 % (maladie du péritoine) ; 99,82 % pour la première prédiction du classement |
| Niveau de Preuve | L3 (maladie du péritoine) ; L5 pour les autres prédictions |
| Statut de Marché en France | Uniquement annulé (AMM abrogées) |
| Nombre d'AMM | 2 (0 valide, 2 annulées) |
| Décision Recommandée | Hold (maintenir en attente) ; piste de recherche pour la maladie du péritoine |

**Remarque sur le choix de la prédiction :** les neuf premières prédictions (myofibroblastome palissadique ganglionnaire, lymphangiome kystique abdominal, syndrome de compression du tronc cœliaque, grossesse ectopique abdominale, chordome sacré, maladie du rétropéritoine, maladie de l'urètre, maladie du ligament large de l'utérus) ne disposent d'aucune preuve clinique ni bibliographique et n'ont pas de lien mécanistique plausible avec un antibiotique. La seule prédiction étayée par de la littérature est la **maladie du péritoine** (rang 9), qui fait l'objet de l'analyse détaillée ci-dessous.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la ticarcilline est une pénicilline à large spectre (carboxypénicilline), généralement associée à l'acide clavulanique (inhibiteur de bêta-lactamases). Les bêta-lactamines inhibent la synthèse de la paroi bactérienne. Son efficacité dans les infections à bactéries à Gram négatif, dont *E. coli*, est établie.

La relation avec la nouvelle indication est de nature **infectieuse** et non pas un véritable changement de mécanisme. Les péritonites et les infections intra-abdominales sont causées principalement par des entérobactéries (*E. coli*) et des anaérobies (*Bacteroides*), que l'association ticarcilline/clavulanate couvre. La prédiction reflète donc probablement la proximité de cette indication avec des infections déjà connues (infections pelviennes, salpingite, etc.) plutôt qu'un signal nouveau.

À noter : ce rationnel est une extension de l'usage antibactérien existant. Les recommandations modernes privilégient d'autres agents, et l'association n'est plus commercialisée en France.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Les publications les plus pertinentes sont listées ci-dessous (le niveau de preuve est établi à partir des titres et résumés ; les textes complets n'ont pas été examinés).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2691475](https://pubmed.ncbi.nlm.nih.gov/2691475/) | 1989 | Étude clinique prospective | J Antimicrob Chemother | 50 patients avec péritonite secondaire traités par ticarcilline/clavulanate 5,2 g trois fois par jour |
| [3302345](https://pubmed.ncbi.nlm.nih.gov/3302345/) | 1987 | Étude clinique | Jpn J Antibiot | BRL 28500 (ticarcilline/acide clavulanique) dans 76 cas d'infections intrapéritonéales et biliaires |
| [3499526](https://pubmed.ncbi.nlm.nih.gov/3499526/) | 1987 | Étude clinique | Jpn J Antibiot | Pelvipéritonite et abcès de Douglas : 18 patients évaluables |
| [2024225](https://pubmed.ncbi.nlm.nih.gov/2024225/) | 1991 | Expérience clinique | Surg Gynecol Obstet | Ticarcilline/acide clavulanique dans le sepsis intra-abdominal du sujet âgé, alternative aux schémas avec aminosides néphrotoxiques |
| [9451930](https://pubmed.ncbi.nlm.nih.gov/9451930/) | 1998 | Revue | World J Surg | Antibiothérapie des infections abdominales |
| [1734854](https://pubmed.ncbi.nlm.nih.gov/1734854/) | 1992 | Recommandations | Arch Surg | Recommandations de la Surgical Infection Society sur les anti-infectieux dans les infections intra-abdominales |
| [367159](https://pubmed.ncbi.nlm.nih.gov/367159/) | 1978 | Série de cas | Am J Med Sci | Carbénicilline/ticarcilline dans des infections à anaérobies : 11 patients guéris |
| [3536827](https://pubmed.ncbi.nlm.nih.gov/3536827/) | 1986 | Étude in vitro | J Antibiot | Activité de l'association contre des souches résistantes à la ticarcilline |
| [3112102](https://pubmed.ncbi.nlm.nih.gov/3112102/) | 1987 | Étude animale | J Antimicrob Chemother | Péritonite à *Pseudomonas* chez des rats neutropéniques traités par amikacine, ceftazidime et ticarcilline |
| [28849402](https://pubmed.ncbi.nlm.nih.gov/28849402/) | 2018 | Revue | Clin Pharmacokinet | Pharmacocinétique/pharmacodynamie de la témocilline (dérivé de la ticarcilline, autre médicament) |

Aucun essai randomisé n'figure parmi ces publications. Il s'agit surtout d'études anciennes, de petite taille et non randomisées.

---

## Informations de Marché en France

Les deux AMM sont annulées. Le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67951898 | CLAVENTIN 3 g/200 mg | Poudre pour solution injectable (I.V.) | Annulée |
| 67557120 | CLAVENTIN 5 g/200 mg | Poudre pour solution injectable (I.V.) | Annulée |

Titulaire : Laboratoires Delbert.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, mononucléose infectieuse, syndrome d'infection chronique par le virus d'Epstein-Barr.
- **Interactions médicamenteuses** : 23 interactions recensées. Principales :
  - **Aminosides** (amikacine, gentamicine, kanamycine, streptomycine) : niveau modéré
  - **Tétracyclines** (doxycycline, tétracycline, minocycline, déméclocycline, oxytétracycline) : niveau modéré
  - **Anticoagulants** (warfarine, dicoumarol) : niveau modéré ; héparine : mineur
  - Chloramphénicol, éthinylestradiol, acide picosulfurique, iodures I-123 et I-131 : niveau modéré
  - Clarithromycine, érythromycine : niveau mineur

Les mises en garde et contre-indications issues de la notice n'ont pas pu être récupérées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la maladie du péritoine correspond à une extension de l'usage antibactérien existant (péritonite et infections intra-abdominales) et non à un repositionnement nouveau. Les preuves se limitent à des études anciennes (1978-1991) non randomisées, sans essai enregistré.
- Le produit n'est plus commercialisé en France (AMM annulées) et les données de sécurité de la notice sont manquantes, ce qui bloque l'évaluation de sécurité. Les autres prédictions du classement n'ont aucune preuve (niveau L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Examiner les textes complets des études sur la péritonite et comparer avec les antibiotiques actuellement recommandés
- Vérifier la pertinence d'un développement pour un produit dont l'AMM est annulée, y compris la disponibilité d'une formulation
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

