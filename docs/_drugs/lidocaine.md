---
layout: default
title: Lidocaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
monitor_inn: "lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
last_modified_at: 2026-10-23
description: "Lidocaine : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (niveau de preuve L5). Indication d'origine : Le texte d'indication des AMM n'est pas renseigné dans les données co…"
---

# Lidocaine
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

## Lidocaïne : De la douleur et des affections cutanées à la prédiction « Kératoconjonctivite ponctuée épithéliale »
{: .text-alpha }

## Résumé en Une Phrase

La lidocaïne est un anesthésique local, dont les relations enregistrées dans le graphe de connaissances concernent notamment la dermatite, les névralgies (dont la névralgie post-zostérienne), les hémorroïdes et la gale.
Le modèle TxGNN prédit en premier rang la **kératoconjonctivite épithéliale ponctuée**, mais sans aucune preuve réelle (**0 essai clinique**, **0 publication**) ; le sujet le mieux documenté parmi les prédictions est le **trouble de la conjonctive** (2 essais cliniques et de nombreuses publications, essentiellement indirects).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Le texte d'indication des AMM n'est pas renseigné dans les données compilées ; les usages connus proviennent uniquement de relations du graphe de connaissances (dermatite, névralgie, hémorroïdes, gale, etc.) |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée |
| Score de Prédiction TxGNN | 0,9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 18) |
| Nombre d'AMM | Au moins 20 AMM (la liste peut être partielle) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la lidocaïne est un anesthésique local de type bloqueur des canaux sodiques, ce qui peut soulager la douleur et la transmission sensitive à la surface de l'œil.

Le score de la prédiction provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ; la relation entre les usages connus (douleur neuropathique, dermatite, prurit) et la prédiction est au mieux symptomatique. La kératoconjonctivite épithéliale ponctuée est le plus souvent inflammatoire ou infectieuse (par exemple adénovirale) : la lidocaïne n'agirait pas sur la cause. Les anesthésiques topiques comportent en outre un risque de toxicité épithéliale cornéenne.

Le score très élevé du modèle reste une prédiction pure, sans étude pour la soutenir. Il en va de même pour les autres prédictions (conjonctivite papillaire, conjonctivite rosacée, syndrome néphrotique), dont plusieurs sont probablement des artefacts du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique n'est enregistré pour la kératoconjonctivite épithéliale ponctuée, indication prédite de rang 1.

À titre indicatif, voici les essais associés à la prédiction de rang 6 (trouble de la conjonctive). Ils concernent l'anesthésie procédurale et non le traitement d'une maladie conjonctivale :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Terminé | 41 | Gel de lidocaïne versus injection sous-conjonctivale lors de l'exérèse de ptérygion |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | Non applicable | Terminé | 34 | Comparaison de la douleur postopératoire avec deux types d'anesthésie locale en chirurgie du ptôsis |

## Preuves de la Littérature

Aucune littérature disponible pour la kératoconjonctivite épithéliale ponctuée. Pour la prédiction de rang 6, la littérature concerne surtout l'anesthésie en chirurgie oculaire et les céphalées SUNCT/SUNA (rapprochement fondé sur le seul nom) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | Essai randomisé | Eye | Gel de lidocaïne versus collyre de tétracaïne comme seul anesthésique en chirurgie du ptérygion primaire |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Étude pilote | Cornea | Injection sous-conjonctivale versus gel de lidocaïne à 2 % ou 5 % en chirurgie du ptérygion |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Étude clinique | Acta Ophthalmol Scand | Efficacité du gel de lidocaïne à 2 % en chirurgie du ptérygion |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Étude clinique | Ophthalmologica | Soulagement de la douleur après chirurgie du ptérygion avec lidocaïne visqueuse |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Préclinique | JCI Insight | Association nerf–cellules caliciformes favorisant la conjonctivite allergique |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Revue (sécurité) | Cephalalgia | Effets indésirables neuropsychiatriques de la lidocaïne dans les céphalées |

## Informations de Marché en France

La liste ci-dessous est partielle (au moins 20 AMM). Les textes d'indication ne sont pas renseignés dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63572616 | MESOCAÏNE 50 mg/5 ml | Solution injectable | Non renseignée |
| 66290522 | LIDOCAINE AGUETTANT 20 mg/ml sans conservateur | Solution injectable | Non renseignée |
| 65191044 | XYLOCONTACT | Crème pour usage dentaire | Non renseignée |
| 65538840 | VERSATIS 700 mg | Emplâtre médicamenteux | Non renseignée |
| 61164434 | LIDOCAÏNE KABI 20 mg/ml | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications relevées dans le graphe de connaissances** (relations du graphe, et non texte de la notice) : hypertension, insuffisance hépatique, épilepsie, maladie rénale, cirrhose, glaucome à angle ouvert, insuffisance surrénalienne, hypothyroïdie, ostéoporose, troubles psychotiques, infections fongiques, gastrite, entre autres.
- **Interactions médicamenteuses** : 534 interactions recensées. Parmi les principales, le bupropion (majeure) ; l'aprépitant, la cimétidine, l'acide obéticholique, la morphine liposomale, le polyéthylène glycol avec électrolytes, l'acide picosulfurique et le sulfate de sodium (modérées).
- **Points de vigilance issus de la littérature** : risque de méthémoglobinémie en cas d'association d'anesthésiques topiques et de co-trimoxazole chez un enfant néphrotique ; modification de la fixation protéique en cas de maladie rénale ; effets neuropsychiatriques et cardiaques en administration intraveineuse ; toxicité épithéliale cornéenne potentielle des anesthésiques topiques oculaires.

Pour le reste, veuillez consulter la notice : les mises en garde et contre-indications issues des notices ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction de rang 1 (kératoconjonctivite épithéliale ponctuée) n'a ni essai clinique ni publication : le niveau de preuve est L5. Pour le trouble de la conjonctive, les études portent sur l'anesthésie procédurale et ne démontrent pas un traitement de la maladie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications issues des notices (ANSM) pour mener le criblage de sécurité
- Les données détaillées sur le mécanisme d'action
- Des études directes de la lidocaïne dans la pathologie conjonctivo-cornéenne visée, avec évaluation de la tolérance épithéliale
- La vérification de la compatibilité des voies d'administration et des formes disponibles avec un usage ophtalmique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

