---
layout: default
title: Rilpivirine
parent: Preuves modérées (L3-L4)
nav_order: 263
evidence_level: L4
indication_count: 5
---

# Rilpivirine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **5** 
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

# Rilpivirine : Du VIH-1 à l'Infection par le Virus de l'Immunodéficience Simienne

## Résumé en Une Phrase

Rilpivirine est un inhibiteur non nucléosidique de la transcriptase inverse (INNTI), utilisé contre l'infection par le VIH-1.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'immunodéficience simienne (SIV)**, mais **aucun essai clinique** ne le soutient. Seules **4 publications** existent, toutes précliniques ou de synthèse, et elles portent sur des modèles animaux du VIH.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, la rilpivirine est un INNTI qui inhibe la transcriptase inverse du VIH-1. Son usage dans l'infection par le VIH-1 est établi, et elle est commercialisée en France sous deux spécialités (Rekambys en injectable à libération prolongée, Eviplera en association fixe). Le texte de l'indication approuvée n'est pas renseigné dans les données réglementaires. L'indication d'origine (VIH-1) découle donc de l'analyse du mécanisme et non des AMM.

Le lien avec le SIV est indirect. Les macaques infectés par le SIV ou par des virus chimériques SHIV sont des modèles précliniques standard pour étudier le VIH-1. Les études trouvées relèvent donc de la recherche sur le VIH plutôt que d'une nouvelle indication chez l'humain.

Il faut aussi retenir que le SIV est naturellement résistant aux INNTI. Une activité de la rilpivirine sur la transcriptase inverse du SIV n'est donc pas garantie. Les études utilisent des constructions RT-SHIV, qui contiennent la transcriptase inverse du VIH-1, et c'est ce choix qui rend la rilpivirine testable dans ces modèles. Le score élevé de TxGNN doit donc être interprété avec prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Préclinique (macaque) | Antimicrob Agents Chemother | Faible fréquence de variants résistants sélectionnés par la rilpivirine à action prolongée chez des macaques infectés par un SIV contenant la transcriptase inverse du VIH-1, dans un contexte de prophylaxie pré-exposition |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Préclinique (macaque) | Nat Commun | Rémission du SHIV chez des macaques avec un traitement précoce associant emtricitabine/ténofovir alafénamide par voie orale et cabotégravir/rilpivirine à action prolongée |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Préclinique (macaque) | EBioMedicine | Évaluation préclinique d'une injection unique de cabotégravir et rilpivirine à action prolongée comme prophylaxie post-exposition au VIH |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Revue | Curr Opin HIV AIDS | Revue des preuves précliniques et cliniques du cabotégravir pour le traitement antirétroviral et la prophylaxie pré-exposition (concerne surtout le cabotégravir, donc indirecte pour la rilpivirine) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60150638 | REKAMBYS 900 mg, suspension injectable à libération prolongée | Suspension injectable à libération prolongée |
| 63578537 | EVIPLERA 200 mg/25 mg/245 mg, comprimé pelliculé | Comprimé pelliculé |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à des études précliniques chez le macaque et à une revue. Il n'y a aucun essai clinique, et la résistance naturelle du SIV aux INNTI limite la portée de la prédiction. Les données de sécurité issues de la notice de l'ANSM manquent également, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice de l'ANSM (récupération et analyse du PDF)
- Les données détaillées sur le mécanisme d'action, à obtenir via l'API DrugBank
- La confirmation de l'activité de la rilpivirine sur la transcriptase inverse des constructions SHIV utilisées
- Une clarification de la finalité : cette prédiction relève d'un modèle de recherche sur le VIH, non d'une indication humaine

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat de repositionnement nécessite une validation clinique avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

