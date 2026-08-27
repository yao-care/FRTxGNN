---
layout: default
title: Quinapril
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Quinapril : De l'Hypertension à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Quinapril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), utilisé pour le traitement de l'hypertension artérielle. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypertension Rénovasculaire Maligne**, avec un score de prédiction de **99,86 %**, mais **aucun essai clinique ni publication** ne soutient actuellement cette direction — et le lien mécanistique comporte un signal de risque notable, l'hypertension rénovasculaire étant une contre-indication relative classique aux IEC.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (déduite des rationales mécanistiques fournies dans le pack de preuves ; non confirmée par une fiche réglementaire dédiée) |
| Nouvelle Indication Prédite | Hypertension Rénovasculaire Maligne |
| Score de Prédiction TxGNN | 99,86 % (rang 1567) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources structurées (ce champ est marqué comme lacune de priorité élevée, DG002, à combler via DrugBank). Sur la base des rationales mécanistiques fournies dans le pack de preuves, Quinapril appartient à la classe des inhibiteurs de l'enzyme de conversion de l'angiotensine (IEC) : il inhibe la production d'angiotensine II et abaisse ainsi la pression artérielle systémique, un effet de classe bien établi dans le traitement de l'hypertension.

Sur le plan mécanistique, une action antihypertensive systémique pourrait sembler transposable à une forme sévère d'hypertension comme l'hypertension rénovasculaire maligne. C'est probablement ce lien générique « IEC ↔ hypertension » que le graphe TxGNN capture pour produire un score élevé.

Ce lien doit toutefois être nuancé fortement : l'hypertension rénovasculaire (en particulier en cas de sténose bilatérale des artères rénales ou de sténose sur rein unique) est une **contre-indication relative reconnue** aux IEC. La dilatation de l'artériole efférente qu'ils provoquent peut faire chuter brutalement la pression de filtration glomérulaire et précipiter une insuffisance rénale aiguë. Le score TxGNN élevé reflète donc vraisemblablement une association générique « IEC-hypertension » dans l'espace d'embedding, sans que le modèle ait capturé cette nuance de risque directionnel propre au sous-type rénovasculaire — d'où le maintien en stade S0/Hold.

Les quatre autres candidats prédits pour ce médicament présentent un profil de preuve similairement faible : la néphropathie hypertensive maligne (rang 2) s'appuie sur un effet de classe rénoprotecteur des IEC plausible mais sans aucun essai ni publication directe ; les deux formes d'hypertension pulmonaire (rangs 3 et 4, groupes OMS 3 et 5) sont dominées par des mécanismes hypoxiques/HIF-1α indépendants du système rénine-angiotensine, et la littérature associée (20 références) ne concerne que la biologie générale de l'hypoxie sans mention de quinapril ni d'IEC ; le syndrome de Braddock (rang 5), une maladie génétique rare, n'a aucun lien biologique connu avec la voie IEC. L'hypertension rénovasculaire maligne reste donc, malgré ses limites, le candidat le mieux étayé mécanistiquement du lot.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'hypertension rénovasculaire maligne.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypertension rénovasculaire maligne.

## Considérations de Sécurité

Les mises en garde, contre-indications et interactions médicamenteuses officielles (notice TFDA) ne sont pas encore disponibles dans le pack de preuves — il s'agit d'une lacune bloquante (DG001) empêchant toute évaluation de sécurité de niveau S1. Veuillez consulter la notice officielle avant toute utilisation.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Niveau de preuve L5 : aucun essai clinique ni publication ne soutient directement l'usage de quinapril dans l'hypertension rénovasculaire maligne.
- Une lacune bloquante (DG001) empêche l'évaluation de sécurité initiale (S1) faute de notice TFDA disponible.
- Le mécanisme proposé comporte un risque directionnel documenté (les IEC sont relativement contre-indiqués en cas de sténose des artères rénales), ce qui affaiblit la plausibilité clinique malgré le score TxGNN élevé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice TFDA (ou équivalente EU/France) pour lever la lacune DG001 (mises en garde, contre-indications)
- Confirmer le mécanisme d'action détaillé via l'API DrugBank (DG002)
- Rechercher spécifiquement la littérature « IEC et sténose de l'artère rénale » ou « hypertension maligne » pour valider ou réfuter ce signal
- Évaluation néphrologique du rapport bénéfice/risque avant toute exploration clinique, compte tenu du risque d'insuffisance rénale aiguë
- Clarifier le statut réglementaire en France (actuellement non commercialisé, 0 AMM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

