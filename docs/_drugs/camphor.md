---
layout: default
title: Camphor
parent: Prédiction du modèle uniquement (L5)
nav_order: 132
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Camphor : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "camphor"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
---

# Camphor
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

## Camphre : De l'indication originale non renseignée à la migraine
{: .text-alpha }

## Résumé en Une Phrase

Le camphre est présent en France dans des spécialités homéopathiques (Camphora Lehning, Camphora Boiron, Rodulos), dont les trois AMM sont aujourd'hui annulées et pour lesquelles aucune indication approuvée n'est renseignée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine** (*migraine disorder*), mais aucun essai clinique n'est enregistré, et les **3 publications** associées sont des cas cliniques ou des analyses indirectes.
Le niveau de preuve reste faible : une étude préclinique récente (2026) soutient le lien avec la migraine, sans données humaines.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 0,9985 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances pharmacologiques générales, le camphre est un modulateur des canaux TRPV1, TRPM8 et TRPA1, doté de propriétés contre-irritantes et vasoactives. Ces propriétés pourraient être pertinentes pour la physiopathologie des céphalées.

Aucune indication originale n'étant renseignée, la relation avec la nouvelle indication ne peut pas être analysée directement. Le lien est donc uniquement mécanistique et indirect.

Une étude préclinique de 2026 (PMID 42849823) rapporte que le (+)-camphre naturel atténue, dans un modèle animal, une migraine induite par la réserpine avec vasospasme cérébral local, via l'inhibition de la voie p38β MAPK/ATF2. C'est le signal le plus prometteur, mais il reste préclinique. Les autres publications ne testent pas le camphre comme traitement de la migraine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42849823](https://pubmed.ncbi.nlm.nih.gov/42849823/) | 2026 | Étude préclinique animale | J Ethnopharmacol | Le (+)-camphre naturel atténue la migraine induite par la réserpine avec vasospasme cérébral local, via l'inhibition de la voie p38β MAPK/ATF2 |
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Série de cas | Headache | Cinq cas d'algie vasculaire de la face secondaires à l'usage de dentifrices contenant des huiles essentielles pro-convulsivantes |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Cas clinique | BMJ Case Rep | Deux cas d'algie vasculaire de la face liés temporellement à des dentifrices contenant des huiles essentielles de camphre et d'eucalyptus |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Revue | Z Kinder Jugendpsychiatr Psychother | Analyse historique de la neuropsychopharmacothérapie pédiatrique des années 1940-50, sans test du camphre dans la migraine |

Les cas cliniques suggèrent plutôt un rôle déclenchant ou aggravant des huiles essentielles contenant du camphre, ce qui va à l'encontre d'un effet bénéfique. Un article d'analyse chimique sur le camphre dans l'huile essentielle de grande camomille (*Tanacetum parthenium*) est également apparu dans les résultats, mais il n'apporte pas de preuve d'efficacité.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66386652 | CAMPHORA LEHNING, degré de dilution compris entre 4CH à 30CH et 8DH à 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée (AMM active) |
| 68197173 | CAMPHORA BOIRON, degré de dilution compris entre 4CH et 30CH ou entre 8DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée (AMM active) |
| 64991955 | RODULOS, solution buvable en gouttes | Solution en gouttes | Non renseignée (AMM active) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Les données compilées pour ce rapport n'incluent ni mises en garde, ni contre-indications, ni interactions médicamenteuses documentées. À titre d'alerte, une étude de toxicité orale aiguë chez le rat (PMID 27955803) rappelle que le camphre possède un profil de toxicité connu, et des cas cliniques décrivent des céphalées liées à des huiles essentielles contenant du camphre.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la migraine repose sur un score de modèle élevé et une seule étude préclinique directe. Il n'existe aucun essai clinique, les AMM françaises sont toutes annulées, et les données de sécurité sont absentes. Les autres indications prédites (par exemple l'hypertension pulmonaire, dont les publications portent sur un questionnaire de qualité de vie homonyme, sans rapport avec le médicament) ne sont pas étayées. Elles restent à ce stade des hypothèses sans valeur clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour l'évaluation de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- La lecture complète de l'étude préclinique de 2026 pour confirmer le mécanisme, les doses et la transposabilité
- Une évaluation de la voie d'administration et de la marge de sécurité, compte tenu de la toxicité connue du camphre
- Des études précliniques complémentaires avant d'envisager tout essai chez l'humain
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

