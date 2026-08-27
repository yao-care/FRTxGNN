---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zidovudine : De l'Infection par le VIH/SIDA au Syndrome d'Immunodéficience Acquise Féline

## Résumé en Une Phrase

Zidovudine (AZT) est le premier inhibiteur nucléosidique de la transcriptase inverse (INTI) approuvé, historiquement destiné au traitement de l'infection par le VIH/SIDA. Le modèle TxGNN prédit en tête de liste une association avec le **Syndrome d'Immunodéficience Acquise Féline** (SIDA du chat, causé par le FIV), actuellement soutenue par **0 essai clinique** et **20 publications**, mais cette piste concerne une maladie vétérinaire féline et non une pathologie humaine.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH/SIDA (connaissance publique établie sur la zidovudine ; non documentée dans les licences TFDA disponibles) |
| Nouvelle Indication Prédite | Syndrome d'Immunodéficience Acquise Féline (SIDA félin, FIV) |
| Score de Prédiction TxGNN | 99.96% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

*Note : les données réglementaires sous-jacentes de ce pack proviennent du TFDA (Taïwan) et non d'une source française ; le statut "non commercialisé" reflète l'absence de licence enregistrée dans ce jeu de données.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce pack (écart de données DG002). Sur la base des informations connues, la zidovudine est un analogue nucléosidique de la thymidine qui, après phosphorylation intracellulaire, est incorporé par la transcriptase inverse virale dans l'ADN en cours de synthèse, provoquant une terminaison de chaîne et bloquant la réplication rétrovirale — mécanisme à l'origine de son efficacité historique contre le VIH.

Le FIV (virus de l'immunodéficience féline) appartient, comme le VIH, au genre des lentivirus et partage une transcriptase inverse structurellement homologue. C'est d'ailleurs pour cette raison que le modèle félin est utilisé depuis les années 1980 comme modèle animal de chimiothérapie anti-rétrovirale pour la recherche sur le SIDA humain. Sur ce plan, une activité inhibitrice de la zidovudine contre la transcriptase inverse du FIV est mécanistiquement plausible et a été documentée expérimentalement chez le chat.

**Cependant, cette prédiction doit être interprétée avec une forte réserve** : le "Syndrome d'Immunodéficience Acquise Féline" est une maladie vétérinaire féline, pas une indication humaine. Le score TxGNN élevé (99.96%) reflète très probablement une confusion d'entités entre FIV et VIH dans le graphe de connaissances (embedding de similarité entre lentivirus félin et humain), plutôt qu'une véritable opportunité de repositionnement clinique chez l'humain. Cette réserve est cohérente avec l'absence totale d'essai clinique et le niveau de preuve limité à des études animales (L3).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | Étude animale | Antimicrob Agents Chemother | Le FIV est proposé comme modèle du SIDA humain ; la transcriptase inverse du FIV est suffisamment proche de celle du VIH-1 pour servir de modèle de chimiothérapie ciblée |
| [3034403](https://pubmed.ncbi.nlm.nih.gov/3034403/) | 1987 | Étude animale | Cancer Research | AZT évalué chez le chat infecté par le FeLV comme modèle thérapeutique/prophylactique précoce des rétrovirus, préfigurant son usage humain |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Étude vétérinaire | Antimicrob Agents Chemother | Interféron alpha-2b combiné à l'AZT chez des chats présymptomatiques atteints de FeLV-FAIDS |
| [2164083](https://pubmed.ncbi.nlm.nih.gov/2164083/) | 1990 | Étude vétérinaire | J Acquir Immune Defic Syndr | AZT en prophylaxie combinée à l'interféron alpha et l'IL-2 contre le FeLV-FAIDS ; effet antiviral in vitro dose-dépendant |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Étude animale | J Acquir Immune Defic Syndr | L'AZT prophylactique réduit la virémie précoce et le déclin lymphocytaire chez les chats inoculés au FIV, sans prévenir l'infection primaire |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Étude animale | Arch Virol | L'AZT réduit le titre viral plasmatique (pas le titre dans les PBMC) chez les chats infectés par le FIV |
| [8399067](https://pubmed.ncbi.nlm.nih.gov/8399067/) | 1993 | Étude animale | J Immunother | Transfert adoptif de lymphocytes activés + IFN-alpha + AZT pour inverser l'infection par le FeLV |
| [2163339](https://pubmed.ncbi.nlm.nih.gov/2163339/) | 1990 | Étude de toxicité | Fundam Appl Toxicol | Toxicité dose-dépendante de l'AZT évaluée chez des chats infectés par le FeLV (données de sécurité pertinentes) |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Étude animale | Vet Immunol Immunopathol | Efficacité additive à synergique de l'AZT/3TC in vitro contre le FIV, mais efficacité limitée in vivo |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Suivi de cohorte | J Feline Med Surg | Suivi à long terme (5-6 ans) de chats infectés par le FIV traités par AZT en première ligne |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le candidat en tête de classement (score TxGNN 99.96%) correspond à une maladie féline, très probablement issue d'une confusion d'entités FIV/VIH dans le graphe de connaissances TxGNN. Aucun essai clinique n'existe, et le niveau de preuve (L3) repose uniquement sur des études animales anciennes sans transposition démontrée à l'humain. Cette piste n'est pas exploitable en l'état comme candidat de repositionnement humain.

**Pour avancer, les éléments suivants sont nécessaires :**
- Lever l'écart bloquant DG001 : obtenir les mises en garde/contre-indications TFDA (téléchargement et analyse de la notice PDF officielle)
- Lever l'écart DG002 (sévérité High) : obtenir le mécanisme d'action structuré via l'API DrugBank
- Faire vérifier par l'équipe modèle si le nœud "feline acquired immunodeficiency syndrome" est correctement distingué de l'entité VIH humaine dans le graphe TxGNN, afin de confirmer ou d'écarter l'hypothèse de confusion d'entités
- Réexaminer les candidats de rang inférieur figurant dans ce même pack (ex. "AIDS related complex", rang 5, niveau de preuve L1, stade S3, recommandation "Proceed with Guardrails") qui, bien que proches de l'usage historique du VIH, disposent d'un socle de preuves cliniques nettement plus solide
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

