---
layout: default
title: Darunavir
parent: Preuves modérées (L3-L4)
nav_order: 100
evidence_level: L4
indication_count: 4
---

# Darunavir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

# Darunavir : Du VIH-1 à l'infection par le virus de l'immunodéficience simienne (SIV)

## Résumé en Une Phrase

Darunavir est un inhibiteur de protéase du VIH-1, déjà commercialisé en France sous forme de comprimés pelliculés.
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'immunodéficience simienne (SIV)**, mais **aucun essai clinique** ne soutient cette direction. Seules **4 publications précliniques** chez le macaque existent, et la présence du darunavir dans les schémas étudiés n'y est pas confirmée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM fournies (le texte d'indication des AMM est vide) ; darunavir est un inhibiteur de protéase du VIH-1 |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne (SIV) |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 17 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, darunavir appartient à la classe des inhibiteurs de protéase du VIH-1. Le SIV est le modèle standard du VIH chez le macaque, si bien qu'un mécanisme de type inhibiteur de protéase est plausible.

Il faut toutefois relativiser cette prédiction. Les 4 publications disponibles sont des études précliniques chez le macaque portant sur des traitements antirétroviraux combinés. Leurs titres sont tronqués, donc la présence du darunavir dans chaque schéma n'est pas confirmée. Sa contribution propre ne peut pas être isolée de celle des autres molécules. Il s'agit d'un substitut préclinique de l'indication VIH déjà approuvée, et non d'une nouvelle indication humaine.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Préclinique (macaque) | AIDS Res Hum Retroviruses | Comparaison de deux schémas antirétroviraux injectables coformulés (dont un « triple schéma » emtricitabine/ténofovir disoproxil) chez des macaques rhésus infectés par SIVmac239 |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Préclinique (macaque) | PLoS One | Traitement antirétroviral combiné intensif associé à l'inhibiteur d'histone désacétylase SAHA chez des macaques rhésus chinois infectés par le SIV, pour étudier les réservoirs viraux |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Préclinique (macaque) | PLoS Pathog | Schéma antirétroviral hautement intensifié : suppression virale durable et restriction du réservoir viral chez des macaques SIVmac251 |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Préclinique (macaque) | AIDS | Association d'un traitement antirétroviral et d'auranofine (composé d'or) : réduction du réservoir viral et contrôle de la charge virale après arrêt du traitement |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65199404 | DARUNAVIR BIOGARAN 800 mg | Comprimé pelliculé | Non renseignée |
| 68220711 | DARUNAVIR TEVA 800 mg | Comprimé pelliculé | Non renseignée |
| 67422090 | DARUNAVIR EG 400 mg | Comprimé pelliculé | Non renseignée |
| 63124787 | DARUNAVIR VIATRIS 600 mg | Comprimé pelliculé | Non renseignée |
| 65602549 | DARUNAVIR VIATRIS 800 mg | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur des études précliniques chez le macaque, sans essai clinique ni démonstration de l'activité propre du darunavir. Il s'agit d'un substitut de l'indication VIH déjà connue, sans indication humaine nouvelle.
- Les autres prédictions du modèle (syndrome d'immunodéficience acquise féline, trouble neurodéveloppemental rare, hyperlipidémie familiale combinée obsolète) sont encore moins étayées. Elles sont en L4 ou L5 et semblent liées à des artefacts du graphe de connaissances. Pour l'hyperlipidémie, la relation est plutôt un risque, car les inhibiteurs de protéase sont associés à des dyslipidémies.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), obligatoire avant toute évaluation de sécurité
- Données détaillées sur le mécanisme d'action (MOA), par exemple via l'API DrugBank
- Texte des indications approuvées des AMM françaises, pour confirmer l'indication originale
- Vérification du texte intégral des 4 publications pour établir si le darunavir figurait dans les schémas testés
- Données d'activité du darunavir sur la protéase du SIV, en études précliniques dédiées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

