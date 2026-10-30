---
layout: default
title: Lorazepam
parent: Prédiction du modèle uniquement (L5)
nav_order: 464
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "lorazepam"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Lorazepam : nouvelle indication prédite, Tumeur du nerf trijumeau (trigeminal nerve neoplasm) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Lorazepam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Lorazepam: Tumeur du nerf trijumeau (trigeminal nerve neoplasm)
{: .text-alpha }

## Résumé en une phrase

Le lorazépam est une benzodiazépine, initialement utilisée dans l'anxiété, l'état de mal épileptique et plusieurs formes d'épilepsie.
Le modèle TxGNN (apprentissage profond) prédit en rang 1 qu'il pourrait être efficace pour la **tumeur du nerf trijumeau**, mais **aucun essai clinique ni publication** ne soutient cette prédiction, qui reflète très probablement des similarités apprises par le modèle entre maladies voisines, et non une preuve biologique.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Tumeur du nerf trijumeau (trigeminal nerve neoplasm) |
| Score de prédiction TxGNN | 0.9987 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le lorazépam est un modulateur allostérique positif des récepteurs GABA-A : il renforce l'inhibition neuronale, d'où ses effets anxiolytique, sédatif, hypnotique et anticonvulsivant.

Pour la tumeur du nerf trijumeau, **aucun lien mécanistique plausible** n'apparaît entre cette modulation et le contrôle tumoral. Un éventuel usage ne pourrait être que symptomatique (anxiété, nausées), et non modificateur de la maladie. Le score très élevé (0,9987) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies voisines, et non une preuve biologique ou clinique.

À titre de comparaison, d'autres prédictions sont mieux étayées sur le plan mécanistique :
- **Insomnie** : l'effet sédatif-hypnotique du lorazépam est cohérent avec cette indication, et des études cliniques anciennes existent.
- **Crises réflexes** (lecture, sursaut, etc.) : la potentialisation GABAergique est plausible, dans la continuité des indications épileptiques d'origine.

---

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la tumeur du nerf trijumeau (ni pour les autres indications prédites dans les données compilées).

---

## Preuves de la littérature

Aucune littérature associée n'est disponible actuellement pour la tumeur du nerf trijumeau.


| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Étude clinique | Int Clin Psychopharmacol | Lorazépam 0,5 mg 3 fois/jour (traitement sur 24 h) comparé à 1,5 mg au coucher dans l'insomnie chronique primaire |
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | Étude comparative croisée en double aveugle | J Clin Pharmacol | Lorazépam 2 mg plus performant que le flurazépam 30 mg sur la plupart des paramètres du sommeil chez 8 insomniaques chroniques |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revue | Med Lett Drugs Ther | Revue des médicaments de l'insomnie chronique |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Revue | J Multidiscip Healthc | Efficacité, sécurité et interactions des traitements de l'insomnie chez les patients COVID-19 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revue (pharmacocinétique) | Expert Opin Drug Metab Toxicol | Pharmacocinétique des anxiolytiques |

Les autres publications retrouvées pour l'insomnie sont indirectes (prescriptions, autres médicaments, modèle murin avec probiotique).

---

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 67917629 | TEMESTA 1 mg, comprimé sécable (active) | Comprimé sécable | Non renseignée |
| 62505828 | LORAZEPAM VIATRIS 1 mg (active) | Comprimé pelliculé sécable | Non renseignée |
| 67177709 | TEMESTA 2,5 mg, comprimé sécable (active) | Comprimé sécable | Non renseignée |
| 66720276 | LORAZEPAM XILMAC 4 mg/mL (active) | Solution injectable | Non renseignée |
| 63159891 | LORAZEPAM VIATRIS 2,5 mg (active) | Comprimé pelliculé sécable | Non renseignée |

Les 5 AMM sur 5 sont valides : le médicament est commercialisé.

---

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie hépatique, encéphalopathie hépatique et coma hépatique, insuffisance respiratoire, syndrome d'apnée du sommeil (dont obstructif), syndrome d'hypoventilation centrale congénitale, glaucome à angle fermé et à angle ouvert, porphyries, maladie rénale, maladie de la vésicule biliaire, troubles liés à l'usage de substances (abus/dépendance).
- **Interactions médicamenteuses** : 265 interactions recensées. Parmi les principales, deux de niveau **majeur** : la morphine et la morphine liposomale (risque de dépression respiratoire et de sédation excessive). Des interactions de niveau modéré concernent notamment le bupropion, le dronabinol, le nabilone, le tédaglutide, le métoclopramide, l'opium et la sibutramine. Plusieurs antiacides (hydroxyde d'aluminium, carbonate de calcium, magaldrate, composés du magnésium) présentent des interactions mineures.
- **Signaux issus de la littérature** : risques de dépendance, de tolérance et d'altération des fonctions le lendemain (usage prolongé dans l'insomnie) ; toxicité du propylène glycol signalée avec les formulations parentérales.

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Pour la tumeur du nerf trijumeau, la prédiction repose uniquement sur le modèle (L5), sans essai, sans publication et sans lien mécanistique crédible. Le statut de marché (AMM toutes annulées) complique en outre toute voie de repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications), une lacune bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Clarifier la situation réglementaire (AMM annulées, raisons et possibilités de réactivation)
- Pour l'insomnie : évaluer le rapport bénéfice/risque (dépendance, interactions) par rapport aux alternatives actuelles, et rechercher des essais récents
- Pour la tumeur du nerf trijumeau : ne pas poursuivre, sauf apparition d'une justification biologique indépendante
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

