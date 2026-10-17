---
layout: default
title: Octreotide
parent: Prédiction du modèle uniquement (L5)
nav_order: 552
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Octreotide : nouvelle indication prédite, Kératose inverse folliculaire vulvaire (niveau de preuve L5). Indication d'origine : Acromégalie, hyperpituitarisme, syndrome carcinoïde"
monitor_inn: "octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
---

# Octreotide
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

# Octréotide : De l'acromégalie à la kératose inverse folliculaire vulvaire

## Résumé en Une Phrase

L'octréotide est un analogue de la somatostatine, initialement utilisé pour traiter l'acromégalie, l'hyperpituitarisme et le syndrome carcinoïde.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératose inverse folliculaire vulvaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acromégalie, hyperpituitarisme, syndrome carcinoïde (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Kératose inverse folliculaire vulvaire |
| Score de Prédiction TxGNN | 99,58 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 18 (0 valide, 18 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'octréotide est un analogue de la somatostatine qui agit sur les récepteurs de la somatostatine (SSTR2/SSTR5) et freine la sécrétion de l'hormone de croissance (GH), de l'IGF-1 et d'autres hormones. Cette action explique son usage dans l'acromégalie et les tumeurs neuroendocrines sécrétantes.

Aucun lien pharmacologique plausible n'est établi entre ce mécanisme et une lésion épithéliale bénigne telle que la kératose inverse folliculaire. Une influence des voies de la somatostatine ou de l'IGF-1 sur la prolifération des kératinocytes peut être évoquée, mais elle reste spéculative. Le score élevé du modèle reflète probablement une proximité dans le réseau du graphe de connaissances plutôt qu'une relation pharmacologique réelle.

Une seconde prédiction, la **kératose séborrhéique** (score 99,55 %), présente les mêmes limites. Elle est étroitement apparentée à la kératose inverse folliculaire, et les deux prédictions ne sont vraisemblablement pas indépendantes. Cette affection étant bénigne et généralement traitée par de simples gestes locaux, le rapport bénéfice/risque d'un peptide systémique est défavorable sans données à l'appui.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 18 AMM recensées sont toutes annulées ; aucune n'est valide actuellement. Cinq exemples :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69161760 | OCTREOTIDE HOSPIRA 100 microgrammes/1 mL | Solution injectable | Non renseignée |
| 61707595 | SANDOSTATINE 500 microgrammes/1 mL | Solution injectable ou pour perfusion | Non renseignée |
| 61881699 | SANDOSTATINE L.P. 30 mg | Poudre et solvant pour suspension injectable à libération prolongée | Non renseignée |
| 65490897 | SIROCTID 0,05 mg/ml | Solution injectable ou à diluer pour perfusion en seringue préremplie | Non renseignée |
| 68949551 | SANDOSTATINE 50 microgrammes/1 mL | Solution injectable ou pour perfusion | Non renseignée |

## Cytotoxicité

Cette section est omise : l'octréotide n'est pas un médicament antinéoplasique cytotoxique. C'est un analogue peptidique de la somatostatine.

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications signalées par le graphe de connaissances** (et non issues du texte de la notice) : hyperglycémie, diabète sucré, acidocétose diabétique, hypoglycémie, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), cirrhose et maladie hépatique, maladie de la vésicule biliaire (lithiase cholédocienne, cholécystolithiase), iléus et occlusion intestinale, arrêt cardiaque soudain, maladie de la conduction cardiaque, insuffisance rénale et urémie, carence en vitamine B12.
- **Interactions médicamenteuses** : 272 interactions recensées. Les 20 premières sont de niveau modéré et concernent surtout les antidiabétiques (insulines, metformine, acarbose, sulfamides hypoglycémiants comme le glimépiride et le chlorpropamide, inhibiteurs du SGLT2 comme la canagliflozine, la dapagliflozine et l'empagliflozine, inhibiteurs de la DPP-4 comme l'alogliptine et la linagliptine, agonistes du GLP-1 comme le sémaglutide, le dulaglutide et l'albiglutide). L'octréotide modifie l'équilibre glycémique, d'où la nécessité d'une surveillance rapprochée de la glycémie en cas d'association.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible avec une lésion cutanée bénigne.
- Toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui bloque le dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (site de l'ANSM).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Mener une revue de la littérature pour détecter tout signal biologique reliant les récepteurs de la somatostatine ou l'IGF-1 aux kératoses.
- Vérifier la compatibilité de la voie d'administration (aujourd'hui uniquement injectable) avec une lésion cutanée bénigne.
- Réévaluer le rapport bénéfice/risque d'un traitement systémique pour une affection bénigne avant toute poursuite.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

