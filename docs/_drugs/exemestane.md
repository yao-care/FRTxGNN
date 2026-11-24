---
layout: default
title: Exemestane
parent: Prédiction du modèle uniquement (L5)
nav_order: 313
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Exemestane : nouvelle indication prédite, Déficience en antithrombine de type 2 (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "exemestane"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura"]
---

# Exemestane
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Exémestane : Du Cancer du Sein à la Déficience en Antithrombine de Type 2
{: .text-alpha }

## Résumé en Une Phrase

L'exémestane est un inhibiteur stéroïdien irréversible de l'aromatase, qui réduit les taux d'œstrogènes. Les données compilées pour ce rapport ne précisent pas d'indication originale dans les AMM françaises.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **déficience en antithrombine de type 2**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Déficience en antithrombine de type 2 |
| Score de Prédiction TxGNN | 0,9983 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 18 sur 19) |
| Nombre d'AMM | 19 (valides : 18) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Exemestane (traduction non officielle) : « La croissance des cellules du cancer du sein peut être estrogéno-dépendante. L'aromatase est la principale enzyme qui convertit les androgènes en estrogènes, tant chez la femme préménopausée que chez la femme ménopausée. […] L'exémestane est un inactivateur stéroïdien irréversible de l'aromatase, structurellement apparenté au substrat naturel, l'androstènedione. » Texte original en anglais : "Breast cancer cell growth may be estrogen-dependent. Aromatase is the principal enzyme that converts androgens to estrogens both in pre- and postmenopausal women. […] Exemestane is an irreversible, steroidal aromatase inactivator, structurally related to the natural substrate androstenedione." ([DailyMed: Aromasin (exemestane) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cf066b7a-032a-416c-8d40-15ba581423e3), version du 2025-12-24 ; consulté le 2026-11-19). D'après les connaissances générales, l'exémestane est un inhibiteur stéroïdien irréversible de l'aromatase : il bloque la conversion des androgènes en œstrogènes et abaisse ainsi les taux d'œstradiol.

La déficience en antithrombine de type 2 est un trouble héréditaire de la coagulation, lié à des variants du gène SERPINC1. **Aucun lien mécanistique n'a été identifié** : l'abaissement des œstrogènes n'est pas connu pour corriger la fonction de l'antithrombine. Le score élevé (0,9983) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Les autres prédictions du modèle se situent dans la même zone (coagulation et thrombophilie) ou concernent des pathologies sans lien démontré :

| Rang | Maladie prédite | Score | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Aménorrhée | 0,9982 | L4 | Littérature indirecte (l'aménorrhée est un état lié au traitement du cancer du sein, pas une cible thérapeutique) |
| 3 | Excès de facteur V avec thrombose spontanée | 0,9982 | L5 | Aucun rationnel mécanistique |
| 4 | Déficit en cofacteur II de l'héparine | 0,9982 | L5 | Aucun lien identifié |
| 5 | Thrombophilie | 0,9967 | L5 | Les inhibiteurs de l'aromatase comportent plutôt un risque thromboembolique |
| 6 | Migraine | 0,9902 | L5 | Lien hormonal hypothétique, sens de l'effet incertain |
| 7 | Migraine avec aura du tronc cérébral | 0,9901 | L5 | Spéculatif, sans données |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la déficience en antithrombine de type 2.

À titre indicatif, 5 publications ont été retrouvées pour la 2ᵉ prédiction (aménorrhée). Elles sont indirectes : l'aménorrhée y est un contexte ou un critère de suivi du cancer du sein, et non une maladie traitée par l'exémestane.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohorte | Annals of Oncology | Récupération de la fonction ovarienne chez des patientes avec aménorrhée induite par la chimiothérapie, passées du tamoxifène à l'exémestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Revue | Oncology (Williston Park) | Rôle de la suppression ovarienne chez les femmes préménopausées avec cancer du sein précoce RH+ |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Revue | Journal of Clinical Oncology | Nécessité du suivi de l'œstradiol sous suppression ovarienne dans le cancer du sein |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Revue | Recenti Progressi in Medicina | Place des analogues de la LHRH dans le cancer du sein chez les patientes préménopausées |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Revue | Klinicka Onkologie | Inhibiteurs de l'aromatase chez les femmes ménopausées avec cancer du sein et gestion des effets indésirables |

---

## Informations de Marché en France

18 AMM sur 19 sont valides. Le texte d'indication n'est pas renseigné dans les données compilées. Principales AMM (5 sur 19) :

<!-- review:begin fr-lic-20261124-exemestane-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 16 AMM sur 16 sont valides. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-exemestane-1 -->

<!-- review:begin fr-lic-20261124-exemestane-2 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Principales AMM (5 sur 16) : » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-exemestane-2 -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66922032 | EXEMESTANE TEVA 25 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 69225138 | AROMASINE 25 mg (Pfizer) | Comprimé enrobé | Non renseignée (AMM active) |
| 64144682 | EXEMESTANE ZENTIVA 25 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 69233035 | AROMASINE 25 mg (Difarmed) | Comprimé enrobé | Non renseignée (AMM active) |
| 61396272 | EXEMESTANE ZYDUS FRANCE 25 mg | Comprimé enrobé | Non renseignée (AMM active) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Hormonothérapie (inhibiteur stéroïdien de l'aromatase), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible (pas de donnée de toxicité compilée ; à vérifier dans la notice) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 203 interactions recensées. Les plus notables, de niveau modéré : **dexaméthasone** et **troglitazone**. Les autres interactions listées (pantoprazole, morphine, metformine, oméprazole, lansoprazole, simvastatine, chlorure de potassium, ranitidine, ondansétron, métronidazole, famotidine, acide acétylsalicylique, sucralfate, rosiglitazone, lactulose, rosuvastatine, orlistat, rabéprazole) ont un niveau de gravité non précisé.
- **Point d'attention thromboembolique** : les inhibiteurs de l'aromatase s'accompagnent d'une alerte thromboembolique ; ce point est particulièrement critique pour les prédictions touchant la coagulation et la thrombophilie.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5), sans essai clinique, sans publication et sans lien mécanistique plausible.

<!-- review:begin fr-lic-20261106-exemestane-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le score du modèle (L5), sans essai clinique, sans publication et sans lien mécanistique plausible. Les AMM françaises sont toutes annulées, et le profil de risque thromboembolique des inhibiteurs de l'aromatase va à l'encontre d'un usage dans les troubles de la coagulation. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 16 AMM pour ce médicament, dont 16 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-exemestane-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) détaillées
- Notice officielle (mises en garde et contre-indications), indispensable pour le dépistage de sécurité
- Indication originale d'après les textes d'AMM
- Preuves précliniques ou mécanistiques reliant l'inhibition de l'aromatase à la fonction de l'antithrombine
- Évaluation de sécurité thromboembolique avant toute poursuite

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les AMM françaises sont toutes annulées, et le profil de risque thromboembolique des inhibiteurs de l'aromatase va à l'encontre d'un usage d » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Aromasin (exemestane) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cf066b7a-032a-416c-8d40-15ba581423e3) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

