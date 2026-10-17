---
layout: default
title: Ceftriaxone
parent: Prédiction du modèle uniquement (L5)
nav_order: 150
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Ceftriaxone : nouvelle indication prédite, Syndrome d'hyperviscosité polyclonale (niveau de preuve L5). Indication d'origine : Infections bactériennes (streptococciques, pneumonie bactérienne…"
monitor_inn: "ceftriaxone"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
---

# Ceftriaxone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Ceftriaxone : Des Infections Bactériennes à l'Otite Moyenne Infectieuse

## Résumé en Une Phrase

Ceftriaxone est un antibiotique de la famille des céphalosporines, utilisé à l'origine pour traiter diverses infections bactériennes (pneumonie, méningite, gonorrhée, salmonellose, arthrite bactérienne, etc.).
Le modèle TxGNN prédit en premier lieu le **syndrome d'hyperviscosité polyclonale**, mais cette prédiction n'est étayée par aucune preuve. La piste la mieux documentée parmi les prédictions est l'**otite moyenne infectieuse**, soutenue par **1 essai clinique** (qui ne teste pas le ceftriaxone) et **18 publications** (dont un essai randomisé de 1997).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (streptococciques, pneumonie bactérienne, méningites, gonorrhée, salmonellose, arthrite bactérienne, etc.) ; le texte d'indication des AMM n'est pas renseigné |
| Nouvelle Indication Prédite (rang 1 du modèle) | Syndrome d'hyperviscosité polyclonale |
| Score de Prédiction TxGNN | 99,39 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (20 annulées) |
| Décision Recommandée | Hold |

Pour information, la prédiction la mieux étayée est l'otite moyenne infectieuse (rang 4, score 99,26 %, niveau de preuve L3, statut « question de recherche »). Elle est détaillée plus bas.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, le ceftriaxone est une céphalosporine qui inhibe la synthèse de la paroi bactérienne en se liant aux protéines de liaison à la pénicilline (PBP). Son efficacité est établie dans de nombreuses infections bactériennes.

**Pour la prédiction de rang 1 (syndrome d'hyperviscosité polyclonale)**, aucun lien mécanistique plausible n'a été identifié. Cette affection hématologique/immunologique est liée à un excès d'immunoglobulines, et le mécanisme antibactérien du ceftriaxone ne la traite pas. Le score élevé provient uniquement du graphe de connaissances, sans essai ni publication à l'appui. Les prédictions « hyperamylasémie », « analbuminémie congénitale » et « incompatibilité de groupe sanguin » présentent la même absence de lien thérapeutique : ce sont des anomalies biologiques ou des maladies génétiques/immunohématologiques sans cible antibactérienne.

**Pour l'otite moyenne infectieuse**, la plausibilité biologique est forte : les pathogènes habituels (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*) sont sensibles au ceftriaxone. Il s'agit davantage d'une extension d'un usage antibactérien existant (injection intramusculaire unique) que d'un véritable repositionnement mécanistique. Les otites suppurées sont moins bien couvertes (activité limitée sur *Pseudomonas aeruginosa*), et pour l'otite chronique les agents topiques ou antipseudomonas sont généralement plus appropriés.

## Preuves d'Essais Cliniques

Aucun essai clinique n'est enregistré pour la prédiction de rang 1. Pour l'otite moyenne infectieuse, un essai est répertorié :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | Non applicable | Terminé | 250 | Pose de drains transtympaniques versus prise en charge non chirurgicale dans l'otite moyenne aiguë récurrente de l'enfant. Ne teste pas le ceftriaxone ; pertinence contextuelle seulement |

## Preuves de la Littérature

Aucune littérature n'est disponible pour la prédiction de rang 1. Pour l'otite moyenne infectieuse (rang 4), les publications les plus pertinentes sont :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | ECR | Pediatrics | Dose unique de ceftriaxone IM comparée à 10 jours de triméthoprime-sulfaméthoxazole oral dans l'otite moyenne aiguë |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Étude clinique | Pediatr Infect Dis J | Efficacité bactériologique et clinique du ceftriaxone IM sur 1 jour versus 3 jours dans l'otite moyenne aiguë non répondeuse de l'enfant |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Étude clinique | Pediatr Infect Dis J | Efficacité bactériologique d'un schéma de ceftriaxone IM de 3 jours dans l'otite moyenne aiguë non répondeuse |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohorte | Int J Pediatr Otorhinolaryngol | Facteurs associés à l'usage du ceftriaxone dans l'otite moyenne aiguë en soins primaires aux États-Unis |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Recommandations de consensus | Clin Pediatr | Recommandations de prise en charge de l'otite moyenne aiguë |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Revue | Clin Ther | Revue des recommandations de traitement antimicrobien de l'otite moyenne aiguë |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Revue | JAMA Netw Open | Prescription optimale d'antibiotiques en pédiatrie ambulatoire |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Revue | Otol Neurotol | Prévention et traitement de la méningite et de l'otite moyenne aiguë chez les enfants porteurs d'implants cochléaires |

Pour l'otite moyenne suppurée (rang 6), une étude japonaise de 1989 ([2523493](https://pubmed.ncbi.nlm.nih.gov/2523493/)) a comparé le ceftriaxone au céfotiam : efficacité clinique de 71 % contre 86 %. Le reste de la littérature est constitué d'enquêtes microbiologiques et de revues.

Pour l'hyperamylasémie (rang 2), les trois publications retrouvées (syndrome de Weil, saignement intracrânien, prophylaxie après sphinctérotomie endoscopique) ne montrent pas d'effet du ceftriaxone sur l'élévation de l'amylase.

## Informations de Marché en France

Les 20 AMM sont annulées. Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Les cinq premières sont listées :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67389167 | CEFTRIAXONE ZENTIVA 1 g/3,5 ml (IM) | Poudre et solvant pour solution injectable | Non renseignée |
| 61493159 | CEFTRIAXONE VIATRIS 1 g/10 ml (IV) | Poudre et solvant pour solution injectable | Non renseignée |
| 68829580 | CEFTRIAXONE TAMRISA 2 g | Poudre pour solution injectable | Non renseignée |
| 63841034 | CEFTRIAXONE EG 1 g/10 ml (IV) | Poudre et solvant pour solution injectable | Non renseignée |
| 67011139 | CEFTRIAXONE TEVA SANTE 1 g/3,5 mL (IM) | Poudre et solvant pour solution injectable | Non renseignée |

## Considérations de Sécurité

- **Maladies associées à une contre-indication (graphe de connaissances, hors notice)** : maladie du foie, maladie de la vésicule biliaire, ictère néonatal, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, anémie hémolytique.
- **Interactions médicamenteuses** : 164 interactions recensées. Les plus importantes (niveau majeur) concernent les sels de calcium : chlorure de calcium, glucoheptonate de calcium et gluconate de calcium. Des interactions de niveau modéré existent avec la kanamycine, la néomycine, la streptomycine et l'acide picosulfurique.
- **Point d'attention lié à la littérature** : le ceftriaxone est connu pour provoquer une pseudolithiase biliaire, ce qui est pertinent chez le nouveau-né et en cas de maladie biliaire.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction de rang 1 (syndrome d'hyperviscosité polyclonale) n'a aucun lien mécanistique plausible ni aucune preuve clinique ou bibliographique. Aucune des prédictions du haut du classement n'apporte de bénéfice thérapeutique démontré.
- Les seules pistes crédibles (otites moyennes aiguës et suppurées) relèvent de l'usage antibactérien déjà connu, avec des preuves de niveau L3 et sans essai de phase 3 testant le ceftriaxone. Par ailleurs, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité) ;
- Les données sur le mécanisme d'action issues de DrugBank ;
- Si l'otite moyenne est retenue, une revue systématique ou un essai randomisé récent comparant le ceftriaxone aux traitements de référence actuels, compte tenu de la résistance aux antibiotiques ;
- La clarification du statut réglementaire en France (AMM toutes annulées) et la compatibilité des voies d'administration ;
- L'évaluation des interactions (notamment avec le calcium) et des populations à risque (nouveau-nés, atteinte hépatique ou biliaire).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

