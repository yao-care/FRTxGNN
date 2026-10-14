---
layout: default
title: Alitretinoin
parent: Prédiction du modèle uniquement (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitrétinoïne : De l'eczéma chronique sévère des mains à l'aménorrhée

## Résumé en Une Phrase

L'alitrétinoïne (acide 9-cis-rétinoïque) est un rétinoïde oral, connu pour le traitement de l'eczéma chronique sévère des mains résistant aux dermocorticoïdes puissants, et également utilisé dans le sarcome de Kaposi.
Le modèle TxGNN la prédit comme potentiellement efficace pour l'**aménorrhée**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM ; les données de pharmacologie mentionnent l'eczéma chronique sévère des mains et le sarcome de Kaposi |
| Nouvelle Indication Prédite | Aménorrhée |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques connues, l'alitrétinoïne est un agoniste pan-récepteur qui active les récepteurs nucléaires RAR (α, β, γ) et RXR (α, β, γ). La signalisation des rétinoïdes influence la différenciation de nombreux tissus, y compris les tissus reproducteurs.

Cependant, aucun mécanisme précis reliant l'alitrétinoïne à l'aménorrhée n'est étayé par les données. Les rétinoïdes sont tératogènes et peuvent perturber le cycle menstruel : un rôle thérapeutique est donc peu plausible. Le score très élevé de TxGNN (0,9999) reflète une association calculée dans le graphe de connaissances, et non une preuve de bénéfice clinique. La similarité avec l'indication originale n'a pas encore été évaluée.

Parmi les autres prédictions, seule l'**acné** (2ᵉ rang, score 99,92 %) repose sur un mécanisme biologiquement plausible (régulation de la différenciation des kératinocytes et de l'activité des sébocytes par RAR/RXR). Elle ne s'appuie toutefois que sur deux revues générales, sans données spécifiques à l'alitrétinoïne, et des rétinoïdes établis (isotrétinoïne, trétinoïne, adapalène) occupent déjà ce domaine. Les autres prédictions (coarctation atypique de l'aorte, ostéoporose, malformation aortique, dysplasie mammaire bénigne, syndrome de Worth, etc.) sont sans preuve et, pour plusieurs d'entre elles, pharmacologiquement peu crédibles.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'aménorrhée.

À titre d'information, deux revues sont rattachées à la prédiction « acné » (rang 2) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Revue | Clinics in Dermatology | Vue d'ensemble de la vitamine A et des rétinoïdes en dermatologie (oraux : isotrétinoïne, acitrétine, alitrétinoïne, bexarotène ; topiques) |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Revue | Skin Pharmacology and Applied Skin Physiology | Fonctions pléiotropes des rétinoïdes et indications dermatologiques futures potentielles |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63446165 | ALIZEM 10 mg, capsule molle (annulée) | Capsule molle | Non renseignée |
| 65014058 | ALIZEM 30 mg, capsule molle (annulée) | Capsule molle | Non renseignée |
| 64156738 | TOCTINO 10 mg, capsule molle (annulée) | Capsule molle | Non renseignée |
| 69219167 | TOCTINO 30 mg, capsule molle (annulée) | Capsule molle | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de notice) : mycosis fongoïde et variantes, lymphome cutané primitif à cellules T, mycosis fongoïde folliculotrope, réticulose pagétoïde localisée, cutis laxa granulomateuse (granulomatous slack skin).
- **Tératogénicité** : les rétinoïdes sont fortement tératogènes ; l'utilisation pendant la grossesse est inacceptable. Cela exclut de fait plusieurs indications prédites (ostéoporose associée à la grossesse, par exemple).
- **Interactions pharmacologiques** : 7 cibles identifiées : récepteurs RARα, RARβ, RARγ, RXRα, RXRβ, RXRγ et la sous-unité 1 du complexe vitamine K époxyde réductase (VKORC1). L'interaction avec VKORC1 mérite une attention particulière en cas d'association avec des antivitamines K ; aucun niveau de gravité n'est précisé.

Veuillez consulter la notice pour les mises en garde détaillées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'aménorrhée repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. Le mécanisme est biologiquement peu plausible et le profil tératogène de la molécule est défavorable. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action détaillées (DrugBank) et analyse du lien mécanistique avec l'indication prédite
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Texte des indications approuvées des AMM annulées et raisons de l'annulation
- Si une piste doit être explorée, privilégier l'acné (niveau L4, « question de recherche ») avec une recherche bibliographique ciblée sur l'alitrétinoïne, en démontrant une valeur ajoutée par rapport aux rétinoïdes établis
- Évaluation de la compatibilité de voie d'administration et de la similarité avec l'indication originale (actuellement en attente)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

