---
layout: default
title: Altretamine
parent: Preuves modérées (L3-L4)
nav_order: 49
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Altretamine : nouvelle indication prédite, Carcinome du sein féminin (niveau de preuve L4). Indication d'origine : Cancer de l'ovaire"
monitor_inn: "altretamine"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
---

# Altretamine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Altrétamine : Du Cancer de l'Ovaire au Carcinome du Sein Féminin

## Résumé en Une Phrase

L'altrétamine (hexaméthylmélamine) est un antinéoplasique de la famille des s-triazines, initialement utilisé pour le traitement du cancer de l'ovaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome du sein féminin**.
Aucun essai clinique n'est enregistré et **3 publications** (précliniques ou indirectes) sont actuellement disponibles pour cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de l'ovaire (indication issue du graphe de connaissances ; le texte de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Carcinome du sein féminin |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Retiré du marché (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'altrétamine est un antinéoplasique de type alkylant de la famille des s-triazines. Elle nécessite une activation métabolique (N-déméthylation en intermédiaires méthylols réactifs). Son efficacité dans le cancer de l'ovaire réfractaire a conduit à son utilisation clinique.

Pour le sein, un modèle préclinique de xénogreffes tumorales humaines chez la souris nude (PMID 7559101) a montré une activité antitumorale in vivo contre plusieurs lignées de carcinome mammaire. Une revue systématique sur les dérivés s-triazines (PMID 37298753) soutient aussi une activité antitumorale au niveau de la classe, y compris dans des modèles de cancer du sein.

L'indication d'origine et la nouvelle indication partagent un contexte de tumeurs gynécologiques/hormono-dépendantes, ce qui rend la prédiction biologiquement plausible. Cependant, il s'agit d'un argument indirect : aucune étude clinique ne le confirme.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37298753](https://pubmed.ncbi.nlm.nih.gov/37298753/) | 2023 | Revue systématique (préclinique, niveau classe) | Molecules | Les dérivés s-triazines, dont l'altrétamine, sont une famille importante en conception d'anticancéreux ; l'altrétamine est approuvée dans le cancer de l'ovaire réfractaire |
| [7559101](https://pubmed.ncbi.nlm.nih.gov/7559101/) | 1995 | Préclinique (xénogreffes humaines) | Jpn J Cancer Res | Activité antitumorale in vivo de l'altrétamine contre des xénogreffes de carcinome mammaire, gastrique et colique chez la souris nude |
| [8411257](https://pubmed.ncbi.nlm.nih.gov/8411257/) | 1993 | Revue / analyse d'intensité de dose (indirecte, ovaire) | J Natl Cancer Inst | Méta-analyse sur l'intensité de dose en chimiothérapie du cancer de l'ovaire avancé ; seule la cisplatine montre une association significative avec la réponse |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69985098 (annulée) | HEXASTAT, gélule (LABORATOIRES DELBERT) | Gélule | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (alkylant de type s-triazine, nécessitant une activation métabolique) |
| Risque de Myélosuppression | Données de toxicité non disponibles ; les contre-indications du graphe de connaissances (thrombopénie, anémie, leucopénie) suggèrent un risque hématologique à surveiller |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS (numération formule sanguine), fonction hépatique et rénale, examen neurologique (neuropathie périphérique) |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

- **Maladies associées à une contre-indication (graphe de connaissances, et non texte de la notice)** : thrombopénie, maladie du système nerveux périphérique, neuropathie périphérique, anémie, anémie macrocytaire, vertige d'origine centrale, leucopénie.
- **Interactions Médicamenteuses** : 120 interactions recensées. Parmi les principales :
  - **Majeures** : déférisprone, samarium (153Sm) lexidronam, adalimumab.
  - **Modérées** : cimétidine, pyridoxine, palifermine, strontium-89, roflumilast, chloramphénicol, doxépine, zidovudine, ganciclovir, alemtuzumab, alefacept.
  - **Mineures** : lévofloxacine, géméfloxacine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,91 %), mais les preuves se limitent à des données précliniques (xénogreffes, 1995) et à une revue de classe. Aucun essai clinique n'existe, le médicament n'est plus commercialisé en France (AMM annulée) et les données de sécurité de la notice font défaut. À ce stade, il s'agit d'une question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice officielle (mises en garde, contre-indications) auprès de l'ANSM, étape bloquante avant tout criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Études précliniques supplémentaires dans le cancer du sein (modèles actuels, sous-types hormonaux), puis, si les résultats sont favorables, un essai clinique de phase précoce
- Évaluation de la faisabilité d'approvisionnement et de formulation, le produit étant retiré du marché
- Comparaison avec les traitements standards actuels du cancer du sein

---

*Remarque : les autres indications prédites (tumeur germinale gonadique, tumeur germinale primitive de l'ovaire, choriocarcinome de l'ovaire, tumeur ovarienne non épithéliale maligne, adénocarcinomes mucineux du rectum, du côlon, de la vésicule biliaire, du col utérin et des voies biliaires extrahépatiques) reposent surtout sur la proximité dans l'ontologie avec les indications d'origine, sans essai ni littérature spécifique ; elles sont classées en Hold ou en question de recherche.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

