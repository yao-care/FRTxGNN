---
layout: default
title: Molsidomine
parent: Prédiction du modèle uniquement (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Molsidomine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Molsidomine : De la maladie coronarienne à l'alopécie

## Résumé en Une Phrase

Molsidomine est un donneur de monoxyde d'azote (NO), utilisé dans la maladie coronarienne et l'angor. Les données réglementaires françaises disponibles ne précisent pas son indication autorisée.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**alopécie** (rang 1), mais **aucun essai clinique** et **aucune publication pertinente** ne soutiennent cette direction.
Parmi les autres prédictions, seule la **maladie vasculaire** (rang 2) est bien documentée, avec **2 essais cliniques** et **20 publications**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données de l'ANSM (la littérature le décrit comme traitement de la maladie coronarienne) |
| Nouvelle Indication Prédite | Alopécie |
| Score de Prédiction TxGNN | 99,99995 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 8 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, molsidomine est une prodrogue dont le métabolite actif (SIN-1) libère du NO. Cela provoque une vasodilatation veineuse et artérielle, et son efficacité est établie dans la maladie coronarienne.

Pour l'alopécie, **aucun lien mécanistique n'est établi**. On peut supposer qu'une vasodilatation induite par le NO améliorerait la perfusion du cuir chevelu, mais cette hypothèse reste purement spéculative. Le score TxGNN très élevé traduit une proximité dans le graphe de connaissances, pas une preuve d'efficacité.

Les deux publications retrouvées portent sur la madarose (perte des cils et sourcils) liée à une mitochondriopathie. Elles ne concernent pas molsidomine et ne soutiennent donc pas cette prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16879589](https://pubmed.ncbi.nlm.nih.gov/16879589/) | 2006 | Cas clinique | Acta Ophthalmologica Scandinavica | Madarose due à une mitochondriopathie ; molsidomine n'est pas concerné (pas de résumé disponible) |
| [16188012](https://pubmed.ncbi.nlm.nih.gov/16188012/) | 2005 | Cas clinique | Acta Ophthalmologica Scandinavica | Même thème (madarose et mitochondriopathie) ; molsidomine n'est pas concerné (pas de résumé disponible) |

## Autres Indications Prédites

### Maladie vasculaire (rang 2) : la seule prédiction appuyée par des preuves

Niveau de preuve **L2**, décision **Proceed with Guardrails**. Le mécanisme (libération de NO, vasodilatation, inhibition de l'agrégation plaquettaire, amélioration de la fonction endothéliale) est cohérent avec cette indication. Molsidomine étant déjà utilisé dans l'angor et la maladie coronarienne sur certains marchés, on est plus proche d'un usage déjà connu que d'un vrai repositionnement.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01363661](https://clinicaltrials.gov/study/NCT01363661) | Phase 4 | Terminé | 165 | Essai randomisé en double aveugle contre placebo : effet de molsidomine sur la dysfonction endothéliale chez des patients avec angor stable, avant une angioplastie coronarienne (critère de substitution, sur 12 mois) |
| [NCT00382421](https://clinicaltrials.gov/study/NCT00382421) | Non applicable | Terminé | Non renseignée | SWISSI 1 : ischémie silencieuse chez des sujets asymptomatiques ; l'utilisation de molsidomine n'est pas confirmée dans les données |

Publications principales sur les 20 retrouvées :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9475269](https://pubmed.ncbi.nlm.nih.gov/9475269/) | 1998 | ECR croisé | J Cardiovasc Pharmacol | 90 patients avec angor stable : amélioration de la capacité d'effort avec molsidomine retard et non retard |
| [15676171](https://pubmed.ncbi.nlm.nih.gov/15676171/) | 2005 | Étude clinique | Int J Cardiol | Efficacité et tolérance de molsidomine en une prise par jour dans l'angor stable |
| [8438599](https://pubmed.ncbi.nlm.nih.gov/8438599/) | 1993 | Étude clinique | Wien Klin Wochenschr | Effets fibrinolytiques et antiplaquettaires synergiques avec la prostacycline dans l'artériopathie périphérique (20 patients) |
| [31085310](https://pubmed.ncbi.nlm.nih.gov/31085310/) | 2019 | Préclinique | Vascul Pharmacol | Chez la souris, molsidomine favorise la stabilité de la plaque d'athérome et réduit l'infarctus |

Limites : il n'existe pas d'essai de phase 3 sur des critères cliniques, et le seul ECR récent porte sur un critère de substitution.

### Autres prédictions (toutes L5, Hold, sans essai ni publication)

| Indication prédite | Score TxGNN | Commentaire |
|------|------|------|
| Syndrome du défilé thoracique veineux | 99,99993 % | La compression est mécanique (traitée par décompression et anticoagulation) |
| Syndrome du défilé thoracique artériel | 99,99993 % | Mêmes réserves : cause mécanique |
| Dissection coronaire spontanée idiopathique | 99,99993 % | Effet symptomatique plausible comme pour les autres nitrés, mais effets hémodynamiques sur un vaisseau disséqué non évalués |
| Hypotrichose simple du cuir chevelu | 99,99993 % | Maladie monogénique, aucun lien mécanistique |
| Calciphylaxie viscérale | 99,99992 % | Spéculatif ; risque d'hypotension chez les patients dialysés |
| Syndrome du défilé thoracique neurogène | 99,99992 % | Compression du plexus brachial, pas de justification pour un donneur de NO |
| Hémangioendothéliome | 99,99990 % | Lien faible ; la vasodilatation pourrait être contre-productive |
| Hypotrichose congénitale avec milium | 99,99990 % | Maladie rare congénitale, aucun lien mécanistique |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62439495 | MOLSIDOMINE EG 2 mg | Comprimé sécable | Non renseignée |
| 60740076 | MOLSIDOMINE ARROW 2 mg | Comprimé sécable | Non renseignée |
| 63967289 | MOLSIDOMINE ARROW 4 mg | Comprimé sécable | Non renseignée |
| 61544116 | MOLSIDOMINE EG 4 mg | Comprimé | Non renseignée |
| 62011103 | MOLSIDOMINE BIOGARAN 2 mg | Comprimé sécable | Non renseignée |

Le dossier recense 8 AMM au total ; seules les 5 premières sont détaillées ci-dessus.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold** (pour l'alopécie)

**Justification :**
- La prédiction pour l'alopécie repose uniquement sur le modèle (L5) : aucun essai, aucun lien mécanistique, et les deux publications retrouvées ne concernent pas molsidomine.
- Pour la maladie vasculaire, la décision serait *Proceed with Guardrails* (L2), mais il s'agit surtout d'un usage cardiovasculaire déjà connu, et non d'un vrai repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde, contre-indications, indication autorisée), car l'absence de ces données bloque l'étape de sécurité
- Compléter les données de mécanisme d'action via DrugBank
- Pour l'alopécie : une étude préclinique ou un mécanisme plausible avant tout examen supplémentaire
- Pour la maladie vasculaire : préciser l'indication autorisée en France et vérifier s'il s'agit d'un usage déjà couvert, ou d'une extension réelle
- Évaluer le risque d'hypotension et l'interaction avec les inhibiteurs de la phosphodiestérase de type 5 pour toute population ciblée

*Ce rapport est destiné à la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

