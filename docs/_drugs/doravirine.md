---
layout: default
title: Doravirine
parent: Prédiction du modèle uniquement (L5)
nav_order: 256
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Doravirine : nouvelle indication prédite, Infection par le virus de l'immunodéficience simienne (niveau de preuve L5). Indication d'origine : Infection par le VIH, SIDA"
monitor_inn: "DORAVIRINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Doravirine : Du VIH à l'Infection par le Virus de l'Immunodéficience Simienne

## Résumé en Une Phrase

Doravirine est un inhibiteur non nucléosidique de la transcriptase inverse (INNTI) du VIH-1, initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'immunodéficience simienne (VIS)**, mais **aucun essai clinique** n'est enregistré et la seule publication liée concerne un autre médicament (l'islatravir), de sorte que cette prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement ; aucune étude directe) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la doravirine est un INNTI du VIH-1, dont l'efficacité dans l'infection par le VIH est établie. Le VIS est un lentivirus proche du VIH, ce qui explique la proximité entre les deux maladies dans le réseau de connaissances.

Cette plausibilité reste toutefois fragile. Les INNTI sont généralement inactifs contre le VIH-2 et de nombreuses souches de VIS, en raison de variations naturelles de la poche de liaison des INNTI sur la transcriptase inverse. L'activité de la doravirine contre le VIS devrait donc être confirmée expérimentalement (tests enzymatiques *in vitro* sur la transcriptase inverse du VIS, études chez le macaque). Le score élevé reflète très probablement une proximité dans le réseau plutôt qu'une preuve directe.

Deux autres prédictions de même score élevé sont à signaler : le syndrome d'immunodéficience acquise féline (FIV), dont la transcriptase inverse diffère aussi de celle du VIH-1 et pour laquelle les INNTI sont peu actifs, sans essai ni publication ; et un trouble neurodéveloppemental rare, sans aucun lien mécanistique plausible, qui semble être un artefact du graphe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Revue | Current Opinion in HIV and AIDS | Discute le rôle potentiel de l'islatravir, un inhibiteur de la translocation de la transcriptase inverse, dans le traitement et la prévention du VIH-1. Cette publication concerne un autre médicament et ne soutient pas directement la doravirine dans l'infection par le VIS. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68914027 | PIFELTRO 100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64419961 | DELSTRIGO 100 mg/300 mg/245 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

**Interactions Médicamenteuses** : 59 interactions ont été recensées. Parmi les exemples relevés :
- **Majeures** : dexaméthasone, lumacaftor
- **Modérées** : phénylbutyrate de glycérol, métréleptine, troglitazone, déférasirox, praziquantel, griséofulvine
- **Mineures** : aprépitant, cimétidine, clarithromycine, clotrimazole, miconazole, cobicistat, ticagrélor, ivacaftor, zafirlukast, chloramphénicol, érythromycine, fluconazole

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, et la seule publication liée porte sur un autre médicament. Les INNTI sont en outre généralement peu actifs contre le VIS, et le médicament n'a plus d'AMM valide en France. Le VIS est par ailleurs un modèle animal plutôt qu'une indication humaine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Tests *in vitro* de l'activité de la doravirine sur la transcriptase inverse du VIS, puis éventuellement des études chez le macaque
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice de l'ANSM (bloquant pour l'évaluation de sécurité)
- Clarification de la pertinence de l'indication (modèle animal ou usage vétérinaire) et du statut réglementaire en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

