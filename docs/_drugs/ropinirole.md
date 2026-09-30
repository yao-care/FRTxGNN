---
layout: default
title: Ropinirole
parent: Preuves modérées (L3-L4)
nav_order: 272
evidence_level: L4
indication_count: 10
---

# Ropinirole
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

# Ropinirole : D'une indication d'origine non renseignée au Trouble déficitaire de l'attention avec hyperactivité (TDAH)

## Résumé en Une Phrase

Le ropinirole est un agoniste dopaminergique D2/D3 commercialisé en France (REQUIP 2 mg). Le texte d'indication de son AMM n'est pas renseigné dans les données disponibles.
Le modèle TxGNN prédit qu'il pourrait être utile dans le **trouble déficitaire de l'attention avec hyperactivité (TDAH)**.
Ce signal repose sur **0 essai clinique** et **8 publications**, dont un seul rapport de cas pédiatrique évoque directement le ropinirole dans cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Trouble déficitaire de l'attention avec hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le ropinirole est un agoniste dopaminergique D2/D3. Son lien avec le TDAH est indirect et passe par le syndrome des jambes sans repos (SJSR).

Le SJSR et le TDAH surviennent souvent chez les mêmes patients. Une revue de la littérature (PMID 16218085) évoque un déficit dopaminergique commun comme explication possible. Les traitements dopaminergiques du SJSR pourraient donc aussi intéresser le TDAH lorsque les deux troubles coexistent.

La seule observation clinique directe est un rapport de cas : un enfant de 6 ans atteint de TDAH et de SJSR probable, peu amélioré par le méthylphénidate. Le ropinirole a été suivi d'une amélioration nette des symptômes de TDAH et du sommeil. On ne peut pas dire si le bénéfice sur le TDAH est indépendant de celui sur le SJSR.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | Rapport de cas | Pediatric Neurology | Enfant de 6 ans avec TDAH et SJSR : amélioration significative des symptômes de TDAH et du sommeil sous ropinirole |
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Revue | Sleep | Association entre SJSR et TDAH, mécanismes hypothétiques et intérêt de traitements communs |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revue | Revue Neurologique | Revue générale du SJSR (2 à 3 % de la population occidentale) |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Étude clinique (autre agoniste : piribédil) | Clinical Neuropharmacology | Vigilance dans la maladie de Parkinson, comparaison avec le pramipexole et le ropinirole ; peu pertinent pour le TDAH |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Préclinique / mécanistique | Pharmacological Research | Hétéromères récepteur D4 / adrénorécepteur α2A et lien avec le TDAH ; ne concerne pas directement le ropinirole |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | Modèle animal | J Neuropathol Exp Neurol | Modèle murin de type SJSR (lésion A11 et carence en fer) |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | Rapport de cas (sécurité) | Cornea | Œdème cornéen chez 3 patients exposés à des agents dopaminergiques |
| [30460371](https://pubmed.ncbi.nlm.nih.gov/30460371/) | 2019 | Rapport de cas (sécurité) | Acta Dermato-Venereologica | Délires d'infestation induits par le traitement avec augmentation de la dopamine cérébrale |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 68209070 | REQUIP 2 mg, comprimé pelliculé | Comprimé pelliculé | GLAXOSMITHKLINE |

---

## Considérations de Sécurité

Le dossier ne contient ni mise en garde, ni contre-indication, ni interaction médicamenteuse exploitable. Veuillez consulter la notice pour les informations de sécurité.

La littérature du dossier signale toutefois des risques à garder en tête, en particulier chez l'enfant :
- **Œdème cornéen** sous agents dopaminergiques (PMID 30950895)
- **Idées délirantes** induites par le traitement (PMID 30460371)

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le signal repose sur un seul rapport de cas pédiatrique et sur une association indirecte via le SJSR. Aucun essai clinique n'existe, et les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'étape de criblage de sécurité.
- Les autres indications prédites (schizophrénie, myopie liée à l'X, etc.) sont également en attente. Pour la schizophrénie, un agoniste dopaminergique pourrait même aggraver les symptômes psychotiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indication autorisée)
- Compléter le mécanisme d'action depuis DrugBank
- Déterminer si l'effet sur le TDAH est indépendant du traitement du SJSR
- Mener ou identifier des essais contrôlés, notamment pédiatriques, ainsi qu'une évaluation de sécurité chez l'enfant (troubles du contrôle des impulsions, psychose, somnolence, atteinte cornéenne)

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

