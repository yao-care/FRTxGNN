---
layout: default
title: Ceftolozane
parent: Prédiction du modèle uniquement (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftolozane : nouvelle indication prédite, Urétrite à Ureaplasma (niveau de preuve L5). Indication d'origine : Infection des voies urinaires"
monitor_inn: "ceftolozane"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Ceftolozane : De l'infection urinaire à l'urétrite à Ureaplasma
{: .text-alpha }

## Résumé en Une Phrase

Ceftolozane est une céphalosporine injectable, initialement utilisée pour le traitement des infections urinaires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**urétrite à Ureaplasma**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction. Cette prédiction est très probablement un artefact du modèle (voir ci-dessous).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection des voies urinaires (selon les indications issues du graphe de connaissances ; le texte de l'AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Urétrite à Ureaplasma |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, ceftolozane est une céphalosporine bêta-lactamine qui agit en inhibant les protéines de liaison à la pénicilline (PLP) et donc la synthèse de la paroi bactérienne. Elle est optimisée pour *Pseudomonas aeruginosa* et les entérobactéries à Gram négatif.

**Cette prédiction n'est pas biologiquement plausible.** Les *Ureaplasma* n'ont pas de paroi cellulaire : les bêta-lactamines sont donc intrinsèquement inefficaces contre elles. Le score élevé s'explique vraisemblablement par la proximité dans le graphe de connaissances entre l'urétrite et l'infection des voies urinaires, sans lien pharmacologique réel.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65166404 | ZERBAXA 1 g/0,5 g, poudre pour solution à diluer pour perfusion (MSD, Pays-Bas) | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 11 interactions de niveau modéré ont été identifiées, notamment avec :
  - les aminoglycosides (kanamycine, néomycine, streptomycine, amikacine, amikacine liposomale, gentamicine) ;
  - les anticoagulants (warfarine, dicoumarol) ;
  - le chloramphénicol ;
  - l'éthinylestradiol ;
  - l'acide mycophénolique.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Elle est contredite par la biologie : les *Ureaplasma* n'ont pas de paroi et sont insensibles aux bêta-lactamines. L'AMM française est en outre annulée.

**Pour avancer, les éléments suivants seraient nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et sur les mises en garde et contre-indications (notice ANSM), actuellement manquantes
- Données de sensibilité *in vitro* démontrant une activité sur *Ureaplasma* (peu probable)

**Autres prédictions du classement :**
- **Urétrite gonococcique** (99,89 %, L5, Hold) : une logique de classe existe pour certaines céphalosporines comme la ceftriaxone, mais aucune donnée ne soutient ceftolozane, et des alternatives efficaces sont établies.
- **Maladie inflammatoire de l'utérus** (99,88 %, L5, Hold) : lien indirect plausible mais non étayé, car l'activité anaérobie de ceftolozane est limitée.
- **Pyélonéphrite xanthogranulomateuse** (99,88 %, L4, question de recherche) : seul lien indirect plausible, via l'indication d'infection urinaire compliquée, mais la seule publication disponible est une revue générale sur les infections urinaires fébriles (PMID [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/), 2016), sans donnée spécifique à ce médicament.
- Les six autres prédictions (syndrome d'hyperviscosité polyclonale, hyperamylasémie, tuberculose urogénitale, analbuminémie congénitale, incompatibilité de groupe sanguin, maladie hématologique prémaligne) sont considérées comme des artefacts du graphe, sans mécanisme plausible (L5, Hold).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

