---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

Le skill TxGNN Pipeline est de nature opérationnelle (entraînement, déploiement) et ne s'applique pas ici. Je génère directement le rapport d'évaluation selon le format défini dans mon rôle d'expert.

---

# Lorlatinib : Évaluation de Repositionnement — Prédictions Non Disponibles

## Résumé en Une Phrase

Lorlatinib (DB12130) est un inhibiteur de tyrosine kinase de 3ᵉ génération ciblant les kinases ALK et ROS1, développé pour le traitement des cancers bronchiques non à petites cellules (CBNPC) ALK-positifs.
Le modèle TxGNN n'a généré **aucune indication prédite** pour ce candidat lors de l'analyse actuelle.
En raison de plusieurs lacunes de données critiques — notamment l'absence de MOA structuré et d'indications originales dans l'Evidence Pack — une évaluation complète de repositionnement n'est pas réalisable à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non renseignée dans l'Evidence Pack |
| Nouvelle Indication Prédite | Aucune prédiction TxGNN disponible |
| Score de Prédiction TxGNN | Non disponible |
| Niveau de Preuve | L5 — Aucune étude réelle associée |
| Statut de Marché | Non commercialisé (données réglementaires fournies) |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Aucune Prédiction n'est-elle Disponible ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cet Evidence Pack. Le pipeline de requêtes confirme que la source DrugBank a été interrogée avec succès (résultat : 1 entrée), mais les champs `original_moa` et `original_indications` n'ont pas été peuplés, ce qui indique une lacune dans l'étape de parsing ou d'enrichissement des données.

Lorlatinib est un inhibiteur de tyrosine kinase de 3ᵉ génération actif sur ALK, ROS1 et MET, avec une pénétration démontrée dans le système nerveux central (SNC). Son usage clinique établi concerne le CBNPC ALK-positif en rechute après traitement par inhibiteur ALK de 1ʳᵉ ou 2ᵉ génération. Mécanistiquement, des repositionnements vers d'autres tumeurs solides présentant des fusions ou mutations de kinases ALK/ROS1 (neuroblastome, carcinome anaplasique de la thyroïde, cholangiocarcinome) seraient biologiquement plausibles — mais sans sorties formelles du modèle TxGNN, aucune conclusion ne peut être validée dans ce cadre.

L'absence de prédictions peut résulter d'une intégration incomplète de Lorlatinib dans le graphe de connaissances biomédicales TxGNN, ou d'un seuil de score trop élevé filtrant les résultats.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Cytotoxicité

> Lorlatinib est un médicament antinéoplasique de la classe des inhibiteurs de tyrosine kinase (ITK), actif dans les tumeurs à réarrangement ALK/ROS1.

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur de tyrosine kinase ALK/ROS1/MET (3ᵉ génération, oral) |
| Risque de Myélosuppression | Faible à modéré (moins marqué que la chimiothérapie cytotoxique conventionnelle) |
| Classification d'Émétogénicité | Faible (ITK oraux, prise quotidienne) |
| Éléments de Surveillance | Bilan lipidique (hypertriglycéridémie fréquente), ECG (allongement QTc), bilan hépatique, évaluation neuropsychiatrique (effets SNC), glycémie |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques (comprimés entiers, ne pas écraser) |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes (avertissements, contre-indications et interactions médicamenteuses non disponibles dans cet Evidence Pack).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le modèle TxGNN n'a produit aucune prédiction d'indication pour Lorlatinib, et les lacunes de données amont (MOA, indications originales, données de sécurité structurées) bloquent l'ensemble de la chaîne d'évaluation. Une décision de repositionnement ne peut être rendue sans output TxGNN valide.

**Pour avancer, les éléments suivants sont nécessaires :**

- **[Bloquant]** Compléter le parsing DrugBank : récupérer `mechanism_of_action`, `categories`, et `indications` pour DB12130 via l'API DrugBank
- **[Bloquant]** Relancer le pipeline TxGNN avec les données du graphe enrichies pour générer les scores de prédiction
- **[Haute priorité]** Télécharger et analyser la notice officielle (ANSM / EMA pour Lorviqua®) afin de renseigner les avertissements et contre-indications
- **[Haute priorité]** Vérifier le statut d'autorisation de mise sur le marché auprès de l'ANSM et intégrer les numéros d'AMM correspondants
- **[Normale]** Collecter les données d'interactions médicamenteuses (DDI) — la requête actuelle a retourné `not_found`
- **[Normale]** Revoir le seuil de score TxGNN si le médicament était intégré au graphe mais filtré en sortie
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

