---
layout: default
title: Doravirine
parent: Prédiction du modèle uniquement (L5)
nav_order: 111
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Doravirine : De l'Infection par le VIH-1 à l'Infection par le Virus de l'Immunodéficience Simienne

## Résumé en Une Phrase

Doravirine est un inhibiteur non nucléosidique de la transcriptase inverse (INNTI), utilisé à l'origine dans le traitement de l'infection par le VIH-1.
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'immunodéficience simienne (SIV)**, mais **aucun essai clinique** et **une seule publication** (sur un autre médicament) existent à ce jour.
Cette prédiction repose donc presque uniquement sur le modèle et reste très fragile.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH-1 (le texte d'indication de l'ANSM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne (SIV) |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la doravirine est un INNTI, sa place dans le traitement du VIH-1 est établie, et le SIV est un lentivirus proche du VIH-1. Le score élevé reflète probablement cette proximité dans le graphe de connaissances.

Cette proximité ne garantit cependant pas l'efficacité. Les transcriptases inverses du SIVmac et du VIH-2 sont naturellement résistantes à la plupart des INNTI. Des variations dans la poche de liaison des INNTI, de type Y181I ou Y188L, en sont l'une des explications. L'activité directe de la doravirine contre le SIV est donc douteuse. Aucune donnée spécifique doravirine/SIV n'a été fournie.

Deux autres prédictions figurent dans le dossier, toutes deux de niveau L5 et en Hold :
- **Syndrome d'immunodéficience acquise féline** (score 99,93 %) : le lien vient probablement de l'ontologie des lentivirus. Aucune preuve n'existe, les INNTI agissent peu sur les lentivirus non primates, et l'indication est vétérinaire, hors du champ du repositionnement chez l'humain.
- **Trouble neurodéveloppemental rare avec démarche ataxique, absence de parole et diminution de la substance blanche corticale** (score 99,91 %) : aucun lien mécanistique plausible, probablement un artefact du graphe de connaissances.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Revue | Current Opinion in HIV and AIDS | Discute du rôle potentiel de l'islatravir, un inhibiteur de la translocation de la transcriptase inverse, dans le traitement et la prévention du VIH-1. Ne concerne ni la doravirine ni le SIV, donc pas de soutien direct à la prédiction. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 68914027 | PIFELTRO 100 mg, comprimé pelliculé | Comprimé pelliculé |
| 64419961 | DELSTRIGO 100 mg/300 mg/245 mg, comprimé pelliculé | Comprimé pelliculé |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni donnée spécifique doravirine/SIV n'existe, et la seule publication porte sur un autre médicament.
- La résistance naturelle connue des transcriptases inverses du SIV aux INNTI rend l'efficacité peu probable.
- Les données de sécurité de l'ANSM manquent, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice de l'ANSM (mises en garde et contre-indications), à télécharger et à analyser
- Données sur le mécanisme d'action, à interroger dans DrugBank
- Données précliniques *in vitro* sur l'activité de la doravirine contre la transcriptase inverse du SIV (SIVmac) et du VIH-2
- Pertinence de l'indication au regard du repositionnement chez l'humain, le SIV étant une infection de primates non humains
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

