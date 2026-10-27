---
layout: default
title: Rifaximin
parent: Preuves modérées (L3-L4)
nav_order: 667
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Rifaximin : nouvelle indication prédite, Candidose buccale (niveau de preuve L4). Indication d'origine : Encéphalopathie hépatique…"
monitor_inn: "rifaximin"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
---

# Rifaximin
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **6** 
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

## Rifaximine : De l'Encéphalopathie Hépatique à la Candidose Buccale
{: .text-alpha }

## Résumé en Une Phrase

La rifaximine est un antibiotique oral peu absorbé, initialement utilisé pour le traitement de l'encéphalopathie hépatique et du coma hépatique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **candidose buccale**, mais **aucun essai clinique** et **une seule publication** sont associés à cette prédiction, et cette publication évoque plutôt un signal de risque (infections à *Candida* résistantes) qu'un bénéfice thérapeutique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Encéphalopathie hépatique, coma hépatique (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Prédite | Candidose buccale |
| Score de Prédiction TxGNN | 99,75 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la rifaximine est un antibactérien oral faiblement absorbé, dont l'action se concentre dans l'intestin. Son efficacité dans l'encéphalopathie hépatique repose sur la réduction de la flore bactérienne intestinale.

**La prédiction ne repose sur aucun lien mécanistique solide.** La rifaximine n'a pas d'activité antifongique connue. Le score élevé du modèle semble refléter des associations au sein du réseau de connaissances plutôt qu'un bénéfice clinique démontré. La seule publication rattachée suggère même l'inverse : l'usage de la rifaximine a été associé à des infections à *Candida* résistantes à la micafungine chez des receveurs de greffe allogénique de cellules souches hématopoïétiques, ce qui évoque une perturbation du microbiote intestinal favorisant *Candida*.

### Autres prédictions examinées

Les autres prédictions du modèle ne sont pas mieux étayées :

| Maladie prédite | Score TxGNN | Niveau de preuve | Remarque |
|------|------|------|------|
| Fistule commissurale des lèvres | 99,64 % | L5 | Aucune étude ; pas de lien mécanistique identifiable |
| Ostéoradionécrose de la mandibule | 99,64 % | L5 | Aucune étude ; l'absorption systémique minime rend l'atteinte de l'os irradié improbable |
| Leucoedème buccal | 99,64 % | L5 | Aucune étude ; variante bénigne de la muqueuse, sans besoin thérapeutique |
| Syndrome de la bouche brûlante | 99,64 % | L5 | Aucune étude ; mécanismes plutôt neuropathiques et hormonaux |
| Candidose (générale) | 99,15 % | L4 | Deux études observationnelles indirectes, suggérant un risque et non un bénéfice |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohorte | Annals of Hematology | Chez des receveurs de greffe allogénique de cellules souches hématopoïétiques, l'usage de la rifaximine en prophylaxie a été associé à des infections à *Candida* résistantes à la micafungine : signal de risque, non de bénéfice |

Pour la candidose en général, une étude cas-témoins supplémentaire ([32360775](https://pubmed.ncbi.nlm.nih.gov/32360775/), 2021, *Clinical Microbiology and Infection*) a identifié les facteurs de risque de candidémie chez des patients hospitalisés atteints de cirrhose, population qui reçoit couramment de la rifaximine. Elle est indirecte et ne démontre aucun bénéfice thérapeutique.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63467355 | TIXTAR 550 mg, comprimé pelliculé (ALFASIGMA FRANCE) | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : colite à *Clostridium difficile* et entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** : 69 interactions recensées, dont une de niveau majeur et la plupart de niveau modéré.
  - **Majeure** : vaccin vivant contre le choléra (*Vibrio cholerae* CVD 103-HgR).
  - **Modérées (exemples)** : warfarine, ciclosporine, tolvaptan, alpélisib, apalutamide, darolutamide, cabozantinib, brigatinib, encorafénib, élagolix, élexacaftor, éliglustat, énasidénib, daclatasvir, lédipasvir, acide picosulfurique, acide bempédoïque, istradéfylline, capmatinib.
- **Signal spécifique à cette prédiction** : une association entre l'usage de la rifaximine et des infections à *Candida* résistantes a été rapportée chez des patients greffés.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,75 %), mais il n'est soutenu par aucun essai clinique, et la seule publication directement liée évoque un risque d'infections à *Candida* plutôt qu'un bénéfice. Le niveau de preuve est L4 et le mécanisme antifongique est absent. Les autres indications prédites relèvent du niveau L5 (prédiction du modèle uniquement).
- L'unique AMM française est annulée, et les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), donnée bloquante.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Produire des données précliniques ou cliniques démontrant une éventuelle activité contre la candidose, et évaluer le signal de risque fongique associé à la rifaximine.
- Clarifier la pertinence de la prédiction par rapport à l'indication d'origine (similarité à documenter) et la compatibilité des voies d'administration (voie orale, action intestinale, face à une atteinte buccale).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

