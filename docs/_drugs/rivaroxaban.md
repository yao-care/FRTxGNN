---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Je vais rédiger le rapport directement à partir du Evidence Pack fourni, en respectant strictement le format demandé (aucune section vide, pas de "[Data Gap]" affiché, table Marché/Cytotoxicité omises car non applicables ici).

# Rivaroxaban : De la Prévention Thromboembolique (TVP/EP, Fibrillation Auriculaire) à la Polyarthrite Rhumatoïde

## Résumé en Une Phrase

Rivaroxaban est un anticoagulant oral (inhibiteur du facteur Xa), utilisé à l'origine dans la prévention et le traitement des événements thromboemboliques veineux (thrombose veineuse profonde/embolie pulmonaire) ainsi que dans la prévention des accidents thromboemboliques liés à la fibrillation auriculaire. Le modèle TxGNN prédit qu'il pourrait présenter un intérêt pour la **Polyarthrite Rhumatoïde**, mais cette piste ne repose actuellement sur **aucun essai clinique dédié** et seulement **4 publications**, majoritairement indirectes.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Polyarthrite Rhumatoïde |
| Score de Prédiction TxGNN | 99,57 % |
| Niveau de Preuve | L4 |
| Statut de Marché à Taïwan | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

*Indication originale non renseignée dans les sources structurées (TFDA/DrugBank licenses vides). Le contexte clinique historique de rivaroxaban (TVP/EP, fibrillation auriculaire) cité dans ce rapport a été reconstitué à partir des essais cliniques et de la littérature inclus dans le dossier de preuves, et non d'un champ d'indication approuvée structuré.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées sur le mécanisme d'action (MOA) de rivaroxaban ne sont pas renseignées dans la fiche DrugBank consultée (écart de données signalé, sévérité Élevée). Néanmoins, l'ensemble des analyses de corrélation mécanistique contenues dans ce dossier identifient de façon cohérente rivaroxaban comme un **inhibiteur direct du facteur Xa (FXa)**, c'est-à-dire un anticoagulant oral agissant sur la cascade de coagulation — cette information ressort de manière convergente des rationnels associés aux 4 indications évaluées, même en l'absence de fiche MOA formelle.

Le contexte d'usage historique de rivaroxaban, tel que documenté par les essais cliniques inclus (par exemple l'étude de cohorte EINSTEIN-CYP, NCT00786422) et la littérature (par exemple PMID 39992678, PMID 24452338), est la prévention et le traitement des événements thromboemboliques veineux (TVP, embolie pulmonaire) ainsi que la prévention des accidents thromboemboliques liés à la fibrillation auriculaire. La polyarthrite rhumatoïde (PR) est une maladie auto-immune inflammatoire chronique associée à un état pro-thrombotique documenté (génération accrue de thrombine, risque accru de TVP/EP chez les patients atteints de maladies auto-immunes).

Le raisonnement mécanistique sous-jacent est que l'inflammation chronique et l'activité auto-immune de la PR favorisent un état d'hypercoagulabilité, et qu'un anticoagulant pourrait théoriquement réduire les complications thromboemboliques associées à la PR. Il s'agit toutefois d'un traitement potentiel des **complications thrombotiques de la PR**, et non d'un traitement de la PR elle-même (inflammation articulaire, activité auto-immune). Sur les 4 publications disponibles, une seule (PMID 34175144) aborde directement un marqueur de coagulation dans le contexte des maladies auto-immunes ; les trois autres portent sur la thromboembolie en général, l'observance médicamenteuse en fibrillation auriculaire, ou un cas clinique périopératoire mentionnant incidemment un antécédent de PR. **Aucune étude interventionnelle n'évalue à ce jour rivaroxaban comme traitement de la PR elle-même.**

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Étude mécanistique/laboratoire | La Revue de médecine interne | Le test de génération de thrombine (TGA) permet d'évaluer l'hypercoagulabilité chez les patients atteints de maladies auto-immunes (dont le syndrome des antiphospholipides), suggérant un lien mécanistique indirect entre inflammation auto-immune et risque thrombotique. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revue | JAMA | Revue générale sur le diagnostic et le traitement de la thrombose veineuse profonde des membres inférieurs ; ne traite pas spécifiquement de la PR. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohorte | PloS one | Comparaison de l'observance au rivaroxaban vs apixaban chez des patients en fibrillation auriculaire non valvulaire ; aucun lien direct avec la PR. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Rapport de cas | Cureus | Cas d'infarctus cérébral thromboembolique périopératoire chez une patiente de 88 ans sous corticoïdes oraux pour polyarthrite rhumatoïde, malgré une anticoagulation en cours pour fibrillation auriculaire — mention incidente de la PR comme comorbidité, non comme cible thérapeutique. |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve actuel (L4) repose uniquement sur des données mécanistiques indirectes (hypercoagulabilité dans les maladies auto-immunes) et aucun essai clinique ne cible spécifiquement rivaroxaban dans la PR. De plus, l'absence de données de sécurité TFDA (écart de données bloquant) empêche toute évaluation de sécurité de stade S1.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice TFDA (mises en garde, contre-indications) — écart de données bloquant (impact : blocage de l'évaluation de sécurité S1)
- Compléter les données structurées de mécanisme d'action via l'API DrugBank — écart de données sévérité Élevée
- Rechercher/surveiller d'éventuels essais cliniques dédiés à rivaroxaban dans la PR ou dans d'autres maladies auto-immunes à risque thromboembolique
- Clarifier si la piste pertinente est « PR avec complication thromboembolique » plutôt que « PR » en tant que maladie inflammatoire elle-même, avant toute progression au-delà du stade S0

---

## Annexe : Autres Indications Prédites Évaluées (Priorité Secondaire)

Le même dossier de preuves comporte 3 autres pistes de repositionnement pour rivaroxaban, toutes avec une recommandation **Hold** et un niveau de preuve faible (L4-L5). Elles sont résumées ci-dessous à titre informatif.

### Goutte (Score TxGNN : 99,51 % — Niveau de Preuve L5)

Aucune preuve mécanistique ou clinique pertinente. La seule publication associée (PMID 34210765) porte sur les interactions du benzbromarone (un médicament de la goutte) avec le cytochrome P450, sans rapport avec un effet thérapeutique du rivaroxaban sur la goutte. **Décision : Hold** — signal de prédiction isolé, sans rationnel exploitable.

### Infection par le VIH (Score TxGNN : 99,17 % — Niveau de Preuve L4)

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00786422](https://clinicaltrials.gov/study/NCT00786422) | Phase 2 | Terminé | 25 | Étude de cohorte EINSTEIN-CYP évaluant l'adaptation posologique du rivaroxaban chez des patients sous TVP/EP aigus recevant un inducteur puissant du CYP3A4 — étude d'interaction médicamenteuse/sécurité, non un essai thérapeutique pour le VIH. |

La littérature associée (8 publications, dont PMID 39992678, 24452338, 32179901) porte quasi exclusivement sur la **sécurité et les interactions médicamenteuses** entre anticoagulants oraux directs et traitements antirétroviraux boostés (ritonavir/cobicistat) chez des patients VIH+ traités par ailleurs pour fibrillation auriculaire ou thromboembolie veineuse. Il s'agit d'un enjeu de co-prescription et non d'un mécanisme thérapeutique contre le VIH. **Décision : Hold** — le score élevé reflète probablement une co-occurrence de prescription plutôt qu'une relation thérapeutique réelle.

### Syndrome de Brachydactylie-Syndactylie (Score TxGNN : 99,10 % — Niveau de Preuve L5)

Aucun essai clinique ni littérature disponible. Il s'agit d'un syndrome génétique rare du développement squelettique, sans lien mécanistique connu avec l'inhibition du facteur Xa. **Décision : Hold** — signal de prédiction pur, non exploitable en l'état.

---

*Ce rapport est fourni à des fins de recherche sur le repositionnement de médicaments uniquement et ne constitue pas un avis médical.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

