---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Iloprost : De l'Hypertension Artérielle Pulmonaire à l'Hypotrichosis Simplex du Scalp

## Résumé en Une Phrase

Iloprost est un analogue synthétique de la prostacycline (PGI2), reconnu dans plusieurs pays pour le traitement de l'hypertension artérielle pulmonaire sévère, bien qu'il ne dispose d'aucune autorisation de mise sur le marché en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypotrichosis Simplex du Scalp**,
cependant **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (médicament non commercialisé en France) |
| Nouvelle Indication Prédite | Hypotrichosis Simplex du Scalp |
| Score de Prédiction TxGNN | 99.45% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action d'iloprost ne sont pas disponibles dans ce dossier. Sur la base des informations connues, iloprost est un analogue synthétique stable de la prostacycline (PGI2) qui agit principalement via les récepteurs IP couplés aux protéines Gs, entraînant une élévation du cAMP intracellulaire. Cette voie confère des effets vasodilatateurs puissants, une inhibition de l'agrégation plaquettaire et une modulation de la réponse inflammatoire. Son efficacité dans l'hypertension artérielle pulmonaire (HAP) a été démontrée par des essais cliniques de Phase 3 et il est approuvé dans plusieurs pays européens et aux États-Unis pour cette indication.

Cependant, la connexion mécanistique entre iloprost et l'hypotrichosis simplex du scalp est extrêmement faible. L'hypotrichosis simplex est une génodermatose rare causée par des mutations des gènes LPAR6 ou LIPH, affectant la signalisation des lysophosphatidates dans le follicule pileux. Cette pathologie est génétiquement déterminée et structurellement étrangère aux voies de la prostacycline et des récepteurs IP.

Bien que certains analogues de prostaglandines — notamment le bimatoprost (analogue de PGF2α) — aient démontré des effets sur la croissance des cils et des poils, le rôle spécifique de PGI2 dans le cycle folliculaire pileux n'a jamais été établi. Le score élevé du modèle TxGNN pour cette indication semble refléter des effets de réseau indirect au sein du graphe de connaissances des prostaglandines, sans soutien de plausibilité biologique directe. Aucune étude préclinique ni clinique n'explore ce lien.

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
Il n'existe à ce jour aucune preuve clinique ni préclinique soutenant l'utilisation d'iloprost dans l'hypotrichosis simplex du scalp. La plausibilité mécanistique est très faible : la pathologie est génétique (mutations LPAR6/LIPH) et ne présente aucun point d'entrée thérapeutique connu pour la voie prostacycline.

> **Note clinique importante :** Bien que la prédiction de rang 1 ne soit pas exploitable, cet Evidence Pack contient des données d'un intérêt clinique significatif pour plusieurs sous-types de l'hypertension artérielle pulmonaire (HAP). En particulier, la HAP associée à l'infection VIH (rang 7) est soutenue par un essai de Phase 3 randomisé en double aveugle complété (NCT00709956, niveau L1), et la HAP associée à la cardiopathie congénitale (rang 3) ainsi que la HAP associée aux maladies du tissu conjonctif (rang 5) disposent toutes deux d'un niveau de preuve L3 avec recommandation « Proceed with Guardrails ». Il est conseillé d'évaluer ces indications en priorité dans la suite du pipeline.

**Pour avancer sur l'indication hypotrichosis simplex du scalp, les éléments suivants seraient nécessaires :**
- Données détaillées sur le mécanisme d'action d'iloprost (MOA complet via DrugBank)
- Études précliniques explorant le rôle de la voie PGI2/IP-receptor dans le follicule pileux
- Validation biologique de la connexion entre la signalisation prostacycline et les gènes LPAR6/LIPH
- Informations réglementaires françaises (ANSM) et données de sécurité complètes (voire juste une consultation de la SmPC internationale)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

