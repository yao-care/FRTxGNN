---
layout: default
title: Artemether
parent: Prédiction du modèle uniquement (L5)
nav_order: 72
evidence_level: L5
indication_count: 8
monitor_inn: "artemether"
predicted_indications: ["acquired angioedema", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
last_modified_at: 2026-11-20
description: "Artemether : nouvelle indication prédite, Angiœdème acquis (acquired angioedema) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Artemether
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Artéméther : antipaludique dérivé de l'artémisinine → Angiœdème acquis (acquired angioedema)
{: .text-alpha }

## Résumé en Une Phrase

L'artéméther est un dérivé de l'artémisinine, commercialisé en France sous le nom RIAMET (association fixe à dose de 20 mg/120 mg, comprimé).
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**angiœdème acquis (acquired angioedema)**, avec un score de 0,9990.
Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Angiœdème acquis (acquired angioedema) |
| Score de Prédiction TxGNN | 0,9990 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Artemether est (traduction non officielle) : « Inhibiteur de la ferriprotoporphyrine IX ». Texte original en anglais : "Ferriprotoporphyrin IX inhibitor" ([ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534), CC BY-SA 3.0 ; consulté le 2026-11-19). L'artéméther est un dérivé de l'artémisinine, mais aucune donnée mécanistique n'a été compilée pour ce rapport.

Pour l'angiœdème acquis, aucun lien mécanistique cliniquement plausible n'est établi. Cette pathologie repose sur l'excès de bradykinine et sur des anomalies de la voie du complément (inhibiteur de la C1-estérase), axes sur lesquels l'artéméther n'a aucune action connue. Le score élevé (0,9990) reflète une proximité dans le réseau du modèle, sans validation biologique ou clinique.

Les autres prédictions listées pour ce médicament (angiœdème, angiœdème héréditaire, syndrome néphrogénique d'antidiurèse inappropriée, conjonctivite contagieuse aiguë, sclérodermie, conjonctivite, angiœdème induit par les bloqueurs du système rénine-angiotensine-aldostérone) présentent également un niveau de preuve L5, sans essai ni publication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65574434 | RIAMET 20 mg/120 mg, comprimé | comprimé | Non renseignée dans les données locales |

## Cytotoxicité

Non applicable : l'artéméther n'est pas un médicament antinéoplasique.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 95 interactions recensées. Parmi les principales, de niveau majeur : clarithromycine, cobicistat, amprénavir, apalutamide, atazanavir, bocéprévir. De niveau modéré : dexaméthasone, miconazole, troglitazone, déférasirox, bosentan, bexarotène, brigatinib, armodafinil, fostamatinib, entre autres.
- **Pathologies à risque signalées** : syndrome du QT long (y compris familial), torsades de pointes et carence en potassium sont associés à une prudence particulière avec ce médicament.

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde et contre-indications non disponibles dans les données compilées).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (0,9990), sans essai clinique, sans publication et sans lien mécanistique plausible avec l'angiœdème acquis. Le profil d'interactions médicamenteuses et les risques liés à l'allongement de l'intervalle QT ajoutent des réserves.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications issues de la notice ANSM
- Une hypothèse mécanistique explicite et des données précliniques reliant l'artéméther à la voie de la bradykinine ou du complément
- Tout essai ou publication étudiant directement l'angiœdème acquis

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

