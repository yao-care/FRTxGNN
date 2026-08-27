---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab : De l'Hémoglobinurie Paroxystique Nocturne à la Neutropénie Congénitale Sévère liée à un Déficit en G6PC3

## Résumé en Une Phrase

Ravulizumab est un inhibiteur du complément terminal (C5), habituellement associé au traitement de maladies médiées par le complément comme l'hémoglobinurie paroxystique nocturne (HPN) et le syndrome hémolytique et urémique atypique (SHUa) — ces indications figurent dans le contexte fourni mais ne sont pas confirmées par les données structurées de ce dossier. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **neutropénie congénitale sévère autosomique récessive liée à un déficit en G6PC3**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction, et le mécanisme d'action proposé n'est pas cohérent avec la physiopathologie de cette maladie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données structurées (contexte disponible : HPN, SHUa — maladies médiées par le complément) |
| Nouvelle Indication Prédite | Neutropénie congénitale sévère autosomique récessive due à un déficit en G6PC3 |
| Score de Prédiction TxGNN | 99.96 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude réelle) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel ne sont pas disponibles dans ce dossier. Selon le contexte du pipeline TxGNN, ravulizumab est un inhibiteur du complément terminal C5 (dérivé à action prolongée de l'eculizumab), dont l'usage connu concerne des maladies médiées par l'activation du complément.

Le déficit en G6PC3 est une maladie métabolique : un défaut de la sous-unité catalytique de la glucose-6-phosphatase entraîne un stress du réticulum endoplasmique et une apoptose accrue des précurseurs myéloïdes médullaires. Ce mécanisme n'implique pas la voie du complément.

L'analyse fournie avec ce dossier est explicite sur ce point : le score TxGNN élevé reflète très probablement une proximité entre nœuds « neutropénie / déficit immunitaire » dans le graphe de connaissances, et non une relation pharmacologique réelle. Aucune hypothèse mécanistique vérifiable ne peut être formulée en l'état — cette réserve s'applique d'ailleurs aux 10 indications prédites listées dans ce dossier, toutes classées L5/Hold pour la même raison.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN est élevé, mais il n'est appuyé par aucun essai clinique, aucune publication, et le rationnel mécanistique disponible indique explicitement l'absence de lien pharmacologique plausible entre l'inhibition du complément C5 et la physiopathologie du déficit en G6PC3. La prédiction ne peut pas franchir l'étape d'évaluation préliminaire de sécurité (S1), notamment parce que les données réglementaires TFDA (avertissements/contre-indications, DG001, sévérité *Blocking*) sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données officielles sur le mécanisme d'action (DrugBank) — DG002
- Notice/avertissements réglementaires TFDA pour l'évaluation de sécurité S1 — DG001, bloquant
- Études précliniques ciblées explorant un éventuel rôle du complément dans le déficit en G6PC3, avant d'envisager toute étude clinique
- Réévaluation si de nouveaux essais cliniques ou publications apparaissent pour cette association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

