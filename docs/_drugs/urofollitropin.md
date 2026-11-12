---
layout: default
title: Urofollitropin
parent: Prédiction du modèle uniquement (L5)
nav_order: 799
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Urofollitropin : nouvelle indication prédite, Trouble migraineux (migraine disorder) (niveau de preuve L5). Indication d'origine : Non renseignee dans les AMM disponibles (usage connu : stimulation o…"
monitor_inn: "urofollitropin"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "His bundle tachycardia", "restless legs syndrome", "obsolete neurogenic bladder (disease)", "multifocal atrial tachycardia (disease)", "postural orthostatic tachycardia syndrome", "Raynaud disease"]
---

# Urofollitropin
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

## Urofollitropine : De la stimulation ovarienne au trouble migraineux
{: .text-alpha }

## Resume en Une Phrase

L'urofollitropine est une preparation de FSH humaine purifiee (derivee de la menotropine), utilisee pour la stimulation ovarienne.
Le modele TxGNN predit qu'elle pourrait etre efficace pour le **trouble migraineux**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prediction purement algorithmique.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignee dans les AMM disponibles (usage connu : stimulation ovarienne) |
| Nouvelle Indication Predite | Trouble migraineux (migraine disorder) |
| Score de Prediction TxGNN | 0,9985 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'urofollitropine est une FSH purifiee d'origine urinaire, utilisee pour stimuler la croissance folliculaire lors des traitements de l'infertilite. Son efficacite dans cette indication est etablie, mais aucune action antimigraineuse n'est connue pour la FSH.

Un lien hormonal est concevable : les fluctuations des oestrogenes sont associees a la migraine menstruelle. Cette hypothese reste toutefois speculative. Le score eleve du modele TxGNN (deep learning) (0,9985) peut refleter des similarites apprises par le modele entre maladies proches, non une preuve biologique ou clinique.

Les autres predictions du classement (migraine avec aura du tronc cerebral, syndrome de la queue de cheval, tachycardie hisienne, syndrome des jambes sans repos, syndrome de tachycardie orthostatique posturale, maladie de Raynaud, etc.) sont egalement sans soutien clinique. Plusieurs sont probablement des artefacts du modele TxGNN (deep learning), qui peut refleter des similarites apprises entre maladies proches : doublons du signal migraineux, terme ontologique obsolete. Dans le cas de la maladie de Raynaud, le risque thromboembolique des gonadotrophines plaide plutot contre l'usage.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 61166549 | FOSTIMONKIT 75 UI | Poudre et solvant pour solution injectable | Non renseignee (AMM active) |
| 62712912 | FOSTIMONKIT 225 UI | Poudre et solvant pour solution injectable | Non renseignee (AMM active) |
| 69325035 | FOSTIMONKIT 300 UI | Poudre et solvant pour solution injectable | Non renseignee (AMM active) |
| 60549797 | FOSTIMONKIT 150 UI | Poudre et solvant pour solution injectable | Non renseignee (AMM active) |

## Considerations de Securite

- **Interactions Medicamenteuses** : 1 interaction identifiee, de niveau modere, avec le **ganirelix** (source : DDInter).

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction repose uniquement sur le modele (niveau L5), sans essai clinique, sans publication et sans lien mecanistique etabli.

<!-- review:begin fr-lic-20261106-urofollitropin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prediction repose uniquement sur le modele (niveau L5), sans essai clinique, sans publication et sans lien mecanistique etabli. De plus, toutes les AMM francaises sont annulees. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 4 AMM pour ce médicament, dont 4 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-urofollitropin-1 -->

**Pour avancer, les elements suivants sont necessaires :**
- Donnees sur le mecanisme d'action de l'urofollitropine, afin d'evaluer un eventuel lien avec la migraine (notamment menstruelle)
- Mises en garde et contre-indications issues de la notice ANSM, indispensables avant tout depistage de securite
- Revue de la litterature sur les gonadotrophines, les hormones sexuelles et la migraine
- Evaluation de la compatibilite des voies d'administration et de la similarite avec l'indication d'origine
- Clarification du statut reglementaire et de l'indication d'origine

<!-- review:begin fr-lic-20261106-urofollitropin-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut reglementaire (AMM annulees) et de l'indication d'origine » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 4 AMM pour ce médicament, dont 4 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-urofollitropin-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, toutes les AMM francaises sont annulees » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulees) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

