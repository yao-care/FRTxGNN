---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine : De l'Hypertension Artérielle à l'Infarctus du Tronc Cérébral

## Résumé en Une Phrase

L'amlodipine est un antagoniste calcique de longue durée d'action (classe dihydropyridine), initialement développé et largement utilisé dans le traitement de l'hypertension artérielle et de l'angor stable chronique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infarctus du tronc cérébral**,
avec **aucun essai clinique** et **aucune publication** soutenant directement cette direction à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle / Angor stable (données de référence non renseignées dans ce dossier) |
| Nouvelle Indication Prédite | Infarctus du tronc cérébral |
| Score de Prédiction TxGNN | 99.94% |
| Niveau de Preuve | L5 |
| Statut de Marché à Taïwan | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, l'amlodipine appartient à la classe des antagonistes calciques dihydropyridiniques (L-type CCB) : elle bloque les canaux calciques voltage-dépendants de type L au niveau des muscles lisses vasculaires, entraînant une vasodilatation artérielle et une réduction de la résistance vasculaire périphérique, ce qui explique son efficacité antihypertensive et antiangineuse bien établie.

Le rationnel mécanistique fourni dans ce dossier repose sur le fait que le blocage des canaux calciques pourrait théoriquement réduire la surcharge calcique intraneuronale lors d'une ischémie du tronc cérébral, atténuant ainsi les lésions d'excitotoxicité. Par ailleurs, l'infarctus du tronc cérébral partage avec l'ensemble des AVC ischémiques les mêmes facteurs de risque vasculaires modifiables — notamment l'hypertension artérielle —, domaine d'indication principal de l'amlodipine.

Cependant, cette prédiction est entièrement issue du modèle TxGNN (réseau de neurones graphique sur base de connaissances biomédicales), sans aucune donnée clinique ou préclinique directement validant l'efficacité de l'amlodipine dans l'infarctus du tronc cérébral. Le passage à des études spécifiques requiert en premier lieu la génération de données précliniques sur des modèles d'ischémie du tronc.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché à Taïwan

Aucune autorisation de mise sur le marché (AMM) enregistrée à Taïwan pour l'amlodipine dans les données interrogées. Le statut de commercialisation est **non commercialisé** (0 AMM).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN pour l'infarctus du tronc cérébral repose exclusivement sur le modèle de graphe de connaissances biomédicales, en l'absence totale d'essais cliniques ou de publications directement associés à cette indication. Le niveau de preuve L5 est insuffisant pour justifier une progression vers des études cliniques ou réglementaires.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) neurovasculaire de l'amlodipine (combler DG002)
- Études précliniques sur des modèles animaux d'ischémie du tronc cérébral (preuve de concept)
- Revue systématique de la littérature sur les antagonistes calciques dans l'AVC ischémique du tronc cérébral
- Clarification du statut réglementaire à Taïwan : téléchargement et analyse de la notice officielle TFDA (combler DG001)
- Réévaluation de la priorité de cette indication au regard d'autres candidats du même dossier présentant un niveau de preuve supérieur (ex. : hémorragie intracérébrale, niveau L3, recommandation *Proceed with Guardrails*)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

