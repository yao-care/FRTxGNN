---
layout: default
title: Molsidomine
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Molsidomine
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

Le skill txgnn-pipeline concerne le pipeline global (entraînement, déploiement multi-pays), pas la génération d'un rapport individuel à partir d'un Evidence Pack déjà fourni — je génère donc directement le rapport selon le template v5 fourni.

---

# Molsidomine : De l'Angine de Poitrine à l'Alopécie

## Résumé en Une Phrase

Molsidomine est un donneur de monoxyde d'azote (NO), historiquement approuvé en Europe pour le traitement de l'angine de poitrine et de la maladie coronarienne. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Alopécie**, mais à ce jour **aucun essai clinique** ne soutient cette direction, et les **2 publications** identifiées sont des faux positifs de recherche sans rapport direct avec le médicament.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Angine de poitrine / maladie coronarienne (usage historique en Europe ; données d'AMM locales indisponibles) |
| Nouvelle Indication Prédite | Alopécie |
| Score de Prédiction TxGNN | 99.99995 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) ne sont pas disponibles dans cette fiche (data gap). Sur la base des informations disponibles ailleurs dans l'Evidence Pack, la molsidomine est une prodrogue de type sydnonimine, métabolisée en linsidomine (SIN-1), qui libère du monoxyde d'azote de façon non enzymatique, active la guanylate cyclase et entraîne une relaxation du muscle lisse vasculaire (artériel et veineux). C'est ce mécanisme qui sous-tend son usage historique établi en Europe dans l'angine de poitrine et la maladie coronarienne.

L'hypothèse de repositionnement vers l'alopécie repose sur une analogie avec le minoxidil, un autre vasodilatateur dont l'effet stimulant sur la pousse des cheveux est attribué à l'amélioration du flux sanguin folliculaire. Par extrapolation mécanistique, un effet vasodilatateur comparable pourrait théoriquement favoriser la croissance capillaire.

Cependant, cette analogie n'est **pas confirmée par des données propres à la molsidomine** : les deux publications retrouvées par la recherche documentaire (PMID 16879589 et 16188012) portent en réalité sur la madarose (perte des cils) causée par une mitochondriopathie, un sujet sans rapport avec la molsidomine — il s'agit d'un faux positif de recherche par mots-clés. Aucun essai clinique n'existe. La prédiction reste donc purement computationnelle (TxGNN), non étayée par une preuve mécanistique ou clinique réelle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16879589](https://pubmed.ncbi.nlm.nih.gov/16879589/) | 2006 | Rapport de cas | Acta Ophthalmologica Scandinavica | Madarose (perte des cils/sourcils) liée à une mitochondriopathie — sans rapport avec la molsidomine (faux positif de recherche) |
| [16188012](https://pubmed.ncbi.nlm.nih.gov/16188012/) | 2005 | Rapport de cas | Acta Ophthalmologica Scandinavica | Même sujet que ci-dessus (possible doublon/variante de la même publication) — sans rapport avec la molsidomine |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(Note interne : les mises en garde TFDA, contre-indications et interactions médicamenteuses sont actuellement des data gaps — DG001, sévérité bloquante — empêchant toute évaluation de sécurité S1.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un score TxGNN très élevé, aucune preuve clinique ou littéraire réelle ne soutient l'usage de la molsidomine dans l'alopécie — les deux publications retrouvées sont des faux positifs sans rapport avec le médicament, et aucun essai clinique n'existe. Le lien mécanistique proposé repose sur une simple analogie avec le minoxidil, non vérifiée pour ce médicament.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le résumé des caractéristiques du produit / mises en garde TFDA (DG001, bloquant) pour permettre l'évaluation de sécurité S1
- Confirmer le mécanisme d'action détaillé via DrugBank (DG002)
- Mener une recherche documentaire et d'essais cliniques ciblée spécifiquement sur « molsidomine + alopécie » afin d'écarter définitivement le faux positif actuel ou d'identifier de vraies données
- À titre de comparaison, noter que la même Evidence Pack identifie une piste bien mieux étayée pour la molsidomine : « vascular disease » (rang 2, niveau de preuve L2, essai de Phase 4 randomisé contrôlé n=165, NCT01363661), cohérente avec son indication d'origine — à évaluer séparément comme candidat prioritaire
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

