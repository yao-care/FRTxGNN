---
layout: default
title: Evolocumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 312
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "evolocumab"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
description: "Evolocumab : nouvelle indication prédite, Forme symptomatique de l'hémophilie chez les porteuses (symptomatic form of hemophilia in female carriers) (niveau de preuve L5). Indication d'origine : Non …"
---

# Evolocumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Evolocumab: Forme symptomatique de l'hémophilie chez les porteuses (symptomatic form of hemophilia in female carriers)
{: .text-alpha }

## Résumé en Une Phrase

Evolocumab est un anticorps monoclonal inhibiteur de PCSK9, initialement utilisé pour traiter l'hypercholestérolémie familiale homozygote et les dyslipidémies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **forme symptomatique de l'hémophilie chez les porteuses**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Forme symptomatique de l'hémophilie chez les porteuses (symptomatic form of hemophilia in female carriers) |
| Score de Prédiction TxGNN | 0.9982 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Evolocumab (traduction non officielle) : « L'évolocumab est une IgG2 monoclonale humaine dirigée contre la proprotéine convertase subtilisine/kexine de type 9 (PCSK9) humaine. La PCSK9 se lie au récepteur des lipoprotéines de basse densité (LDLR) à la surface des hépatocytes afin de favoriser la dégradation du LDLR dans le foie. » Texte original en anglais : "Evolocumab is a human monoclonal IgG2 directed against human proprotein convertase subtilisin kexin type 9 (PCSK9). PCSK9 binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes to promote LDLR degradation within the liver." ([DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e), version du 2026-10-12 ; consulté le 2026-11-19). Sur la base des informations connues, evolocumab est un anticorps monoclonal qui inhibe PCSK9, augmente la disponibilité des récepteurs du LDL et abaisse le LDL-cholestérol. Son efficacité dans l'hypercholestérolémie familiale est établie.

**Le lien mécanistique avec la nouvelle indication est très faible, voire inexistant.** Les symptômes hémorragiques des porteuses d'hémophilie résultent d'une activité réduite du facteur VIII ou IX, liée à des variants portés par le chromosome X et à une inactivation biaisée de ce chromosome. L'inhibition de PCSK9 n'agit pas sur la cascade de coagulation. Le score élevé du modèle TxGNN (deep learning) (0.9982) peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique, sans support clinique ou bibliographique.

À titre de comparaison, les autres prédictions du modèle (déficit en apolipoprotéine C-II, purpura thrombopénique, déficit en facteur XI, hémophilie A avec anomalie vasculaire, « maladie de l'activité catalytique ») ne disposent pas non plus de preuves. Seul le déficit en apoC-II présente un lien indirect, limité au métabolisme lipidique en général.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60966449 | REPATHA 140 mg, solution injectable en stylo prérempli | Solution injectable | AMGEN EUROPE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une seule entrée de pharmacologie est enregistrée, correspondant à la cible d'evolocumab, la protéine PCSK9 (proprotein convertase subtilisin/kexin type 9). Il s'agit de l'interaction avec sa cible et non d'une interaction médicamenteuse cliniquement significative ; aucun niveau de gravité n'est précisé.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication, et aucun mécanisme plausible reliant l'inhibition de PCSK9 à l'hémophilie des porteuses.

<!-- review:begin fr-lic-20261106-evolocumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication, et aucun mécanisme plausible reliant l'inhibition de PCSK9 à l'hémophilie des porteuses. De plus, la seule AMM française recensée est annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-evolocumab-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (étape bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Des données précliniques ou cliniques justifiant un lien biologique avec la coagulation, sans quoi il est préférable de réorienter l'évaluation vers des indications plus proches du métabolisme lipidique
- La clarification du statut réglementaire actuel d'evolocumab en France (la présentation répertoriée est annulée)

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, la seule AMM française recensée est annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Repatha (evolocumab) prescribing information, Amgen USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cd61e902-166d-4aa6-9f3c-a18c1008d07e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

