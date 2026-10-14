---
layout: default
title: Lonoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 459
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
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

# Lonoctocog alfa : De l'hémophilie à la pseudo-maladie de von Willebrand

## Résumé en Une Phrase

Lonoctocog alfa est un facteur VIII de coagulation recombinant à chaîne unique, initialement utilisé pour le traitement de l'hémophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand** (de type plaquettaire).
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction issue du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie (la base de données réglementaire française ne fournit pas de texte d'indication ; l'indication provient du graphe de connaissances TxGNN) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, lonoctocog alfa est un facteur VIII recombinant à chaîne unique (rVIII-SingleChain), dont l'affinité pour le facteur von Willebrand (VWF) est renforcée. Son efficacité a été établie dans l'hémophilie, où il remplace le facteur VIII déficient.

La pseudo-maladie de von Willebrand (forme plaquettaire) résulte de variants à gain de fonction de la GPIbα plaquettaire. Ceux-ci augmentent la fixation du VWF aux plaquettes, entraînant une perte des multimères de VWF de haut poids moléculaire, puis une baisse secondaire du VWF et du FVIII. Le lien théorique est qu'un apport de FVIII pourrait corriger ce déficit secondaire.

Cette hypothèse reste toutefois limitée : le FVIII ne corrige pas le défaut plaquettaire sous-jacent. Le score élevé du modèle reflète une proximité dans le réseau de connaissances entre maladies hémorragiques, et non une preuve mécanistique ou clinique.

**Autres prédictions du modèle (toutes de niveau L5, sans essai ni publication) :**

| Maladie prédite | Score TxGNN | Commentaire |
|------|------|------|
| Trouble primaire de la libération plaquettaire | 99,84 % | Le médicament agit sur la cascade de coagulation, pas sur la sécrétion plaquettaire ; aucun fondement mécanistique clair |
| Thrombasthénie de Glanzmann | 99,76 % | Déficit de l'intégrine αIIbβ3 ; le FVIII n'est pas déficient et ne corrige pas l'agrégation plaquettaire |
| Syndrome de Scott | 99,44 % | Lien ténu (le FVIII est un cofacteur du complexe ténase), mais le défaut primaire est l'absence de surface phospholipidique procoagulante |

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
| 61906519 | AFSTYLA 1000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 64477690 | AFSTYLA 2000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 67710662 | AFSTYLA 500 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 60944716 | AFSTYLA 1500 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 66216027 | AFSTYLA 250 UI | Poudre et solvant pour solution injectable | Non renseignée |

Les 7 AMM (titulaire : CSL Behring, Allemagne) sont annulées ; seules les 5 premières sont listées ici. Aucune AMM n'est actuellement valide en France.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le mécanisme est peu plausible, car le FVIII ne corrige pas le défaut plaquettaire sous-jacent. De plus, aucune AMM n'est valide en France et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) pour pouvoir réaliser le premier criblage de sécurité (point bloquant)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank)
- Rechercher activement des cas cliniques, études observationnelles ou données précliniques sur le FVIII dans la pseudo-maladie de von Willebrand
- Clarifier la situation réglementaire du produit (raisons de l'annulation des AMM, disponibilité éventuelle sous un autre statut)
- Évaluer la compatibilité des voies d'administration, aujourd'hui non analysée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

