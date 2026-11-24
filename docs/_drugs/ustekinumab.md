---
layout: default
title: Ustekinumab
parent: Preuves élevées (L1-L2)
nav_order: 800
evidence_level: L2
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "ustekinumab"
predicted_indications: ["dermatitis", "neonatal dermatomyositis", "acne keloid", "acrodermatitis chronica atrophicans", "amyopathic dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "pityriasis lichenoides", "acute lichenoid pityriasis"]
description: "Ustekinumab : nouvelle indication prédite, Dermatite (dermatitis) (niveau de preuve L2). En France, AMM dans la BDPM : au moins 20"
---

# Ustekinumab
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

## Ustekinumab: Dermatite (dermatitis)
{: .text-alpha }

## Résumé en Une Phrase

Ustékinumab est un anticorps monoclonal initialement utilisé pour le traitement du rhumatisme psoriasique, du psoriasis et du parapsoriasis.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dermatite**, avec **6 essais cliniques** enregistrés (dont seulement 2 testent directement ustékinumab dans la dermatite atopique) et **aucune publication** disponible actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Dermatite (dermatitis) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ustekinumab (traduction non officielle) : « Les produits à base d'ustékinumab sont des anticorps monoclonaux IgG1κ humains qui se lient de manière spécifique à la sous-unité protéique p40 utilisée à la fois par les cytokines IL-12 et IL-23. L'IL-12 et l'IL-23 sont des cytokines naturelles impliquées dans les réponses inflammatoires et immunitaires, telles que l'activation des cellules tueuses naturelles et la différenciation et l'activation des lymphocytes T CD4+. » Texte original en anglais : "Ustekinumab products are human IgG1κ monoclonal antibodies that bind with specificity to the p40 protein subunit used by both the IL-12 and IL-23 cytokines. IL-12 and IL-23 are naturally occurring cytokines that are involved in inflammatory and immune responses, such as natural killer cell activation and CD4+ T-cell differentiation and activation." ([DailyMed: Selarsdi (ustekinumab-aekn) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=87f75b59-e48b-47c7-a4c0-5fe5965660e7), version du 2026-11-11 ; consulté le 2026-11-19). Selon l'analyse mécanistique disponible, ustékinumab bloque la sous-unité p40 commune à l'IL-12 et à l'IL-23, ce qui inhibe les voies Th1 et Th17. Ces voies sont impliquées dans le psoriasis, indication d'origine du médicament.

Ces mêmes voies contribuent à l'inflammation dans plusieurs sous-types de dermatite, notamment la dermatite atopique chronique. L'adéquation mécanistique reste toutefois **partielle** : la dermatite atopique est surtout dominée par la voie Th2 (IL-4/IL-13), ce qui pourrait expliquer l'efficacité limitée observée dans les essais.

Il convient aussi de noter que le score élevé du modèle TxGNN (apprentissage profond) est en grande partie lié au terme très large et peu spécifique de « dermatite ». Ce score peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique ; il doit donc être interprété avec prudence.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Terminé | 79 | Étude randomisée en double aveugle contre placebo d'ustékinumab (2 doses) chez des adultes japonais atteints de dermatite atopique sévère ; pertinence probable, à vérifier |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Terminé | 32 | Étude pilote randomisée d'ustékinumab dans la dermatite atopique chronique avec réponse sous-optimale aux traitements antérieurs ; petit effectif limitant les conclusions |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Actif, non en recrutement | 45 | Modèle de dermatite de contact avec des biothérapies pour étudier l'inflammation cutanée ; étude mécanistique, rôle précis d'ustékinumab incertain |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Terminé | 676 | Sécukinumab comparé à ustékinumab dans le psoriasis en plaques (CLEAR) ; pas de preuve directe dans la dermatite |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Terminé | 126 | Évaluation du risque cardiovasculaire chez des patients atteints de psoriasis sévère sous biothérapies ; ne porte pas sur l'efficacité dans la dermatite |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Pas encore en recrutement | 10 | Microdispositif cutané pour tester des médicaments in situ (dermatite atopique, psoriasis) ; étude méthodologique sans preuve d'efficacité |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67522169 | STELARA 45 mg, solution injectable | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 61145149 | OTULFI 130 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | FRESENIUS KABI DEUTSCHLAND (ALLEMAGNE) | Active |
| 64226115 | WEZENLA 45 mg, solution injectable en stylo prérempli | Solution injectable | AMGEN TECHNOLOGY (IRELAND) | Active |
| 68430695 | WEZENLA 45 mg, solution injectable | Solution injectable | AMGEN TECHNOLOGY (IRELAND) | Active |
| 65283311 | STELARA 45 mg, solution injectable en seringue préremplie | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 69661655 | STELARA 90 mg, solution injectable en stylo prérempli | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 66170398 | STELARA 90 mg, solution injectable en seringue préremplie | Solution injectable | JANSSEN CILAG INTERNATIONAL NV | Active |
| 60926807 | WEZENLA 90 mg, solution injectable en seringue préremplie | Solution injectable | AMGEN TECHNOLOGY (IRELAND) | Active |
| 62157777 | STEQEYMA 90 mg, solution injectable en seringue préremplie | Solution injectable | CELLTRION HEALTHCARE HUNGARY (HONGRIE) | Active |
| 60611409 | UZPRUVO 130 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | STADA ARZNEIMITTEL AG | Active |
| 66346483 | OTULFI 90 mg, solution injectable en seringue préremplie | Solution injectable | FRESENIUS KABI DEUTSCHLAND (ALLEMAGNE) | Active |
| 63596332 | PYZCHIVA 90 mg, solution injectable en seringue préremplie | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |
| 65536437 | IMULDOSA 90 mg, solution injectable en seringue préremplie | Solution injectable | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 67693597 | YESINTEK 130 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 62800604 | IMULDOSA 45 mg, solution injectable en seringue préremplie | Solution injectable | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 61082122 | WEZENLA 45 mg, solution injectable en seringue préremplie | Solution injectable | AMGEN TECHNOLOGY (IRELAND) | Active |
| 60101438 | PYZCHIVA 45 mg, solution injectable en seringue préremplie | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |
| 64586679 | WEZENLA 90 mg, solution injectable en stylo prérempli | Solution injectable | AMGEN TECHNOLOGY (IRELAND) | Active |
| 62125605 | OTULFI 45 mg, solution injectable en seringue préremplie | Solution injectable | FRESENIUS KABI DEUTSCHLAND (ALLEMAGNE) | Active |
| 62685842 | UZPRUVO 45 mg, solution injectable en seringue préremplie | Solution injectable | STADA ARZNEIMITTEL AG | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

Les AMM recensées (tableau ci-dessus) concernent Stelara et plusieurs biosimilaires : Wezenla, Otulfi, Uzpruvo, Pyzchiva, Imuldosa, Yesintek, Steqeyma.

<!-- review:begin fr-lic-20261106-ustekinumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Au total, 20 AMM sont enregistrées (Stelara et plusieurs biosimilaires : Wezenla, Otulfi, Uzpruvo, Pyzchiva, Imuldosa, Yesintek, Steqeyma), toutes au statut annulé. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ustekinumab-1 -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 333 interactions sont recensées. Les principales, de niveau modéré, concernent les corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisone, prednisolone), la simvastatine, les anticoagulants (apixaban, warfarine, rivaroxaban, dicoumarol) et des radiopharmaceutiques (iobenguane I-131, ibritumomab tiuxétan, tositumomab). Les sels de zinc présentent des interactions mineures.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations. Cette lacune est bloquante pour une évaluation de sécurité complète.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Deux essais de phase 2 testent directement ustékinumab dans la dermatite atopique, mais ils sont de petite taille et l'adéquation mécanistique est partielle (voie Th2 dominante). Le score TxGNN est gonflé par un terme très général et les données de sécurité de la notice manquent.

<!-- review:begin fr-lic-20261106-ustekinumab-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le score TxGNN est gonflé par un terme très général, les AMM françaises sont toutes annulées et les données de sécurité de la notice manquent. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ustekinumab-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats détaillés des essais NCT01945086 et NCT01806662 (efficacité et sécurité)
- Notice de l'ANSM (mises en garde et contre-indications) pour lever la lacune de sécurité bloquante
- Données détaillées sur le mécanisme d'action (DrugBank)
- Précision de la population « dermatite » visée (atopique, de contact, autre)
- Clarification du statut réglementaire actuel en France

<!-- review:begin fr-lic-20261115-ustekinumab-1 -->

> **Correction de vérification (2026-11-15)**: Texte initial : « Clarification du statut réglementaire actuel en France (AMM annulées) » D’après la BDPM complète (CIS_bdpm et CIS_COMPO_bdpm, 2026-11-15), les spécialités contenant USTÉKINUMAB comptent 17 AMM, dont 17 actives ; aucune n’est abrogée ou archivée. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt).

<!-- review:end fr-lic-20261115-ustekinumab-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « toutes au statut annulé » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « les AMM françaises sont toutes annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-15 | « Clarification du statut réglementaire actuel en Fr » → « Clarification du statut réglementaire actuel en Fr » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Selarsdi (ustekinumab-aekn) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=87f75b59-e48b-47c7-a4c0-5fe5965660e7) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

