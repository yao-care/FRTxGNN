---
layout: default
title: Acebutolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 15
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Acebutolol : nouvelle indication prédite, Maladie rénale hypertensive maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "acebutolol"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Acebutolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Acébutolol : De l'Hypertension à l'Hypertension Rénale Maligne
{: .text-alpha }

## Résumé en Une Phrase

L'acébutolol est un bêta-bloquant cardiosélectif, initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne** (et, en second rang, l'**hypertension rénovasculaire maligne**).
Actuellement, **aucun essai clinique** et **une seule publication** indirecte (une étude de 1975 sur l'hypertension en général) soutiennent cette direction : la prédiction repose donc essentiellement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (le texte de l'indication de l'AMM française n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne |
| Score de Prédiction TxGNN | 99,10 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'acébutolol est un bêta-1 bloquant cardiosélectif doté d'une activité sympathomimétique intrinsèque. Son efficacité dans l'hypertension est établie, et mécanistiquement il pourrait être applicable à l'atteinte rénale hypertensive.

Le blocage bêta-1 abaisse la pression artérielle et réduit la libération de rénine par l'appareil juxtaglomérulaire. Ce mécanisme est biologiquement plausible pour l'hypertension rénovasculaire, dans laquelle l'axe rénine-angiotensine joue un rôle central, ainsi que pour l'atteinte rénale liée à l'hypertension.

Il faut toutefois rester prudent : l'hypertension maligne avec atteinte rénale est une urgence hypertensive, généralement prise en charge par des traitements parentéraux, et les bêta-bloquants oraux n'y sont pas un traitement de première intention. Les deux prédictions affichent exactement le même score (0,991), ce qui suggère une inférence issue du graphe plutôt qu'un soutien spécifique à chaque indication. Le lien reste donc théorique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Pour l'indication de rang 2 (hypertension rénovasculaire maligne), une seule publication a été retrouvée ; aucune pour l'indication principale.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [768911](https://pubmed.ncbi.nlm.nih.gov/768911/) | 1975 | Étude clinique ouverte (indirecte) | La Nouvelle Presse Médicale | 50 patients hypertendus traités un an par acébutolol seul ou associé : résultats bons ou modérés chez 74 % des patients, échecs chez 26 %, très bonne tolérance. Étude portant sur l'hypertension en général, non spécifique de la forme maligne ou rénovasculaire. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61969626 | SECTRAL 40 mg/mL, solution buvable en flacon (CHEPLAPHARM ARZNEIMITTEL, Allemagne) | Solution buvable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : asthme (y compris intrinsèque et allergique), emphysème pulmonaire, bloc auriculo-ventriculaire, maladie du sinus, maladies artérielles périphériques (claudication intermittente), phéochromocytome et paragangliome sympathique, myasthénie grave et maladies de la jonction neuromusculaire, diabète et acidocétose diabétique, insuffisance rénale, maladie hépatique et des voies biliaires, psoriasis, ainsi que troubles anxieux, névrotiques et dysthymiques. Ces éléments sont à confirmer par la notice officielle.
- **Interactions médicamenteuses** : 230 interactions recensées. Parmi les principales, de niveau modéré : antidiabétiques (acétohexamide, chlorpropamide, canagliflozine, dapagliflozine), corticoïdes (bétaméthasone, budésonide), atropine, clidinium, bupropion, cimétidine et sels de calcium. De niveau mineur : hydroxyde d'aluminium, acide acétylsalicylique, attapulgite.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées ; veuillez consulter la notice pour les informations de securité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5 pour l'indication principale, L4 pour la seconde, avec une seule étude indirecte), sans essai clinique. L'AMM française est de plus annulée, ce qui limite le développement pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Rechercher des études spécifiques à l'hypertension maligne et à l'atteinte rénale hypertensive
- Évaluer la place d'un bêta-bloquant oral par rapport aux traitements standards de l'urgence hypertensive
- Vérifier la compatibilité des voies d'administration (solution buvable uniquement, AMM annulée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

