---
layout: default
title: Ezetimibe
parent: Prédiction du modèle uniquement (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
monitor_inn: "ezetimibe"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Ezetimibe : nouvelle indication prédite, Déficit en protéine de transfert des esters de cholestérol (niveau de preuve L5). Indication d'origine : Hyperlipidémie"
---

# Ezetimibe
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Ézétimibe : De l'hyperlipidémie au déficit en protéine de transfert des esters de cholestérol
{: .text-alpha }

## Résumé en Une Phrase

L'ézétimibe est un médicament hypocholestérolémiant, enregistré dans le graphe de connaissances pour l'hyperlipidémie, l'hypercholestérolémie familiale homozygote et la sitostérolémie.
Le modèle TxGNN prédit qu'il pourrait être utile dans le **déficit en protéine de transfert des esters de cholestérol (CETP)**,
mais **aucun essai clinique** et **aucune publication** ne l'étudie directement : cette prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperlipidémie (relation enregistrée dans le graphe de connaissances ; les textes d'indication des AMM ne sont pas renseignés dans les données compilées) |
| Nouvelle Indication Prédite | Déficit en protéine de transfert des esters de cholestérol |
| Score de Prédiction TxGNN | 0,9909 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | Au moins 20 (la liste peut être partielle) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales en pharmacologie, l'ézétimibe inhibe l'absorption intestinale du cholestérol via la protéine NPC1L1 et abaisse ainsi le LDL-cholestérol.

Le déficit en CETP se caractérise par un HDL-cholestérol élevé et un transfert réduit des esters de cholestérol des HDL vers les lipoprotéines contenant l'apoB. Les deux situations touchent le métabolisme des lipoprotéines, ce qui explique probablement le score élevé du modèle.

Cependant, le déficit en CETP est généralement un phénotype bénin, voire potentiellement protecteur, qui ne nécessite pas de traitement hypocholestérolémiant. Aucun lien mécanistique ou clinique direct entre l'inhibition de NPC1L1 et ce déficit n'a été démontré. La prédiction est vraisemblablement un artefact de proximité dans le réseau de connaissances.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les deux publications recensées ne portent pas directement sur l'ézétimibe dans le déficit en CETP : l'une est une revue générale sur les cibles hypolipémiantes, l'autre une étude animale (modèle de hamster) sur un anticorps anti-PCSK9.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Revue | European Heart Journal | Panorama des cibles hypolipémiantes (LDL-C, triglycérides, apoB, Lp(a)) et de leurs implications translationnelles ; pas d'étude directe sur le déficit en CETP |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Étude animale | International Journal of Molecular Sciences | Hamster Ldlr+/- comme modèle pour évaluer un anticorps anti-PCSK9 dans l'hyperlipidémie et l'athérosclérose ; sans lien direct avec l'ézétimibe |

## Informations de Marché en France

L'ézétimibe est commercialisé en France. Les données compilées recensent au moins 20 AMM, toutes valides, et la liste peut être partielle. Les textes d'indication approuvée ne sont pas renseignés. Plusieurs produits listés sont des associations (par exemple avec la rosuvastatine) ; leurs AMM ne décrivent pas l'usage de l'ézétimibe seul.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60887592 | EZETIMIBE ALMUS 10 mg | comprimé | Non renseignée |
| 69510055 | EZETIMIBE EG 10 mg | comprimé | Non renseignée |
| 65825737 | EZETIMIBE CRISTERS PHARMA 10 mg | comprimé | Non renseignée |
| 66718898 | EZETIMIBE SANDOZ 10 mg | comprimé | Non renseignée |
| 60981789 | EZETROL 10 mg | comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications relevées dans le graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : pancréatite, maladie du foie, maladie de la vésicule biliaire, myopathie, maladie musculaire, maladie du muscle squelettique, paralysie périodique familiale, abus/dépendance à une substance, rhabdomyolyse, fasciite nodulaire.
- **Interactions médicamenteuses** : 171 interactions recensées. Parmi les principales, de niveau modéré : acide chénodésoxycholique, éluxadoline, rosuvastatine, simvastatine. D'autres interactions (calcitriol, pantoprazole, metformine, oméprazole, morphine, vancomycine, etc.) ont un niveau de gravité non précisé.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication étudiant directement le déficit en CETP. Cette maladie est le plus souvent bénigne et ne justifie pas de traitement hypocholestérolémiant. Le lien est probablement un artefact du réseau.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action détaillé de l'ézétimibe
- Éléments de preuve directs (études mécanistiques ou cliniques) sur l'ézétimibe dans le déficit en CETP
- Démonstration d'un bénéfice clinique d'un traitement hypolipémiant dans cette maladie
- Mises en garde et contre-indications issues de la notice officielle de l'ANSM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

