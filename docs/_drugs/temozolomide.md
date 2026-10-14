---
layout: default
title: Temozolomide
parent: Preuves élevées (L1-L2)
nav_order: 735
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **2** 
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

# Témozolomide : Des astrocytomes et du glioblastome à la tumeur astrocytaire de l'adulte

## Résumé en Une Phrase

Le témozolomide est un agent alkylant oral, initialement utilisé pour traiter l'astrocytome anaplasique, l'astrocytome (hors glioblastome) et le glioblastome cérébral.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tumeur astrocytaire de l'adulte**, mais cette indication recoupe en grande partie les indications d'origine : il s'agit plus d'une confirmation que d'un véritable repositionnement.
Les données compilées pour ce rapport comptent **2 essais cliniques** et **20 publications** pour cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Astrocytome anaplasique ; astrocytome (hors glioblastome) ; glioblastome cérébral (le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Tumeur astrocytaire de l'adulte |
| Score de Prédiction TxGNN | 99,36 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (dont 0 valide, 20 annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Selon les connaissances pharmacologiques générales, le témozolomide est un agent alkylant oral qui méthyle l'ADN (positions O6 et N7 de la guanine, N3 de l'adénine). Ces lésions sont cytotoxiques et entraînent l'apoptose des cellules tumorales.

L'efficacité est la plus marquée dans les tumeurs dont le promoteur du gène MGMT est méthylé, car leur capacité de réparation de l'ADN est réduite. Les tumeurs astrocytaires de l'adulte (astrocytome anaplasique et glioblastome) font déjà partie des indications d'origine du médicament. Le score élevé du modèle est donc cohérent avec une relation mécanisme-maladie bien établie.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Terminé | 500 | Essai randomisé comparant le témozolomide au schéma PCV (procarbazine, lomustine, vincristine) dans les tumeurs astrocytaires récidivantes de grade III et IV de l'OMS. Teste directement le témozolomide dans la maladie cible. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Terminé | 26 | Détermination de la dose maximale tolérée du XL184 (cabozantinib) associé au témozolomide et à la radiothérapie dans le glioblastome en première ligne. Étude de sécurité d'un autre agent ; peu de valeur directe pour l'efficacité du témozolomide. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | ECR | N Engl J Med | Radiothérapie avec témozolomide concomitant et adjuvant versus radiothérapie seule dans le glioblastome (essai fondateur) |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | ECR | Lancet Oncol | Analyse à 5 ans de l'essai de phase III EORTC-NCIC sur le témozolomide avec radiothérapie |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | ECR | Lancet Oncol | NOA-08 : témozolomide seul versus radiothérapie seule dans l'astrocytome malin du sujet âgé |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | ECR | Lancet | CeTeG/NOA-09 : association lomustine-témozolomide versus témozolomide standard dans le glioblastome à promoteur MGMT méthylé |
| [29260225](https://pubmed.ncbi.nlm.nih.gov/29260225/) | 2017 | ECR | JAMA | Champs de traitement des tumeurs (TTFields) avec témozolomide d'entretien versus témozolomide seul |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | ECR | JAMA | TTFields avec témozolomide d'entretien versus témozolomide seul dans le glioblastome |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | ECR | N Engl J Med | Essai randomisé du bévacizumab dans le glioblastome nouvellement diagnostiqué, sur fond de traitement standard par témozolomide |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | ECR | JAMA Oncol | Ajout du véliparib au témozolomide dans le glioblastome à MGMT méthylé |
| [34898238](https://pubmed.ncbi.nlm.nih.gov/34898238/) | 2022 | Recommandations | J Clin Oncol | Recommandations ASCO-SNO sur le traitement des tumeurs astrocytaires et oligodendrogliales diffuses de l'adulte |
| [17478095](https://pubmed.ncbi.nlm.nih.gov/17478095/) | 2007 | Revue | Crit Rev Oncol Hematol | Revue sur l'astrocytome anaplasique de l'adulte ; la chimiothérapie y a donné des résultats irréguliers selon les données randomisées |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60691017 | Temozolomide Accord 250 mg | Gélule | Non renseignée (AMM annulée) |
| 66186993 | Temozolomide Viatris 140 mg | Gélule | Non renseignée (AMM annulée) |
| 68196114 | Temodal 140 mg | Gélule | Non renseignée (AMM annulée) |
| 61710965 | Temodal 2,5 mg/ml | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 65421470 | Temozolomide Sun 5 mg | Gélule | Non renseignée (AMM annulée) |

Au total, 20 AMM sont enregistrées, toutes annulées ; seules les 5 premières sont listées ici.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant) |
| Risque de Myélosuppression | Élevé : les contre-indications issues du graphe de connaissances incluent thrombocytopénie, neutropénie, agranulocytose, pancytopénie et anémie aplasique |
| Classification d'Émétogénicité | Moyenne (selon la classe du médicament) |
| Éléments de Surveillance | NFS avec formule (neutrophiles, plaquettes), fonction hépatique et rénale |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, thrombocytopénie, neutropénie, agranulocytose, anémie, anémie macrocytaire, pneumocystose, pancytopénie, lymphopénie, syndrome myélodysplasique, anémie aplasique idiopathique, anémie aplasique.
- **Interactions médicamenteuses** : 320 interactions sont recensées. Parmi les principales, la naltrexone (modérée) et la lévofloxacine (mineure). Les autres interactions listées (par exemple oméprazole, prednisone, métformine, morphine) ont un niveau de gravité inconnu.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai randomisé de phase 3 terminé (NCT00052455) et plusieurs essais randomisés majeurs soutiennent le témozolomide dans les tumeurs astrocytaires. L'indication prédite recoupe les indications d'origine, donc l'enjeu est celui d'une confirmation et non d'un repositionnement.
- Toutes les AMM françaises sont annulées et le profil hématologique impose une surveillance étroite.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (données bloquantes pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (MOA)
- Clarification des raisons de l'annulation des AMM et de la disponibilité actuelle du produit en France
- Statut MGMT des patients et plan de surveillance hématologique

---

### Note sur la seconde indication prédite

Le modèle propose aussi la **néoplasie de la queue de cheval** (score 99,30 %), mais avec un niveau de preuve **L4** (décision : question de recherche). Seul un rapport de cas isolé, portant sur un épendymome myxopapillaire spinal récidivant, est pertinent ; aucun essai clinique n'est enregistré. Cette piste n'est pas recommandée à ce stade.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

