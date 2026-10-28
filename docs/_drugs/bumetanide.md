---
layout: default
title: Bumetanide
parent: Prédiction du modèle uniquement (L5)
nav_order: 122
evidence_level: L5
indication_count: 1
monitor_inn: "bumetanide"
predicted_indications: ["acute pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Bumetanide : nouvelle indication prédite, Cœur pulmonaire aigu (acute pulmonary heart disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Bumetanide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Bumétanide : diurétique de l'anse (inhibiteur du cotransporteur Na-K-2Cl) → Cœur pulmonaire aigu (acute pulmonary heart disease)
{: .text-alpha }

## Résumé en Une Phrase

Le bumétanide est un diurétique de l'anse, utilisé à l'origine dans le traitement de l'insuffisance cardiaque congestive.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **cœur pulmonaire aigu (acute pulmonary heart disease)**,
mais **aucun essai clinique** et **aucune publication** ne portent directement sur cette maladie : seules 5 publications sur l'insuffisance cardiaque et les diurétiques de l'anse en général sont disponibles.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Cœur pulmonaire aigu (acute pulmonary heart disease) |
| Score de Prédiction TxGNN | 0,9958 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le bumétanide inhibe le cotransporteur Na-K-2Cl (NKCC2) dans la branche ascendante épaisse de l'anse de Henlé. Il provoque ainsi une natriurèse et une diurèse rapides et marquées.

Dans le cœur pulmonaire aigu, la surcharge volumique du ventricule droit et la congestion systémique pourraient être soulagées par la diurèse, selon le même principe que dans l'insuffisance cardiaque congestive. Le lien est donc plausible, mais indirect : la littérature disponible concerne l'insuffisance cardiaque gauche, aiguë et chronique, et la pharmacologie générale des diurétiques de l'anse, pas le cœur pulmonaire aigu en lui-même.

Une prudence particulière s'impose : une défaillance ventriculaire droite dépendante de la précharge (par exemple dans une embolie pulmonaire massive) peut s'aggraver en cas de diurèse excessive. Le score très élevé du modèle est une prédiction computationnelle ; il reflète probablement la proximité avec l'insuffisance cardiaque plutôt qu'une preuve indépendante. Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'étudie directement le cœur pulmonaire aigu.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Étude hémodynamique interventionnelle (petite taille) | Br J Clin Pharmacol | Le bumétanide IV réduit la pression d'occlusion de l'artère pulmonaire chez 24 patients coronariens en insuffisance cardiaque aiguë (induite par l'effort) ou chronique |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Revue | Drugs | Propriétés pharmacodynamiques et pharmacocinétiques du bumétanide ; usage dans les œdèmes d'origine cardiaque, hépatique et rénale et dans la congestion pulmonaire aiguë |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Revue | Am J Ther | Prise en charge de l'insuffisance cardiaque aiguë et rôle des diurétiques |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Revue | Ann Pharmacother | Comparaison des diurétiques de l'anse (pharmacocinétique, efficacité, sécurité, coûts) |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohorte | Am J Emerg Med | Épidémiologie des consultations pour insuffisance cardiaque aux urgences américaines, 2016-2023 |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67563415 | BURINEX 5 mg, comprimé | Comprimé | Non renseignée |
| 68232635 | BURINEX 1 mg, comprimé | Comprimé | Non renseignée |
| 61834055 | BURINEX 2 mg/4 ml IV, solution injectable en ampoule | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications signalées dans les données compilées** (relations issues de bases de données, et non du texte de la notice) : maladie hépatique, encéphalopathie et coma hépatiques, anurie, hypercalcémie, néphrocalcinose, carence en potassium, troubles du métabolisme du phosphore, diabète et acidocétose diabétique, thrombopénie, affections de la vésicule biliaire, troubles de l'audition.
- **Interactions médicamenteuses** : 240 interactions recensées. Parmi elles, plusieurs de niveau modéré : antidiabétiques (metformine, acarbose, alogliptine, albiglutide, acétohexamide), corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, béclométasone), amphotéricine B (plusieurs formes), oméprazole, rabéprazole, bupropion, morphine et bisacodyl. Deux interactions mineures : doxycycline et acide acétylsalicylique.
- Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.
- Risque spécifique à cette indication : une diurèse excessive peut aggraver une défaillance ventriculaire droite dépendante de la précharge.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle : aucun essai ni aucune publication n'étudie le bumétanide dans le cœur pulmonaire aigu. Le niveau de preuve est donc L5, et le risque d'aggravation par sur-diurèse impose la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études ou séries de cas évaluant les diurétiques de l'anse dans le cœur pulmonaire aigu
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Définition des populations à exclure (notamment défaillance ventriculaire droite dépendante de la précharge)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

