---
layout: default
title: Letrozole
parent: Preuves élevées (L1-L2)
nav_order: 446
evidence_level: L1
indication_count: 10
---

# Letrozole
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Létrozole : Du cancer du sein hormonodépendant au carcinome mammaire féminin

## Résumé en une phrase

Le létrozole est un inhibiteur non stéroïdien de l'aromatase, utilisé dans le traitement du cancer du sein hormonodépendant chez la femme ménopausée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome mammaire féminin**, avec **41 essais cliniques** et **20 publications** rattachés à cette prédiction dans les données compilées pour ce rapport. Il s'agit toutefois d'une indication déjà établie : la prédiction valide l'usage existant plutôt qu'elle n'ouvre une nouvelle voie thérapeutique.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données d'AMM (texte d'indication vide) |
| Nouvelle indication prédite | Carcinome mammaire féminin |
| Score de prédiction TxGNN | 99,98 % |
| Niveau de preuve | L1 |
| Statut de marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 |
| Décision recommandée | Proceed with Guardrails |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. D'après la littérature compilée, le létrozole est un inhibiteur non stéroïdien de l'aromatase : il bloque la conversion des androgènes en œstrogènes, ce qui abaisse les œstrogènes circulants chez la femme ménopausée et prive les tumeurs hormonodépendantes de leur signal de croissance.

Le cancer du sein à récepteurs hormonaux positifs dépend de ce signal œstrogénique. La prédiction du modèle est donc cohérente avec le mécanisme connu. Le létrozole est un traitement de référence dans les contextes adjuvant, néoadjuvant et métastatique, y compris en association aux inhibiteurs de CDK4/6 (palbociclib, ribociclib, abémaciclib).

Le champ d'indication d'origine est vide dans la base d'AMM, et le statut « annulé » concerne uniquement ces enregistrements. Il s'agit de lacunes de données, non d'un argument contre l'usage.

---

## Preuves d'essais cliniques

Parmi les essais les plus pertinents (classés A/B par l'analyse de pertinence) :

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3 | Terminé | 3246 | COMPLEEMENT-1 : ribociclib + létrozole dans le cancer du sein avancé HR+/HER2-, sans hormonothérapie préalable |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Terminé | 131 | Palbociclib + létrozole chez des femmes ménopausées HR+/HER2- |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Terminé | 666 | PALOMA-2 : palbociclib + létrozole versus placebo + létrozole en première ligne |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | Actif, ne recrute plus | 1050 | SONIA : séquence inhibiteur de l'aromatase + CDK4/6 en première ou deuxième ligne |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Phase 3 | Inconnu | 3966 | Létrozole 5 ans versus placebo après 5 ans d'hormonothérapie, en traitement adjuvant prolongé |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | Arrêté | 123 | Létrozole préopératoire de 4 mois versus chirurgie première (essai DBCG) ; preuve limitée par l'arrêt précoce |
| [NCT00433589](https://clinicaltrials.gov/study/NCT00433589) | Phase 3 | Terminé | 6600 | MINDACT : signature à 70 gènes pour guider la chimiothérapie ; le létrozole fait partie des traitements hormonaux |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | Actif, ne recrute plus | 84 | Hormonothérapie préopératoire chez les femmes âgées pour éclairer la décision de radiothérapie |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | Terminé | 108 | Létrozole néoadjuvant dans le carcinome canalaire in situ (CCIS) RE+ |
| [NCT02712723](https://clinicaltrials.gov/study/NCT02712723) | Phase 2 | Actif, ne recrute plus | 121 | FELINE : létrozole + ribociclib ou placebo en traitement néoadjuvant |

Dans la plupart de ces essais, le létrozole est le socle hormonal d'une association : sa contribution propre est donc indirecte.

---

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | ECR | Ann Oncol | MONALEESA-2 : résultats actualisés de ribociclib + létrozole en première ligne, HR+/HER2- |
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | ECR | N Engl J Med | Survie globale améliorée avec ribociclib + létrozole dans le cancer du sein avancé |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | ECR | Breast Cancer Res Treat | PALOMA-2 : palbociclib + létrozole, suivi prolongé |
| [31513453](https://pubmed.ncbi.nlm.nih.gov/31513453/) | 2019 | Cohorte | Future Oncol | NEOLETEXE : absence de résistance croisée entre létrozole et exémestane en néoadjuvant |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Revue | Life Sci | Pharmacologie, toxicité et effets thérapeutiques potentiels du létrozole |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Revue | Expert Opin Drug Metab Toxicol | Aspects pharmacodynamiques, pharmacocinétiques, efficacité et sécurité du létrozole |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Non classé | Breast Cancer Res Treat | Découverte et mécanisme d'action du létrozole |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | Non classé | Comput Math Methods Med | Tamoxifène suivi du létrozole versus létrozole seul |
| [34096894](https://pubmed.ncbi.nlm.nih.gov/34096894/) | 2021 | Cohorte | Pharmacogenet Genomics | Étude d'association pangénomique des concentrations plasmatiques de létrozole et du métabolisme par CYP2A6 |
| [17544670](https://pubmed.ncbi.nlm.nih.gov/17544670/) | 2007 | Non classé | Breast | Prescription du létrozole adjuvant prolongé (essai MA-17) |

---

## Informations de marché en France

Les 20 AMM recensées sont toutes au statut « annulé », sans texte d'indication renseigné. Cinq d'entre elles, à titre d'illustration :

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 64492112 | FEMARA 2,5 mg, comprimé pelliculé (Novartis Pharma) | Comprimé pelliculé | Non renseignée |
| 64722435 | FEMARA 2,5 mg, comprimé pelliculé (BB Farma) | Comprimé pelliculé | Non renseignée |
| 69489312 | LETROZOLE ACCORD HEALTHCARE 2,5 mg | Comprimé pelliculé | Non renseignée |
| 66935695 | LETROZOLE BIOGARAN 2,5 mg | Comprimé pelliculé | Non renseignée |
| 65224722 | LETROZOLE SANDOZ 2,5 mg | Comprimé pelliculé | Non renseignée |

---

## Cytotoxicité

Le létrozole est un traitement hormonal antinéoplasique.

| Élément | Contenu |
|------|------|
| Classification de cytotoxicité | Hormonothérapie (inhibiteur non stéroïdien de l'aromatase) ; non cytotoxique conventionnel |
| Risque de myélosuppression | Faible (aucune donnée de toxicité hématologique dans les données compilées) |
| Classification d'émétogénicité | Faible |
| Éléments de surveillance | Densité osseuse, bilan lipidique, fonction hépatique ; NFS selon le contexte clinique |
| Protection de manipulation | Les mesures spécifiques de manipulation des cytotoxiques ne sont pas documentées dans les données compilées ; veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de notice) : insuffisance hépatique, cirrhose, ostéoporose (y compris post-ménopausique), hyperbilirubinémie (y compris héréditaire), syndrome de Gilbert, maladie cérébrovasculaire.
- **Interactions médicamenteuses** : 259 interactions recensées. Une est de niveau modéré (aprépitant) ; les autres sont de niveau non précisé, par exemple le calcitriol, le glimépiride, la metformine, la simvastatine, la prednisone, l'oméprazole ou la morphine.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

---

## Conclusion et prochaines étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés et des ECR publiés (MONALEESA-2, PALOMA-2) soutiennent l'usage du létrozole dans le cancer du sein HR+, ce qui correspond au niveau L1.
- L'indication est déjà établie ; les principaux points de vigilance sont la sélection des patientes (récepteurs hormonaux positifs) et le profil de sécurité (os, foie), ainsi que l'absence de notice et de statut de marché actif dans les données françaises.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice ANSM (mises en garde, contre-indications, indication approuvée) : lacune bloquante pour le dépistage de sécurité.
- Obtenir les données détaillées de mécanisme d'action depuis DrugBank.
- Vérifier le statut réglementaire réel : les 20 AMM annulées peuvent refléter des lacunes de base de données ou des transferts de produit.
- Définir un plan de surveillance de la sécurité (densité osseuse, fonction hépatique) pour les populations à risque.

**Autres indications prédites (à titre d'information) :**
- **Cancer du sein à récepteurs œstrogéniques positifs** : même niveau L1, validé et non repositionné ; Proceed with Guardrails.
- **Cancer du sein bilatéral** (L2) : Proceed with Guardrails ; les preuves directes sont surtout des cas cliniques.
- **Cancer du sein hormonorésistant** (L2) et **cancer du sein défini par profil d'expression génique** (L2) : Research Question ; l'apport propre du létrozole n'est pas isolable.
- **Cancer du mamelon, tumeur d'Ehrlich, dysplasie mammaire bénigne, maladie fibrokystique du sein** : Hold ; preuves limitées à des cas cliniques, du préclinique chez la souris, ou absentes.
- **Cancer du sein à récepteurs œstrogéniques négatifs** : Hold ; une efficacité est mécanistiquement improbable, et les essais retrouvés concernent des tumeurs RE+, associés par chevauchement d'ontologie.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

