---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 2
---

# Nimodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Nimodipine : De la Prévention du Vasospasme Cérébral à l'Hypercholestérolémie Familiale Homozygote

## Résumé en Une Phrase

Nimodipine est un inhibiteur calcique de type L hautement sélectif, historiquement utilisé pour prévenir le vasospasme cérébral après hémorragie sous-arachnoïdienne.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypercholestérolémie Familiale Homozygote (HoFH)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction — la prédiction repose uniquement sur le score du modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Prévention du vasospasme cérébral après hémorragie sous-arachnoïdienne (usage pharmacologique connu de la classe ; aucune fiche AMM structurée disponible dans les données reçues) |
| Nouvelle Indication Prédite | Hypercholestérolémie Familiale Homozygote (HoFH) |
| Score de Prédiction TxGNN | 99.29 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles pour nimodipine dans ce dossier. Sur la base des informations connues, il s'agit d'un inhibiteur calcique de type L hautement sélectif dont l'usage clinique établi cible le muscle lisse vasculaire cérébral (prévention du vasospasme après hémorragie sous-arachnoïdienne).

La HoFH résulte de mutations du récepteur LDL (ou d'APOB/PCSK9) empêchant la clairance du LDL-cholestérol ; les traitements actuels (statines, inhibiteurs de PCSK9, lomitapide, evinacumab) agissent tous sur la voie du métabolisme lipoprotéique. Aucune donnée mécanistique ou bibliographique disponible ne relie les inhibiteurs calciques à l'expression du récepteur LDL, à PCSK9 ou à la voie ANGPTL3.

En l'état, le lien entre le mécanisme connu de nimodipine et la physiopathologie de la HoFH n'est pas établi : cette prédiction est portée uniquement par le score statistique du modèle TxGNN (99.29 %), sans support biologique ou clinique identifié à ce jour.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(Remarque : les mises en garde et contre-indications réglementaires (TFDA) ne sont pas encore disponibles dans ce dossier — il s'agit d'un écart bloquant pour l'évaluation de sécurité, cf. section suivante.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucune preuve clinique ou bibliographique (0 essai, 0 publication) ne soutient cette indication, et le lien mécanistique entre nimodipine et la HoFH n'est pas établi. La prédiction repose uniquement sur le score TxGNN (niveau de preuve L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données du mécanisme d'action (MOA) de nimodipine, actuellement en écart bloquant
- Mises en garde et contre-indications réglementaires (notice TFDA), écart bloquant pour toute évaluation de sécurité (DG001)
- Études précliniques explorant un lien biologique plausible entre blocage calcique de type L et voies du métabolisme lipoprotéique
- Toute donnée clinique ou observationnelle émergente sur cette association

---

*Note complémentaire : les données fournies contiennent une seconde indication prédite — le syndrome néphrogénique de sécrétion inappropriée d'ADH (NSIAD), score TxGNN 99.05 %, également sans essai clinique ni littérature associée (L5). Le même constat s'applique : absence de lien mécanistique identifié entre le blocage calcique et la voie AVPR2/cAMP-PKA, décision Hold.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

