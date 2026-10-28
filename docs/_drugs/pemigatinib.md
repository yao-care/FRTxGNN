---
layout: default
title: Pemigatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 586
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Pemigatinib : nouvelle indication prédite, Néoplasie endocrinienne multiple (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM disponibles"
monitor_inn: "pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "axial spondylometaphyseal dysplasia"]
---

# Pemigatinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Pémigatinib : D'une indication d'origine non renseignée à l'Néoplasie endocrinienne multiple
{: .text-alpha }

## Résumé en Une Phrase

Le pémigatinib est un inhibiteur sélectif des récepteurs FGFR1 à 3, dont les autorisations de mise sur le marché françaises (AMM) sont aujourd'hui toutes annulées et dont l'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **néoplasie endocrinienne multiple**, mais il s'agit d'une prédiction pure du modèle.
Aucun essai clinique et aucune publication ne soutiennent cette direction (**0 essai clinique**, **0 publication**).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM disponibles |
| Nouvelle Indication Prédite | Néoplasie endocrinienne multiple |
| Score de Prédiction TxGNN | 0,9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. D'après les informations connues, le pémigatinib est un inhibiteur sélectif des récepteurs FGFR1, FGFR2 et FGFR3, une classe de thérapies ciblées en oncologie.

Les syndromes de néoplasie endocrinienne multiple (NEM) sont principalement liés à des altérations de *MEN1* et de *RET*. Aucun mécanisme dépendant de FGFR n'est établi pour ces syndromes. Le score élevé (0,9971) provient du modèle TxGNN (apprentissage profond) et peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique.

La prédiction doit être considérée comme une simple hypothèse, sans soutien mécanistique ni clinique à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67695203 | PEMAZYRE 13,5 mg, comprimé | Comprimé | Non renseignée (AMM active) |
| 66412702 | PEMAZYRE 4,5 mg, comprimé | Comprimé | Non renseignée (AMM active) |
| 61156252 | PEMAZYRE 9 mg, comprimé | Comprimé | Non renseignée (AMM active) |

Les trois AMM sont détenues par Incyte Biosciences Distribution (Pays-Bas).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase FGFR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 50 interactions ont été identifiées dans les données compilées. Parmi les principales :
  - **Majeures** : aprépitant, dexaméthasone, clarithromycine, cobicistat, lumacaftor, chloramphénicol, érythromycine, kétoconazole, fluconazole.
  - **Modérées** : cimétidine, métréleptine, clotrimazole, phénylbutyrate de glycérol, troglitazone, déférasirox, ivacaftor, zafirlukast, griséofulvine, elagolix, osilodrostat.

  Plusieurs de ces interactions concernent des inhibiteurs ou inducteurs enzymatiques (antifongiques azolés, macrolides, cobicistat), ce qui suggère une vigilance particulière sur le métabolisme. Seules 20 interactions sont détaillées ici.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations de sécurité.

## Autres Prédictions Évaluées

Les autres indications prédites présentent toutes un niveau de preuve L5 et une recommandation Hold :

| Rang | Indication prédite | Score TxGNN | Commentaire |
|------|------|------|------|
| 2 | Aménorrhée | 0,9954 | Symptôme multifactoriel, aucun mécanisme plausible |
| 3 | Carcinome du sein HER2 positif | 0,9949 | Rationnel biologique faible (FGFR et résistance aux thérapies anti-HER2) ; une seule revue générale sur les inhibiteurs de kinases (PMID 33513356, 2021), non spécifique |
| 4 | Infection à cytomégalovirus | 0,9946 | Aucun lien connu |
| 5 | Rhinotrachéite infectieuse bovine | 0,9943 | Maladie vétérinaire |
| 6 | Catarrhe malin | 0,9943 | Maladie vétérinaire |
| 7 | Sclérose latérale amyotrophique | 0,9941 | Rôle de FGF/FGFR incertain, effet potentiellement délétère |
| 8 | SLA de type 22 | 0,9927 | Redondant avec la SLA |
| 9 | SLA, susceptibilité | 0,9925 | Redondant avec la SLA |
| 10 | Dysplasie spondylométaphysaire axiale | 0,9925 | Aucun lien FGFR établi |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et sans mécanisme FGFR plausible pour la néoplasie endocrinienne multiple.
- Les 3 AMM françaises sur 3 sont valides et le médicament est commercialisé, mais les données de sécurité de la notice manquent, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (point bloquant).
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Clarifier l'indication d'origine et les raisons de l'annulation des AMM.
- Rechercher des preuves précliniques ou cliniques spécifiques reliant la signalisation FGFR à la néoplasie endocrinienne multiple, ou réorienter l'évaluation vers des indications oncologiques à rationnel biologique plus solide.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

