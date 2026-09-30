---
layout: default
title: Diltiazem
parent: Prédiction du modèle uniquement (L5)
nav_order: 105
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Diltiazem : De l'Indication Originale Non Renseignée à la Susceptibilité (Obsolète) à l'Accident Vasculaire Cérébral Ischémique

## Résumé en Une Phrase

Le diltiazem est commercialisé en France sous la marque Tildiem (Sanofi Winthrop Industrie), mais le texte de son indication originale n'est pas renseigné dans les données disponibles.
Le modèle TxGNN prédit qu'il pourrait être utile pour la **susceptibilité à l'accident vasculaire cérébral ischémique** (un terme d'ontologie signalé comme « obsolète »).
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction, qui repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (aucun texte d'indication dans les 5 AMM) |
| Nouvelle Indication Prédite | Susceptibilité à l'accident vasculaire cérébral ischémique (terme obsolète) |
| Score de Prédiction TxGNN | 99,08 % (rang 6011) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des connaissances pharmacologiques générales (et non des données fournies), le diltiazem est un inhibiteur calcique de type L, de la famille des non-dihydropyridines. Son action vasodilatatrice et son effet sur la pression artérielle pourraient, en théorie, réduire le risque vasculaire.

Le lien avec l'accident vasculaire cérébral ischémique reste donc une inférence pharmacologique générale. Aucune annotation validée (mécanisme d'action, indications d'origine) ne permet de la confirmer.

Le libellé de la maladie est marqué « obsolète », ce qui indique un terme d'ontologie déprécié. Il peut correspondre à un concept ancien ou fusionné plutôt qu'à une entité clinique distincte, de sorte que la prédiction ne se rattache pas forcément à une indication actuelle de l'AVC. Le score élevé ne doit pas être interprété comme un soutien clinique.

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
| 60998977 | TILDIEM 100 mg, poudre pour solution injectable (IV) | Poudre pour solution injectable | Non renseignée |
| 63692245 | TILDIEM 60 mg, comprimé | Comprimé | Non renseignée |
| 68227652 | BI TILDIEM L.P. 90 mg | Comprimé enrobé à libération prolongée | Non renseignée |
| 65662076 | BI TILDIEM L.P. 120 mg | Comprimé enrobé à libération prolongée | Non renseignée |
| 62018628 | TILDIEM 25 mg, poudre et solution pour préparation injectable I.V. | Poudre et solution pour préparation injectable | Non renseignée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication.
- Le terme de maladie est obsolète, et les données de sécurité et de mécanisme d'action sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité).
- Obtenir le mécanisme d'action et les indications d'origine via DrugBank et les textes d'AMM.
- Identifier le terme actuel de l'ontologie qui remplace ou fusionne le concept obsolète, et vérifier s'il correspond à une indication clinique réelle de l'AVC ischémique.
- Mener une recherche ciblée d'essais cliniques et de littérature (diltiazem et AVC ischémique) une fois le terme clarifié.

---

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

