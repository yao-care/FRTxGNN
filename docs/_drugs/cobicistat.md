---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Cobicistat : De l'Amplificateur Pharmacocinétique HIV au Syndrome d'Immunodéficience Acquise Féline

## Résumé en Une Phrase

Cobicistat est un inhibiteur sélectif du CYP3A4, utilisé comme agent d'amplification pharmacocinétique dans les combinaisons antirétrovirales pour le traitement du VIH chez l'humain. Le modèle TxGNN prédit qu'il pourrait être utile dans le **syndrome d'immunodéficience acquise féline (FIV)**, en s'appuyant sur la proximité phylogénétique entre le FIV et le VIH (tous deux appartenant à la famille des lentivirus). Cependant, **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Amplificateur pharmacocinétique dans les combinaisons anti-VIH (non approuvé en France en monothérapie) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline (FIV) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier actuel. Sur la base des informations connues, cobicistat est un inhibiteur puissant et sélectif du CYP3A4 (et accessoirement de CYP2D6), sans activité antivirale intrinsèque. Son rôle clinique est exclusivement celui d'un « boosteur » pharmacocinétique : il ralentit le métabolisme des antirétroviraux co-administrés (ex. elvitégravir, atazanavir, darunavir), augmentant ainsi leur exposition plasmatique.

La relation entre l'indication originale (VIH) et la nouvelle indication prédite (FIV) repose sur une homologie virale : le virus de l'immunodéficience féline (FIV) est un lentivirus, tout comme le VIH. TxGNN exploite cette connexion dans son graphe de connaissances pour transposer l'association médicament–maladie. Cette inférence est biologiquement plausible en théorie, mais elle se heurte à une limite fondamentale : cobicistat n'agit pas directement contre le virus, il potentialise uniquement d'autres molécules antivirales. Son utilisation isolée dans le FIV serait donc sans effet thérapeutique direct.

Un obstacle supplémentaire est l'incertitude sur la conservation de l'enzyme CYP3A4 chez le chat (*Felis catus*), dont le profil métabolique diffère significativement de celui des primates. L'efficacité de l'inhibition enzychimique chez cette espèce n'a pas été évaluée. La prédiction relève donc d'une extrapolation graphique du modèle, sans ancrage mécanistique ou clinique démontré.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN repose uniquement sur une inférence graphique (lentivirus VIH ↔ FIV), sans aucun soutien clinique, préclinique ou mécanistique. Cobicistat étant dépourvu d'activité antivirale propre, son repositionnement isolé dans le FIV est pharmacologiquement non fondé en l'état.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action complètes (MOA DrugBank) pour confirmer le profil enzymatique
- Évaluation de la conservation du CYP3A4 félin et de sa sensibilité à l'inhibition par cobicistat
- Identification d'un agent antiviral vétérinaire actif contre le FIV avec lequel cobicistat pourrait jouer un rôle de boosteur
- Études précliniques chez le chat (*in vitro* ou modèle animal) avant toute considération clinique
- Données de sécurité (avis en garde, contre-indications, interactions) pour compléter l'évaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

