---
layout: default
title: Lomitapide
parent: Prédiction du modèle uniquement (L5)
nav_order: 456
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "lomitapide"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "platelet storage pool deficiency"]
description: "Lomitapide : nouvelle indication prédite, Marcothrombocytopenia with mitral valve insufficiency (niveau de preuve L5). En France, AMM dans la BDPM : 3 (valides : 3)"
---

# Lomitapide
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

## Lomitapide: Marcothrombocytopenia with mitral valve insufficiency
{: .text-alpha }

## Résumé en Une Phrase

Le lomitapide est un inhibiteur de la protéine de transfert des triglycérides microsomiaux (MTP), initialement utilisé pour traiter l'hypercholestérolémie familiale homozygote.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **macrothrombocytopénie avec insuffisance mitrale**, avec un score très élevé (0,9992).
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Marcothrombocytopenia with mitral valve insufficiency |
| Score de Prédiction TxGNN | 0.9992 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Lomitapide (traduction non officielle) : « JUXTAPID se lie directement à la protéine microsomale de transfert des triglycérides (MTP), située dans la lumière du réticulum endoplasmique, et l'inhibe, empêchant ainsi l'assemblage des lipoprotéines contenant l'apo B dans les entérocytes et les hépatocytes. Cela inhibe la synthèse des chylomicrons et des VLDL. » Texte original en anglais : "JUXTAPID directly binds and inhibits microsomal triglyceride transfer protein (MTP), which resides in the lumen of the endoplasmic reticulum, thereby preventing the assembly of apo B-containing lipoproteins in enterocytes and hepatocytes. This inhibits the synthesis of chylomicrons and VLDL." ([DailyMed: Juxtapid (lomitapide mesylate) prescribing information, Chiesi USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61a0be9d-ee58-43e0-b5cb-141011835081), version du 2026-03-30 ; consulté le 2026-11-19). D'après les connaissances générales, le lomitapide inhibe la MTP. Il réduit ainsi l'assemblage et la sécrétion des lipoprotéines contenant l'apoB (VLDL, chylomicrons), ce qui abaisse le LDL-cholestérol. Son efficacité est établie dans l'hypercholestérolémie familiale homozygote.

**Aucun lien mécanistique plausible** n'a pu être établi entre l'inhibition de la MTP et la physiopathologie plaquettaire ou valvulaire de la maladie prédite. Les autres prédictions de haut rang pour ce médicament appartiennent au même groupe de troubles plaquettaires : thrombopénie héréditaire, maladie des granules denses, thrombasthénie de Glanzmann, déficit du pool de stockage plaquettaire, etc.

La similarité avec l'indication originale n'a pas pu être évaluée. La prédiction doit donc être considérée comme une hypothèse purement computationnelle.

Il s'agit toutefois essentiellement de l'indication d'origine (hypercholestérolémie familiale homozygote), et non d'un véritable repositionnement. Les essais de phase 3 y concernent des populations atteintes d'hypercholestérolémie sévère, et non l'hyperlipoprotéinémie au sens large.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69243759 | LOJUXTA 10 mg, gélule | Gélule | CHIESI FARMACEUTICI | Active |
| 69565055 | LOJUXTA 20 mg, gélule | Gélule | CHIESI FARMACEUTICI | Active |
| 69851117 | LOJUXTA 5 mg, gélule | Gélule | CHIESI FARMACEUTICI | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

La disponibilité réelle du produit en France doit donc être vérifiée.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 206 interactions sont recensées, ce qui représente une charge d'interactions élevée. Parmi les principales :
  - **Majeures** : acarbose, doxycycline, minocycline, tétracycline, pioglitazone, bupropion, aprépitant, clarithromycine, acide chénodésoxycholique, naltrexone, oxandrolone, oxymétholone.
  - **Modérées** : ranitidine, cimétidine, lopéramide, budésonide (y compris nasal), saxagliptine, linagliptine, éliglustat.
- **Points d'attention connus pour la classe** : toxicité hépatique (accumulation de graisse hépatique, élévation des transaminases), effets indésirables digestifs et interactions avec les inhibiteurs du CYP3A4. Ces éléments sont à confirmer dans la notice.

Les mises en garde et contre-indications détaillées de l'ANSM ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : elle repose uniquement sur le score du modèle, sans essai clinique, sans publication et sans lien mécanistique plausible. Le score élevé ne suffit pas à justifier une poursuite.
- Le profil de sécurité est contraignant (toxicité hépatique, nombreuses interactions).

<!-- review:begin fr-lic-20261106-lomitapide-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le profil de sécurité est contraignant (toxicité hépatique, nombreuses interactions) et les AMM françaises sont toutes annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-lomitapide-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de mécanisme d'action (MOA) du médicament, pour analyser un éventuel lien avec la pathologie plaquettaire ou valvulaire.
- Les mises en garde et contre-indications de la notice ANSM, nécessaires pour tout dépistage de sécurité.
- Des preuves précliniques ou cliniques reliant l'inhibition de la MTP à la macrothrombocytopénie, ou le choix d'une autre indication prédite mieux étayée.

<!-- review:begin fr-lic-20261106-lomitapide-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Des preuves précliniques ou cliniques reliant l'inhibition de la MTP à la macrothrombocytopénie, ou le choix d'une autre indication prédite mieux étayée. / La confirmation de la disponibilité réelle du produit en France, compte tenu de l'annulation des AMM. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-lomitapide-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « et les AMM françaises sont toutes annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « La confirmation de la disponibilité réelle du produit en France, compte tenu de l'annulation des AMM » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Juxtapid (lomitapide mesylate) prescribing information, Chiesi USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61a0be9d-ee58-43e0-b5cb-141011835081) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

