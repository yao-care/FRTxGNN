---
layout: default
title: Pazopanib
parent: Preuves élevées (L1-L2)
nav_order: 231
evidence_level: L2
indication_count: 10
---

# Pazopanib
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

# Pazopanib : De l'Indication Originale (non renseignée dans les données) au Carcinome à Cellules Rénales Non Classé

## Résumé en Une Phrase

Le texte d'indication des deux AMM françaises du pazopanib n'est pas renseigné dans les données reçues. L'analyse du dossier le présente néanmoins comme un inhibiteur de tyrosine kinase multi-cibles, déjà commercialisé dans le carcinome à cellules rénales (CCR).
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **carcinome à cellules rénales non classé**, avec **1 essai clinique de phase 3** et **6 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (texte d'indication vide dans les deux AMM) |
| Nouvelle Indication Prédite | Carcinome à cellules rénales non classé |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action issues de DrugBank ne sont pas disponibles. Selon l'analyse du dossier, le pazopanib est un inhibiteur de tyrosine kinase multi-cibles (VEGFR-1/2/3, PDGFR-alpha/beta, c-Kit). Le blocage anti-angiogénique du VEGFR est le mécanisme établi de son usage commercialisé dans le CCR.

Le CCR non classé (ou non à cellules claires) est une extension histologique de cette indication. La voie VEGFR/PDGFR y reste plausible comme cible, mais le bénéfice propre à ce sous-type est moins certain que dans le CCR à cellules claires. Les études disponibles sur les formes non à cellules claires sont surtout des cohortes rétrospectives et un essai de phase 2 à bras unique. Le score TxGNN très élevé est donc cohérent avec le mécanisme, mais il ne remplace pas une preuve spécifique à ce sous-type.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Terminé | 544 | Sorafénib puis pazopanib versus pazopanib puis sorafénib dans le CCR avancé ou métastatique. Preuve directe dans le CCR, mais population non spécifique à l'histologie non classée. Résultats chiffrés non fournis dans les données. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase 2, bras unique | Cancer Res Treat | Étude multicentrique évaluant l'efficacité et la tolérance du pazopanib dans le CCR non à cellules claires métastatique |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Cohorte rétrospective multicentrique (PANORAMA) | Clin Genitourin Cancer | Analyse de l'efficacité et de la toxicité du pazopanib en première ligne dans le CCR non à cellules claires (Italie) |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Cohorte rétrospective | Clin Genitourin Cancer | Devenir des patients atteints de CCR non à cellules claires métastatique traités par pazopanib |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Cohorte en vie réelle | Ecancermedicalscience | Comparaison du sunitinib et du pazopanib en première ligne dans les CCR non à cellules claires et sarcomatoïdes |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Cohorte rétrospective (base IMDC) | Eur Urol Oncol | Comparaison des traitements de première ligne du CCR non à cellules claires selon le sous-type histologique, dont le CCR non classé |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Cohorte (preuve indirecte) | Clin Genitourin Cancer | Carcinomes de primitif inconnu à caractéristiques de CCR métastatique, traités par thérapies ciblées anti-VEGF |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63803884 | VOTRIENT 400 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 62894653 | VOTRIENT 200 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

Les deux AMM appartiennent à NOVARTIS EUROPHARM (Irlande).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase multi-cibles) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai de phase 3 terminé dans le CCR, un essai de phase 2 dans le CCR non à cellules claires et plusieurs cohortes soutiennent la plausibilité de cette extension (niveau L2).
- Aucune donnée randomisée ne cible spécifiquement l'histologie non classée, et les données de sécurité de la notice ANSM manquent, ce qui impose des garde-fous.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications). Cette lacune est bloquante pour le criblage de sécurité.
- Compléter les données de mécanisme d'action via DrugBank.
- Confirmer les critères d'éligibilité de NCT01613846, dont le titre est tronqué.
- Extraire les résultats propres au CCR non classé dans les cohortes (notamment PMID 41558869).

**Autres indications prédites dans le même dossier (pour information) :**
- **Liposarcome, dermatofibrosarcome protubérant (DFSP) et néoplasme fibroblastique :** niveau L2, Proceed with Guardrails. Des essais de phase 2 avec le pazopanib existent, dont deux spécifiques au liposarcome (NCT01506596, NCT01692496) et un au DFSP (NCT01059656, arrêté prématurément, n = 23).
- **Carcinome rénal de l'enfant et fibrosarcome cardiaque :** niveau L4, question de recherche.
- **CCR associé au neuroblastome, CCR à translocation Xp11.2/TFE3, liposarcome myxoïde ovarien et fibrosarcome rénal :** niveau L5, Hold. Aucune donnée clinique n'est fournie.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

