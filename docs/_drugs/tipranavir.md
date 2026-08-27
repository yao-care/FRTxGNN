---
layout: default
title: Tipranavir
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir : De l'Infection à VIH-1 au Syndrome d'Immunodéficience Acquise Féline

## Résumé en Une Phrase

Tipranavir est un inhibiteur non-peptidique de la protéase du VIH-1, initialement utilisé pour le traitement de l'infection à VIH-1 chez les patients prétraités et multirésistants.
Le modèle TxGNN predit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline (FIV)**,
mais cette direction n'est actuellement soutenue par **aucun essai clinique** ni **aucune publication**, et le lien mécanistique est jugé faible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection à VIH-1 (patients prétraités) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline (FIV) |
| Score de Prédiction TxGNN | 99.99% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier (Data Gap). Sur la base des informations connues rapportées dans l'analyse de repositionnement, tipranavir est un inhibiteur non-peptidique de la protéase du VIH-1 ; son efficacité dans le traitement de l'infection à VIH-1 (notamment chez les patients multirésistants) est établie, et mécanistiquement l'inhibition d'une protéase virale pourrait, en théorie, être extrapolée à d'autres infections rétrovirales.

Le VIH-1 (humain) et le FIV (félin) sont tous deux des lentivirus, ce qui explique la proximité de ces deux maladies dans l'espace de représentation du modèle TxGNN et le score de prédiction très élevé (99.99%).

Cependant, cette similarité reste superficielle : la structure de la protéase du FIV diffère sensiblement de celle du VIH-1, et les inhibiteurs de protéase développés pour le VIH-1 ne présentent généralement pas d'activité croisée contre le FIV. Aucune étude clinique ou préclinique ne vient étayer cette prédiction à ce jour — elle doit donc être considérée comme un signal de faible fiabilité, probablement lié à un artefact du modèle plutôt qu'à une réelle transférabilité pharmacologique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un score TxGNN élevé, aucune preuve clinique, préclinique ou bibliographique ne soutient l'usage de tipranavir dans le FIV, et le lien mécanistique est jugé faible du fait des différences structurelles entre les protéases du VIH-1 et du FIV (niveau de preuve L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) confirmées via DrugBank
- Fiche officielle (notice/mises en garde) de l'autorité de santé compétente, actuellement bloquante pour toute évaluation de sécurité
- Étude in vitro confirmant (ou infirmant) une activité inhibitrice de tipranavir sur la protéase du FIV avant toute investigation clinique
- Réévaluation des autres candidats du même lot de prédictions : la piste « congenital human immunodeficiency virus » (rang 6, niveau L3, 9 essais cliniques identifiés bien que portant sur d'autres molécules que tipranavir) mérite un examen distinct, indépendant de la prédiction FIV présentée ici
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

