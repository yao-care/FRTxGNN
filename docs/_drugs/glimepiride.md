---
layout: default
title: Glimepiride
parent: Prédiction du modèle uniquement (L5)
nav_order: 365
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "glimepiride"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
description: "Glimepiride : nouvelle indication prédite, Syndrome de la personne raide classique (classic stiff person syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locale"
---

# Glimepiride
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

## Glimepiride: Syndrome de la personne raide classique (classic stiff person syndrome)
{: .text-alpha }

## Résumé en Une Phrase

Le glimépiride est un sulfamide hypoglycémiant, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la personne raide classique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome de la personne raide classique (classic stiff person syndrome) |
| Score de Prédiction TxGNN | 0.9975 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Glimepiride (traduction non officielle) : « Le glimépiride diminue la glycémie principalement en stimulant la libération d'insuline par les cellules bêta du pancréas. Les sulfonylurées se lient au récepteur des sulfonylurées situé dans la membrane plasmique des cellules bêta du pancréas, ce qui entraîne la fermeture du canal potassique sensible à l'ATP et stimule ainsi la libération d'insuline. » Texte original en anglais : "Glimepiride primarily lowers blood glucose by stimulating the release of insulin from pancreatic beta cells. Sulfonylureas bind to the sulfonylurea receptor in the pancreatic beta-cell plasma membrane, leading to closure of the ATP-sensitive potassium channel, thereby stimulating the release of insulin." ([DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa), version du 2024-08-20 ; consulté le 2026-11-19). Sur la base des connaissances générales, le glimépiride est un sulfamide hypoglycémiant qui bloque les canaux potassiques ATP-dépendants (K-ATP) des cellules bêta pancréatiques et stimule ainsi la sécrétion d'insuline. Son efficacité dans le diabète de type 2 est établie.

Le syndrome de la personne raide est une maladie auto-immune liée aux anticorps anti-GAD65, avec une altération de la signalisation GABAergique. **Aucun lien mécanistique n'est établi** avec le blocage des canaux K-ATP. Le seul rapprochement plausible est la fréquente association du syndrome avec le diabète de type 1 (auto-immunité GAD commune), ce qui ne justifie pas un rôle thérapeutique du glimépiride.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les cinq premières sont listées ci-dessous ; le texte d'indication approuvée n'est pas renseigné.

<!-- review:begin fr-lic-20261106-glimepiride-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 20 AMM recensées sont annulées. Les cinq premières sont listées ci-dessous ; le texte d'indication approuvée n'est pas renseigné. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-glimepiride-1 -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67054585 | Glimépiride Arrow Génériques 2 mg | Comprimé sécable | Active |
| 67447122 | Glimépiride Evolugen 3 mg | Comprimé | Active |
| 63422748 | Glimépiride Arrow Génériques 3 mg | Comprimé sécable | Active |
| 65604468 | Glimépiride Zentiva 2 mg | Comprimé | Active |
| 66017203 | Glimépiride EG 2 mg | Comprimé | Active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, déficits hypophysaires (dont hypopituitarisme et syndrome de Sheehan), hypogonadisme hypogonadotrope (dont syndrome de Kallmann), déficit en hormone de croissance, ostéoporose (dont post-ménopausique), maladie du thymus et maladies infectieuses.
- **Interactions médicamenteuses** : 599 interactions recensées. Parmi les exemples, la plupart sont de niveau modéré : phénylephrine, acébutolol, acétazolamide, famotidine, ranitidine, acitrétine, formotérol, pseudoéphédrine, kétorolac, épinéphrine, ibuprofène, éthinylestradiol, hydrocortisone, albiglutide, salbutamol, éthanol, nitazoxanide et hydrochlorothiazide. Les corticoïdes topiques (hydrocortisone, alclométasone) sont de niveau mineur.

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'est identifié.

<!-- review:begin fr-lic-20261106-glimepiride-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'est identifié. De plus, toutes les AMM françaises du glimépiride sont annulées et les données de sécurité de la notice sont manquantes, ce qui empêche l'étape de dépistage de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-glimepiride-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Mener une recherche bibliographique et d'essais ciblée sur le glimépiride dans le syndrome de la personne raide ; à défaut de signal, ne pas poursuivre.
- Clarifier la situation réglementaire en France (la plupart des AMM sont actives ; certaines sont abrogées ou archivées) et la compatibilité des voies d'administration.

<!-- review:begin fr-lic-20261115-glimepiride-1 -->

> **Correction de vérification (2026-11-15)**: Texte initial : « Clarifier la situation réglementaire en France (AMM annulées) » D’après la BDPM complète (CIS_bdpm et CIS_COMPO_bdpm, 2026-11-15), les spécialités contenant GLIMÉPIRIDE comptent 51 AMM, dont 48 actives et 3 abrogées ou archivées. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt).

<!-- review:end fr-lic-20261115-glimepiride-1 -->

**Autres prédictions du modèle (toutes de niveau L5, décision Hold) :** syndrome du membre raide focal, opsismodysplasie, syndrome de dysfonctionnement répondant à la thiamine, lipodystrophie localisée induite par médicament, lipodystrophie centrifuge, lipoatrophie localisée induite par pression, lipodystrophie localisée idiopathique et agénésie pancréatique. Pour l'agénésie pancréatique, le mécanisme est même contradictoire : sans cellules bêta fonctionnelles, un sulfamide hypoglycémiant ne peut être efficace. Seule une publication non pertinente a été retrouvée pour cette dernière.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 20 AMM recensées sont annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « De plus, toutes les AMM françaises du glimépiride sont annulées et les données de sécurité de la notice sont manquantes, ce qui empêche l'ét » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-15 | « Clarifier la situation réglementaire en France (AM » → « Clarifier la situation réglementaire en France (la » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Glimepiride 3 Mg (glimepiride) prescribing information, Lifsa Drugs LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51157849-7990-4a8b-ae50-eda1baf93cfa) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

