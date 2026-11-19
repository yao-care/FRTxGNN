---
layout: default
title: Esomeprazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 299
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "esomeprazole"
predicted_indications: ["duodenal obstruction"]
description: "Esomeprazole : nouvelle indication prédite, Duodenal obstruction (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Esomeprazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Esomeprazole: Duodenal obstruction
{: .text-alpha }

## Résumé en Une Phrase

L'ésoméprazole est un inhibiteur de la pompe à protons, initialement utilisé pour les maladies liées à l'acidité gastrique (ulcère peptique, reflux gastro-œsophagien, œsophagite, syndrome de Zollinger-Ellison).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **reflux duodénogastrique**, mais cette prédiction repose sur **0 essai clinique** et **1 publication** de portée générale, qui ne traite pas directement de cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Duodenal obstruction |
| Score de Prédiction TxGNN | 0.9945 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 18) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Esomeprazole (traduction non officielle) : « L'ésoméprazole appartient à une classe de composés antisécrétoires, les benzimidazoles substitués, qui suppriment la sécrétion d'acide gastrique par inhibition spécifique du système enzymatique H+/K+ ATPase à la surface sécrétoire de la cellule pariétale gastrique. L'ésoméprazole est protoné et converti dans le compartiment acide de la cellule pariétale pour former l'inhibiteur actif, le sulfénamide achiral. » Texte original en anglais : "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), version du 2025-12-19 ; consulté le 2026-11-19). Sur la base des informations connues, l'ésoméprazole fait partie de la classe des inhibiteurs de la pompe à protons (H+/K+ ATPase). Son efficacité a été établie dans les pathologies liées à l'acidité gastrique.

Dans le reflux duodénogastrique, le contenu duodénal (bile, sécrétions pancréatiques) remonte dans l'estomac. En réduisant l'acidité, l'ésoméprazole pourrait diminuer la composante acide du liquide refluant et soulager l'irritation de la muqueuse et les symptômes.

**Le lien reste toutefois indirect et, au mieux, symptomatique.** Ce reflux est principalement dû à la bile, aux sécrétions pancréatiques et à des troubles de la motricité, que la suppression acide ne traite pas directement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revue | European Journal of Clinical Pharmacology | Mise à jour sur l'usage clinique et la pharmacocinétique des inhibiteurs de la pompe à protons (ulcère peptique, infection à *H. pylori*, RGO, lésions liées aux AINS, syndrome de Zollinger-Ellison). Ne traite pas directement du reflux duodénogastrique. |

---

## Informations de Marché en France

Voici les 5 premières :

<!-- review:begin fr-lic-20261106-esomeprazole-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 20 AMM recensées sont toutes annulées. Voici les 5 premières : » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-esomeprazole-1 -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|------|
| 62358997 | ESOMEPRAZOLE ARROW LAB 40 mg | Gélule gastro-résistante | Active |
| 62824142 | INEXIUM 40 mg | Comprimé gastro-résistant | Active |
| 67972216 | ESOMEPRAZOLE EG 40 mg | Gélule gastro-résistante | Active |
| 66628995 | ESOMEPRAZOLE ZENTIVA 40 mg | Gélule gastro-résistante | Active |
| 64359642 | ESOMEPRAZOLE ETHYPHARM 20 mg | Gélule gastro-résistante | Active |

Les autres formes recensées sont les granulés pour suspension buvable (INEXIUM 10 mg) et la poudre pour solution injectable ou pour perfusion.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, ostéoporose, ostéoporose post-ménopausique, fracture osseuse, gastrite atrophique chronique.
- **Interactions médicamenteuses** : 168 interactions recensées. Parmi celles listées, deux sont de niveau **majeur** : l'acalabrutinib et l'atazanavir. Plusieurs sont de niveau modéré, par exemple l'hydrochlorothiazide, l'atorvastatine, le fénofibrate, l'amphotéricine B, l'amikacine, l'amphétamine, l'apalutamide, le bosutinib, la bendamustine et le bumétanide. D'autres sont de niveau mineur, par exemple l'acide acétylsalicylique, la cyanocobalamine, l'axitinib et le bortézomib.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni publication spécifique ne soutient l'usage de l'ésoméprazole dans le reflux duodénogastrique.
- Le lien mécanistique est indirect, et le score élevé du modèle ne remplace pas des preuves réelles.

Elle correspond toutefois à un usage déjà établi du médicament et ne constitue pas un véritable repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données cliniques ou observationnelles spécifiques au reflux duodénogastrique (ou reflux biliaire) : essais contrôlés, études sur le soulagement des symptômes
- Les données détaillées sur le mécanisme d'action
- Les informations officielles de sécurité (mises en garde et contre-indications de la notice ANSM)

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 20 AMM recensées sont toutes annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

