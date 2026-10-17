---
layout: default
title: Colchicine
parent: Prédiction du modèle uniquement (L5)
nav_order: 196
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Colchicine : nouvelle indication prédite, Paludisme à Plasmodium falciparum (niveau de preuve L5). Indication d'origine : Goutte"
monitor_inn: "COLCHICINE"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Colchicine : De la Goutte et de la Fièvre Méditerranéenne Familiale au Paludisme à *Plasmodium falciparum*

## Résumé en Une Phrase

La colchicine est un médicament anti-inflammatoire utilisé à l'origine dans le traitement de la goutte et de la fièvre méditerranéenne familiale.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **paludisme à *Plasmodium falciparum***, mais **aucun essai clinique** ne soutient cette direction et seules **2 publications** indirectes (études précliniques) ont été identifiées.
Il s'agit donc d'une prédiction purement computationnelle, à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Goutte ; fièvre méditerranéenne familiale (le texte d'indication des AMM françaises n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Paludisme à *Plasmodium falciparum* |
| Score de Prédiction TxGNN | 99,60 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (aucune en cours de validité) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, la colchicine se lie à la tubuline et perturbe la polymérisation des microtubules. Son efficacité dans la goutte et la fièvre méditerranéenne familiale repose sur cet effet : réduction de la chimiotaxie des neutrophiles et de l'activation de l'inflammasome, avec diminution de l'inflammation dépendante de l'IL-1β.

*Plasmodium falciparum* dépend des microtubules pour la formation du fuseau mitotique et la division cellulaire. Un médicament ciblant la tubuline est donc biologiquement plausible. Toutefois, le lien avec l'indication originale (maladies inflammatoires) est indirect : il s'agit d'une hypothèse de mécanisme, et non d'une similarité entre maladies.

Cette plausibilité reste fragile. Les deux publications identifiées ne portent pas sur l'efficacité antipaludique de la colchicine : l'une concerne la curcumine et les microtubules du parasite, l'autre l'expression du gène pfmdr1 et la sensibilité à la chloroquine. De plus, l'indice thérapeutique étroit de la colchicine et sa toxicité pour l'hôte (digestive, myélosuppression) aux concentrations antiparasitaires sont des obstacles majeurs. Le score élevé de TxGNN est une prédiction informatique uniquement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro / préclinique | PloS one | La curcumine (et non la colchicine) perturbe les microtubules de *P. falciparum* ; appui indirect à l'idée d'une cible tubuline |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / préclinique | Molecular and cellular biology | L'expression de pfmdr1 dans des cellules de mammifère augmente la sensibilité à la chloroquine ; sans lien direct avec la colchicine |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68066715 | COLCHICINE OPOCALCIUM 1 mg, comprimé sécable (annulée) | Comprimé sécable | Non renseignée |
| 61331730 | COLCHIMAX, comprimé pelliculé sécable (annulée) | Comprimé pelliculé sécable | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, insuffisance rénale, maladies hématologiques (thrombocytopénie, leucopénie, agranulocytose, neutropénie sous toutes ses formes, anémie aplasique), ulcère gastro-duodénal, maladies diarrhéiques, myopathie et maladies musculaires, rhabdomyolyse, paralysie périodique familiale, néphropathie aiguë urique.
- **Interactions médicamenteuses** (100 interactions recensées ; principales ci-dessous) :
  - *Majeures* : aprépitant, clarithromycine, éliglustat, rolapitant, rosuvastatine, simvastatine, cobicistat, déférifrone.
  - *Modérées* : métronidazole, cimétidine, éluxadoline, miconazole, tinidazole, déférasirox, ticagrélor, chloroquine, benznidazole, disulfirame, fostamatinib, chlorure de strontium Sr-89.

Il est à noter que la chloroquine, antipaludique de référence, présente une interaction modérée avec la colchicine, ce qui est pertinent pour toute association envisagée dans le paludisme.

Pour les mises en garde officielles, veuillez consulter la notice, car les données de la notice ne sont pas disponibles dans les informations compilées.

---

## Autres Prédictions Examinées

- **Fièvre méditerranéenne familiale, forme autosomique dominante** (score 99,38 % ; niveau L4) : la colchicine est déjà le traitement de première intention de la fièvre méditerranéenne familiale, qui est une indication d'origine. Il s'agit d'une variante d'une indication existante, donc d'une question de classification des indications et non d'un véritable repositionnement. Les 20 publications identifiées sont essentiellement des revues narratives, sans essai clinique ni données contrôlées spécifiques à ce sous-type.
- **Dermatofibrosarcome protubérant** (score 99,37 % ; niveau L5 ; Hold) : aucune donnée clinique ni bibliographique. L'hypothèse antimitotique est spéculative, la maladie étant pilotée par la fusion COL1A1-PDGFB et traitée par chirurgie et imatinib. La toxicité de la colchicine limite son usage comme antinéoplasique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le paludisme repose uniquement sur le modèle (L5), sans essai clinique et avec deux études précliniques indirectes. L'indice thérapeutique étroit de la colchicine et l'absence d'AMM en vigueur en France renforcent la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Mises en garde et contre-indications officielles issues de la notice ANSM (données bloquantes pour le criblage de sécurité)
- Études in vitro et précliniques directes de la colchicine sur *P. falciparum*, avec marge de sécurité entre concentrations antiparasitaires et toxicité chez l'hôte
- Évaluation des interactions avec les antipaludiques, notamment la chloroquine
- Clarification du statut réglementaire (AMM annulées) et de la voie d'administration requise
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

