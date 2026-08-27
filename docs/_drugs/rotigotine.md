---
layout: default
title: Rotigotine
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Rotigotine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Voici le rapport d'évaluation généré à partir de l'Evidence Pack fourni (candidat `TW-DB05271-multi`, ROTIGOTINE).

---

# ROTIGOTINE : De la Maladie de Parkinson / Syndrome des Jambes sans Repos au Trouble Déficit de l'Attention avec Hyperactivité (TDAH)

## Résumé en Une Phrase

La rotigotine (DrugBank DB05271) est un agoniste dopaminergique connu pour son usage dans la maladie de Parkinson et le syndrome des jambes sans repos (SJSR).
Le modèle TxGNN prédit qu'elle pourrait présenter un intérêt pour le **Trouble Déficit de l'Attention avec Hyperactivité (TDAH)**,
mais cette piste repose actuellement sur **0 essai clinique** et **3 publications à pertinence indirecte** — il s'agit d'une hypothèse de recherche précoce, pas d'un signal clinique établi.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson / Syndrome des Jambes sans Repos (usage connu rapporté dans la littérature ; donnée réglementaire structurée non disponible — voir note ci-dessous) |
| Nouvelle Indication Prédite | Trouble Déficit de l'Attention avec Hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99,997 % (rang interne #110) |
| Niveau de Preuve | L4 |
| Statut de Marché | ✗ Non commercialisé (0 AMM enregistrée) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

> **Note sur l'indication originale :** le champ structuré `original_indications` et le MOA structuré sont marqués comme données manquantes dans l'Evidence Pack. L'usage en Parkinson/SJSR mentionné ci-dessus provient d'une publication indexée dans le pack lui-même (PMID 37221270), pas d'une source réglementaire (TFDA) — aucune notice officielle n'a pu être consultée à ce stade (voir gap bloquant DG001 en conclusion).

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées de mécanisme d'action (MOA) ne sont pas disponibles dans cet Evidence Pack (gap DG002, sévérité élevée). Toutefois, la littérature indexée fournit une information mécanistique utile : selon PMID 37221270 (Cell Research, 2023), la rotigotine est un **agoniste pan-dopaminergique** se liant aux cinq sous-types de récepteurs dopaminergiques (D1 à D5), ce qui explique son efficacité historique dans la maladie de Parkinson et le SJSR, deux pathologies liées à un déficit de signalisation dopaminergique.

Le lien avec le TDAH repose sur une hypothèse génétique et pharmacologique plausible mais indirecte : le récepteur dopaminergique D4 (gène *DRD4*) est un gène de susceptibilité bien documenté dans le TDAH. PMID 34182128 décrit l'hétéromérisation entre le récepteur α2A-adrénergique et des variants polymorphes du récepteur D4, un mécanisme pertinent pour les troubles du contrôle des impulsions — dont le TDAH fait partie. Comme la rotigotine possède une affinité partielle pour D4, il existe une rationalité mécanistique de premier niveau.

Cependant, il faut souligner une limite importante : les deux autres publications retrouvées (PMID 18656214, PMID 21476956) ne portent pas sur le TDAH mais sur le syndrome des jambes sans repos chez l'enfant. Le lien avec le TDAH n'est établi qu'indirectement via la comorbidité clinique connue entre SJSR pédiatrique et TDAH, pas via une preuve d'efficacité directe de la rotigotine sur les symptômes du TDAH. Aucun essai clinique n'existe à ce jour sur cette indication.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Pharmacologie fondamentale (in vitro) | Pharmacological Research | Hétéromérisation entre récepteurs α2A-adrénergiques et variants du récepteur D4 (DRD4) ; le gène DRD4 est associé au TDAH et le récepteur α2A est la cible de la guanfacine, un traitement du TDAH — apporte une rationalité mécanistique indirecte, sans donnée sur la rotigotine elle-même en clinique. |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Revue | Current Pharmaceutical Design | Revue des options pharmacologiques du SJSR chez l'enfant ; ne traite pas du TDAH directement, mais documente le contexte de comorbidité SJSR-TDAH en pédiatrie. |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revue | Revue Neurologique | Revue générale du SJSR (critères diagnostiques, épidémiologie) ; sujet centré sur le SJSR, pas sur le TDAH. |

**Limite à noter :** aucune des trois publications ne rapporte une étude clinique ou préclinique testant directement la rotigotine dans le TDAH.

---

## Autres Pistes Prédites par TxGNN (Vue d'Ensemble)

Pour la transparence de l'évaluation, l'Evidence Pack contient 9 autres indications prédites (rangs 2 à 10) que le TDAH. Il est important de les mentionner car elles illustrent la fiabilité variable des prédictions à très haut score :

- **Schizophrénie (rang 2, score 99,996 %)** — Niveau L4, décision **Hold**. Il existe une base pharmacologique connue (hypothèse « prodopaminergique » dans les symptômes négatifs, PMID 31688399 ; activité antipsychotique potentielle d'agonistes D2/D3 apparentés, PMID 1974516). Mais un agoniste dopaminergique pan-récepteur comme la rotigotine comporte un **risque mécanistique documenté d'aggravation des symptômes positifs** (hallucinations, délires) — un frein de sécurité, pas seulement un manque de preuves.
- **Rangs 3 à 10 (score ≥ 99,99 %, niveau L5, décision Hold)** — Il s'agit de maladies génétiques rares sans aucun essai clinique ni littérature pertinente retrouvée (polymicrogyrie périsylvienne, syndrome faciodigitogénital, trouble congénital de la glycosylation, dystrophie rétinienne, myopie liée à l'X, encéphalopathie à la glycine, maladie de Charcot-Marie-Tooth type 1G). Le rang 6 (dystrophie rétinienne) mérite une mention spécifique : les 15 publications associées concernent en réalité des pathologies ophtalmologiques structurelles sans rapport avec la voie dopaminergique — un **faux positif probable lié à une similarité d'embedding** plutôt qu'un signal réel. Ces 9 pistes ne justifient aucune action à ce stade.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(La notice officielle TFDA n'a pas pu être obtenue à ce jour — voir gap bloquant ci-dessous. Aucune donnée sur les mises en garde, contre-indications ou interactions médicamenteuses n'est actuellement disponible dans ce pack.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le signal TDAH repose uniquement sur un niveau de preuve L4 (mécanistique/indirect), sans aucun essai clinique et avec une littérature majoritairement hors-sujet (SJSR pédiatrique plutôt que TDAH). De plus, un gap de sécurité bloquant (absence de notice TFDA) empêche toute entrée en évaluation de sécurité de niveau S1, indépendamment de la force du signal d'efficacité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle TFDA (mises en garde, contre-indications) — **bloquant**, condition préalable à toute évaluation de sécurité (S1)
- Obtenir les données structurées de mécanisme d'action via l'API DrugBank
- Rechercher des données précliniques ou des séries de cas ciblant spécifiquement la rotigotine dans le TDAH (au-delà de la comorbidité SJSR)
- Réévaluer la piste schizophrénie séparément, avec un focus sur le risque d'aggravation des symptômes positifs avant toute poursuite
- Ne pas poursuivre les rangs 3 à 10 en l'absence de tout nouveau signal clinique ou littéraire
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

