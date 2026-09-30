---
layout: default
title: Ipilimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 157
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Ipilimumab : Prédiction de Repositionnement vers la Choroïdérémie

## Résumé en Une Phrase

Ipilimumab est un anticorps anti-CTLA-4 commercialisé en France sous le nom Yervoy. L'indication d'origine n'est pas renseignée dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **choroïdérémie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction. Elle repose uniquement sur le score du modèle et est probablement un artefact du graphe.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Choroïdérémie |
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Ipilimumab bloque CTLA-4, un frein de l'activation des lymphocytes T. Ce mécanisme est validé en oncologie, où il aide le système immunitaire à attaquer les tumeurs.

La choroïdérémie est une dégénérescence rétinienne héréditaire liée à l'X, causée par la perte du gène CHM/REP1. Elle n'est pas due à un échappement immunitaire tumoral. **Aucun lien mécanistique plausible** n'a été identifié : le blocage de CTLA-4 n'a pas de rôle thérapeutique vraisemblable dans cette maladie.

Le score élevé (0,99) doit donc être considéré comme une prédiction seule, probablement un artefact du graphe de connaissances. Il ne peut être corroboré par aucune donnée clinique ou publiée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66532840 | YERVOY 5 mg/mL | Solution à diluer pour perfusion | Non renseignée dans les données extraites |

Titulaire : BRISTOL-MYERS SQUIBB / PFIZER EEIG (Irlande).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (inhibiteur de point de contrôle immunitaire anti-CTLA-4) |

Pour le risque de myélosuppression, l'émétogénicité, les éléments de surveillance et la protection de manipulation, veuillez consulter les mises en garde et précautions de la notice.

## Considérations de Sécurité

- **Mises en garde liées à la prédiction** : ipilimumab est associé à des effets indésirables oculaires d'origine immunitaire, tels que l'uvéite. C'est un point d'attention particulier pour une maladie rétinienne.

Pour les autres informations de sécurité (mises en garde, contre-indications, interactions), veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : aucun essai, aucune publication, aucun mécanisme plausible. Le risque d'effets oculaires immuno-médiés va à l'encontre de l'usage envisagé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), données actuellement manquantes et bloquantes pour tout criblage de sécurité
- Données de mécanisme d'action (MOA) et indication d'origine, à récupérer via DrugBank
- Preuve biologique démontrant un lien entre la voie CTLA-4 et la choroïdérémie, sans quoi la piste n'a pas de fondement

**Note :** la 2ᵉ prédiction du modèle, le **mélanome non cutané** (uvéal et muqueux ; score 99,02 %), est nettement mieux étayée. Elle compte de nombreux essais cliniques, dont des études de Phase 2/3 sur le mélanome, et une cohorte incluant des mélanomes uvéaux et muqueux (PMID 24999899). Elle est classée L3 et « Research Question ». Ces données portent surtout sur le mélanome cutané, donc l'applicabilité aux sous-types non cutanés reste indirecte. Il faudrait extraire les résultats stratifiés par sous-type avant toute recommandation.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

