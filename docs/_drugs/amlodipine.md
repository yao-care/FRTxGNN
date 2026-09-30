---
layout: default
title: Amlodipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine : De l'Antihypertenseur à l'Infarctus du Tronc Cérébral

## Résumé en Une Phrase

L'amlodipine est un inhibiteur calcique de type dihydropyridine, classiquement utilisé comme antihypertenseur. Le texte d'indication des AMM françaises n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**infarctus du tronc cérébral**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction pour cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM du pack |
| Nouvelle Indication Prédite | Infarctus du tronc cérébral (brain stem infarction) |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 6 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. L'amlodipine est un inhibiteur calcique de type dihydropyridine. Son mécanisme plausible est le blocage des canaux calciques de type L, qui provoque une vasodilatation et une baisse de la pression artérielle. Une neuroprotection est également envisageable.

Le lien avec l'infarctus du tronc cérébral repose sur deux hypothèses. La première est le contrôle tensionnel, facteur de risque majeur des accidents vasculaires cérébraux. La seconde est un effet neuroprotecteur, suggéré par des modèles animaux d'ischémie cérébrale (voir la conclusion).

Ce raisonnement reste théorique. Il s'agit d'une prédiction du modèle seul, sans essai clinique ni publication propre à cette indication. La similarité avec l'indication originale n'a pas encore été évaluée.

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
| 63566442 | AMLODIPINE ZYDUS 5 mg | Gélule | Non renseignée |
| 62204255 | AMLODIPINE VIATRIS GENERIQUES 5 mg | Gélule | Non renseignée |
| 63811710 | AMLODIPINE EG 5 mg | Gélule | Non renseignée |
| 68500357 | AMLODIPINE ZYDUS 10 mg | Gélule | Non renseignée |
| 63436445 | AMLODIPINE VIATRIS GENERIQUES 10 mg | Gélule | Non renseignée |

Six AMM sont recensées au total, dont cinq sont listées ci-dessus. Une forme à libération modifiée (comprimé) figure aussi dans les données de voies d'administration.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'infarctus du tronc cérébral repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. Les données de sécurité de la notice ANSM manquent également et bloquent le passage au criblage de sécurité.
- Le pack contient d'autres indications prédites mieux documentées. L'**hémorragie intracérébrale** est au niveau L2 : l'essai de phase 3 TRIDENT (n=1671, terminé) teste une trithérapie antihypertensive à faible dose contenant de l'amlodipine, donc l'effet de l'amlodipine seule ne peut pas être isolé. L'**occlusion d'artère cérébrale** est au niveau L4, avec des études précliniques chez l'animal. Ces pistes méritent d'être évaluées en priorité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), une lacune bloquante.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Renseigner les indications approuvées des AMM françaises.
- Réévaluer le choix de l'indication prioritaire, en comparant l'infarctus du tronc cérébral aux indications mieux étayées.
- Rechercher des études spécifiques à l'amlodipine dans l'infarctus du tronc cérébral.

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

