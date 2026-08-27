---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# IOVERSOL : d'Agent de Contraste Radiologique à la Susceptibilité à l'Arthrose

## Résumé en Une Phrase

Ioversol est un agent de contraste iodé utilisé en imagerie médicale (angiographie, uro-TDM), sans indication thérapeutique classique enregistrée dans les données disponibles ni commercialisation en France. Le modèle TxGNN prédit une association avec la **Susceptibilité à l'Arthrose**, mais cette piste n'est actuellement soutenue par **aucun essai clinique ni aucune publication**, ce qui correspond au niveau de preuve le plus faible (L5).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Agent de contraste radiologique (imagerie médicale) — aucune indication thérapeutique officielle enregistrée dans les données disponibles |
| Nouvelle Indication Prédite | Susceptibilité à l'Arthrose (osteoarthritis susceptibility) |
| Score de Prédiction TxGNN | 99.67 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles (data gap DrugBank/TFDA). Sur la base des informations connues issues du dossier de preuves, Ioversol est un agent de contraste iodé destiné à l'imagerie diagnostique, sans mécanisme pharmacologique anti-inflammatoire, immunomodulateur ou chondroprotecteur connu. Il n'existe donc pas de lien mécanistique établi entre son usage diagnostique et la susceptibilité génétique à l'arthrose.

L'analyse des indications prédites de rang inférieur apporte un éclairage important sur l'origine probable de cette prédiction : la piste la mieux documentée du lot (« osteoarthritis », rang 2) repose sur des essais cliniques et une publication portant en réalité sur l'**embolisation des artères géniculées** (Genicular Artery Embolization), une procédure interventionnelle utilisant le **Lipiodol** (une émulsion huileuse iodée), et non l'Ioversol. Le rapport d'analyse joint indique explicitement que le score élevé de TxGNN provient vraisemblablement d'une proximité d'embedding dans le graphe de connaissances entre les nœuds « agent de contraste » et « intervention vasculaire par embolisation », créant une association médicament-maladie faussement positive plutôt qu'un signal thérapeutique réel.

En conséquence, pour l'indication de tête (« osteoarthritis susceptibility »), qui ne dispose d'aucun essai ni d'aucune publication associée, il n'existe aucun élément — ni mécanistique, ni empirique — permettant de soutenir la plausibilité biologique de cette prédiction. Il s'agit d'un signal statistique isolé du modèle, sans validation externe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Ioversol n'est actuellement **pas commercialisé en France** : aucune AMM (0/0) n'a été identifiée dans les données de régulation disponibles. Aucun tableau de spécialités ne peut donc être produit.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*Remarque : les mises en garde, contre-indications et interactions médicamenteuses (DDI) n'ont pu être extraites d'aucune source (TFDA, DrugBank) au moment de la collecte — ce point est identifié comme un blocage (DG001, sévérité « Blocking ») empêchant le passage à l'étape d'évaluation de sécurité S1.*

---

## Autres Indications Prédites (Vue d'Ensemble)

Le dossier de preuves couvre 10 indications prédites par TxGNN pour Ioversol (rangs 1 à 10). Toutes reçoivent la même recommandation **Hold**, ce qui renforce le constat que ce candidat ne présente pas de signal de repositionnement exploitable en l'état :

| Rang | Indication | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------------|-------------|------------------|-------------|
| 1 | Susceptibilité à l'Arthrose | 99.67 % | L5 | Aucune preuve ; prédiction pure du modèle |
| 2 | Arthrose | 99.63 % | L4 | Essais/littérature portent sur l'embolisation au Lipiodol, pas sur Ioversol (probable faux positif d'embedding) |
| 3 | Polyarthrite Rhumatoïde | 99.56 % | L5 | Littérature sans rapport direct (embolisation + criblage in silico d'inhibiteurs PAD4) |
| 4 | Brachyolmie | 99.36 % | L5 | Aucune preuve ; maladie rare sans lien mécanistique |
| 5 | Hémoglobinopathie | 99.33 % | L4 | Littérature traite de la **sécurité d'injection** de produits de contraste chez les patients drépanocytaires — sens inverse de la logique de repositionnement |
| 6 | Syndrome Brachyolmie-Amélogenèse Imparfaite | 99.32 % | L5 | Aucune preuve ; syndrome génétique rarissime |
| 7 | Dysplasie Acromésomélique de type Hunter-Thompson | 99.32 % | L5 | Aucune preuve |
| 8 | Myosclérose | 99.29 % | L5 | Aucune preuve |
| 9 | Syndrome de Microphtalmie Colobomateuse avec Dysplasie Rhizomélique | 99.26 % | L5 | Aucune preuve |
| 10 | Alopécie | 99.25 % | L5 | Aucune preuve |

*Point notable : pour la piste « Hémoglobinopathie » (rang 5), la littérature identifiée concerne la tolérance des produits de contraste iodés chez les patients atteints de drépanocytose — c'est-à-dire une question de sécurité d'usage du diagnostic, et non une preuve d'efficacité thérapeutique. Cette confusion de direction illustre un risque récurrent d'interprétation erronée pour ce candidat.*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication de tête (Susceptibilité à l'Arthrose) est un pur produit du modèle (L5), sans aucun essai clinique ni publication à l'appui.
- Les 10 indications prédites reçoivent uniformément la recommandation « Hold » ; même la piste la mieux « documentée » (Arthrose, rang 2) repose sur des preuves indirectes concernant un autre produit (Lipiodol) et une autre modalité thérapeutique (embolisation artérielle), suggérant un artefact de similarité d'embedding plutôt qu'un signal pharmacologique réel.
- Un blocage de sécurité critique (DG001) empêche toute progression vers l'étape d'évaluation S1 : les mises en garde et contre-indications TFDA sont absentes des données.

**Pour avancer, les éléments suivants sont nécessaires :**
- Lever le blocage de sécurité (DG001) : récupérer et analyser la notice TFDA d'Ioversol.
- Compléter les données de mécanisme d'action (DG002) via l'API DrugBank.
- Clarifier si Ioversol lui-même (et non le Lipiodol ou un autre agent) a été testé comme intervention thérapeutique dans un contexte pertinent, avant d'envisager une ré-évaluation de ce candidat.
- Étant donné la nature diagnostique (non thérapeutique) du produit, réexaminer la pertinence globale d'Ioversol comme candidat au repositionnement avant d'allouer davantage de ressources d'investigation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

