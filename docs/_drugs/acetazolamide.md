---
layout: default
title: Acetazolamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acetazolamide : nouvelle indication prédite, Hyperthermie maligne d'effort (niveau de preuve L5). Indication d'origine : Épilepsie-absence, insuffisance cardiaque congestive, glaucome…"
monitor_inn: "acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
---

# Acetazolamide
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

# Acétazolamide : De l'épilepsie-absence et du glaucome à l'hyperthermie maligne d'effort

## Résumé en Une Phrase

L'acétazolamide est un inhibiteur de l'anhydrase carbonique, initialement utilisé dans l'épilepsie-absence, l'insuffisance cardiaque congestive, le glaucome (à angle ouvert et à angle fermé) et le mal des montagnes.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hyperthermie maligne d'effort**, mais cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Épilepsie-absence, insuffisance cardiaque congestive, glaucome, mal des montagnes (source : graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Predite | Hyperthermie maligne d'effort |
| Score de Prediction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'acétazolamide appartient à la classe des inhibiteurs de l'anhydrase carbonique. Son efficacité a été établie dans plusieurs indications (glaucome, mal des montagnes, certaines formes d'épilepsie, œdème lié à l'insuffisance cardiaque).

Un lien plausible, mais **purement spéculatif**, passerait par la modification du pH et de la gestion des ions dans le muscle squelettique. Aucune donnée fournie ne confirme ce lien. Le score très élevé du modèle (99,95 %) reflète une proximité dans le graphe de connaissances, et non une preuve d'efficacité.

À titre de comparaison, d'autres prédictions du même modèle portent sur la cardiomyopathie hypertrophique, la cardiomyopathie, l'occlusion intestinale, etc. Pour celles-ci, la littérature disponible est indirecte, voire signale un risque (par exemple des cas d'iléus adynamique sous acétazolamide). Elles ne modifient pas l'évaluation de l'indication principale.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 68693244 | DIAMOX 250 mg, comprimé sécable (annulée) | Comprimé sécable | Non renseignée |
| 63463588 | DIAMOX 500 mg, poudre et solvant pour préparation injectable (annulée) | Poudre et solution pour préparation injectable | Non renseignée |

Les deux AMM, détenues par COOPER (Coopération Pharmaceutique Française), sont annulées : aucune AMM n'est actuellement valide en France.

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique et maladies du foie, maladies rénales, acidose tubulaire rénale, insuffisance respiratoire, maladies hématologiques, maladies de la vésicule biliaire, goutte, diabète de type 1 et de type 2, acidocétose diabétique, maladie d'Addison et insuffisances surrénaliennes (dont hyperplasie congénitale des surrénales).
- **Interactions médicamenteuses** : 165 interactions recensées. Parmi les exemples consultés, des interactions **majeures** avec l'acide acétylsalicylique et le cisapride. Les interactions **modérées** concernent notamment les antidiabétiques (acarbose, alogliptine, canagliflozine, dapagliflozine, chlorpropamide, dulaglutide), les corticoïdes (bétaméthasone, dexaméthasone, béclométasone), l'amphotéricine B (et ses formulations) et certains laxatifs (bisacodyl, huile de ricin). Une interaction **mineure** est signalée avec la doxycycline.
- **Signaux de sécurité issus de la littérature** : cas d'œdème pulmonaire non cardiogénique après acétazolamide intraveineuse, et cas d'iléus adynamique induit par l'acétazolamide. Chez le patient cirrhotique, un risque d'hyperammoniémie et d'encéphalopathie est à considérer.

Les mises en garde et contre-indications officielles de la notice ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction pour l'hyperthermie maligne d'effort repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ni mécanisme démontré.
- Aucune AMM valide n'existe en France, et les données de sécurité officielles sont absentes. Il n'est donc pas possible de passer à l'étape de dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) sur le site de l'ANSM.
- Obtenir les données détaillées sur le mécanisme d'action, par exemple via DrugBank.
- Mener une recherche ciblée de la littérature et des essais sur l'hyperthermie maligne d'effort, afin de vérifier s'il existe un fondement biologique.
- Clarifier le statut réglementaire (AMM annulées) et la disponibilité réelle du produit.
- Évaluer les contre-indications issues du graphe de connaissances et les interactions majeures pour la population cible.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

