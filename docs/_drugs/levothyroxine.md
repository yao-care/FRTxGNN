---
layout: default
title: Levothyroxine
parent: Prédiction du modèle uniquement (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levothyroxine : nouvelle indication prédite, Goitre endémique (niveau de preuve L5). Indication d'origine : Hypothyroïdie"
monitor_inn: "levothyroxine"
predicted_indications: ["endemic goiter", "renal hypodysplasia/aplasia", "nodular goiter (disease)", "bilateral renal agenesis", "nontoxic goiter", "lingual goiter", "substernal goiter", "dyshormonogenic goiter", "Potter sequence", "Carney complex"]
---

# Levothyroxine
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

# Lévothyroxine : De l'hypothyroïdie au goitre endémique

## Résumé en Une Phrase

La lévothyroxine est une hormone thyroïdienne de synthèse, initialement utilisée pour traiter l'hypothyroïdie et d'autres maladies de la thyroïde.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **goitre endémique**, avec **20 publications** (aucun essai clinique enregistré) soutenant actuellement cette direction.
À noter : plusieurs indications voisines (goitre nodulaire, goitre non toxique) disposent de preuves plus solides, présentées plus bas.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypothyroïdie (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Goitre endémique |
| Score de Prédiction TxGNN | 99,81 % |
| Niveau de Preuve | L5 (aucun essai clinique ; publications de type pré-évaluation, dont plusieurs études comparatives non classées) |
| Statut de Marché en France | Uniquement annulées |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la lévothyroxine est la forme synthétique de la thyroxine (T4). Son efficacité dans l'hypothyroïdie est établie, et elle freine la sécrétion de TSH par l'hypophyse.

Le goitre endémique est lié à une carence en iode qui stimule la thyroïde via la TSH. En réduisant la TSH, la lévothyroxine pourrait limiter la croissance du tissu thyroïdien. La relation avec l'indication originale est donc étroite : il s'agit d'une même glande et d'un même axe hormonal.

La littérature indique toutefois que la lévothyroxine seule laisse persister la carence en iode intrathyroïdienne et que les rechutes sont fréquentes ; l'iode, seul ou associé, est souvent privilégié (PMID 8147031). Le score élevé du modèle est donc plausible, mais le bénéfice thérapeutique reste nuancé.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour le goitre endémique.

À titre d'information, deux essais concernent l'indication voisine du **goitre nodulaire** (rang 3) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00277589](https://clinicaltrials.gov/study/NCT00277589) | Phase 4 | Terminé | 1024 | Traitement adapté à la TSH, randomisé, en aveugle pour l'observateur, contrôlé par placebo ; critère principal : variation du volume total des nodules |
| [NCT00941551](https://clinicaltrials.gov/study/NCT00941551) | N/A | Terminé | 150 | Lobectomie thyroïdienne avec ou sans lévothyroxine postopératoire ; récidive nodulaire à 5 ans (résultats non fournis) |

---

## Preuves de la Littérature

Sélection pour le goitre endémique :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2515973](https://pubmed.ncbi.nlm.nih.gov/2515973/) | 1989 | Essai multicentrique randomisé | Eur J Clin Invest | 166 patients : lévothyroxine 150 µg, iode 400 µg ou association, sur 12 mois |
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Étude multicentrique | Dtsch Med Wochenschr | 74 patients : lévothyroxine seule vs lévothyroxine + iodure pendant 6 mois |
| [1789063](https://pubmed.ncbi.nlm.nih.gov/1789063/) | 1991 | Étude prospective en double aveugle | Acta Endocrinol | Concentration thyroïdienne d'iode sous iode seul vs iode + lévothyroxine |
| [8676600](https://pubmed.ncbi.nlm.nih.gov/8676600/) | 1996 | Étude comparative | Klin Padiatr | 106 adolescents : iode seul vs iode + lévothyroxine, avec paramètres lipidiques |
| [9011485](https://pubmed.ncbi.nlm.nih.gov/9011485/) | 1996 | Étude comparative | Dtsch Med Wochenschr | Iodure vs lévothyroxine chez des patients d'âge moyen et âgés |
| [7900936](https://pubmed.ncbi.nlm.nih.gov/7900936/) | 1993 | Étude clinique | Clin Endocrinol | Effet de la lévothyroxine ou de l'iode sur le volume thyroïdien et les immunoglobulines stimulant la croissance |
| [11256036](https://pubmed.ncbi.nlm.nih.gov/11256036/) | 2001 | Étude comparative | Dtsch Med Wochenschr | Deux doses d'association lévothyroxine-iodure dans le goitre euthyroïdien diffus |
| [9711053](https://pubmed.ncbi.nlm.nih.gov/9711053/) | 1998 | Étude de biodisponibilité en double aveugle | Med Klin | Bioéquivalence de l'association lévothyroxine-iode vs lévothyroxine seule |
| [24393641](https://pubmed.ncbi.nlm.nih.gov/24393641/) | 1998 | Étude longitudinale | Asia Pac J Clin Nutr | Lévothyroxine 100 µg/jour chez des populations autochtones en zone endémique |
| [8147031](https://pubmed.ncbi.nlm.nih.gov/8147031/) | 1993 | Revue | Z Gesamte Inn Med | L'iode devrait toujours faire partie du traitement ; la lévothyroxine seule laisse persister la carence intrathyroïdienne |

Pour le goitre non toxique (rang 5), un essai randomisé compare la lévothyroxine à l'iode radioactif ([PMID 11238476](https://pubmed.ncbi.nlm.nih.gov/11238476/), 2001, J Clin Endocrinol Metab, 64 patients). Son niveau de preuve reste provisoire, faute de vérification des détails de conception.

---

## Informations de Marché en France

Les 20 AMM sont annulées ; le texte des indications approuvées n'est pas renseigné. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66426100 | LEVOTHYROX 112 microgrammes | Comprimé sécable | Non renseignée |
| 65706277 | L-THYROXIN HENNING 137 microgrammes | Comprimé sécable | Non renseignée |
| 60254754 | TSOLUDOSE 150 microgrammes | Solution buvable | Non renseignée |
| 61296560 | TCAPS 137 microgrammes | Capsule molle | Non renseignée |
| 64952190 | THYROFIX 125 microgrammes | Comprimé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : hypertension, hypopituitarisme et déficits hypophysaires, syndrome de Kallmann, ostéoporose (dont post-ménopausique), diabète et acidocétose diabétique, maladie coronarienne, infarctus du myocarde, maladies du thymus.
- **Risques liés à la suppression de la TSH** (selon la littérature) : hyperthyroïdie subclinique iatrogène, fibrillation auriculaire, perte osseuse.
- **Interactions médicamenteuses** : 666 interactions recensées, surtout de niveau modéré, notamment :
  - antidiabétiques (metformine, pioglitazone, canagliflozine, dapagliflozine, empagliflozine, alogliptine, acarbose, chlorpropamide, albiglutide, dulaglutide) ;
  - inhibiteurs de la pompe à protons (oméprazole, rabéprazole, dexlansoprazole) ;
  - sels de calcium et de magnésium (phosphate et acétate de calcium, oxyde de magnésium) ;
  - sympathomimétiques (épinéphrine, isométhepténe, diéthylpropion) ;
  - cimétidine (mineure).

Veuillez consulter la notice pour les mises en garde officielles : les données de notice de l'ANSM n'ont pas pu être exploitées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le goitre endémique, aucun essai clinique n'est enregistré et les publications sont anciennes (1987-2004), souvent comparatives, avec des résultats en faveur de l'iode ou de l'association plutôt que de la lévothyroxine seule. Le statut réglementaire (toutes les AMM annulées) et l'absence de données de notice sur la sécurité empêchent aussi une progression.
- Parmi les autres prédictions, le **goitre nodulaire** et le **goitre non toxique** sont classés L1 avec « Proceed with Guardrails », mais avec réserves : le grade L1 repose sur un essai de Phase 4 (non Phase 3) et sur un essai identifié par son seul titre, et le bénéfice est modeste face aux risques. Les prédictions rénales (hypodysplasie, agénésie, séquence de Potter) et le complexe de Carney semblent des artefacts du graphe, sans aucune preuve.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications), lacune bloquante pour le dépistage de sécurité.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Clarifier la situation réglementaire en France (AMM toutes annulées) et vérifier si des spécialités équivalentes restent commercialisées.
- Faire valider par un évaluateur le niveau de preuve des essais randomisés (phase, conception, critères) et classer les publications.
- Définir un plan de surveillance (TSH, fonction cardiaque, densité osseuse) pour tout traitement suppressif.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

