---
layout: default
title: Ifosfamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Ifosfamide
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

# Ifosfamide : D'une Indication Originale Non Renseignée au Carcinome Mammaire Féminin

## Résumé en Une Phrase

L'ifosfamide est un agent alkylant (chimiothérapie cytotoxique) commercialisé en France sous le nom HOLOXAN. Le texte de son indication originale n'est pas renseigné dans les données de l'ANSM fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome mammaire féminin**, avec **8 essais cliniques** et **20 publications** associés. Aucun essai de phase 3 terminé ne porte toutefois directement sur le cancer du sein.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide pour les 2 AMM) |
| Nouvelle Indication Prédite | Carcinome mammaire féminin |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L3 (voir la note ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

**Note sur le niveau de preuve :** le dossier d'évidence attribue L1, mais les critères ne sont pas remplis : il n'y a pas 2 ECR de phase 3 terminés dans le cancer du sein. Le seul essai de phase 3 (NCT00954174) est de statut « inconnu », sans résultats, et concerne le carcinosarcome gynécologique. Les données mammaires reposent sur des études de phase 2 et des séries de patientes, d'où L3.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base DrugBank fournie. D'après le dossier d'évidence, l'ifosfamide est un promédicament alkylant qui doit être activé par les enzymes hépatiques CYP450 (CYP3A4, CYP2B6, CYP2C9). Son métabolite actif forme des pontages sur l'ADN et provoque la mort des cellules tumorales.

Des travaux de la littérature soutiennent ce lien pour le sein. Les tissus tumoraux mammaires expriment ces enzymes et métabolisent l'ifosfamide (PMID 14970873). Des lésions de l'ADN ont aussi été observées dans les cellules tumorales de patientes traitées (PMID 11138456). Les études de phase 2 montrent surtout une activité dans les cancers du sein déjà traités ou résistants aux anthracyclines.

Comme l'indication originale n'est pas renseignée, la relation avec la nouvelle indication ne peut pas être analysée précisément. Le score TxGNN (0,999) est une prédiction du modèle et non une preuve clinique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Inconnu | 637 | Paclitaxel + carboplatine vs ifosfamide + paclitaxel dans le carcinosarcome de l'utérus, des trompes, du péritoine ou de l'ovaire (pas le sein). Aucun résultat fourni |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Inconnu | 42 | Docétaxel + ifosfamide en première ligne du cancer du sein métastatique. Étude à un seul bras, de petite taille |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Inconnu | N/D | Chimiothérapie à haute dose multicycle vs chimiothérapie conventionnelle optimisée dans le cancer du sein métastatique. Rôle propre de l'ifosfamide non isolable |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminé prématurément | N/D | Topotécan, ifosfamide/mesna et étoposide à dose intensive avec autogreffe de cellules souches dans le cancer du sein métastatique |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Complété | 33 | Cycles séquentiels à haute dose (cisplatine, cyclophosphamide, étoposide, ifosfamide, carboplatine, taxol) avec autogreffe. Données de faisabilité et de sécurité |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminé prématurément | 12 | Samarium-153 avec double autogreffe de moelle dans le cancer du sein stade IV. Ifosfamide composant mineur |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminé prématurément | 7 | Lymphocytes T activés après autogreffe dans le cancer du sein stade IV. Ifosfamide en conditionnement de fond |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | Non applicable | Inconnu | 35 | Sélection de chimiothérapie par criblage sur organoïdes dans les tumeurs solides réfractaires. L'ifosfamide n'est pas une intervention définie |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 | Cancer | Paclitaxel en perfusion de 24 h + ifosfamide dans le cancer du sein métastatique résistant aux anthracyclines : évaluation de l'efficacité et de la tolérance |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Phase 2 | Tumori | Ifosfamide + étoposide chez des patientes déjà traitées pour un cancer du sein avancé : réponse et toxicité évaluées |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Étude clinique | J Chemother | Ifosfamide, mesna et épirubicine en deuxième ligne (16 patientes) : taux de réponse global de 50 %, durée médiane de rémission de 9,6 mois |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Étude clinique | J Clin Oncol | Ifosfamide + vinorelbine en première ligne du cancer du sein métastatique : efficacité et toxicité |
| [10602903](https://pubmed.ncbi.nlm.nih.gov/10602903/) | 1999 | Étude clinique prospective | Cancer Chemother Pharmacol | Ifosfamide + vinorelbine après anthracyclines dans le cancer du sein métastatique, avec évaluation du schéma d'administration |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Étude clinique | Cancer Chemother Pharmacol | Ifosfamide/étoposide avec mesna chez 44 patientes atteintes d'un cancer du sein avancé réfractaire |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Étude clinique | Cancer Chemother Pharmacol | Ifosfamide à la place du cyclophosphamide dans le schéma CMF chez 25 patientes résistantes ou en rechute |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Étude clinique | Curr Probl Cancer | Expérience de la chimiothérapie à base d'ifosfamide dans le cancer du sein métaplasique, variante rare peu sensible aux anthracyclines et taxanes |
| [7695982](https://pubmed.ncbi.nlm.nih.gov/7695982/) | 1995 | Cohorte PK | Eur J Cancer | Pharmacocinétique et métabolisme de l'ifosfamide (5 g/m² en 24 h) chez 15 patientes atteintes d'un cancer du sein |
| [14970873](https://pubmed.ncbi.nlm.nih.gov/14970873/) | 2004 | Préclinique | Br J Cancer | Expression de CYP3A4, CYP2C9 et CYP2B6 et métabolisation de l'ifosfamide dans les microsomes de tissu tumoral mammaire |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61848140 | HOLOXAN 1000 mg (BAXTER) | Poudre pour solution injectable | Non renseignée |
| 69622218 | HOLOXAN 2000 mg (BAXTER) | Poudre pour usage parentéral | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, promédicament) |
| Risque de Myélosuppression | Élevé (myélosuppression signalée dans le dossier, aussi liée aux syndromes myélodysplasiques secondaires) |
| Classification d'Émétogénicité | Moyenne à élevée selon la dose (estimation d'après la classe, à confirmer avec la notice) |
| Éléments de Surveillance | NFS avec différentielle, fonction rénale, fonction hépatique, analyse d'urine (hématurie), état neurologique |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

Ces éléments sont déduits de la classe du médicament et du dossier d'évidence, car DrugBank ne fournit pas de données de toxicité détaillées ici. Veuillez consulter les mises en garde et précautions de la notice.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Le dossier ne contient ni mises en garde, ni contre-indications, ni interactions médicamenteuses exploitables.

À titre indicatif, le dossier d'évidence signale ces risques connus de l'ifosfamide :
- néphrotoxicité ;
- neurotoxicité, dont un cas d'encéphalopathie (PMID 41818182) ;
- cystite hémorragique, prévenue par le mesna ;
- myélosuppression ;
- syndromes myélodysplastiques et leucémies secondaires.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le cancer du sein, les preuves se limitent à des études de phase 2 anciennes et de petite taille, surtout chez des patientes en maladie avancée ou prétraitées. Le seul essai de phase 3 est de statut inconnu, sans résultats, et ne concerne pas le sein.
- Les données de sécurité de l'ANSM manquent (lacune bloquante), ce qui empêche un criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées).
- Récupérer les données de mécanisme d'action via DrugBank.
- Obtenir des données comparatives ou des essais randomisés dans le cancer du sein, y compris les variantes rares comme le cancer métaplasique.
- Définir un plan de surveillance de sécurité (rein, système nerveux, vessie, moelle osseuse).

À noter : parmi les autres indications prédites, seul le **rhabdomyosarcome** est bien étayé (niveau L1, Proceed with Guardrails). L'ifosfamide y fait déjà partie des schémas standards, ce qui relève de la confirmation plutôt que d'un repositionnement nouveau. Les autres prédictions (syndromes myélodysplasiques, anémies, leucémie monocytaire) reposent sur le modèle seul ou vont à l'encontre du profil de toxicité du médicament, et restent en Hold.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

