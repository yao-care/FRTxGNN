---
layout: default
title: Sirolimus
parent: Prédiction du modèle uniquement (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus : Du Carcinome Rénal à Cellules à la Lipo­sarcome

## Résumé en Une Phrase

Le sirolimus est un inhibiteur de mTOR, dont les indications d'origine dans les données compilées sont le carcinome rénal (dont le carcinome à cellules claires) et la lymphangioléiomyomatose (LAM).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **liposarcome**, mais les preuves restent limitées : **1 essai clinique** de phase 2 à bras unique (associant le sirolimus au cyclophosphamide) et **7 publications**, dont la plupart sont des revues ou des données indirectes.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome rénal (carcinome à cellules claires, non papillaire) et lymphangioléiomyomatose (le texte des indications des AMM n'est pas renseigné ; source : graphe de connaissances) |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L2 (selon le niveau attribué dans les données ; essai de phase 2 unique, à bras unique, sans groupe contrôle) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold (question de recherche) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. Sur la base des connaissances générales, le sirolimus inhibe le complexe mTORC1, une kinase centrale qui régule la croissance et la prolifération cellulaires. Son efficacité dans la LAM a été démontrée, cette maladie étant due à la perte de TSC1/TSC2 et à une activation permanente de mTORC1.

La voie PI3K/AKT/mTOR est décrite comme activée dans les sarcomes des tissus mous, dont le liposarcome. L'inhibition de mTOR y est donc plausible sur le plan biologique, et des modèles murins évoqués dans la description de l'essai suggèrent qu'elle peut freiner la croissance tumorale.

Cette plausibilité reste toutefois indirecte. Le seul essai disponible associe le sirolimus à un autre médicament (dont le partenaire est tronqué dans le titre), ce qui empêche d'isoler la contribution propre du sirolimus. Les articles sur les patients transplantés suggérant une réduction du risque de cancer sous sirolimus ne constituent qu'un appui indirect.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Terminé | 70 | Essai à bras unique associant sirolimus et cyclophosphamide dans le liposarcome myxoïde et le chondrosarcome métastatiques ou non résécables ; les résultats d'efficacité ne sont pas détaillés dans les données compilées |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECR (analyse secondaire) | J Am Soc Nephrol | Chez des transplantés rénaux, le sirolimus après arrêt précoce de la ciclosporine réduit le risque de cancer (soutien indirect) |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revue | Cancers | Progrès thérapeutiques récents dans les sarcomes des tissus mous |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revue | Curr Opin Oncol | Essais récents sur les thérapies ciblées dans les sarcomes avancés |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revue | Bull Cancer | Traitements ciblés des tumeurs conjonctives rares et des sarcomes |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Revue | Transplant Proc | Dépistage des cancers chez les transplantés rénaux sous immunosuppresseurs (indirect) |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohorte | Fam Cancer | Spectre clinique du syndrome des hamartomes PTEN (indirect) |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Rapport de cas | Diagn Pathol | Anomalies vasculaires fibro-adipeuses et voie mTOR (indirect) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61752409 | RAPAMUNE 1 mg/ml | Solution buvable | Non renseignée (AMM annulée) |
| 64597615 | RAPAMUNE 1 mg | Comprimé enrobé | Non renseignée (AMM annulée) |
| 65164182 | RAPAMUNE 2 mg | Comprimé enrobé | Non renseignée (AMM annulée) |
| 69171174 | RAPAMUNE 0,5 mg | Comprimé enrobé | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de mTOR) ; indications d'origine oncologiques (carcinome rénal) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; une surveillance hématologique, hépatique, rénale et lipidique est généralement pertinente (voir contre-indications issues du graphe de connaissances) |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie, diabète et acidocétose diabétique, hypertriglycéridémie et hyperlipidémie, accident vasculaire cérébral et maladies cérébrovasculaires, hyperbilirubinémie (dont syndrome de Gilbert), pneumopathie interstitielle, maladies infectieuses (pneumocystose, infection à cytomégalovirus, leucoencéphalopathie multifocale progressive), cancer (dont cancer du cerveau), épanchement péricardique.
- **Interactions médicamenteuses** (100 interactions recensées ; extrait) :
  - Majeures : amphotéricine B (y compris complexe lipidique), mésalazine, balsalazide, clarithromycine.
  - Modérées : antidiabétiques (acarbose, metformine, pioglitazone, alogliptine, canagliflozine, dapagliflozine, chlorpropamide, albiglutide), corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), aprépitant, cimétidine.

## Conclusion et Prochaines Étapes

**Décision : Hold (question de recherche)**

**Justification :**
- Pour le liposarcome, la seule preuve clinique est un essai de phase 2 à bras unique en association, sans résultats détaillés ni contrôle. La littérature se compose surtout de revues et de données indirectes. Le niveau L2 attribué repose sur un essai de faible poids probant.
- Les données de sécurité de la notice manquent (lacune bloquante), et toutes les AMM françaises sont annulées, ce qui empêche d'avancer vers un criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) et les données de mécanisme d'action depuis DrugBank.
- Obtenir les résultats publiés de NCT02821507 et en isoler la contribution du sirolimus ; vérifier la composition des sous-types de sarcome.
- Rechercher des essais randomisés ou comparatifs de sirolimus dans le liposarcome.
- Clarifier la situation réglementaire française (AMM annulées) et la disponibilité des formes.

**Remarques complémentaires :**
- D'autres prédictions sont mieux étayées, mais concernent des indications déjà existantes. La LAM (« lymphangiomyome », niveau L1, phase 3 MILES NCT00414648) confirme une indication d'origine plutôt qu'un vrai repositionnement. Le « PEComa pulmonaire » correspond à la LAM pulmonaire et relève du même constat.
- Les PEComas bénins (L4) et utérins reposent sur un rationnel mécanistique fort (perte de TSC1/TSC2), mais uniquement sur des cas cliniques et des séries rétrospectives.
- Les sous-types de carcinome rénal, le liposarcome myxoïde ovarien et le sarcome vulvaire n'ont qu'une prédiction du modèle ou des données non spécifiques (L5, Hold).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

