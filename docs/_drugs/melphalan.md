---
layout: default
title: Melphalan
parent: Prédiction du modèle uniquement (L5)
nav_order: 478
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Melphalan : nouvelle indication prédite, Tumeur germinale gonadique (niveau de preuve L5). Indication d'origine : Cancer de l'ovaire"
monitor_inn: "MELPHALAN"
predicted_indications: ["gonadal germ cell tumor", "ovarian primitive germ cell tumor", "choriocarcinoma of ovary", "female breast carcinoma", "malignant non-epithelial tumor of ovary", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
---

# Melphalan
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

# Melphalan : Du Cancer de l'Ovaire à la Tumeur Germinale Gonadique

## Résumé en Une Phrase

Melphalan est un agent alkylant, initialement utilisé dans le traitement du cancer de l'ovaire et de tumeurs apparentées (adénocarcinomes ovariens, tumeurs germinales de l'ovaire, etc.).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tumeur germinale gonadique**,
avec **7 essais cliniques** (dont 2 directement pertinents) et **1 publication** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de l'ovaire (les textes d'indication des AMM françaises ne sont pas renseignés ; l'indication provient du graphe de connaissances) |
| Nouvelle Indication Prédite | Tumeur germinale gonadique |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L2 (selon l'évaluation compilée ; essais de phase 2 achevés, mais mélphalan non confirmé comme composant du schéma principal) |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, melphalan est un agent alkylant bifonctionnel : il crée des ponts entre les brins d'ADN, ce qui bloque la division des cellules tumorales et induit leur mort.

Les tumeurs germinales sont connues pour leur forte chimiosensibilité aux agents endommageant l'ADN. Les indications originales de melphalan comprennent déjà des tumeurs germinales de l'ovaire (tumeur du sac vitellin, tumeurs germinales malignes non dysgerminomateuses, choriocarcinome ovarien primitif). La nouvelle indication prédite est donc proche de l'indication d'origine, ce qui rend la prédiction plausible sur le plan biologique.

Des schémas de chimiothérapie à haute dose contenant du melphalan, suivis d'une autogreffe de cellules souches, ont été testés dans les tumeurs germinales récidivantes ou de mauvais pronostic. Ces schémas entraînent toutefois une toxicité importante, notamment une myélosuppression sévère.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Terminé | 64 | Chimiothérapie à haute dose en 2 cycles (gemcitabine, docétaxel, melphalan, carboplatine, puis ifosfamide, carboplatine, étoposide) dans les tumeurs germinales récidivantes de mauvais pronostic ; le rôle du melphalan au sein du schéma n'est pas isolé |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Terminé | 25 | Escalade de dose de melphalan avec support de cellules souches autologues et amifostine, chez des patients atteints de cancers variés |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Terminé | 451 | Huit schémas de chimiothérapie à haute dose avec autogreffe dans des hémopathies malignes et certaines tumeurs solides ; population hétérogène |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Terminé | 25 | Busulfan, melphalan et topotécan suivis d'une autogreffe dans des tumeurs avancées ou récidivantes ; contribution du melphalan non séparable |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | Non applicable | Terminé | 174 | Chimiothérapie à haute dose avec ou sans irradiation corporelle totale avant autogreffe ; faible spécificité |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Arrêté | 13 | Amifostine comme chimioprotecteur lors d'une autogreffe dans des tumeurs pédiatriques ; soins de support, sans lien avec l'efficacité |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Terminé | 6 | Melphalan intrathécal dans la méningite néoplasique ; contexte différent, non pertinent pour l'efficacité dans les tumeurs germinales |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Préclinique / autre | Acta - Unio Internationalis Contra Cancrum | Influence d'agents hormonaux et alkylants sur la fonction folliculo-stimulante de l'hypophyse ; ancienne et peu pertinente pour l'efficacité antitumorale |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68262525 | ALKERAN 2 mg, comprimé pelliculé (annulée) | Comprimé pelliculé | Non renseignée |
| 68708664 | ALKERAN 50 mg/10 ml, lyophilisat et solution pour usage parentéral (I.V.) (annulée) | Lyophilisat et solution pour usage parentéral | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, moutarde azotée) |
| Risque de Myélosuppression | Élevé (en particulier avec les schémas à haute dose avec support de cellules souches) |
| Classification d'Émétogénicité | Veuillez consulter la notice |
| Éléments de Surveillance | NFS (leucocytes, neutrophiles, plaquettes, hémoglobine), fonction rénale et hépatique, fonction pulmonaire |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (non issues du texte de la notice) : maladie rénale, thrombopénie, anémie (dont anémie macrocytaire et hémolytique), leucopénie, agranulocytose, neutropénie (y compris formes congénitales et constitutionnelles), pneumopathie interstitielle, fibrose pulmonaire, atteinte hépatique d'origine médicamenteuse, vascularite.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Modérées : amphotéricine B (y compris formes lipidique, sulfate de cholestéryl et liposomale).
  - Mineures : cimétidine, lévofloxacine, sulfate de zinc, gluconate de zinc.
  - Niveau non classé : lansoprazole, oméprazole, pantoprazole, famotidine, dolasétron, granisétron, acide acétylsalicylique, morphine, metformine, vancomycine, prednisone, simvastatine.

Les mises en garde et contre-indications issues de la notice française ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les essais sont de petite taille ou à population hétérogène, et le melphalan est le plus souvent administré en association à haute dose, sans démonstration de sa contribution propre. Aucun essai de phase 3 n'est disponible.
- Les deux AMM françaises sont annulées et les données de sécurité issues de la notice manquent. L'étape de dépistage de sécurité ne peut donc pas être franchie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice (mises en garde et contre-indications) auprès de l'ANSM.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Publier ou analyser les résultats de l'essai NCT00936936 pour isoler la contribution du melphalan.
- Disposer de données spécifiques aux tumeurs germinales gonadiques (phase 2/3), et clarifier le statut réglementaire et la voie d'administration, étant donné l'annulation des AMM.
- Établir un plan de surveillance de la myélosuppression et de la toxicité organique.

**Autres indications prédites :** la tumeur germinale primitive de l'ovaire (L3) et le carcinome mammaire féminin (L2) disposent de preuves limitées, avec une toxicité importante pour les schémas à haute dose. Le choriocarcinome de l'ovaire, la tumeur ovarienne non épithéliale maligne et les adénocarcinomes mucineux (rectum, côlon, vésicule biliaire, col de l'utérus, endomètre) reposent uniquement sur la prédiction du modèle (L5) et restent en attente (Hold).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

