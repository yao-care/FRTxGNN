---
layout: default
title: Mianserin
parent: Prédiction du modèle uniquement (L5)
nav_order: 496
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mianserin : nouvelle indication prédite, Torticolis paroxystique bénin du nourrisson (niveau de preuve L5). Indication d'origine : Dépression unipolaire, dépression endogène, trouble dépressif majeur…"
monitor_inn: "mianserin"
predicted_indications: ["benign paroxysmal torticollis of infancy", "dysthymic disorder", "agoraphobia", "Ohdo syndrome and variants", "melancholia", "neurotic depression", "neurotic disorder"]
---

# Mianserin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Mianserine : De la dépression unipolaire à la torticolis paroxystique bénigne du nourrisson

## Résumé en Une Phrase

La mianserine est un antidépresseur tétracyclique, initialement utilisé pour le traitement de la dépression (unipolaire, endogène, trouble dépressif majeur) et des troubles anxieux.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **torticolis paroxystique bénin du nourrisson**, mais cette prédiction repose **uniquement sur le modèle** : **aucun essai clinique** et **aucune publication** ne la soutiennent.
Pour des indications voisines de l'indication d'origine (dysthymie, mélancolie, dépression névrotique), la littérature disponible est plus fournie, mais reste surtout indirecte.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dépression unipolaire, dépression endogène, trouble dépressif majeur, trouble anxieux (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Torticolis paroxystique bénin du nourrisson |
| Score de Prédiction TxGNN | 99,49 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations pharmacologiques compilées, la mianserine se lie à plusieurs récepteurs sérotoninergiques (5-HT1B, 5-HT2A, 5-HT2B, 5-HT2C, 5-HT6, 5-HT7), aux récepteurs adrénergiques α1 (A, B, D), au récepteur LPA1 et au transporteur de la noradrénaline (NET). Elle agit donc sur les systèmes sérotoninergique et noradrénergique.

Le torticolis paroxystique bénin du nourrisson est un trouble pédiatrique de type canalopathie (souvent lié au gène CACNA1A), apparenté au spectre des migraines. Le lien avec l'action de la mianserine sur ces récepteurs reste **spéculatif** : aucune donnée ne le documente. De plus, la mianserine n'est plus commercialisée en France sous la forme recensée et aucune donnée de sécurité n'est disponible chez le nourrisson.

Il faut donc considérer cette prédiction comme une hypothèse issue du graphe, non comme un résultat étayé. D'autres prédictions du même modèle sont nettement plus plausibles, car proches de l'indication d'origine :
- **Dysthymie** (score 99,45 %, niveau L4) : trouble dépressif chronique de moindre intensité, très proche de la dépression ; une méta-analyse d'essais contrôlés sur les antidépresseurs (PMID 21527126) existe, mais elle porte sur la classe et non sur la mianserine.
- **Mélancolie** (99,17 %, L4) et **dépression névrotique** (99,16 %, L4) : quasiment des indications d'origine, avec des revues propres à la mianserine et des méta-analyses sur les antidépresseurs.
- **Trouble névrotique** (99,02 %, L3) : études comparatives propres à la mianserine (vs imipramine, vs clomipramine), mais anciennes et de petite taille.
- **Agoraphobie** (99,40 %, L4) : une seule publication, portant sur les IMAO-A réversibles, donc très indirecte.
- **Syndrome d'Ohdo et variants** (99,23 %, L5) : aucun lien mécanistique visible.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le torticolis paroxystique bénin du nourrisson.

À titre indicatif, pour les indications voisines, les publications les plus pertinentes sont :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Méta-analyse d'ECR | J Clin Psychiatry | Efficacité des antidépresseurs dans la dysthymie (analyse de classe, sans résultat propre à la mianserine) |
| [7710969](https://pubmed.ncbi.nlm.nih.gov/7710969/) | 1994 | Étude comparative | Rom J Neurol Psychiatry | Mianserine vs imipramine dans les troubles dépressifs mineurs (129 patients) |
| [7032887](https://pubmed.ncbi.nlm.nih.gov/7032887/) | 1981 | Analyse d'études contrôlées | L'Encéphale | Mianserine vs clomipramine : pas de différence significative d'efficacité ; début d'action plus précoce dans la dépression endogène |
| [6824555](https://pubmed.ncbi.nlm.nih.gov/6824555/) | 1983 | Essai comparatif en double aveugle | Br J Clin Pharmacol | Mianserine vs doxépine dans la dépression avec anxiété : amélioration substantielle avec les deux, sans différence constante |
| [2864794](https://pubmed.ncbi.nlm.nih.gov/2864794/) | 1985 | Essai multicentrique en double aveugle | Acta Psychiatr Scand Suppl | Mianserine vs nomifensine chez 61 patients déprimés |
| [29530157](https://pubmed.ncbi.nlm.nih.gov/29530157/) | 2016 | Revue systématique / méta-analyse | J Prim Health Care | Antidépresseurs dans la dépression en soins primaires |
| [38379028](https://pubmed.ncbi.nlm.nih.gov/38379028/) | 2024 | Analyse comparative | Acta Psychiatr Scand | Réponses comparées à 17 antidépresseurs dans le trouble dépressif majeur |
| [6805758](https://pubmed.ncbi.nlm.nih.gov/6805758/) | 1982 | Rapport de cas | Br Med J | Agranulocytose induite par la mianserine |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61179297 | MIANSERINE VIATRIS 10 mg, comprimé pelliculé (VIATRIS SANTE) | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions et pharmacologie** : l'interrogation a porté sur 11 entrées, qui sont des cibles pharmacologiques (récepteurs 5-HT, récepteurs α1-adrénergiques, LPA1, NET) et non des interactions médicamenteuses cliniques classées. Elles ne permettent pas d'établir de niveau de risque.
- **Signal de sécurité issu de la littérature** : un rapport de cas d'agranulocytose induite par la mianserine (PMID 6805758) est présent. Une surveillance hématologique est donc à considérer.
- **Population pédiatrique** : aucune donnée de sécurité chez le nourrisson n'est disponible.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le torticolis paroxystique bénin du nourrisson repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, avec un lien mécanistique spéculatif, une population nourrisson sans données de sécurité et une AMM annulée.
- Les indications voisines (dysthymie, mélancolie, dépression névrotique) relèvent plutôt d'une extension de l'indication d'origine que d'un véritable repositionnement ; elles pourraient faire l'objet de questions de recherche (niveau L3-L4), mais avec des preuves indirectes ou anciennes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice (mises en garde, contre-indications) auprès de l'ANSM : ce point est bloquant pour tout dépistage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Vérifier les raisons de l'annulation de l'AMM et le statut de commercialisation actuel.
- Pour le torticolis du nourrisson : établir un lien mécanistique documenté (par exemple avec CACNA1A et la physiopathologie migraineuse) et disposer de données de sécurité pédiatriques avant toute évaluation.
- Pour les indications dépressives voisines : rechercher des essais contrôlés spécifiques à la mianserine, plus récents que les études actuelles.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

