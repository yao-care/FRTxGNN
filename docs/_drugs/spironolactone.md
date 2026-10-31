---
layout: default
title: Spironolactone
parent: Prédiction du modèle uniquement (L5)
nav_order: 713
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone : nouvelle indication prédite, Hypotrichose simple du cuir chevelu (hypotrichosis simplex of the scalp) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données lo…"
---

# Spironolactone
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

## Spironolactone: Hypotrichose simple du cuir chevelu (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Résumé en Une Phrase

Spironolactone est un antagoniste de l'aldostérone, initialement utilisé pour traiter l'hypertension artérielle, l'insuffisance cardiaque congestive et l'hyperaldostéronisme.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu (hypotrichosis simplex of the scalp) |
| Score de Prédiction TxGNN | 0.9926 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la spironolactone est un antagoniste des récepteurs minéralocorticoïdes, dont l'efficacité dans l'hypertension et l'insuffisance cardiaque est établie. Elle possède aussi une activité anti-androgénique (blocage du récepteur des androgènes, réduction de la synthèse androgénique), exploitée en pratique clinique dans l'alopécie féminine de type androgénique.

Cependant, l'hypotrichose simple est un trouble héréditaire de la pousse des cheveux, lié à des variants de gènes tels que CDSN, APCDD1 et RPL21, et non à une cause androgénique. Le raisonnement anti-androgénique ne s'applique donc pas clairement. Le score élevé du modèle TxGNN (apprentissage profond) (0,9926) peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Pour la seconde prédiction (hypotrichose congénitale avec milia, score 0,9904), la situation est similaire : aucune preuve fournie et aucune pertinence établie de l'action anti-androgénique pour cette maladie congénitale rare. Le lien reste spéculatif.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69360552 | Spironolactone Zydus 25 mg | Comprimé pelliculé sécable | Non renseignée |
| 65618628 | Spironolactone Pfizer 25 mg | Comprimé sécable | Non renseignée |
| 67368301 | Aldactone 50 mg | Comprimé sécable | Non renseignée |
| 64565845 | Aldactone 25 mg | Comprimé sécable | Non renseignée |
| 68492540 | Aldactone 75 mg | Comprimé sécable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, et non du texte de la notice)** : maladie rénale, anurie, pyourétère, pancréatite, lupus érythémateux systémique (y compris pédiatrique), carence en potassium, diabète sucré, acidocétose diabétique, hyperuricémie, goutte, hyperparathyroïdie, ostéite fibreuse, coma hépatique, encéphalopathie hépatique, ictère néonatal, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore.
- **Interactions médicamenteuses** (100 interactions recensées ; exemples) :
  - **Majeure** : lopéramide.
  - **Modérée** : hydrocortisone, metformine, bupropion, triamcinolone, morphine, dexaméthasone, bétaméthasone, budésonide, bisacodyl, canagliflozine, dapagliflozine, empagliflozine, ertugliflozine, exénatide, huile de ricin, dronabinol.
  - **Mineure** : doxycycline, acide acétylsalicylique, fidaxomicine.

Les mises en garde et contre-indications issues de la notice officielle n'ont pas pu être consultées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme anti-androgénique ne correspond pas à l'origine héréditaire de l'hypotrichose simple, et les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, ce qui bloque actuellement l'évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action
- Réaliser une revue de la littérature et des registres d'essais pour l'hypotrichose simple et l'hypotrichose congénitale avec milia
- Évaluer la compatibilité des voies d'administration (seules des formes orales sont connues) et la pertinence d'une formulation adaptée
- Clarifier la situation réglementaire (raison de l'annulation des AMM) avant toute démarche
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

