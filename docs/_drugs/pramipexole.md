---
layout: default
title: Pramipexole
parent: Preuves modérées (L3-L4)
nav_order: 620
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Pramipexole : nouvelle indication prédite, Trouble déficit de l'attention avec hyperactivité (TDAH) (niveau de preuve L4). Indication d'origine : Syndrome des jambes sans repos"
---

# Pramipexole
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Pramipexole : De la Maladie de Parkinson au Trouble Déficit de l'Attention avec Hyperactivité (TDAH)

## Résumé en Une Phrase

Pramipexole est un agoniste dopaminergique D2/D3, initialement utilisé dans le traitement de la maladie de Parkinson et du syndrome des jambes sans repos.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble déficit de l'attention avec hyperactivité (TDAH)**, mais aucun essai clinique n'est enregistré et les **7 publications** retrouvées sont presque toutes indirectes (une seule étude de cas évoque le TDAH en comorbidité).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome des jambes sans repos ; maladie de Parkinson (les textes d'indication des AMM ne sont pas renseignés dans les données compilées) |
| Nouvelle Indication Prédite | Trouble déficit de l'attention avec hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99,998 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, le pramipexole est un agoniste dopaminergique non ergoté, à affinité préférentielle pour les récepteurs D3. Son efficacité dans la maladie de Parkinson et le syndrome des jambes sans repos repose sur la stimulation dopaminergique.

Une dérégulation dopaminergique est impliquée dans le TDAH, ce qui fournit un lien mécanistique plausible. Toutefois, ce lien reste théorique : aucun essai n'est enregistré, et la littérature retrouvée est surtout indirecte (revues sur le syndrome des jambes sans repos, essai randomisé dans le syndrome de Gilles de la Tourette, travaux sur l'hétéromérisation des récepteurs D4). Le score TxGNN très élevé est une prédiction du modèle et ne remplace pas une preuve clinique.

Les autres prédictions du modèle (rang 2 à 10) sont, pour la plupart, sans lien mécanistique identifiable ni preuve. La seule exception est la **schizophrénie** (rang 9, niveau L1, essai de phase 3 NCT01320982 et plusieurs études randomisées), qui mériterait une évaluation séparée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [22407510](https://pubmed.ncbi.nlm.nih.gov/22407510/) | 2012 | ECR (syndrome de Gilles de la Tourette, indirect pour le TDAH) | Movement Disorders | Essai multicentrique contrôlé contre placebo du pramipexole dans le syndrome de Gilles de la Tourette, trouble neurodéveloppemental apparenté ; hypothèse d'une hypersensibilité dopaminergique centrale |
| [37342213](https://pubmed.ncbi.nlm.nih.gov/37342213/) | 2023 | Cas clinique | Frontiers in Pain Research | Rémission de lombalgie chronique et de dysesthésie orale chez un patient avec TDAH comorbide, traité par atomoxétine et pramipexole |
| [19412489](https://pubmed.ncbi.nlm.nih.gov/19412489/) | 2006 | Revue | Neuropsychiatric Disease and Treatment | Utilisation du pramipexole dans le syndrome des jambes sans repos (pas de données sur le TDAH) |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revue | Revue Neurologique | Revue sur le syndrome des jambes sans repos (pas de données directes sur le TDAH) |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Étude clinique (autre médicament, pipéribédil, dans la maladie de Parkinson) | Clinical Neuropharmacology | Comparaison de la vigilance sous pipéribédil versus pramipexole et ropinirole, chez des patients parkinsoniens somnolents |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Préclinique / in vitro | Pharmacological Research | Hétéromérisation entre récepteurs α2A-adrénergiques et variants du récepteur dopaminergique D4, avec implications pour les troubles du contrôle des impulsions et le TDAH |
| [38649244](https://pubmed.ncbi.nlm.nih.gov/38649244/) | 2024 | Cas clinique | BMJ Case Reports | Hypokaliémie liée à une consommation excessive de colas ; le TDAH et le pramipexole ne figurent que dans les antécédents du patient (sans lien avec l'efficacité) |

---

## Informations de Marché en France

Les 9 AMM recensées sont toutes **annulées** ; aucune n'est actuellement valide. Les textes d'indication approuvée ne sont pas renseignés dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67527910 | SIFROL 0,26 mg | Comprimé à libération prolongée | Annulée |
| 60267171 | SIFROL 1,05 mg | Comprimé à libération prolongée | Annulée |
| 67696401 | PRAMIPEXOLE ZENTIVA 0,18 mg | Comprimé sécable | Annulée |
| 63005092 | PRAMIPEXOLE TEVA 0,18 mg | Comprimé | Annulée |
| 66881233 | SIFROL 0,7 mg | Comprimé | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, dyskinésie d'origine médicamenteuse, maladie rénale, troubles psychotiques, schizophrénie et troubles apparentés (trouble schizophréniforme, trouble schizo-affectif), troubles mentaux, mélanome, syndrome d'apnée du sommeil (obstructive ou non), syndrome d'hypoventilation centrale congénitale, narcolepsie (avec ou sans cataplexie), maladies du système nerveux central, sclérose concentrique de Balo, adrénoleucodystrophie liée à l'X.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Modérées : morphine (y compris liposomale), cimétidine, dronabinol, nabilone, métoclopramide, opium
  - Mineures : ranitidine (y compris citrate de bismuth)
  - Niveau non précisé : notamment calcitriol, pantoprazole, glimépiride, métformine, oméprazole, vancomycine

Les mises en garde et contre-indications de la notice officielle n'ont pas pu être consultées : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le TDAH, aucun essai n'est enregistré et aucune donnée d'efficacité directe n'existe ; le niveau de preuve est L4 malgré un score TxGNN très élevé. Par ailleurs, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Études précliniques ou essais pilotes directement dans le TDAH
- Évaluation séparée de la schizophrénie (niveau L1) : résultats publiés de NCT01320982 et de l'ECR PMID 35921506, avec vigilance sur le risque d'aggravation psychotique
- Clarification du statut réglementaire en France (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

