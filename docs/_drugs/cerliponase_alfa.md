---
layout: default
title: Cerliponase Alfa
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase Alfa : De la Maladie CLN2 au Syndrome de Scheie

## Résumé en Une Phrase

Cerliponase alfa (Brineura) est une thérapie enzymatique substitutive ciblant la tripeptidyl peptidase 1 (TPP1), initialement développée pour le traitement de la céroïde-lipofuscinose neuronale de type 2 (maladie CLN2 / maladie de Batten tardive à apparition infantile).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome de Scheie (MPS I-S)**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction — le niveau de preuve reste au stade L5 (prédiction algorithmique uniquement).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie CLN2 (céroïde-lipofuscinose neuronale de type 2) |
| Nouvelle Indication Prédite | Syndrome de Scheie (MPS I-S) |
| Score de Prédiction TxGNN | 99,98% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Cerliponase alfa est une enzyme recombinante humaine (rhTPP1 — tripeptidyl peptidase 1) administrée par voie intracérébroventriculaire (ICV). Dans la maladie CLN2, un déficit en TPP1 entraîne l'accumulation de substrats protéiques dans les lysosomes des neurones, provoquant une dégénérescence neurologique progressive. La thérapie substitutive par cerliponase alfa restaure cette activité enzymatique directement dans le compartiment cérébral.

Le syndrome de Scheie (MPS I-S) est quant à lui causé par un déficit en α-L-iduronidase (IDUA), une enzyme lysosomale entièrement distincte de TPP1. Dans cette pathologie, c'est l'accumulation de glycosaminoglycanes (héparane et dermatane sulfate) qui est responsable de la symptomatologie. Le traitement de référence approuvé est la laronidase (Aldurazyme), une IDUA recombinante. Le mécanisme d'action de cerliponase alfa et la pathophysiologie du syndrome de Scheie n'ont aucun substrat ou voie enzymatique en commun.

La seule analogie entre ces deux pathologies réside dans le concept général de « thérapie enzymatique substitutive lysosomale » — cerliponase alfa et laronidase appartiennent toutes deux à cette classe thérapeutique, mais ciblent des enzymes et des substrats entièrement différents. Le score TxGNN élevé (99,98%) reflète vraisemblablement la proximité de ces deux maladies dans le graphe de connaissances (toutes deux classées comme maladies de surcharge lysosomale / maladies rares neurodégénératives), et non une véritable pertinence pharmacologique. La prédiction est considérée comme un **faux positif probable** du modèle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le Syndrome de Scheie.

---

## Informations de Marché en France

Cerliponase alfa (Brineura) ne dispose d'aucune AMM enregistrée en France dans les données disponibles. Le médicament est approuvé aux États-Unis (FDA, 2017) et dans l'Union Européenne (EMA, 2017) pour la maladie CLN2, mais n'est pas commercialisé sur le marché français à la date de ce rapport.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> **Note :** Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce pack de données. Il est à noter que cerliponase alfa est administré par voie intracérébroventriculaire (ICV), ce qui implique des risques spécifiques liés au dispositif d'implantation (infection, méningite, complications procédurales) qui doivent être soigneusement évalués.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN pour le syndrome de Scheie repose uniquement sur la proximité dans le graphe de connaissances entre maladies lysosomales rares, sans aucun fondement mécanistique direct. Cerliponase alfa supplée TPP1, une enzyme sans lien fonctionnel avec l'IDUA déficiente dans le syndrome de Scheie. De plus, la voie d'administration intracérébroventriculaire est incompatible avec le profil clinique systémique du MPS I-S. Aucun essai clinique ni publication ne soutient cette direction.

**Pour avancer, les éléments suivants sont nécessaires :**
- Clarification du mécanisme d'action détaillé (données DrugBank / notices officielles EMA/FDA)
- Vérification de la compatibilité de la voie d'administration ICV avec les indications cibles
- Analyse mécanistique approfondie démontrant une interaction directe entre TPP1 et la pathophysiologie cible avant tout investissement clinique
- Consultation du dossier d'AMM européen (EMA, EPAR Brineura) pour les données de sécurité complètes

---

> ⚠️ **Note de contexte — Analyse des 10 indications prédites :** L'ensemble des 10 indications prédites par TxGNN pour cerliponase alfa reçoivent une recommandation **Hold** (L5) sans aucune preuve clinique. Ce schéma systématique suggère que le modèle capture la position de cerliponase alfa dans le graphe des maladies lysosomales et neurodégénératives rares, sans identifier de cible thérapeutique viable. Une révision manuelle des prédictions de rang plus élevé (ex. CLN1, CLN3, autres NCL) pourrait identifier des candidats biologiquement plus plausibles non inclus dans ce pack.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

