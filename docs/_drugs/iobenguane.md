---
layout: default
title: Iobenguane
parent: Prédiction du modèle uniquement (L5)
nav_order: 152
evidence_level: L5
indication_count: 4
---

# Iobenguane
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Iobenguane : D'un Radiopharmaceutique Diagnostique à l'Hypotension (Prédiction TxGNN)

## Résumé en Une Phrase

L'iobenguane (MIBG) est un analogue de la noradrénaline. En France, il est commercialisé sous forme de solution injectable marquée à l'iode 123 (MIBG [123I]).
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**hypotension (trouble hypotensif)**, mais aucun **essai clinique** ne l'étudie et les **20 publications** associées décrivent un usage diagnostique (imagerie de la dénervation sympathique cardiaque), pas un effet thérapeutique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Trouble hypotensif (hypotension) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L4 (données diagnostiques et physiopathologiques, sans preuve thérapeutique) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après la littérature fournie, l'iobenguane est un analogue de la noradrénaline, capté par les terminaisons nerveuses sympathiques cardiaques. Il est décrit comme un analogue pharmacologiquement inactif, métabolisé comme la noradrénaline dans les neurones noradrénergiques.

Dans les publications retenues, l'iobenguane sert de **marqueur diagnostique** de la dénervation sympathique cardiaque, notamment dans la maladie de Parkinson associée à l'hypotension orthostatique. Il n'est pas utilisé comme traitement. Le score élevé de TxGNN reflète donc très probablement une association dans le graphe de connaissances (hypotension orthostatique neurogène et dénervation cardiaque), et non un effet thérapeutique.

Le mécanisme ne peut pas être confronté à la pharmacologie connue du produit, faute de données sur l'indication d'origine et le mécanisme d'action. Il n'existe à ce stade aucun argument mécanistique en faveur d'un bénéfice thérapeutique dans l'hypotension.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucun essai contrôlé randomisé n'est disponible. Le tableau présente les 10 publications les plus pertinentes sur 20, dont aucune n'évalue un effet thérapeutique.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11482743](https://pubmed.ncbi.nlm.nih.gov/11482743/) | 2001 | Revue | Drugs Aging | Physiopathologie et prise en charge de l'hypotension orthostatique dans la maladie de Parkinson (prévalence symptomatique pouvant atteindre 20 %) |
| [27091624](https://pubmed.ncbi.nlm.nih.gov/27091624/) | 2016 | Revue | Mov Disord | Lien entre hypotension orthostatique et troubles cognitifs dans la maladie de Parkinson : causalité ou association, question non tranchée |
| [24332912](https://pubmed.ncbi.nlm.nih.gov/24332912/) | 2014 | Revue | Parkinsonism Relat Disord | La scintigraphie myocardique au MIBG est un marqueur précoce de la maladie de Parkinson, avec une sensibilité et une spécificité élevées |
| [39232705](https://pubmed.ncbi.nlm.nih.gov/39232705/) | 2024 | Cohorte | BMC Neurol | Recherche d'un lien entre tachycardie atténuée (marqueur d'hypotension orthostatique neurogène) et dénervation sympathique cardiaque dans le trouble du comportement en sommeil paradoxal isolé |
| [26944118](https://pubmed.ncbi.nlm.nih.gov/26944118/) | 2016 | Cohorte | J Neurol Sci | Association entre hypotension orthostatique, dénervation sympathique cardiaque et trouble du comportement en sommeil paradoxal dans la maladie de Parkinson |
| [34568970](https://pubmed.ncbi.nlm.nih.gov/34568970/) | 2021 | Cohorte | J Neural Transm | 77 patients parkinsoniens et 54 témoins : relation entre la neurofilament light chain plasmatique et des marqueurs non moteurs (dont hypotension orthostatique et dénervation cardiaque) |
| [32134983](https://pubmed.ncbi.nlm.nih.gov/32134983/) | 2020 | Non classé | PLoS One | Relation entre le taux de lavage du MIBG-I123 et la fonction autonome dans la maladie de Parkinson (résultats non détaillés dans l'extrait) |
| [29880316](https://pubmed.ncbi.nlm.nih.gov/29880316/) | 2018 | Non classé | Parkinsonism Relat Disord | Recherche d'une dénervation sympathique centrale chez les patients parkinsoniens avec hypotension orthostatique à noradrénaline élevée |
| [11322922](https://pubmed.ncbi.nlm.nih.gov/11322922/) | 2001 | Non classé | Biochem Pharmacol | Le MIBG figure parmi les composés guanidiniques d'usage établi en oncologie, avec une similarité structurale avec la noradrénaline |
| [32169989](https://pubmed.ncbi.nlm.nih.gov/32169989/) | 2020 | Cas clinique | BMJ Case Rep | Syncope de miction secondaire à un paragangliome vésical (contexte de tumeur sécrétant des catécholamines) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 64886840 | MIBG [123 I] 74 MBq/mL solution injectable | Solution injectable | Curium Netherlands (Pays-Bas) |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (99,90 %). Aucun essai clinique n'existe, et la littérature décrit l'iobenguane comme outil d'imagerie, sans données thérapeutiques dans l'hypotension.
- Les données de sécurité et de mécanisme d'action manquent. L'analyse de sécurité ne peut donc pas commencer.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indication officielle)
- Obtenir le mécanisme d'action détaillé via DrugBank
- Trancher si la question relève d'un usage diagnostique (évaluation de la dénervation sympathique dans l'hypotension orthostatique neurogène) plutôt que d'un repositionnement thérapeutique
- Réunir des preuves précliniques ou cliniques d'un effet thérapeutique avant toute réévaluation

Les autres prédictions du modèle suivent le même schéma. L'atrophie multisystématisée (L3) et le syndrome de tachycardie orthostatique posturale (L4) reposent sur des études diagnostiques ou physiopathologiques, et la prionopathie sensible aux protéases de façon variable (L5) n'a aucune preuve associée.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

