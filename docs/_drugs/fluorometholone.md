---
layout: default
title: Fluorometholone
parent: Prédiction du modèle uniquement (L5)
nav_order: 338
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis"]
description: "Fluorometholone : nouvelle indication prédite, Postinfectious vasculitis (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Fluorometholone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Fluorometholone: Postinfectious vasculitis
{: .text-alpha }

## Résumé en Une Phrase

Le fluorométholone est un corticoïde topique ophtalmique, initialement utilisé pour traiter les inflammations du segment antérieur de l'œil (uvéite, iridocyclite, conjonctivites allergiques, etc.).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **postinfectious vasculitis** (vascularite post-infectieuse, première prédiction du classement), mais cette piste n'est étayée par **aucun essai clinique** ni **aucune publication**. La piste la plus plausible sur le plan biologique est la **kératoconjonctivite ponctuée épithéliale**, pour laquelle seules **2 publications** de contexte indirect sont disponibles.

> Remarque : le titre reprend l'indication prédite la plus plausible (kératoconjonctivite ponctuée épithéliale, rang 6) plutôt que la première du classement, car cette dernière est mécanistiquement peu crédible pour une forme ophtalmique topique. La section « Aperçu Rapide » détaille les deux.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite (rang 1 TxGNN) | Postinfectious vasculitis |
| Nouvelle Indication Prédite la plus plausible (rang 6) | Postinfectious vasculitis |
| Score de Prédiction TxGNN | 0.9991 |
| Niveau de Preuve | L5 (rang 1) ; L4 (rang 6) |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold (rang 1) ; Research Question (rang 6) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Fluorometholone (traduction non officielle) : « Les corticostéroïdes inhibent la réponse inflammatoire à divers agents déclenchants et retardent ou ralentissent probablement la cicatrisation. Ils inhibent l'œdème, le dépôt de fibrine, la dilatation capillaire, la migration leucocytaire, la prolifération capillaire, la prolifération des fibroblastes, le dépôt de collagène et la formation de cicatrices associés à l'inflammation. […] Dans des études cliniques menées chez des sujets répondeurs aux stéroïdes documentés, la fluorométholone a présenté un délai moyen significativement plus long que le phosphate de dexaméthasone avant de provoquer une élévation de la pression intraoculaire ; cependant, chez un faible pourcentage d'individus, une élévation significative de la pression intraoculaire est survenue en moins d'une semaine. » Texte original en anglais : "Corticosteroids inhibit the inflammatory response to a variety of inciting agents and probably delay or slow healing. They inhibit the edema, fibrin deposition, capillary dilation, leukocyte migration, capillary proliferation, fibroblast proliferation, deposition of collagen, and scar formation associated with inflammation. […] In clinical studies of documented steroid-responders, fluorometholone demonstrated a significantly longer average time to produce a rise in intraocular pressure than dexamethasone phosphate; however, in a small percentage of individuals, a significant rise in intraocular pressure occurred within one week." ([DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01), version du 2026-08-12 ; consulté le 2026-11-19). Sur la base des informations connues, le fluorométholone est un corticoïde synthétique qui se lie au récepteur des glucocorticoïdes (NR3C1) et exerce un effet anti-inflammatoire et immunosuppresseur. Son efficacité dans les inflammations oculaires antérieures est reconnue.

Pour la **kératoconjonctivite ponctuée épithéliale**, la proximité avec les indications d'origine est élevée : il s'agit d'une inflammation de la surface oculaire, et les corticoïdes sont utilisés pour les infiltrats sous-épithéliaux et les séquelles inflammatoires des kératoconjonctivites adénovirales (épidémiques) et microsporidiennes. Toutefois, les deux publications retrouvées portent sur la prise en charge des séquelles et sur le suivi par OCT du segment antérieur : il s'agit d'un contexte indirect, non de données d'efficacité propres au fluorométholone. Les corticoïdes dans les kératoconjonctivites infectieuses comportent aussi des risques (excrétion virale prolongée, élévation de la pression intraoculaire, aggravation de l'infection).

Pour la **vascularite post-infectieuse** (rang 1), un mécanisme glucocorticoïde est plausible, la maladie étant à médiation immunitaire. Mais le fluorométholone est un agent ophtalmique topique à exposition systémique limitée : une indication systémique est mal soutenue. Le score TxGNN est le seul élément en faveur de cette prédiction.

Deux autres pistes proches des indications d'origine sont à signaler (niveau L4, sans essai ni publication spécifiques) : l'**iridocyclite induite par le cristallin** (traitement définitif généralement chirurgical, corticoïdes en appoint) et la **crise glaucomato-cyclitique** (syndrome de Posner-Schlossman, uvéite antérieure récidivante avec hypertonie oculaire, pour laquelle la moindre tendance du fluorométholone à élever la PIO est un avantage théorique).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Pour la kératoconjonctivite ponctuée épithéliale :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Revue | Indian J Ophthalmol | Caractérisation des séquelles de la kératoconjonctivite microsporidienne et de sa prise en charge |
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Revue | J Curr Ophthalmol | Rôle de l'OCT du segment antérieur dans le suivi de la kératoconjonctivite épidémique et effet des corticoïdes topiques sur son évolution |

Aucune littérature associée disponible pour les autres indications prédites.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68728453 | FLUCON, collyre | Collyre | IMMEDICA PHARMA (SUEDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : kératite à herpès simplex, glaucome à angle ouvert, hypertonie oculaire, infections oculaires (infectieuses, fongiques, virales, tuberculose oculaire), conjonctivite, pigmentation cornéenne, diabète et acidocétose diabétique, porphyries, déficit en G6PD, glycogénose, cystinurie, galactosémie.
- **Interactions médicamenteuses** : 11 interactions recensées (doxycycline, salbutamol, ciclosporine, paracétamol, digoxine, brimonidine, céphalexine, acide alendronique, aciclovir, diazépam, fénofibrate), toutes de niveau de gravité non précisé. Le récepteur des glucocorticoïdes est par ailleurs la cible pharmacologique identifiée.
- **Points d'attention propres aux nouvelles indications** : risque d'élévation de la PIO et d'aggravation d'infection dans les kératoconjonctivites infectieuses ; risque de réactivation parasitaire sous immunosuppression dans la cardiomyopathie de Chagas.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold** (vascularite post-infectieuse et autres prédictions systémiques ou non spécifiques) ; **Research Question** pour la kératoconjonctivite ponctuée épithéliale, l'iridocyclite induite par le cristallin et la crise glaucomato-cyclitique.

**Justification :**
- Les prédictions de rang 1 à 5 et 7 à 8 reposent uniquement sur le score du modèle, sans essai ni publication, et plusieurs sont peu crédibles pour un collyre à faible exposition systémique. Les pistes ophtalmiques sont plus plausibles mais ne disposent que de preuves indirectes.

<!-- review:begin fr-lic-20261106-fluorometholone-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les pistes ophtalmiques sont plus plausibles mais ne disposent que de preuves indirectes. De plus, l'unique AMM française est annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-fluorometholone-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications officielles issues de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études spécifiques au fluorométholone dans la kératoconjonctivite (essais ou séries comparatives)
- Évaluation de la compatibilité de voie d'administration et de formulation pour chaque indication envisagée
- Clarification du statut réglementaire et de la disponibilité du produit en France

<!-- review:begin fr-lic-20261106-fluorometholone-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire (AMM annulée) et de la disponibilité du produit en France » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-fluorometholone-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, l'unique AMM française est annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

