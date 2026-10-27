---
layout: default
title: Lactic Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 430
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lactic Acid : nouvelle indication prédite, Coarctation atypique de l'aorte (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM (texte d'indication vide)"
monitor_inn: "lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome"]
---

# Lactic Acid
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Acide lactique : De l'usage homéopathique à la malformation aortique atypique (coarctation atypique de l'aorte)
{: .text-alpha }

## Résumé en Une Phrase

L'acide lactique est un métabolite endogène, commercialisé en France sous forme de préparations homéopathiques (Lacticum acidum Lehning et Boiron), dont les deux autorisations sont aujourd'hui annulées et sans indication approuvée renseignée.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **coarctation atypique de l'aorte**, avec un score élevé (99,59 %).
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutient pour cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Coarctation atypique de l'aorte |
| Score de Prédiction TxGNN | 99,59 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. L'acide lactique est un métabolite endogène du métabolisme énergétique, présent dans l'organisme, et les produits français concernés sont des préparations homéopathiques diluées, sans indication officielle renseignée.

Les données compilées pour ce rapport ne permettent pas d'établir de lien mécanistique crédible entre l'acide lactique et la coarctation atypique de l'aorte. Il s'agit d'une malformation vasculaire congénitale, d'origine développementale. On ne connaît à l'acide lactique aucune action pharmacologique sur le développement structurel de l'aorte. Le score élevé du modèle (99,59 %) reflète une association dans le graphe de connaissances, et non une preuve biologique ou clinique.

La similarité avec l'indication d'origine ne peut pas être évaluée, faute d'indication originale documentée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

À titre de contexte, pour la deuxième prédiction (malformation aortique), 14 publications ont été retrouvées, mais elles sont très éloignées du sujet : métabolisme de la paroi aortique dans l'athérosclérose expérimentale chez le lapin (1988), chirurgie cardiaque pédiatrique, dispositifs biodégradables en acide poly-L-lactique, extrait de plante chez le rat hypertendu. L'acide lactique n'y apparaît, au mieux, que comme biomarqueur ou matériau, jamais comme traitement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 62740203 | LACTICUM ACIDUM LEHNING, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée | Annulée |
| 61120110 | LACTICUM ACIDUM BOIRON, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée | Annulée |

## Considérations de Sécurité

**Interactions Médicamenteuses** : 17 interactions ont été recensées, de niveau modéré ou mineur (aucune de niveau majeur).

- **Niveau modéré** : doxycycline, tétracycline, minocycline, déméclocycline, oxytétracycline, acide acétylsalicylique, salicylate de sodium, éphédrine (y compris nasale), pseudoéphédrine.
- **Niveau mineur** : sulfamides hypoglycémiants (chlorpropamide, tolazamide, glipizide, glyburide, acétohexamide, tolbutamide) et méthotrexate.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente. Aucun lien mécanistique plausible n'est identifié entre l'acide lactique et une malformation aortique congénitale. Les deux AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de l'acide lactique, afin d'analyser un éventuel lien mécanistique.
- Mises en garde et contre-indications issues de la notice officielle de l'ANSM (bloquant pour toute étape de sécurité).
- Une hypothèse biologique crédible reliant l'acide lactique à la malformation aortique, étayée par des études précliniques.
- Évaluation de la compatibilité des voies d'administration, aujourd'hui non établie.

**Autres prédictions examinées (pour information) :**

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|---|---|---|---|---|
| 2 | Malformation aortique | 99,35 % | L5 | Hold |
| 3 | Malformation œsophagienne non syndromique | 99,23 % | L5 | Hold |
| 4 | Aménorrhée | 99,16 % | L5 | Hold |
| 5 | Syndrome de l'œil sec | 99,13 % | L4 | Question de recherche |

Parmi elles, seul le syndrome de l'œil sec présente un indice indirect : l'acide lactique est un composant normal du film lacrymal et des altérations métaboliques sont décrites dans le syndrome de Sjögren. Les études disponibles portent cependant sur des probiotiques ou d'autres agents, et non sur l'acide lactique lui-même. Cette piste reste une hypothèse de recherche (pH ou osmolarité de la surface oculaire), sans soutien clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

