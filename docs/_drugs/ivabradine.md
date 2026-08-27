---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ivabradine : Indication d'Origine Non Documentée vers l'Hypertrichose

## Resume en Une Phrase

Les donnees disponibles ne permettent pas actuellement de documenter l'indication d'origine ni le mecanisme d'action complet d'ivabradine (lacune de donnees signalee, severite Blocking/High). Le modele TxGNN predit une efficacite potentielle pour l'**Hypertrichose**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction — il s'agit d'une prediction purement computationnelle (score TxGNN de 99,79 %, niveau de preuve L5).

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non documentee dans les donnees disponibles (lacune signalee) |
| Nouvelle Indication Predite | Hypertrichose |
| Score de Prediction TxGNN | 99,79 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action et sur l'indication d'origine d'ivabradine ne sont pas disponibles dans ce dossier (lacunes signalees DG001 et DG002). Les seules informations mecanistiques disponibles proviennent des notes d'analyse associees a la prediction elle-meme : ivabradine est connu pour inhiber le canal HCN4 (courant If, dit "funny current") du noeud sino-atrial, ce qui reduit la frequence cardiaque.

Or, selon ces memes notes d'analyse, il n'existe **aucun recoupement biologique connu** entre l'inhibition du canal HCN4 cardiaque et les voies de regulation de la croissance folliculaire impliquees dans l'hypertrichose. La prediction TxGNN repose donc sur un score de similarite eleve dans le graphe de connaissances, sans appui mecanistique, clinique ou bibliographique identifie a ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

## Informations de Marche en France

Ivabradine n'est actuellement **pas commercialise** en France selon les donnees disponibles (0 AMM recensee, aucune licence trouvee).

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
La prediction repose uniquement sur le score du modele TxGNN (niveau de preuve L5), sans essai clinique, sans publication et sans lien mecanistique identifie entre le mode d'action connu d'ivabradine et l'hypertrichose. De plus, l'absence de donnees sur l'indication d'origine, le MOA complet et le profil de securite (mises en garde, contre-indications, TFDA) empeche toute evaluation de securite initiale (S1).

**Pour avancer, les elements suivants sont necessaires :**
- Recuperation du texte de notice/allegement TFDA (mises en garde, contre-indications) — lacune bloquante (DG001)
- Confirmation du mecanisme d'action complet via l'API DrugBank (DG002)
- Documentation de l'indication d'origine et du statut d'AMM d'ivabradine
- Recherche exploratoire (preclinique/mecanistique) d'un lien plausible entre l'inhibition du canal HCN4 et la croissance pilaire, avant toute reevaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

