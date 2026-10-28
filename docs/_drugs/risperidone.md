---
layout: default
title: Risperidone
parent: Prédiction du modèle uniquement (L5)
nav_order: 673
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "risperidone"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder"]
description: "Risperidone : nouvelle indication prédite, Paralysie familiale du regard horizontal avec scoliose progressive (gaze palsy, familial horizontal… (niveau de preuve L5). Indication d'origine : Non rense…"
---

# Risperidone
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

## Risperidone: Paralysie familiale du regard horizontal avec scoliose progressive (gaze palsy, familial horizontal, with progressive scoliosis)
{: .text-alpha }

## Résumé en Une Phrase

La rispéridone est un antipsychotique atypique, initialement utilisé pour la schizophrénie, les troubles bipolaires (manie) et les troubles du spectre autistique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **paralysie familiale du regard horizontal avec scoliose progressive**, une maladie génétique rare.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction, qui repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Paralysie familiale du regard horizontal avec scoliose progressive (gaze palsy, familial horizontal, with progressive scoliosis) |
| Score de Prédiction TxGNN | 0.9976 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, la rispéridone est un antagoniste des récepteurs dopaminergiques D2 et sérotoninergiques 5-HT2A. Son efficacité est établie dans la schizophrénie et la manie bipolaire.

Pour cette nouvelle indication, **aucun lien mécanistique identifiable n'existe**. La paralysie familiale du regard horizontal avec scoliose progressive est une maladie génétique rare, liée au gène ROBO3, qui touche le guidage des axones dans le tronc cérébral. L'antagonisme D2/5-HT2A de la rispéridone n'a aucune pertinence connue pour cette pathologie.

Le score élevé de TxGNN (0,9976) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Il ne constitue pas une preuve d'efficacité et doit être considéré avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Autres Indications Prédites par le Modèle

Les données compilées contiennent d'autres indications prédites, mieux documentées que la première. Elles sont résumées ici à titre d'information.

| Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|
| Syndrome amélo-cérébro-hypohidrotique | 0,9969 | L5 | Aucun lien mécanistique crédible, aucune preuve |
| Syndrome de Phelan-McDermid | 0,9959 | L4 | Une revue clinique et une étude préclinique sur le poisson-zèbre (shank3) ; aucun essai chez l'humain ; bénéfice éventuel uniquement symptomatique (irritabilité, agressivité) |
| Trichotillomanie | 0,9951 | L4 | Plusieurs cas cliniques et petites séries (potentialisation des inhibiteurs de recapture de la sérotonine) ; aucun essai contrôlé |
| Trouble affectif majeur | 0,9911 | L1 | Deux essais de Phase 3 terminés sur la rispéridone en appoint dans la dépression résistante : [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) (630 patients) et [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) (258 patients), ainsi que plusieurs méta-analyses ; décision *Proceed with Guardrails* |

Pour le trouble affectif majeur, le bénéfice se limite à la dépression résistante, en appoint d'un antidépresseur. Il s'accompagne de risques métaboliques, extrapyramidaux, de somnolence et d'hyperprolactinémie. Les essais portant sur le trouble bipolaire chevauchent l'indication existante et ne constituent pas une nouvelle preuve de repositionnement.

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Les textes d'indication approuvée ne sont pas renseignés. Voici cinq d'entre elles :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60605064 | RISPERIDONE VIATRIS 1 mg | Comprimé orodispersible |
| 66315751 | RISPERIDONE VIATRIS 2 mg | Comprimé pelliculé sécable |
| 63436769 | RISPERIDONE TEVA SANTE 1 mg/ml | Solution buvable |
| 65893318 | RISPERDALCONSTA L.P. 50 mg/2 ml | Poudre et solvant pour suspension injectable à libération prolongée |
| 60260497 | RISPERDAL 2 mg | Comprimé pelliculé |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (elles ne proviennent pas du texte de la notice) : hypotension orthostatique et atrophie multisystématisée, insuffisance et maladies hépatiques, épilepsie, diabète, hyperglycémie et acidocétose diabétique, neutropénie et agranulocytose, hyperlipidémie, obésité, accident vasculaire cérébral et maladies cérébrovasculaires, infarctus du myocarde, arrêt cardiaque soudain, troubles de la conduction cardiaque et maladies cardiovasculaires, maladies de la vésicule biliaire, carcinome mammaire chez la femme, hémoglobinopathies.
- **Interactions médicamenteuses** : 362 interactions sont recensées. Parmi les exemples rapportés, deux sont de niveau majeur : le **bupropion** et la **morphine**. Plusieurs sont de niveau modéré, notamment la metformine, l'acarbose, l'épinéphrine, l'hydrocortisone, l'atropine, le glycopyrronium et l'amphotéricine B.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la paralysie familiale du regard horizontal avec scoliose progressive repose uniquement sur le score du modèle (L5). Elle n'est soutenue par aucun essai, aucune publication ni aucun mécanisme plausible.
- Le médicament est commercialisé, avec 20 AMM valides.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM.
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank).
- Si une réévaluation est souhaitée, privilégier le trouble affectif majeur (dépression résistante, en appoint), le mieux documenté, en vérifiant la disponibilité des formulations et en analysant les 362 interactions médicamenteuses.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

