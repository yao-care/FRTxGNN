---
layout: default
title: Cefuroxime
parent: Prédiction du modèle uniquement (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefuroxime : nouvelle indication prédite, Infection urinaire (rang 6 (niveau de preuve L5). Indication d'origine : Infections bactériennes (otite moyenne infectieuse…"
---

# Cefuroxime
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

# Céfuroxime : Des infections bactériennes à l'infection urinaire (prédiction TxGNN)

## Résumé en Une Phrase

La céfuroxime est une céphalosporine de deuxième génération, utilisée à l'origine contre diverses infections bactériennes (otite moyenne, pneumonie, méningite, gonorrhée, maladie de Lyme, etc.).
Le modèle TxGNN a placé en tête de liste l'**hyperamylasémie**, mais cette prédiction ne repose sur aucune preuve : c'est l'**infection urinaire**, première indication prédite appuyée par des données, qui est analysée en détail ci-dessous (**5 essais cliniques** et **20 publications**, sans essai de phase 3 démontrant l'efficacité de la céfuroxime).

> **Remarque importante :** la prédiction de rang 1 (hyperamylasémie, score 99,76 %) n'est soutenue par aucun essai ni aucune publication, et aucun lien mécanistique plausible n'a été identifié. Pour que le rapport soit exploitable, l'analyse porte sur l'infection urinaire (rang 6), la première indication prédite qui dispose de preuves. Cette indication relève davantage d'une extension de l'usage antibactérien existant que d'un véritable repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (otite moyenne infectieuse, pneumonie bactérienne, méningite bactérienne, gonorrhée, maladie de Lyme, etc.) |
| Nouvelle Indication Prédite | Infection urinaire (rang 6 ; rang 1 : hyperamylasémie, sans preuve) |
| Score de Prédiction TxGNN | 99,62 % (infection urinaire) ; 99,76 % (hyperamylasémie) |
| Niveau de Preuve | L3 (infection urinaire) ; L5 (hyperamylasémie) |
| Statut de Marché en France | Retirée du marché (AMM toutes annulées) |
| Nombre d'AMM | 20 (0 valide, 20 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, la céfuroxime est une céphalosporine de deuxième génération, bactéricide, qui inhibe la synthèse de la paroi bactérienne. Son efficacité est reconnue dans les infections respiratoires, ORL et d'autres infections bactériennes.

Pour l'**infection urinaire**, le lien mécanistique est solide : la céfuroxime est active sur de nombreuses entérobactéries responsables d'infections urinaires et a été utilisée en clinique pour la pyélonéphrite. Il s'agit donc d'une confirmation ou d'une extension de l'usage antibactérien existant, et non d'un repositionnement au sens strict.

Pour la **prédiction de rang 1 (hyperamylasémie)** et la plupart des autres prédictions de tête (syndrome d'hyperviscosité polyclonale, analbuminémie congénitale, maladies hématologiques prémalignes, etc.), aucun lien plausible n'a été identifié. Il s'agit de sorties du graphe de connaissances sans fondement pharmacologique ni clinique. Deux autres prédictions (otite moyenne suppurée, infection à *Peptostreptococcus*) sont mécanistiquement plausibles mais reposent sur des preuves indirectes ; la première recoupe d'ailleurs l'indication d'origine.

## Preuves d'Essais Cliniques

(Infection urinaire)

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A (non interventionnel) | Terminé | 973 | Effet d'un traitement inapproprié par céfuroxime chez des adultes hospitalisés pour pyélonéphrite ; pertinence élevée (grade A) |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Terminé | 220 | Antibiothérapie préventive en post-partum chez des femmes enceintes avec infections urinaires récidivantes ; schéma non spécifique à la céfuroxime |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Inconnu | 1000 | Antibioprophylaxie lors du retrait de sonde urinaire ; antibiotique non confirmé comme étant la céfuroxime |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Phase 1 précoce | Inconnu | 150 | Prévention de l'infection urinaire par antibiotiques une semaine avant lithotritie mini-invasive ; rôle de la céfuroxime peu clair |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Retiré | 0 | Prophylaxie des infections post-césarienne ; aucun patient inclus, donc aucune preuve |

## Preuves de la Littérature

(Infection urinaire ; sélection des publications les plus pertinentes)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | ECR | Infection | Comparaison randomisée aztréonam vs céfuroxime dans les infections urinaires hautes à Gram négatif |
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Revue systématique | Pharmacotherapy | β-lactamines orales dans les infections urinaires compliquées, comparées au TMP/SMX et aux fluoroquinolones |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | ECR | Lancet Infect Dis | Désescalade à partir des β-lactamines antipseudomonas dans les bactériémies à entérobactéries (non spécifique à la céfuroxime) |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Revue | Drugs | Activité antibactérienne, pharmacocinétique et efficacité thérapeutique de la céfuroxime axétil |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Revue | Int J Antimicrob Agents | Céfuroxime axétil : sensibilité des principaux pathogènes respiratoires |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Revue | Ther Drug Monit | Activité antimicrobienne, pharmacologie et efficacité clinique de la céfuroxime |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Revue | Pharmacotherapy | Mécanisme d'action, pharmacocinétique, effets indésirables et indications de la céfuroxime |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Cohorte/microbiologie | Infect Dis Clin Microbiol | Micro-organismes des infections urinaires communautaires et facteurs de risque de BLSE |

Les autres publications retrouvées sont surtout des études de sensibilité ou de résistance (infections urinaires de l'enfant, entérocoques, etc.) ou portent sur d'autres antibiotiques, sans valeur démonstrative pour la céfuroxime.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63992335 | CEFUROXIME ZENTIVA 250 mg | Comprimé pelliculé | Non renseignée |
| 61068069 | ZINNAT 125 mg/5 ml enfants et nourrissons | Granulés pour suspension buvable | Non renseignée |
| 64731103 | CEFUROXIME SANDOZ 500 mg | Comprimé enrobé | Non renseignée |
| 67104586 | CEFUROXIME VIATRIS 250 mg | Comprimé enrobé | Non renseignée |
| 64292072 | ZINNAT 1,5 g | Poudre pour solution pour perfusion | Non renseignée |

Les 20 AMM recensées sont toutes annulées ; aucune n'est actuellement valide.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pyourètre, maladie hépatique, maladie de la vésicule biliaire, troubles de la coagulation, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, déficit congénital en prothrombine.
- **Interactions médicamenteuses** : 143 interactions recensées. Les 20 premières sont de niveau modéré et concernent surtout :
  - les antiacides et les médicaments réduisant l'acidité gastrique (famotidine, ranitidine, cimétidine, nizatidine, oméprazole, ésoméprazole, lansoprazole, dexlansoprazole, pantoprazole, rabéprazole, hydroxyde d'aluminium, carbonate de calcium, sels de magnésium, magaldrate) ;
  - les aminosides (kanamycine, néomycine) ;
  - le balsalazide.

Les mises en garde et contre-indications issues de la notice officielle ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction de rang 1 (hyperamylasémie) et la plupart des prédictions de tête n'ont aucun support clinique ni mécanistique (niveau L5). L'infection urinaire (L3) est mécanistiquement cohérente mais relève d'une extension de l'usage antibactérien existant, sans essai de phase 3 spécifique à la céfuroxime ; de plus, toutes les AMM françaises sont annulées, ce qui limite tout développement pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le passage à l'étape de criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Vérifier la pertinence réelle de l'indication infection urinaire par rapport aux indications déjà approuvées et à la disponibilité de produits commercialisés.
- Si l'infection urinaire est retenue, rechercher des essais comparatifs spécifiques à la céfuroxime et examiner les profils de résistance actuels.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

