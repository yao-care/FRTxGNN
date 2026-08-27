---
layout: default
title: Raltitrexed
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Raltitrexed
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

# Raltitrexed : d'une Indication d'Origine Non Renseignée à la Cholangite Sclérosante

## Résumé en Une Phrase

Le pack de preuves actuel ne renseigne aucune indication d'origine ni aucune licence pour la Raltitrexed (données de marché : non commercialisé, 0 AMM). Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **Cholangite Sclérosante**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — et l'analyse de repositionnement associée qualifie elle-même ce signal de mécaniquement non plausible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans ce pack (aucune licence ni `original_indications` enregistrée) |
| Nouvelle Indication Prédite | Cholangite Sclérosante (sclerosing cholangitis) |
| Score de Prédiction TxGNN | 99.97 % (rang TxGNN interne 527) |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude réelle) |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées sur le mécanisme d'action (MOA) ne sont pas disponibles dans ce pack. Les éléments qualitatifs fournis par l'analyse de repositionnement indiquent toutefois que la Raltitrexed agit par **inhibition de la thymidylate synthase (TS)**, un mécanisme cytotoxique antimétabolite ; sa toxicité dose-limitante rapportée est la **myélosuppression**.

L'indication d'origine du médicament n'étant pas renseignée dans ce pack (champ `original_indications` vide, aucune AMM française), la relation entre l'usage historique et la Cholangite Sclérosante ne peut pas être établie sur cette base.

Sur le plan mécanistique, l'analyse de repositionnement elle-même conclut à l'**absence de lien plausible** : la cholangite sclérosante est une maladie biliaire auto-immune/fibrosante, sans rapport connu avec un mécanisme cytotoxique anti-métabolite d'inhibition de la TS. Le pack qualifie explicitement ce signal de possible **bruit de l'espace d'embedding du modèle (faux positif)**. Ce jugement doit être pris en compte avant toute exploration supplémentaire.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Raltitrexed n'est pas commercialisé en France : statut « non commercialisé », 0 AMM enregistrée dans ce pack.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimétabolite, inhibiteur de la thymidylate synthase — TS) |
| Risque de Myélosuppression | Élevé — la toxicité dose-limitante rapportée dans l'analyse de repositionnement est la myélosuppression |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS (numération formule sanguine avec différentielle), fonction hépatique et rénale |
| Protection de Manipulation | Manipulation à réaliser selon les précautions applicables aux agents cytotoxiques (chimiothérapie) |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni aucune publication ne soutient l'indication prédite (niveau de preuve L5), et l'analyse de repositionnement qualifie elle-même le lien mécanistique de non plausible (probable bruit de l'espace d'embedding). Les autres indications prédites dans ce pack (ex. syndrome myélodysplasique, syndromes drépanocytaires) présentent en outre des mécanismes contradictoires avec un agent myélosuppresseur, renforçant la prudence globale sur ce candidat.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résolution du data gap bloquant DG001 (mises en garde/contre-indications TFDA) avant toute évaluation de sécurité S1
- Résolution du data gap DG002 (mécanisme d'action structuré via DrugBank)
- Confirmation ou infirmation du signal TxGNN par une recherche mécanistique ciblée (le pack suspecte un faux positif)
- Données réglementaires manquantes : indication d'origine et statut de licence à documenter
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

