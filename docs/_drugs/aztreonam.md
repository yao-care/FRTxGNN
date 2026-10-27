---
layout: default
title: Aztreonam
parent: Prédiction du modèle uniquement (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aztreonam : nouvelle indication prédite, Hyperamylasémie (rang 1) (niveau de preuve L5). Indication d'origine : Infections urinaires et infections à Gram négatif"
monitor_inn: "aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Aztréonam : Des infections à Gram négatif à l'urétrite gonococcique
{: .text-alpha }

## Résumé en Une Phrase

L'aztréonam est un antibiotique de la famille des monobactames, utilisé à l'origine contre les infections à bactéries Gram négatif (infections urinaires, infections à *Pseudomonas aeruginosa*, péritonite, infections à *Escherichia coli*, endométrite).
Le modèle TxGNN prédit en premier rang l'**hyperamylasémie**, mais cette prédiction n'est soutenue par aucune preuve. La piste la mieux étayée parmi les 10 candidates est l'**urétrite gonococcique**, avec **6 publications** (dont un essai ouvert à bras unique de 2020) et **aucun essai clinique** enregistré.

---

## Aperçu Rapide

Le tableau ci-dessous porte sur la prédiction de rang 1 (hyperamylasémie), telle que classée par le modèle. La piste de rang 4 (urétrite gonococcique), la mieux documentée, est détaillée dans les sections suivantes.

| Élément | Contenu |
|------|------|
| Indication Originale | Infections urinaires et infections à Gram négatif (indication issue du graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hyperamylasémie (rang 1) |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

**Autres prédictions examinées :**

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|---|---|---|---|---|
| 2 | Syndrome d'hyperviscosité polyclonale | 99,73 % | L5 | Hold |
| 3 | Analbuminémie congénitale | 99,69 % | L5 | Hold |
| 4 | Urétrite gonococcique | 99,59 % | L3 | Research Question |
| 5 | Urétrite à *Ureaplasma* | 99,59 % | L5 | Hold |
| 6 | Incompatibilité de groupe sanguin | 99,59 % | L5 | Hold |
| 7 | Maladie hématologique prémaligne | 99,54 % | L5 | Hold |
| 8 | Épiglottite | 99,53 % | L4 | Research Question |
| 9 | Gammapathie monoclonale | 99,50 % | L4 | Hold |
| 10 | Pyélonéphrite xanthogranulomateuse | 99,49 % | L5 | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'aztréonam est un monobactame qui inhibe la protéine de liaison à la pénicilline 3 (PBP3) des bactéries Gram négatif aérobies, bloquant ainsi la synthèse de la paroi bactérienne.

**Pour le rang 1 (hyperamylasémie)** et les rangs 2, 3, 6, 7 et 9, aucun lien mécanistique plausible n'existe : l'aztréonam n'a aucun effet connu sur l'amylase, la viscosité sanguine, la synthèse d'albumine ou les processus hématologiques prémalins. Ces scores élevés relèvent très probablement d'artefacts du graphe de connaissances. Pour le rang 5 (*Ureaplasma*), le mécanisme est même défavorable : ces bactéries n'ont pas de paroi cellulaire, et les bêta-lactamines sont donc intrinsèquement inefficaces.

**Les pistes plausibles sont antibactériennes** : l'urétrite gonococcique (rang 4), l'épiglottite (rang 8, due notamment à *Haemophilus influenzae*) et la pyélonéphrite xanthogranulomateuse (rang 10, souvent liée à *Proteus* ou *E. coli*). Elles restent toutefois proches de l'usage antibactérien d'origine : il s'agit moins d'un véritable repositionnement que d'une extension au sein de la même classe d'usage.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature n'existe pour le rang 1. Le tableau ci-dessous présente la littérature de l'urétrite gonococcique (rang 4), la piste la mieux documentée.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Essai clinique ouvert à bras unique | Antimicrob Agents Chemother | Aztréonam 2 g en dose unique intramusculaire chez des hommes atteints de gonorrhée, dans un contexte de menace de résistance à la ceftriaxone |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Étude d'efficacité non contrôlée | Antimicrob Agents Chemother | 1 g IM comparé à la spectinomycine 2 g : aucun échec dans les deux groupes ; satisfaisant pour la gonorrhée urétrale non compliquée chez l'homme |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Étude en dose unique non contrôlée | Genitourin Med | Éradication chez 61 hommes et 26 femmes (sauf un site pharyngé) après 1 g IM ; efficace sur souches sensibles et résistantes à la pénicilline |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Étude épidémiologique et thérapeutique non contrôlée | Hinyokika Kiyo | Étude de l'aztréonam en dose unique dans les infections gonococciques |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Étude in vitro/clinique | J Infect Dis | Efficacité contre les gonocoques résistants à la pénicilline |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Surveillance de la résistance | J Infect Chemother | Émergence de souches de *N. gonorrhoeae* hautement résistantes aux céphèmes et à l'aztréonam, sans bêta-lactamase |

**Autres publications retrouvées (indirectes) :**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Série de cas pédiatrique | Am J Dis Child | Essai ouvert chez 59 enfants avec infections graves à Gram négatif (dont un cas d'épiglottite) : soutien indirect uniquement |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Étude clinique | Jpn J Antibiot | Infections chez 109 patients atteints d'hémopathies : efficacité de 51,1 % ; traite les infections, pas la gammapathie elle-même |
| [34956120](https://pubmed.ncbi.nlm.nih.gov/34956120/) | 2021 | Rapport de microbiologie/génomique | Front Microbiol | Co-occurrence de bla NDM-1 et mcr-9 chez *K. pneumoniae* ; sans rapport avec l'incompatibilité de groupe sanguin (probable artefact de mots-clés) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61054849 | CAYSTON 75 mg (Gilead Sciences Ireland UC) | Poudre et solvant pour solution pour inhalation par nébuliseur | Non renseignée (AMM annulée) |
| 63918096 | AZACTAM 1 g (Laboratoires Delbert) | Poudre pour solution injectable pour perfusion | Non renseignée (AMM annulée) |
| 68544663 | EMBLAVEO 1,5 g/0,5 g (Pfizer Europe MA EEIG) | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pyourètre, maladie hépatique, maladie de la vésicule biliaire, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, maladie bronchique.
- **Interactions médicamenteuses** : 27 interactions recensées. Les plus notables sont de niveau **modéré** : acide picosulfurique, dicoumarol et warfarine (surveillance de la coagulation à envisager). Les autres (par ex. vancomycine, amikacine, amphotéricine B, tacrolimus, héparine, oméprazole, pantoprazole, morphine) ont un niveau de gravité non précisé.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être obtenues : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction de rang 1 (hyperamylasémie) repose uniquement sur le score du modèle, sans essai, sans publication ni lien mécanistique plausible (niveau L5). Les AMM françaises sont toutes annulées.
- Seule l'urétrite gonococcique (L3, « Research Question ») présente un début de soutien, mais sans essai randomisé, avec des signalements de résistance, des traitements de référence établis, et une proximité avec l'usage antibactérien d'origine. Aucune indication ne justifie un passage à l'étape suivante pour l'instant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Pour l'urétrite gonococcique : essai comparatif randomisé, données de sensibilité actuelles de *N. gonorrhoeae* et évaluation de la voie d'administration (dose unique intramusculaire) par rapport aux formes autrefois autorisées
- Clarification du statut réglementaire (toutes les AMM étant annulées) et de la disponibilité réelle du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

