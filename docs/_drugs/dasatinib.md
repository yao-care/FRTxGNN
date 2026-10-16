---
layout: default
title: Dasatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dasatinib : nouvelle indication prédite, Sarcome d'Ewing (niveau de preuve L5). Indication d'origine : Leucémie myéloïde chronique BCR-ABL1 positive"
---

# Dasatinib
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

# Dasatinib : De la leucémie myéloïde chronique BCR-ABL1 positive au sarcome d'Ewing

## Resume en Une Phrase

Dasatinib est un inhibiteur de tyrosine kinases, initialement utilisé pour le traitement de la leucémie myéloïde chronique BCR-ABL1 positive (y compris en phase blastique).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **sarcome d'Ewing**, mais les preuves restent limitées : **2 essais cliniques** (Phase 1/2 terminé prématurément et Phase 2 en sarcomes mixtes) et **10 publications**, majoritairement précliniques, soutiennent actuellement cette direction.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Leucémie myéloïde chronique BCR-ABL1 positive (le texte d'indication des AMM n'est pas renseigné dans les données compilées ; indication issue du graphe de connaissances) |
| Nouvelle Indication Predite | Sarcome d'Ewing |
| Score de Prediction TxGNN | 99,90 % |
| Niveau de Preuve | L2 (selon les données compilées ; voir la réserve ci-dessous) |
| Statut de Marche en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Decision Recommandee | Hold |

*Réserve sur le niveau de preuve : les données compilées attribuent L2, mais les deux essais disponibles ne sont ni des ECR de Phase 2/3 ni concluants. L'essai de Phase 2 (NCT00464620) est à un seul bras, et une revue indique que dasatinib a échoué en monothérapie dans le sarcome d'Ewing. Une lecture prudente situerait donc ce niveau plutôt entre L3 et L4.*

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après la littérature, dasatinib inhibite BCR-ABL ainsi que les kinases de la famille SRC, et possède aussi une activité contre c-KIT et PDGFR. Son efficacité dans la leucémie myéloïde chronique repose sur l'inhibition de BCR-ABL.

Le lien avec le sarcome d'Ewing passe par SRC et non par BCR-ABL. Des études précliniques montrent que SRC favorise la formation d'invadopodes, la migration et l'invasion des cellules d'Ewing, et que dasatinib inhibe la migration et induit l'apoptose dans des cellules de sarcomes osseux dépendantes de SRC. La voie FAK-SRC est proposée comme cible dans ce sarcome.

Ce lien est plausible, mais il n'a pas été confirmé en clinique. Une revue de 2022 rapporte que dasatinib en monothérapie a échoué dans un essai de Phase 2 incluant des sarcomes d'Ewing et des rhabdomyosarcomes. Les pistes actuelles portent donc plutôt sur des associations, par exemple le schéma RIST (rapamycine, irinotécan, dasatinib, témozolomide), décrit dans une série de cas de 2026.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminé (arrêt anticipé) | 7 | Dasatinib avec ifosfamide, carboplatine et étoposide en pédiatrie ; seulement 7 patients, donc très peu d'informations sur l'efficacité et la sécurité |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Terminé | 366 | Dasatinib en monothérapie dans les sarcomes avancés (taux de réponse, survie sans progression à 6 mois) ; population mixte, résultats spécifiques au sarcome d'Ewing non fournis |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [42804591](https://pubmed.ncbi.nlm.nih.gov/42804591/) | 2026 | Série de cas | J Pediatr Hematol Oncol | Expérience monocentrique du schéma RIST (rapamycine, irinotécan, dasatinib, témozolomide) dans le sarcome d'Ewing en rechute |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Revue | Sarcoma | Ciblage du complexe FAK-SRC ; dasatinib en monothérapie a échoué dans le sarcome d'Ewing et le rhabdomyosarcome en Phase 2 |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revue | Oncol Lett | Importance de la signalisation SRC dans les sarcomes et faisabilité de SRC comme cible |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro | Cancer Res | Dasatinib inhibe la migration et l'invasion de lignées de sarcomes et induit l'apoptose dans les sarcomes osseux dépendants de SRC |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro | Oncol Rep | Activité antiproliférative et antimigratoire de dasatinib dans des lignées de neuroblastome et de sarcome d'Ewing |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | In vitro | Neoplasia | Le stress microenvironnemental active l'invasion des cellules d'Ewing via SRC |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | In vitro | Neoplasia | Coopération entre ténascine C et SRC dans la formation d'invadopodes du sarcome d'Ewing |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Revue | Curr Treat Options Oncol | Traitement systémique du chondrosarcome (pertinence indirecte pour le sarcome d'Ewing) |

---

## Informations de Marche en France

Les 20 AMM recensées sont toutes annulées ; le texte d'indication approuvée n'est pas renseigné. Les cinq premières sont listées ci-dessous.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60926629 | DASATINIB SANDOZ 100 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64498745 | DASATINIB KRKA 100 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 61237544 | DASATINIB BIOGARAN 50 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 66031135 | DASATINIB VIATRIS 20 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 63719525 | DASATINIB ZENTIVA 100 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Thérapie ciblée (inhibiteur de tyrosine kinases) |
| Risque de Myélosuppression | Élevé : la thrombopénie, la neutropénie et l'anémie figurent parmi les contre-indications relevées dans le graphe de connaissances, ce qui indique un risque hématologique à surveiller |
| Classification d'Emetogenicite | Faible à moyenne (estimation selon la classe ; non précisée dans les données compilées) |
| Elements de Surveillance | NFS avec formule, fonction hépatique, ECG (intervalle QT), surveillance des épanchements pleuraux et péricardiques |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considerations de Securite

- **Contre-indications ou terrains à risque (issus du graphe de connaissances, et non du texte de la notice)** : syndrome du QT long (y compris familial), torsades de pointes, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, neutropénie, agranulocytose, anémie, insuffisance cardiaque (congestive), infarctus du myocarde, hémoglobinopathie, ulcère gastroduodénal actif, hémorragie intracérébrale, épanchement péricardique et hémopéricarde.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - *Majeures* : famotidine, ranitidine, cimétidine, oméprazole, rabéprazole (antiacides et inhibiteurs de la sécrétion gastrique, avec réduction possible de l'absorption), dexaméthasone, acide acétylsalicylique, clarithromycine.
  - *Modérées* : hydrocortisone, budésonide, lopéramide, aprépitant, bisacodyl, oxyde de magnésium, hydroxyde d'aluminium, carbonate de calcium, saxagliptine, huile de ricin, polyéthylène glycol.

Les mises en garde et contre-indications issues de la notice de l'ANSM ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
- Le mécanisme (inhibition de SRC) est plausible et appuyé par des données précliniques, mais l'efficacité clinique dans le sarcome d'Ewing n'est pas démontrée, et dasatinib en monothérapie a échoué dans un essai de Phase 2. Les seuls éléments cliniques sont un essai terminé prématurément (7 patients), un essai en population mixte de sarcomes et une série de cas.
- Aucune AMM n'est actuellement valide en France pour ce médicament, ce qui complique toute perspective d'utilisation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats de l'essai NCT00464620 propres au sous-groupe sarcome d'Ewing
- Données prospectives sur les associations (par exemple le schéma RIST), idéalement dans un essai contrôlé
- Texte de la notice ANSM (mises en garde, contre-indications) et clarification du statut réglementaire des AMM annulées
- Données détaillées sur le mécanisme d'action
- Plan de surveillance de sécurité (hématologique, cardiaque, épanchements), notamment en population pédiatrique

---

*Remarque complémentaire : parmi les autres indications prédites, la « leucémie myéloïde » (rang 2) correspond largement à l'indication d'origine (LMC BCR-ABL1 positive) et ne constitue donc pas un véritable repositionnement. Elle est soutenue par plusieurs essais de Phase 3 (par exemple DASISION). Les indications des rangs 3 à 10 reposent sur des preuves précliniques ou sur la seule prédiction du modèle.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

