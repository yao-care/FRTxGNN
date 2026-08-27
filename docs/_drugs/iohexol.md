---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 2
---

# Iohexol
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

この Evidence Pack には `predicted_indications[0]`（insomnia, score 99.87%）と `[1]`（anxiety, score 99.25%）の2件が含まれていますが、v5テンプレートの「Aperçu Rapide」「Preuves d'Essais Cliniques」「Preuves de la Littérature」は明示的に `predicted_indications[0]` を参照するよう指定されているため、これに従い insomnia を主要候補として報告を作成します。anxiety（第2候補）についてはエビデンスが弱く関連性が低いため、結論部分で補足情報として簡潔に触れます。

以下、ご指定のセクション順に報告書を作成します。

---

# Iohexol : De l'Agent de Contraste Radiologique a l'Insomnie

## Resume en Une Phrase

Iohexol est un agent de contraste iode non ionique utilise en imagerie medicale (myelographie, angiographie, urographie, etc.), et non un medicament a visee therapeutique classique.
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**Insomnie**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — la prediction repose uniquement sur le score algorithmique du modele.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Agent de contraste radiologique (usage diagnostique par imagerie, pas d'indication therapeutique enregistree) |
| Nouvelle Indication Predite | Insomnie |
| Score de Prediction TxGNN | 99.87% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | ✗ Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles pour l'iohexol. Sur la base des informations connues, il s'agit d'un agent de contraste iode non ionique utilise exclusivement a des fins diagnostiques (radiographie, myelographie, angiographie), sans rapport rapporte avec des recepteurs du systeme nerveux central impliques dans le sommeil (GABA-A, 5-HT, etc.).

Aucun lien mecanistique credible ne permet d'expliquer un effet hypnotique ou sedatif de l'iohexol. Le score eleve attribue par TxGNN provient tres probablement d'une co-occurrence indirecte dans le graphe de connaissances — par exemple, le fait que des patients subissant des examens d'imagerie (contexte ou l'iohexol est utilise) presentent frequemment de l'insomnie associee — plutot que d'une relation pharmacologique reelle.

En l'absence de toute donnee clinique ou pharmacologique de soutien, cette prediction doit etre consideree comme un signal statistique du modele necessitant une verification approfondie avant toute exploration ulterieure, et non comme une piste therapeutique etablie.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

> ⚠️ **Point bloquant** : les mises en garde et contre-indications officielles de la notice TFDA ne sont pas encore disponibles dans ce dossier, ce qui empeche toute evaluation de securite preliminaire (etape S1). Cette lacune doit etre comblee en priorite avant de poursuivre l'evaluation.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Le score TxGNN est eleve mais ne s'appuie sur aucun essai clinique ni aucune publication (Niveau de Preuve L5) ; il n'existe pas de mecanisme pharmacologique plausible reliant l'iohexol au traitement de l'insomnie.
- Les donnees de securite (mises en garde, contre-indications, notice TFDA) sont manquantes, ce qui empeche meme le franchissement de l'etape d'evaluation initiale de securite (S0 → S1).
- A titre de comparaison, le modele a egalement identifie l'**anxiete** comme candidat secondaire (rang 2, score 99.25%), mais les 6 essais cliniques et 6 publications associes concernent tous l'utilisation de l'iohexol comme produit de contraste ou outil de mesure de la fonction renale (pertinence classee C / faible), sans lien therapeutique direct avec l'anxiete. Ce second signal renforce l'hypothese que les predictions pour ce medicament resultent d'artefacts de similarite dans le graphe plutot que d'une piste pharmacologique reelle.

**Pour avancer, les elements suivants sont necessaires :**
- Obtention et analyse de la notice TFDA (mises en garde et contre-indications officielles) — element bloquant pour l'etape S1
- Donnees detaillees sur le mecanisme d'action (MOA) via DrugBank
- Une recherche cible sur une eventuelle activite au niveau du systeme nerveux central de l'iohexol (ex. cas de neurotoxicite/convulsions en cas de passage intrathecal), afin de confirmer l'absence de lien mecanistique plutot que de se fier a l'absence actuelle de donnees
- Reevaluation de la pertinence de ce candidat si de nouvelles publications ou essais cliniques directement lies au sommeil apparaissent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

