---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase : De l'Hyperuricémie du Syndrome de Lyse Tumorale à l'Hypouricémie Rénale

## Résumé en Une Phrase

Rasburicase est une urate-oxydase recombinante, initialement utilisée pour traiter l'hyperuricémie aiguë liée au syndrome de lyse tumorale en oncologie. Le modèle TxGNN prédit qu'elle pourrait être pertinente pour l'**hypouricémie rénale**, mais cette prédiction n'est soutenue par **aucun essai clinique** ni **aucune publication**, et l'analyse mécanistique jointe au dossier indique que la direction pharmacologique est contradictoire (voir section suivante).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperuricémie aiguë associée au syndrome de lyse tumorale (chimiothérapie oncologique) |
| Nouvelle Indication Prédite | Hypouricémie rénale (renal hypouricemia) |
| Score de Prédiction TxGNN | 99.99% |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude réelle) |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Rasburicase est une urate-oxydase recombinante : elle oxyde l'acide urique en allantoïne, une molécule beaucoup plus soluble, ce qui **abaisse** rapidement l'uricémie. C'est ce mécanisme qui justifie son indication historique dans la prévention et le traitement de l'hyperuricémie aiguë du syndrome de lyse tumorale.

L'hypouricémie rénale (défaut de réabsorption tubulaire proximale de l'acide urique, lié à des anomalies des transporteurs URAT1/GLUT9) est à l'inverse une pathologie caractérisée par un acide urique **trop bas**. Administrer un médicament qui abaisse encore davantage l'uricémie n'a donc pas de logique mécanistique cohérente avec cette indication — le sens pharmacologique va à l'encontre du besoin clinique. Le dossier de preuves signale explicitement ce point comme une probable erreur de similarité d'embedding dans le graphe de connaissances (proximité du nœud « uricémie » sans distinction de direction), plutôt qu'un signal biologique réel.

Une hypothèse alternative plus cohérente figure en rang 2 du même lot de prédictions : le déficit partiel en HGPRT (syndrome de Kelley-Seegmiller), qui provoque au contraire une **hyperuricémie** par blocage de la voie de récupération des purines. Cette direction est compatible avec le mécanisme connu de rasburicase, mais aucune preuve clinique ou littéraire n'existe non plus pour cette piste à ce jour.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Rasburicase n'est actuellement pas commercialisé en France dans ce dossier (0 AMM active recensée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction de premier rang (hypouricémie rénale) est dépourvue de toute preuve clinique ou littéraire et présente une incohérence mécanistique majeure (direction pharmacologique opposée au besoin clinique). Aucune des 10 indications prédites pour cette molécule n'est soutenue par une étude réelle (toutes en niveau L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Résoudre l'écart bloquant DG001 : obtenir les mises en garde et contre-indications officielles (ANSM/notice), actuellement absentes, avant tout examen de sécurité (S1)
- Compléter l'écart DG002 : confirmer formellement le mécanisme d'action via l'API DrugBank
- Réévaluer la piste rang 2 (déficit partiel en HGPRT / syndrome de Kelley-Seegmiller), mécanistiquement plus plausible, et lancer une recherche ciblée d'essais cliniques et de littérature sur cette association
- Écarter ou requalifier la piste hypouricémie rénale sauf apparition d'un rationnel mécanistique solide contredisant l'analyse actuelle
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

