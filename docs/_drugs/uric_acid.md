---
layout: default
title: Uric Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 798
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Uric Acid : nouvelle indication prédite, Polyarthrite rhumatoïde (niveau de preuve L5). Indication d'origine : Non renseignée dans les autorisations françaises"
---

# Uric Acid
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Acide urique : De l'absence d'indication officielle à la polyarthrite rhumatoïde

## Résumé en Une Phrase

L'acide urique est un métabolite purique endogène. En France, il n'est présent que dans des médicaments homéopathiques (Uricum acidum), dont les autorisations sont aujourd'hui annulées et dont aucune indication officielle n'est renseignée.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **polyarthrite rhumatoïde**.
Les données compilées ne contiennent **aucun essai clinique** testant l'acide urique dans cette maladie. Les **20 publications** retrouvées portent surtout sur l'acide urique comme biomarqueur ou facteur de risque, pas comme traitement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les autorisations françaises |
| Nouvelle Indication Predite | Polyarthrite rhumatoïde |
| Score de Prédiction TxGNN | 99,68 % |
| Niveau de Preuve | L4 (selon l'évaluation compilée ; en pratique, la preuve thérapeutique directe est absente) |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données. Sur la base des informations connues, l'acide urique est un métabolite de la dégradation des purines. Il agit à la fois comme antioxydant et comme signal de danger : les cristaux d'urate monosodique activent l'inflammasome NLRP3 et l'IL-1β.

Dans la polyarthrite rhumatoïde, la littérature décrit l'acide urique surtout comme un **marqueur biologique** et un corrélat du risque cardiovasculaire et des comorbidités (atteinte pulmonaire interstitielle, mortalité, activité de la maladie). Elle ne le décrit pas comme un agent thérapeutique.

Le score élevé du modèle reflète probablement une **proximité dans le réseau de connaissances** (voies inflammatoires et métabolisme des purines communs, lien entre goutte et polyarthrite) plutôt qu'un effet thérapeutique. Administrer de l'acide urique augmenterait la charge en urate, qui est elle-même un facteur de risque (cardiovasculaire, rénal, goutte). Le sens de l'hypothèse de repositionnement n'est donc pas étayé.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03194204](https://clinicaltrials.gov/study/NCT03194204) | Non applicable | Terminé | 160 | Doxycycline en association dans la polyarthrite rhumatoïde. L'acide urique n'est pas l'intervention testée : l'essai n'apporte aucune preuve directe. |

## Preuves de la Littérature

Aucune de ces publications n'évalue l'acide urique comme traitement de la polyarthrite rhumatoïde.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37627564](https://pubmed.ncbi.nlm.nih.gov/37627564/) | 2023 | Revue systématique / méta-analyse | Antioxidants | Association entre les concentrations d'acide urique et d'allantoïne et la polyarthrite rhumatoïde (état pro-oxydant, risque cardiovasculaire) |
| [35110331](https://pubmed.ncbi.nlm.nih.gov/35110331/) | 2022 | Revue (recommandations) | Ann Rheum Dis | Recommandations EULAR sur la gestion du risque cardiovasculaire dans les maladies rhumatismales |
| [40837562](https://pubmed.ncbi.nlm.nih.gov/40837562/) | 2025 | Cohorte | Front Med | Valeur prédictive et pronostique de l'acide urique sérique dans la pneumopathie interstitielle associée à la polyarthrite |
| [37650291](https://pubmed.ncbi.nlm.nih.gov/37650291/) | 2024 | Cohorte | Clin Exp Rheumatol | Association entre acide urique sérique et mortalité globale et cardiovasculaire dans la polyarthrite |
| [35314903](https://pubmed.ncbi.nlm.nih.gov/35314903/) | 2022 | Étude clinique et cellulaire | Inflammation | Acide urique sérique comme biomarqueur diagnostique de la pneumopathie interstitielle associée à la polyarthrite |
| [38026718](https://pubmed.ncbi.nlm.nih.gov/38026718/) | 2023 | Observationnelle | Open Access Rheumatol | Association entre le taux d'acide urique sérique et l'activité de la polyarthrite |
| [21115462](https://pubmed.ncbi.nlm.nih.gov/21115462/) | 2011 | Revue | Rheumatology | Acide urique et risque cardiovasculaire dans la polyarthrite rhumatoïde |
| [15346653](https://pubmed.ncbi.nlm.nih.gov/15346653/) | 2004 | Observationnelle | Free Radic Res | Allantoïne, produit d'oxydation de l'acide urique, comme marqueur de stress oxydant dans la polyarthrite (21 patients) |
| [39968300](https://pubmed.ncbi.nlm.nih.gov/39968300/) | 2025 | Revue | Front Endocrinol | Impact de l'acide urique sur les maladies musculo-squelettiques, dont la polyarthrite |
| [40710524](https://pubmed.ncbi.nlm.nih.gov/40710524/) | 2025 | Revue | Metabolites | Acide urique, colchicine et maladies inflammatoires chroniques, dans une perspective cardiovasculaire |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61517329 | URICUM ACIDUM LEHNING (dilutions 3CH à 30CH ou 6DH à 60DH), annulée | Comprimé, solution(s), granules, poudre et pommade | Non renseignée |
| 61992596 | URICUM ACIDUM BOIRON (dilutions 4CH à 30CH ou 8DH à 60DH), annulée | Comprimé, solution(s), granules, poudre et pommade | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. Par ailleurs, l'administration d'acide urique augmenterait la charge en urate, un facteur de risque cardiovasculaire, rénal et de goutte.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ne teste l'acide urique dans la polyarthrite rhumatoïde. La littérature le présente comme marqueur ou facteur de risque, et non comme traitement.
- Le score TxGNN élevé semble refléter une proximité dans le réseau de connaissances. Le sens de l'hypothèse est contestable, car un apport d'acide urique risquerait d'aggraver la charge en urate.
- Les autorisations françaises sont annulées et aucune donnée de sécurité n'est disponible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le premier filtrage de sécurité.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Mener des études précliniques pour savoir si l'acide urique a un effet bénéfique, neutre ou délétère dans la polyarthrite rhumatoïde.
- Réévaluer la pertinence de l'hypothèse. Il est possible que l'hypouricémie ou l'inhibition de la voie de l'urate soit la piste à explorer, plutôt que l'apport d'acide urique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

