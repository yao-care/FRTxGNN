---
layout: default
title: Aceclofenac
parent: Prédiction du modèle uniquement (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aceclofenac : nouvelle indication prédite, Syndrome brachyolmie-amélogenèse imparfaite (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, spondylarthrite ankylosante, arthrose"
monitor_inn: "aceclofenac"
predicted_indications: ["brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx", "inflammatory spondylopathy", "Kummell disease"]
---

# Aceclofenac
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Aceclofénac : Des Maladies Rhumatismales Inflammatoires à la Brachyolmie-Amélogenèse Imparfaite

## Résumé en Une Phrase

L'aceclofénac est un anti-inflammatoire non stéroïdien (AINS) initialement utilisé dans le traitement de la polyarthrite rhumatoïde, de la spondylarthrite ankylosante et de l'arthrose.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome brachyolmie-amélogenèse imparfaite**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, spondylarthrite ankylosante, arthrose (les textes d'indication des AMM françaises ne sont pas renseignés ; ces indications proviennent du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome brachyolmie-amélogenèse imparfaite |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'aceclofénac est un AINS dont l'effet anti-inflammatoire et antalgique repose classiquement sur l'inhibition des cyclo-oxygénases (COX) et de la synthèse des prostaglandines. Son efficacité symptomatique dans les rhumatismes inflammatoires et dégénératifs est documentée.

Le syndrome brachyolmie-amélogenèse imparfaite est une maladie génétique rare, touchant le squelette et les dents (liée à *LTBP3*). L'inhibition des COX ne corrige pas le défaut sous-jacent. **Aucun lien mécanistique plausible n'a pu être établi** : le score élevé du modèle est une prédiction issue du graphe de connaissances, sans confirmation expérimentale ni clinique. Le lien avec l'indication d'origine se limite à l'atteinte ostéo-articulaire, ce qui est insuffisant.

À titre de comparaison, les neuf autres candidats prédits présentent le même profil de preuve (L5), à l'exception de la spondylopathie inflammatoire (L4), qui recoupe en grande partie l'indication déjà connue de spondylarthrite ankylosante et apporte donc peu de nouveauté de repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour le syndrome brachyolmie-amélogenèse imparfaite.

À titre indicatif, la littérature disponible pour un autre candidat (la spondylopathie inflammatoire) comprend notamment des essais sur la spondylarthrite ankylosante, indication déjà connue :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8823693](https://pubmed.ncbi.nlm.nih.gov/8823693/) | 1996 | Étude clinique contrôlée multicentrique | J Rheumatol | Efficacité et tolérance de l'aceclofénac versus indométacine dans la spondylarthrite ankylosante active |
| [8823692](https://pubmed.ncbi.nlm.nih.gov/8823692/) | 1996 | ECR | J Rheumatol | Aceclofénac aussi sûr et efficace que le ténoxicam dans la spondylarthrite ankylosante (essai comparatif de 3 mois) |
| [34876850](https://pubmed.ncbi.nlm.nih.gov/34876850/) | 2021 | Revue | J Pain Res | Effets antalgiques et anti-inflammatoires de l'aceclofénac dans les affections musculo-squelettiques |
| [11511027](https://pubmed.ncbi.nlm.nih.gov/11511027/) | 2001 | Revue | Drugs | Réévaluation de l'usage de l'aceclofénac dans la douleur et les maladies rhumatismales |
| [15163279](https://pubmed.ncbi.nlm.nih.gov/15163279/) | 2004 | Revue | Expert Opin Pharmacother | Aceclofénac aussi efficace que diclofénac, naproxène et piroxicam dans l'arthrose |

Ces publications concernent des indications existantes et ne constituent pas une preuve pour la nouvelle indication prédite.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66300735 | CARTREX 100 mg, comprimé pelliculé (ALMIRALL) | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 63092688 | ACECLOFENAC VIATRIS 100 mg (VIATRIS SANTE) | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 68600724 | ACECLOFENAC ACCORD 100 mg (ACCORD HEALTHCARE FRANCE) | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64130871 | ACECLOFENAC BIOGARAN 100 mg (BIOGARAN) | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64937530 | ACECLOFENAC EG LABO 100 mg (EG LABO) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport. Par ailleurs, la littérature mentionne un cas de psoriasis pustuleux généralisé précipité par l'aceclofénac (PMID 16922973), et, comme pour les AINS en général, une vigilance digestive est classique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5) : aucun essai, aucune publication et aucun mécanisme plausible ne la soutient pour une maladie génétique rare du squelette et des dents. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) afin d'analyser un éventuel lien mécanistique
- Mises en garde et contre-indications issues de la notice ANSM (actuellement manquantes, ce qui bloque l'étape de criblage de sécurité)
- Preuves précliniques ou cliniques spécifiques à la nouvelle indication
- Vérification de la disponibilité du produit en France, toutes les AMM étant annulées
- Si une piste est retenue, une priorisation vers des candidats plus plausibles, comme la spondylopathie inflammatoire (L4, mais largement redondante avec l'indication existante) ou une évaluation symptomatique ciblée (par ex. douleur coccygienne)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

