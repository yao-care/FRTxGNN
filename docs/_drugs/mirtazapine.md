---
layout: default
title: Mirtazapine
parent: Prédiction du modèle uniquement (L5)
nav_order: 504
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "MIRTAZAPINE"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
description: "Mirtazapine : nouvelle indication prédite, Syndrome d'Ohdo et variantes (Ohdo syndrome and variants) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Mirtazapine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Mirtazapine: Syndrome d'Ohdo et variantes (Ohdo syndrome and variants)
{: .text-alpha }

## Résumé en Une Phrase

La mirtazapine est un antidépresseur initialement utilisé pour traiter la dépression unipolaire, la dépression endogène, le trouble dépressif majeur et le trouble anxieux.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome d'Ohdo et ses variantes**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'un signal purement computationnel.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome d'Ohdo et variantes (Ohdo syndrome and variants) |
| Score de Prédiction TxGNN | 0.9942 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 15 sur 15) |
| Nombre d'AMM | 15 (valides : 15) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la mirtazapine est un antidépresseur dont l'efficacité dans la dépression a été établie. Toutefois, les données compilées pour ce rapport ne permettent de relier ce mécanisme à aucune voie biologique du syndrome d'Ohdo.

Le syndrome d'Ohdo est une maladie génétique rare (liée à KAT6B), associant notamment un blépharophimosis et une déficience intellectuelle. Aucun lien pharmacologique connu ne le rattache à l'activité de la mirtazapine. La similarité avec l'indication d'origine (dépression, anxiété) n'a pas pu être évaluée.

Le score élevé (0,9942) doit donc être considéré uniquement comme un signal générateur d'hypothèses. Deux autres prédictions de même nature figurent dans les données : la forme « blépharophimosis - déficience intellectuelle, type Ohdo » (0,9911), très probablement non indépendante de la première, son score issu du modèle TxGNN (apprentissage profond) pouvant refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique, et le torticolis paroxystique bénin du nourrisson (0,9911), affection pédiatrique spontanément résolutive pour laquelle le rapport bénéfice/risque d'un antidépresseur sédatif paraît faible.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 15 AMM recensées sont annulées. Le texte d'indication approuvée n'est pas renseigné. Cinq AMM sont présentées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69084246 | Mirtazapine Arrow Génériques 15 mg | Comprimé pelliculé sécable | Active |
| 68022786 | Mirtazapine Teva 15 mg | Comprimé pelliculé | Active |
| 66402996 | Mirtazapine Biogaran 15 mg | Comprimé orodispersible | Active |
| 62485126 | Mirtazapine Arrow 15 mg | Comprimé orodispersible | Active |
| 65124914 | Norset 15 mg (Organon France) | Comprimé pelliculé | Active |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, épilepsie, trouble bipolaire de type maniaque, maladie hépatique, maladie de la vésicule biliaire, neutropénie, agranulocytose, hypotension, hypertriglycéridémie, obésité (y compris monogénique), accident vasculaire cérébral et troubles cérébrovasculaires, infarctus cérébral, infarctus du myocarde, thrombose coronarienne, hémoglobinopathie, insuffisance rénale, syndrome sérotoninergique, akathisie d'origine médicamenteuse.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles listées, les interactions de niveau **majeur** concernent le bupropion, la lorcasérine, le dolasétron et le palonosétron. Des interactions de niveau modéré sont notées, entre autres, avec la famotidine, le lopéramide, l'aprépitant, la morphine, la dexaméthasone, la cimétidine, la clarithromycine et la lévofloxacine.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique démontré. De plus, les 15 AMM françaises sont annulées, et les données de sécurité officielles sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice (mises en garde et contre-indications) auprès de l'ANSM, étape bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action pour évaluer un éventuel lien avec le syndrome d'Ohdo
- Réaliser une revue de la littérature et des registres d'essais afin de vérifier l'existence de toute preuve préclinique ou clinique
- Clarifier le statut réglementaire en France (AMM annulées) et la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

