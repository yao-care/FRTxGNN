---
layout: default
title: Disopyramide
parent: Prédiction du modèle uniquement (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Disopyramide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Disopyramide : D'antiarythmique de classe Ia au syndrome de Gilles de la Tourette

## Résumé en Une Phrase

Le disopyramide est un médicament antiarythmique commercialisé en France (Isorythm L.P., Rythmodan). Le texte de son indication d'origine n'est pas renseigné dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Gilles de la Tourette**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette piste : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (classe antiarythmique) |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette (Tourette syndrome) |
| Score de Prédiction TxGNN | 99,86 % (rang 1542) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, le disopyramide est un antiarythmique de classe Ia, bloqueur des canaux sodiques, doté d'une activité anticholinergique.

Le syndrome de Gilles de la Tourette relève de circuits dopaminergiques cortico-striataux. Aucun lien mécanistique établi ne relie le blocage des canaux sodiques ou l'effet anticholinergique à cette physiopathologie. Le score élevé (0,9986) reflète probablement une proximité dans le graphe de connaissances avec des nœuds de maladies neuropsychiatriques, et non une justification biologique.

**Cette prédiction n'est donc pas soutenue mécanistiquement.** La piste la plus cohérente biologiquement dans cette liste est la tachycardie atriale multifocale (voir ci-dessous).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Autres Prédictions du Modèle

Aucune de ces prédictions n'a d'essai clinique. Le niveau de preuve est L5, sauf indication contraire.

| Rang | Indication prédite | Score TxGNN | Commentaire |
|------|------|------|------|
| 2 | Trouble déficitaire de l'attention avec hyperactivité (TDAH) | 99,82 % | Aucun lien avec les cibles catécholaminergiques du TDAH |
| 3 | Trichotillomanie | 99,81 % | Aucun mécanisme identifié |
| 4 | TDAH, type inattentif | 99,74 % | Sous-type redondant avec le TDAH |
| 5 | Syndrome facio-digito-génital | 99,66 % | Syndrome génétique rare, sans lien plausible |
| 6 | Trouble spécifique du développement | 99,54 % | Catégorie trop large et non spécifique |
| 7 | Flutter atrial néonatal idiopathique | 99,42 % | Plausible en principe, mais l'usage néonatal exigerait une évaluation pharmacocinétique et de sécurité dédiée |
| 8 | Fibrome chondromyxoïde | 99,41 % | Tumeur osseuse bénigne, sans lien plausible |
| 9 | Tachycardie atriale multifocale | 99,21 % | **L4, question de recherche.** Piste la plus cohérente, mais preuve indirecte (voir ci-dessous) |
| 10 | Tumeur du nerf trijumeau | 99,16 % | Aucun lien plausible |

**Tachycardie atriale multifocale (rang 9) :** la seule publication disponible est [PMID 7418495](https://pubmed.ncbi.nlm.nih.gov/7418495/) (Chest, 1980, cohorte). Elle porte sur la lorcaïnide, un autre antiarythmique, dans des arythmies ventriculaires résistantes. Le disopyramide y figure seulement parmi les traitements ayant échoué. Elle n'évalue donc ni le disopyramide ni la tachycardie atriale multifocale. Ce n'est qu'un soutien indirect, au niveau de la classe. Les effets anticholinergiques et inotropes négatifs, ainsi que la pathologie pulmonaire sous-jacente fréquente dans cette arythmie, nécessiteraient une revue de sécurité.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 66198796 | ISORYTHM L.P. 125 mg (SERP) | Gélule à libération prolongée |
| 66308461 | ISORYTHM L.P. 250 mg (SERP) | Gélule à libération prolongée |
| 63063487 | RYTHMODAN 100 mg (Cheplapharm) | Gélule |
| 69235837 | RYTHMODAN 250 mg à libération prolongée (Cheplapharm) | Comprimé enrobé |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les prédictions reposent uniquement sur le score du modèle (L5), sans essai ni publication, et pour le syndrome de Gilles de la Tourette aucun lien mécanistique plausible n'est identifié.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) en téléchargeant et analysant le PDF.
- Obtenir le mécanisme d'action détaillé via l'API DrugBank.
- Si une piste doit être poursuivie, prioriser la tachycardie atriale multifocale : revue de littérature ciblée sur le disopyramide dans les arythmies atriales et évaluation de sécurité.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

