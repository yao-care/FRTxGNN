---
layout: default
title: Acalabrutinib
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 0
---

# Acalabrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

Voici le rapport d'évaluation généré à partir de l'Evidence Pack fourni :

---

# Acalabrutinib : Évaluation Préliminaire — Données Insuffisantes pour le Repositionnement

## Résumé en Une Phrase

L'acalabrutinib (DB11703) est un inhibiteur sélectif de la tyrosine kinase de Bruton (BTK), utilisé internationalement dans le traitement de la leucémie lymphoïde chronique (LLC) et du lymphome à cellules du manteau (LCM). **Aucune nouvelle indication n'a été prédite par le modèle TxGNN** dans le cadre de cette évaluation, et le médicament **n'est pas commercialisé en France** selon les données disponibles. L'Evidence Pack présente des lacunes de données critiques (mécanisme d'action, données de sécurité) qui empêchent une évaluation complète.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le pack (LLC/LCM internationalement reconnues) |
| Nouvelle Indication Prédite | **Aucune prédiction disponible** |
| Score de Prédiction TxGNN | N/A |
| Niveau de Preuve | **L5** (Aucune preuve de repositionnement identifiée) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

## Pourquoi Cette Évaluation est-elle Limitée ?

L'acalabrutinib est un inhibiteur sélectif et irréversible de la tyrosine kinase de Bruton (BTK), une enzyme clé dans la voie de signalisation du récepteur des cellules B (BCR). En bloquant la BTK, l'acalabrutinib inhibe la prolifération et la survie des cellules B malignes. Il est commercialisé sous le nom de **Calquence®** (AstraZeneca) et approuvé par la FDA et l'EMA pour le traitement de la LLC/SLL et du LCM.

Cependant, les données du mécanisme d'action (MOA) ne sont pas disponibles dans le pack de données fourni, ce qui limite l'analyse de la relation mécanistique avec d'éventuelles nouvelles indications. De plus, le tableau des indications prédites (`predicted_indications`) est **vide**, ce qui signifie que le modèle TxGNN n'a pas identifié de candidat de repositionnement pour ce médicament dans cette itération.

L'absence de données réglementaires françaises (aucune AMM, aucune notice de sécurité disponible) constitue un obstacle bloquant (« Blocking ») pour toute évaluation de sécurité de Phase S1. Ces lacunes doivent être comblées avant de relancer une analyse de repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé à une nouvelle indication prédite n'est enregistré actuellement.

> *Note : L'acalabrutinib fait l'objet de nombreux essais cliniques dans ses indications approuvées (LLC, LCM) et dans des indications exploratoires (lymphomes à cellules B, GVHD, etc.), mais ceux-ci ne sont pas liés à une prédiction TxGNN spécifique dans ce pack.*

## Preuves de la Littérature

Aucune littérature associée à une nouvelle indication prédite n'est disponible actuellement.

## Informations de Marché en France

Aucune AMM n'est enregistrée dans les données fournies pour le marché français.

> *Note : L'acalabrutinib (Calquence®) dispose d'une autorisation de mise sur le marché européenne (EMA) depuis 2020 pour la LLC. Il est possible que les données du pack ne reflètent pas l'ensemble des autorisations en vigueur. Une vérification auprès de l'ANSM ou de la base de données européenne est recommandée.*

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | **Thérapie ciblée** (inhibiteur de BTK — petite molécule kinase) |
| Risque de Myélosuppression | Modéré (neutropénie, thrombocytopénie et anémie rapportées dans les études pivotales) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | NFS avec différentielle, fonction hépatique, surveillance des infections, surveillance des événements hémorragiques et de la fibrillation auriculaire |
| Protection de Manipulation | Précautions standard pour les agents antinéoplasiques oraux ; pas de manipulation de cytotoxiques injectable requise |

> *Note : L'acalabrutinib est une thérapie ciblée orale, non un cytotoxique conventionnel. La myélosuppression est généralement moins sévère qu'avec les chimiothérapies classiques.*

## Considérations de Sécurité

> Veuillez consulter la notice pour les informations de sécurité.

Les données de sécurité (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans l'Evidence Pack fourni. Cependant, il est connu sur le plan international que l'acalabrutinib présente les risques suivants à prendre en compte :

- **Risques cardiovasculaires** : Fibrillation auriculaire / flutter auriculaire rapportés
- **Risques hémorragiques** : Risque accru de saignements, prudence avec les anticoagulants
- **Risques infectieux** : Infections opportunistes possibles (réactivation du VHB)
- **Interactions CYP3A** : Substrat majeur du CYP3A4 ; éviter les inhibiteurs/inducteurs puissants du CYP3A

> ⚠️ *Ces informations sont issues des connaissances générales et non de l'Evidence Pack. Une validation avec la notice officielle est indispensable.*

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'Evidence Pack ne contient aucune indication prédite par le modèle TxGNN, et présente des lacunes de données critiques (MOA, sécurité, données réglementaires). En l'absence de signal de repositionnement et de données de sécurité exploitables, il n'est pas possible de recommander une avancée vers l'évaluation clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- ☐ Relancer le modèle TxGNN avec des données d'entrée complètes pour obtenir des prédictions d'indications
- ☐ Obtenir les données de mécanisme d'action (MOA) depuis DrugBank API (lacune DG002)
- ☐ Vérifier le statut d'AMM auprès de l'ANSM/EMA (Calquence® est autorisé en Europe depuis 2020)
- ☐ Récupérer la notice (RCP) pour extraire les mises en garde, contre-indications et interactions (lacune DG001)
- ☐ Compléter l'Evidence Pack et relancer l'évaluation

---

*Ce rapport a été généré le 2026-04-03 (v4). Les résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit faire l'objet d'une validation clinique rigoureuse avant toute application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

