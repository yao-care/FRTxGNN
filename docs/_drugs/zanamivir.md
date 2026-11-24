---
layout: default
title: Zanamivir
parent: Prédiction du modèle uniquement (L5)
nav_order: 826
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "zanamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
description: "Zanamivir : nouvelle indication prédite, Pyélonéphrite (pyelonephritis) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Zanamivir
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

## Zanamivir: Pyélonéphrite (pyelonephritis)
{: .text-alpha }

## Résumé en Une Phrase

Zanamivir est un inhibiteur de la neuraminidase virale, initialement utilisé pour le traitement de la **grippe** (y compris les formes sévères).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pyélonéphrite**, mais cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Pyélonéphrite (pyelonephritis) |
| Score de Prédiction TxGNN | 0.9984 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Zanamivir (traduction non officielle) : « Le zanamivir est un médicament antiviral actif contre le virus de la grippe. […] Le zanamivir est un inhibiteur de la neuraminidase (NA) du virus de la grippe, une enzyme qui libère les particules virales de la membrane plasmique des cellules infectées et favorise la propagation du virus dans les voies respiratoires. Dans les tests d'inhibition de la neuraminidase, le zanamivir est actif contre tous les sous-types enzymatiques de NA, de N1 à N9. » Texte original en anglais : "Zanamivir is an antiviral drug with activity against influenza virus. […] Zanamivir is an inhibitor of influenza virus neuraminidase (NA), an enzyme that releases viral particles from the plasma membrane of infected cells and promotes virus spread in the respiratory tract. In neuraminidase inhibition assays, zanamivir is active against all NA enzyme subtypes N1 to N9." ([DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d), version du 2026-07-23 ; consulté le 2026-11-19). Sur la base des informations connues, le zanamivir est un inhibiteur de la neuraminidase du virus de la grippe, dont l'efficacité a été établie dans la grippe.

Le lien mécanistique avec la pyélonéphrite n'est **pas établi**. La pyélonéphrite est une infection rénale principalement bactérienne, due surtout à des bactéries uropathogènes comme *E. coli*. Ces bactéries possèdent leurs propres sialidases, mais elles ne sont pas une cible reconnue du zanamivir, qui n'a pas d'activité antibactérienne connue.

Le score très élevé du modèle TxGNN (apprentissage profond), 0,9984, provient du modèle et peut refléter des similarités apprises entre maladies apparentes, et non une preuve biologique. Cette prédiction doit donc être considérée avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la pyélonéphrite.

Pour information, la deuxième prédiction du modèle (trouble du métabolisme de la tyrosine, score 0,9902) n'est soutenue que par trois publications sans rapport réel avec cette indication. Elles portent sur la virologie de la grippe : résistance à l'oseltamivir, test de résonance plasmonique de surface, mutation N294S de la neuraminidase. Elles semblent avoir été retrouvées par simple correspondance de termes. Cette prédiction reste également au niveau L5, avec la recommandation Hold.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 64427189 | DECTOVA 10 mg/1 mL, solution pour perfusion | Solution pour perfusion | GLAXOSMITHKLINE TRADING SERVICES (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non le texte de la notice) : épilepsie, bronchopneumopathie chronique obstructive (BPCO, y compris les formes précoces sévères), maladie bronchique, délire.
- **Interactions médicamenteuses** (8 identifiées) :
  - Modérée : insuline humaine (inhalée, à action rapide).
  - Niveau non déterminé : clarithromycine, loratadine, montélukast, kétotifène, fexofénadine, ibuprofène, diclofénac.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication pertinente, et aucun mécanisme plausible reliant un inhibiteur de neuraminidase virale à une infection bactérienne.
- Les données de sécurité officielles sont absentes, ce qui bloque l'étape de criblage de sécurité.

<!-- review:begin fr-lic-20261106-zanamivir-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'AMM française est annulée et les données de sécurité officielles sont absentes, ce qui bloque l'étape de criblage de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-zanamivir-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action (via DrugBank).
- Démontrer une activité *in vitro* ou préclinique du zanamivir contre les uropathogènes ou dans un modèle de pyélonéphrite.
- Vérifier la compatibilité de la voie d'administration (perfusion uniquement) avec le contexte clinique visé.
- Réévaluer la pertinence de la prédiction en gardant à l'esprit que le score du modèle TxGNN (apprentissage profond) peut refléter des similarités apprises entre maladies apparentées, et non une preuve biologique.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'AMM française est annulée et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

