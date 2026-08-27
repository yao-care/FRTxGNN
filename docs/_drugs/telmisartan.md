---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan : De l'Hypertension Artérielle à l'Angine de Prinzmetal

## Résumé en Une Phrase

Le telmisartan est un antagoniste des récepteurs de l'angiotensine II (ARB), initialement indiqué dans le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Angine de Prinzmetal**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — il s'agit d'une prédiction algorithmique isolée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle |
| Nouvelle Indication Prédite | Angine de Prinzmetal |
| Score de Prédiction TxGNN | 99.98% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, le telmisartan appartient à la classe des ARB (antagonistes des récepteurs AT1 de l'angiotensine II), dont l'efficacité dans l'hypertension artérielle est bien établie.

L'angine de Prinzmetal est cependant une entité clinique distincte, causée par un vasospasme des artères coronaires, dont le traitement de référence repose sur les inhibiteurs calciques et les dérivés nitrés — des classes pharmacologiques sans lien direct avec le blocage du système rénine-angiotensine-aldostérone.

Selon l'analyse de plausibilité mécanistique associée à cette prédiction, **il n'existe actuellement aucune base mécanistique connue** justifiant l'usage d'un ARB dans le traitement du vasospasme coronarien, et aucun essai clinique ni aucune publication ne vient étayer cette hypothèse. Cette prédiction repose donc uniquement sur le score du modèle TxGNN, sans corroboration mécanistique ou empirique.

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
Malgré un score TxGNN élevé (99.98%), cette prédiction ne dispose d'aucun essai clinique, d'aucune publication, et d'aucune base mécanistique établie — le traitement de référence de l'angine de Prinzmetal (inhibiteurs calciques, dérivés nitrés) n'a pas de lien pharmacologique connu avec les ARB. Le niveau de preuve L5 (prédiction du modèle seule) ne justifie pas de poursuivre l'évaluation à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) du telmisartan via l'API DrugBank (DG002)
- Mises en garde et contre-indications TFDA (DG001), actuellement bloquantes pour toute évaluation de sécurité (S1)
- Études précliniques explorant un lien potentiel entre blocage AT1 et vasospasme coronarien, si l'hypothèse doit être creusée
- À noter : ce même dossier candidat contient une prédiction alternative (hémorragie intracérébrale, rang 9) appuyée par un essai de Phase 3 positif (TRIDENT, N=1671, réduction du risque de récidive de 7,4 % à 4,6 %) et classée en niveau de preuve L1 avec recommandation « Proceed with Guardrails » — cette piste mérite une évaluation prioritaire distincte.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

