---
layout: default
title: Omalizumab
parent: Preuves modérées (L3-L4)
nav_order: 559
evidence_level: L3
indication_count: 10
---

# Omalizumab
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **10** 
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

# Omalizumab : De l'asthme à la bronchite

## Résumé en Une Phrase

Omalizumab est un anticorps monoclonal anti-IgE, initialement utilisé pour traiter l'asthme (allergique et intrinsèque) et l'urticaire idiopathique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, mais les preuves directes sont faibles : **2 essais cliniques** étiquetés sous cette indication (de pertinence limitée) et **7 publications**, essentiellement des revues centrées sur l'asthme.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme, asthme intrinsèque, asthme allergique, urticaire idiopathique (source : graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,999 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations connues, l'omalizumab se lie aux IgE libres et réduit l'expression du récepteur FcεRI sur les mastocytes et les basophiles, ce qui atténue l'inflammation allergique des voies aériennes. Cette cible (IGHE, chaîne lourde epsilon) est confirmée par les données pharmacologiques.

La bronchite et l'asthme touchent tous deux les voies respiratoires inférieures. Un lien est plausible pour les bronchites d'origine allergique ou associées à l'asthme, et pour le chevauchement asthme-BPCO. Il n'est pas établi pour les bronchites infectieuses ou chroniques sans composante allergique.

Les deux essais associés à la bronchite sont indirects : l'un est une étude de réduction de corticoïdes chez des patients asthmatiques avec bronchite à éosinophiles, l'autre porte sur l'urticaire chronique spontanée. Le score élevé du modèle doit donc être interprété avec prudence.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Terminé | 11 | Essai contre placebo sur l'effet d'épargne des corticoïdes (prednisone) chez des patients avec asthme et bronchite à éosinophiles persistante ; effectif trop faible pour conclure |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Terminé | 382 | Étude de recherche de dose (QGE031) dans l'urticaire chronique spontanée ; lien avec la bronchite peu clair |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohorte | Postepy Dermatol Alergol | Omalizumab chez des patients d'âge moyen ou âgés avec chevauchement asthme allergique sévère-BPCO |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Analyse de sécurité groupée | Curr Med Res Opin | Sécurité et tolérance de l'omalizumab chez l'enfant avec asthme allergique |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Revue | Clin Rev Allergy Immunol | Efficacité de l'omalizumab dans l'asthme persistant modéré à sévère et expérience post-approbation |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revue | Expert Opin Pharmacother | Prise en charge de l'asthme associé aux maladies des voies aériennes liées au tabac (bronchite chronique, emphysème) |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Revue | Masui | Prise en charge préopératoire de l'asthme ou de la bronchite chronique ; mention de l'omalizumab |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Revue | Allergol Immunopathol | Anticorps monoclonaux en pédiatrie, dont les maladies allergiques |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Rapport de cas | J Investig Allergol Clin Immunol | Cas rare de bronchite plastique après thermoplastie bronchique |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66107946 | OMLYCLO 75 mg, seringue préremplie | Solution injectable | Non renseignée |
| 62877141 | XOLAIR 75 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61771263 | XOLAIR 300 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61971520 | XOLAIR 150 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61112487 | XOLAIR 75 mg, stylo prérempli | Solution injectable | Non renseignée |

Les 10 AMM recensées (Novartis Europharm et Celltrion Healthcare Hungary) sont toutes au statut « annulée » ; aucune AMM valide n'apparaît dans les données compilées.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 8 interactions recensées.
  - Modérée : omacétaxine mépésuccinate.
  - Mineures : sulfate de zinc, acétate de zinc, gluconate de zinc, chlorure de zinc, échinacée, vitamine E.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai ne cible directement la bronchite avec des résultats d'efficacité ; les deux essais associés sont indirects ou de très petite taille, et la littérature se limite à des revues centrées sur l'asthme (L3).
- Les données de sécurité de la notice sont manquantes, ce qui bloque le passage au criblage de sécurité, et aucune AMM française valide n'est en vigueur.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Préciser le sous-type de bronchite visé (allergique, à éosinophiles, associée à l'asthme ou à la BPCO) et mener un essai ciblé.
- Vérifier la situation réglementaire en France, toutes les AMM étant annulées.

## Autres Indications Prédites (pour information)

- **Eczéma atopique / dermatite** (L2, recherche) : l'essai de phase 4 NCT02300701 (n = 62, eczéma pédiatrique sévère) est le plus direct. Les résultats cliniques sont mitigés et les recommandations placent l'omalizumab derrière d'autres biologiques.
- **Maladie pulmonaire obstructive** (L1, Proceed with Guardrails) : recoupe largement l'indication asthmatique existante. La vraie question nouvelle est la BPCO avec sensibilisation allergique (essai de phase 2 NCT07059091, en recrutement).
- **Rangs 5 à 10** (néoplasme bronchique, acné chéloïdienne, acrodermatite chronique atrophiante, hydroa vacciniforme, dermatomyosite néonatale, pneumopathie interstitielle de l'enfant) : prédictions sans preuve clinique ni justification mécanistique plausible (L5, Hold).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

