---
layout: default
title: Vestronidase Alfa
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
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

# Vestronidase Alfa : De la Mucopolysaccharidose de Type VII (Syndrome de Sly) au Syndrome de Scheie

## Resume en Une Phrase

Vestronidase alfa est une β-glucuronidase humaine recombinante (GUSB), utilisee comme therapie de remplacement enzymatique pour la mucopolysaccharidose de type VII (MPS VII, syndrome de Sly), une maladie ultra-rare.
Le modele TxGNN predit qu'elle pourrait etre efficace pour le **syndrome de Scheie** (une forme legere de MPS I),
mais cette direction n'est actuellement soutenue par **aucun essai clinique ni aucune publication**, et son mecanisme d'action est incompatible avec celui de la maladie ciblee.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Mucopolysaccharidose de type VII (syndrome de Sly)* |
| Nouvelle Indication Predite | Syndrome de Scheie |
| Score de Prediction TxGNN | 99.90% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

*Le champ officiel d'indication d'origine est absent des donnees reglementaires (aucune AMM en France). L'indication ci-dessus est reconstituee a partir des publications citees dans le dossier de preuves (PMID 32063397, 30467742), qui decrivent vestronidase alfa comme le traitement enregistre de la MPS VII.

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les donnees structurees de MOA sont marquees comme absentes (`[Data Gap]`) dans le dossier. Sur la base des publications disponibles, vestronidase alfa est une β-glucuronidase (GUSB) recombinante administree par voie IV, qui restaure l'activite enzymatique deficiente dans la MPS VII et reduit l'accumulation urinaire de glycosaminoglycanes (GAG).

Le syndrome de Scheie, cible par la prediction de rang 1, est en realite une forme legere de MPS I, causee par un deficit en **α-L-iduronidase (IDUA)** et non en β-glucuronidase. Les deux enzymes agissent sur des liaisons glycosidiques differentes (liaison iduronique vs liaison glucuronique) et ne sont pas interchangeables dans une therapie de remplacement enzymatique. Le dossier de preuves lui-meme signale ce point : *« Scheie syndrome ... avec GUSB 酵素替代機轉不匹配，無任何直接或間接臨床證據支持 »*.

Ce constat n'est pas isole : les predictions de rang 2 a 9 pour ce medicament presentent le meme profil — scores TxGNN eleves mais absence de lien mecanistique verifie (plusieurs sont des syndromes ophtalmologiques ou neurologiques congenitaux sans rapport avec le metabolisme lysosomal). Cela suggere un signal de similarite d'embedding plutot qu'une hypothese biologiquement fondee, probablement du fait de la rarete extreme de la maladie d'origine et du peu de donnees d'entrainement disponibles.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement pour l'indication Syndrome de Scheie.

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement pour l'indication Syndrome de Scheie.

---

## Informations de Marche en France

Vestronidase alfa n'est associe a aucune AMM en France (0 AMM enregistree, statut : non commercialise).

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le score TxGNN est eleve, mais aucune preuve clinique ou litteraire ne soutient l'indication Syndrome de Scheie, et le mecanisme d'action (GUSB) est incompatible avec la physiopathologie de cette maladie (deficit en IDUA). Il s'agit vraisemblablement d'un artefact du modele plutot que d'une hypothese exploitable.

**Pour avancer, les elements suivants sont necessaires :**
- Mises en garde et contre-indications officielles (donnee bloquante DG001 — necessaire avant toute evaluation de securite S1)
- Confirmation du mecanisme d'action detaille aupres de DrugBank (DG002)
- Une revalidation biologique du lien MPS VII → syndrome de Scheie, ou l'exploration d'indications alternatives mieux alignees mecanistiquement (ex. autres formes de MPS avec deficit en GUSB)
- Si aucune piste mecanistique solide n'emerge, ecarter cette prediction au profit d'autres candidats du pipeline TxGNN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

