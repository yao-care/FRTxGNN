---
layout: default
title: Eribulin
parent: Prédiction du modèle uniquement (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eribulin : nouvelle indication prédite, Néoplasme fibroblastique (niveau de preuve L5). Indication d'origine : Liposarcome"
monitor_inn: "eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "ovarian myxoid liposarcoma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Éribuline : Du Liposarcome au Néoplasme Fibroblastique
{: .text-alpha }

## Résumé en Une Phrase

L'éribuline est un agent antimitotique (inhibiteur de la dynamique des microtubules) utilisé à l'origine pour le traitement du liposarcome.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **néoplasme fibroblastique** (par exemple la tumeur fibreuse solitaire), avec **1 essai clinique** de phase 2 et **8 publications** soutenant actuellement cette direction, essentiellement précliniques.

*Remarque : parmi les 10 indications prédites, le néoplasme fibroblastique (rang 8 du modèle) est la seule à disposer d'un essai clinique. Il a été retenu comme indication principale de ce rapport, car il est le mieux documenté. Les autres prédictions n'ont aucune preuve ou des preuves très limitées.*

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Liposarcome (selon le graphe de connaissances TxGNN ; aucun texte d'indication n'est disponible dans les AMM françaises) |
| Nouvelle Indication Prédite | Néoplasme fibroblastique |
| Score de Prédiction TxGNN | 99,36 % |
| Niveau de Preuve | L2 (un essai de phase 2 terminé, sans résultats disponibles) |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'éribuline est un inhibiteur de la dynamique des microtubules (agent anti-tubuline). Son efficacité dans le liposarcome est reconnue, et elle est également utilisée comme chimiothérapie de deuxième ligne dans les sarcomes des tissus mous.

Le liposarcome et les néoplasmes fibroblastiques (dont la tumeur fibreuse solitaire et le fibrosarcome) sont tous deux des tumeurs mésenchymateuses. Une activité antimitotique est donc plausible. Les travaux précliniques sur des lignées de fibrosarcome (HT1080) montrent une sensibilité à l'éribuline, des mécanismes de résistance, ainsi qu'une synergie avec la méthioninase recombinante. Des modèles de xénogreffes de tumeur fibreuse solitaire suggèrent aussi un potentiel de l'éribuline.

Cette cohérence biologique reste toutefois indirecte : aucune donnée d'efficacité clinique n'est disponible, et la similarité formelle avec l'indication d'origine n'a pas été évaluée.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Terminé | 16 | Étude ERASING : éribuline dans la tumeur fibreuse solitaire avancée (groupe italien des sarcomes). Résultats non fournis ; petit effectif |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Revue | Cancers | Diagnostic et traitement des tumeurs fibreuses solitaires extraméningées |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Préclinique (xénogreffe) | Eur J Cancer | Xénogreffes de tumeur fibreuse solitaire : forte sensibilité à doxorubicine/dacarbazine ; efficacité potentielle de la trabectédine ou de l'éribuline |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Préclinique (in vitro) | Anticancer Res | Synergie de la méthioninase recombinante et de l'éribuline sur les cellules de fibrosarcome, mais pas sur les fibroblastes normaux |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Préclinique (in vitro) | Anticancer Res | La méthioninase recombinante multiplie par 16 l'efficacité de l'éribuline dans des cellules HT1080 très résistantes |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Préclinique (in vitro/souris) | In Vivo | Les cellules HT1080 super-résistantes à l'éribuline sont plus malignes mais contrôlées par la combinaison éribuline + restriction en méthionine chez la souris |

*Trois autres publications (lignées cellulaires de myxofibrosarcome, rapport de cas sur une tumeur des gaines nerveuses périphériques traitée par entrectinib) sont peu pertinentes pour l'éribuline et ne sont pas détaillées.*

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63816522 | HALAVEN 0,44 mg/ml, solution injectable (EISAI) | Solution injectable | Non renseignée (AMM annulée) |
| 63980742 | ERIBULINE EVER PHARMA 0,44 mg/mL | Solution injectable | Non renseignée (AMM annulée) |
| 62435664 | ERIBULINE ZENTIVA 0,44 mg/mL | Solution injectable | Non renseignée (AMM annulée) |
| 60267292 | ERIBULINE ADVANZ PHARMA 0,44 mg/mL | Solution injectable | Non renseignée (AMM annulée) |
| 64894431 | ERIBULINE BAXTER 0,44 mg/mL | Solution injectable | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (inhibiteur de la dynamique des microtubules, agent anti-tubuline) |
| Risque de Myélosuppression | Élevé : la neutropénie, l'agranulocytose et la thrombocytopénie figurent parmi les contre-indications/conditions à risque du graphe de connaissances |
| Classification d'Émétogénicité | Veuillez consulter la notice |
| Éléments de Surveillance | NFS avec formule (neutrophiles, plaquettes), électrolytes (kaliémie), ECG (intervalle QT), fonction hépatique et rénale, examen neurologique (neuropathie périphérique) |
| Protection de Manipulation | Appliquer les règles de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Pathologies associées à un risque (graphe de connaissances, non issues de la notice)** : syndrome du QT long (y compris familial), thrombopénie, déficit en potassium, neutropénie, agranulocytose, maladie du système nerveux périphérique, neuropathie périphérique, constipation.
- **Interactions médicamenteuses** : 375 interactions recensées. Parmi celles listées, deux sont de niveau **majeur** : **dolasétron** et **cisapride** (risque probable lié à l'allongement du QT). Les interactions de niveau modéré incluent notamment l'ondansétron, le palonosétron, la clarithromycine, la lévofloxacine, le métronidazole, le tinidazole, la rosuvastatine, la simvastatine, la famotidine, le lopéramide et plusieurs laxatifs (bisacodyl, picosulfate, lactulose, lactitol, polyéthylène glycol, sulfate de sodium, huile de ricin).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à un petit essai de phase 2 (16 patients) sans résultats disponibles et à des études précliniques ; aucune donnée de phase 3 n'existe. Toutes les AMM françaises sont annulées et les données de sécurité de la notice font défaut, ce qui bloque le passage à l'étape de criblage de sécurité.
- Les neuf autres indications prédites (dont la fièvre méditerranéenne familiale, les mésothéliomes, le dermatofibrosarcome protubérant et le sarcome cardiaque) reposent presque uniquement sur la prédiction du modèle et restent en suspens.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice officielle (ANSM) avec mises en garde et contre-indications
- Données détaillées sur le mécanisme d'action (DrugBank)
- Résultats publiés de l'essai ERASING (NCT03840772) : taux de réponse, survie sans progression, tolérance
- Revue ciblée de la littérature sur l'éribuline dans la tumeur fibreuse solitaire et le fibrosarcome
- Clarification du statut réglementaire actuel de l'éribuline en France (AMM annulées vs. produits commercialisés)
- Plan de surveillance de sécurité (hématologique, cardiaque/QT, neurologique) et gestion des interactions majeures
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

