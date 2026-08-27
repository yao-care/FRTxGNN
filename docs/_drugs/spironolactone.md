---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone : De l'Hypertension et des Œdèmes à l'Hypotrichose Simple du Cuir Chevelu

## Résumé en Une Phrase

Spironolactone est un antagoniste de l'aldostérone (diurétique épargneur de potassium), historiquement utilisé dans l'hypertension artérielle, les œdèmes (insuffisance cardiaque, cirrhose) et l'hyperaldostéronisme primaire. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypotrichose simple du cuir chevelu** (*hypotrichosis simplex of the scalp*), mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction — la prédiction repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle, œdèmes (insuffisance cardiaque, cirrhose), hyperaldostéronisme primaire *(usage établi ; non documenté dans les licences françaises de cette source — médicament non commercialisé en France)* |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu |
| Score de Prédiction TxGNN | 99.26 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cette source (donnée manquante classée « High »). Sur la base des informations connues, la spironolactone est un antagoniste du récepteur de l'aldostérone possédant également une activité anti-androgénique (blocage du récepteur aux androgènes, inhibition de la synthèse de testostérone), ce qui explique son usage établi dans l'alopécie androgénétique et l'hirsutisme chez la femme.

Cependant, l'hypotrichose simple du cuir chevelu est une maladie congénitale à transmission autosomique dominante, généralement liée à des mutations des gènes *APCDD1* ou *CDH3*, qui altèrent le développement structurel du follicule pileux — un mécanisme totalement indépendant de la voie des androgènes ou de l'aldostérone.

Le score élevé attribué par TxGNN provient donc très probablement d'une proximité sémantique dans le graphe de connaissances (les concepts « alopécie » et « hypotrichose » étant lexicalement proches), plutôt que d'un lien mécanistique réel. Il s'agit d'un lien faible, à considérer avec un haut degré de scepticisme.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Spironolactone n'est actuellement pas commercialisé en France selon cette source (0 AMM enregistrée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. *(À noter : les mises en garde et contre-indications TFDA n'ont pas pu être récupérées — écart de données classé « Blocking », ce qui empêche l'évaluation initiale de sécurité S1.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle seule, sans essai clinique ni publication), et le lien mécanistique lui-même est jugé faible — probablement un artefact de proximité sémantique dans le graphe de connaissances plutôt qu'une relation causale. De plus, une donnée bloquante (allergies/mises en garde TFDA) empêche toute évaluation de sécurité, et le médicament n'est pas commercialisé en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde et contre-indications TFDA (écart bloquant DG001)
- Données complètes sur le mécanisme d'action via DrugBank (écart DG002)
- Étude préclinique ou mécanistique établissant un lien plausible entre la voie anti-androgénique et l'hypotrichose simple (maladie structurelle/génétique)
- Au moins une publication ou un essai clinique corroborant l'hypothèse, actuellement absents

**Note :** Une seconde indication prédite, *congenital hypotrichosis milia* (score 99.04 %, rang 6219), présente le même profil — L5, Hold, aucune preuve clinique, et une justification mécanistique jugée tout aussi faible (syndrome génétique structurel sans lien évident avec la voie de l'aldostérone/androgènes).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

