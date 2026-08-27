---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam : De l'Anti-Inflammatoire Rhumatismal au Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## Résumé en Une Phrase

Le piroxicam est un anti-inflammatoire non stéroïdien (AINS) de la classe des oxicams, traditionnellement associé aux affections rhumatismales inflammatoires (aucune indication officielle française n'est disponible car le produit n'est pas commercialisé en France). Le modèle TxGNN prédit un lien avec le **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, une maladie génétique rare, mais **aucun essai clinique ni publication** ne soutient actuellement cette direction — le rationnel généré signale lui-même l'absence de lien physiopathologique connu.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible officiellement (produit non commercialisé en France) ; AINS historiquement utilisé pour l'arthrose, la polyarthrite rhumatoïde et la spondylarthrite ankylosante |
| Nouvelle Indication Prédite | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action du piroxicam ne sont pas disponibles dans ce pack. Sur la base des informations générales connues, le piroxicam appartient à la classe des AINS oxicams, dont l'efficacité repose sur l'inhibition non sélective de la cyclo-oxygénase (COX) et la réduction de la synthèse des prostaglandines dans les pathologies inflammatoires.

Il s'agit ici d'un syndrome génétique rare (anomalies congénitales du développement oculaire et des membres) sans lien physiopathologique connu avec le mécanisme d'inhibition de la COX des AINS. Le score élevé attribué par TxGNN pourrait refléter une similarité entre nœuds phénotypiques dans le graphe de connaissances plutôt qu'une véritable pertinence pharmacologique — c'est d'ailleurs l'avertissement explicite associé à cette prédiction.

En l'état, aucun élément mécanistique, clinique ou bibliographique ne permet de rattacher raisonnablement le piroxicam à cette indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle uniquement, aucune étude clinique ni publication), et le rationnel de repositionnement généré indique lui-même l'absence de lien mécanistique plausible entre le piroxicam et ce syndrome développemental rare. Le score TxGNN élevé n'est pas corroboré par des données réelles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résolution du data gap bloquant DG001 (mises en garde/contre-indications TFDA) avant toute évaluation de sécurité (S1)
- Résolution du data gap DG002 (mécanisme d'action via DrugBank) pour permettre une analyse de plausibilité mécanistique
- Revue par un expert pour confirmer si le score TxGNN reflète un artefact du graphe de connaissances (similarité phénotypique) plutôt qu'un signal pharmacologique réel
- Évaluation de la faisabilité réglementaire, le produit n'étant pas commercialisé en France (0 AMM)

**Remarque :** ce pack de preuves contient 9 autres indications prédites pour le piroxicam. Parmi elles, la **polyarthrite juvénile idiopathique** (rang TxGNN 10, score 99,93 %) dispose d'un niveau de preuve nettement supérieur (L1 — revues systématiques, méta-analyses en réseau, et essais cliniques historiques testant directement le piroxicam) et affiche déjà une recommandation « Proceed with Guardrails ». Un rapport dédié à cette indication serait prioritaire par rapport à la présente prédiction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

