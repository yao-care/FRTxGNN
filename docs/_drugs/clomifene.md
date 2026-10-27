---
layout: default
title: Clomifene
parent: Preuves élevées (L1-L2)
nav_order: 185
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomifene : nouvelle indication prédite, Anovulation (niveau de preuve L1). Indication d'origine : Infertilité féminine"
monitor_inn: "clomifene"
predicted_indications: ["46,XY disorder of sex development due to testicular steroidogenesis defect", "transverse vaginal septum", "longitudinal vaginal septum", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "anovulation"]
---

# Clomifene
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

## Clomifène : De l'infertilité féminine à l'anovulation
{: .text-alpha }

## Résumé en Une Phrase

Le clomifène (CLOMID 50 mg, comprimé) est un modulateur sélectif des récepteurs aux estrogènes, initialement utilisé pour le traitement de l'infertilité féminine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**anovulation**, avec **3 essais cliniques** et **20 publications** associés. Il s'agit toutefois d'une indication très proche de l'indication d'origine, donc davantage d'un usage déjà établi que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infertilité féminine (selon le graphe de connaissances TxGNN ; aucun texte d'indication n'est renseigné dans l'AMM) |
| Nouvelle Indication Prédite | Anovulation |
| Score de Prédiction TxGNN | 99,52 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | AMM annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

Remarque : l'anovulation a été retenue car c'est la seule indication prédite disposant de preuves cliniques. Les neuf autres prédictions les mieux classées (par exemple le trouble du développement sexuel 46,XY, les cloisons vaginales, les syndromes chromosomiques) n'ont aucun essai ni publication, sont de niveau L5 et restent en « Hold ».

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le clomifène bloque les récepteurs aux estrogènes de l'hypothalamus. Le rétrocontrôle négatif est ainsi levé, ce qui augmente la pulsatilité de la GnRH et la sécrétion de FSH et de LH. Cela stimule le développement folliculaire et l'ovulation. Il se lie notamment au récepteur alpha des estrogènes (ESR1).

L'infertilité féminine d'origine ovulatoire et l'anovulation relèvent du même mécanisme physiopathologique : le défaut de stimulation hormonale de l'ovulation, notamment dans le syndrome des ovaires polykystiques (SOPK). L'anovulation est donc essentiellement une indication proche ou identique à l'indication d'origine, et non un repositionnement au sens strict. Le clomifène est d'ailleurs le traitement de première intention de l'induction de l'ovulation dans la littérature disponible.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00478504](https://clinicaltrials.gov/study/NCT00478504) | Phase 4 | Terminé | 159 | Essai croisé randomisé en double aveugle comparant le létrozole au citrate de clomifène pour l'induction de l'ovulation dans le SOPK (taux de grossesse, grossesses multiples, naissances vivantes) |
| [NCT02544776](https://clinicaltrials.gov/study/NCT02544776) | Non applicable | Terminé | 60 | Amlodipine associée au Clomid : amélioration du flux sanguin utérin et ovarien, de la taille du follicule préovulatoire et de la progestérone mi-lutéale dans le SOPK |
| [NCT07398924](https://clinicaltrials.gov/study/NCT07398924) | Non applicable | Terminé | 90 | Estradiol vaginal et guaïfénésine orale chez des patientes sous clomifène : effets sur l'endomètre, la glaire cervicale et les grossesses cliniques (pertinence indirecte) |

---

## Preuves de la Littérature

Les 10 publications les plus pertinentes sont listées ci-dessous (revues et essais randomisés en priorité).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29273245](https://pubmed.ncbi.nlm.nih.gov/29273245/) | 2018 | ECR (essai factoriel 2x2) | Lancet | Gonadotrophines versus clomifène, avec ou sans insémination intra-utérine, en cas d'anovulation normogonadotrope et d'échec du clomifène (M-OVIN) |
| [22128296](https://pubmed.ncbi.nlm.nih.gov/22128296/) | 2012 | ECR | Hum Reprod | Citrate de clomifène ou FSH à faible dose en première intention dans l'anovulation liée au SOPK |
| [14576245](https://pubmed.ncbi.nlm.nih.gov/14576245/) | 2003 | Revue systématique / méta-analyse | BMJ | Efficacité de la metformine sur les caractéristiques cliniques et biochimiques du SOPK |
| [12917943](https://pubmed.ncbi.nlm.nih.gov/12917943/) | 2003 | Revue systématique | Cochrane Database Syst Rev | Médicaments insulinosensibilisants dans le SOPK |
| [17137400](https://pubmed.ncbi.nlm.nih.gov/17137400/) | 2006 | Revue | Drugs | Inhibiteurs de l'aromatase pour l'induction de l'ovulation ; le clomifène reste le traitement de première intention, avec des effets antiestrogéniques endométriaux et cervicaux et un risque de grossesses multiples |
| [18487613](https://pubmed.ncbi.nlm.nih.gov/18487613/) | 2008 | Analyse de sous-groupes (étude de type revue) | Hum Reprod | Intérêt de la metformine associée au clomifène dans des sous-groupes de femmes atteintes de SOPK |
| [35351379](https://pubmed.ncbi.nlm.nih.gov/35351379/) | 2022 | Cohorte | Reprod Biomed Online | Influence de l'origine ethnique sur les résultats de l'induction de l'ovulation par clomifène dans le SOPK |
| [21406133](https://pubmed.ncbi.nlm.nih.gov/21406133/) | 2010 | Revue | BMJ Clin Evid | Infertilité féminine : causes (anovulation, atteinte tubaire, endométriose) et prise en charge |
| [31296604](https://pubmed.ncbi.nlm.nih.gov/31296604/) | 2019 | Revue | J Clin Pathol | Évaluation et prise en charge de l'hypofertilité |
| [8521770](https://pubmed.ncbi.nlm.nih.gov/8521770/) | 1995 | Revue | Drugs | Interventions pharmacologiques pour l'induction de l'ovulation ; le clomifène est le premier choix en cas d'aménorrhée |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65338028 | CLOMID 50 mg, comprimé (LABORATOIRES FIDIA), AMM annulée | Comprimé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, hypothyroïdie, hyperthyroïdie, insuffisance surrénalienne (maladie d'Addison), thrombophlébite, SOPK, endométriose, cancer de l'endomètre, tumeur de l'hypophyse, kyste ovarien, syndrome d'hyperstimulation ovarienne, troubles de la vision et cécité, troubles anxieux, troubles névrotiques et dysthymie.
- **Interactions médicamenteuses** : une interaction majeure est signalée avec le **bexarotène**. Par ailleurs, le clomifène se lie au récepteur alpha des estrogènes (ESR1) et au canal VRAC, ce qui relève de sa pharmacologie et non d'une interaction médicamenteuse cliniquement documentée.
- **Points de vigilance issus de la littérature** : grossesses multiples, syndrome d'hyperstimulation ovarienne, effets antiestrogéniques sur l'endomètre et la glaire cervicale.

Les mises en garde et contre-indications de la notice n'ont pas pu être compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai randomisé contrôlé en double aveugle de phase 4 (n = 159) et des essais randomisés publiés (dont M-OVIN dans le Lancet) soutiennent directement l'usage du clomifène dans l'anovulation. Les preuves restent toutefois concentrées sur l'anovulation liée au SOPK, et le critère formel de deux essais de phase 3 pour le niveau L1 n'est pas strictement rempli (phase 4 uniquement). Cette indication est de plus proche de l'indication d'origine.
- Les autres indications prédites (niveau L5, sans aucune preuve) restent en « Hold ».

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier le statut réglementaire : l'unique AMM française est annulée, ce qui doit être confronté à l'étiquetage actuel.
- Obtenir les mises en garde et contre-indications de la notice ANSM (données manquantes bloquantes pour le criblage de sécurité).
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Définir un plan de surveillance des grossesses multiples, de l'hyperstimulation ovarienne et de l'interaction avec le bexarotène.
- Confirmer l'extension des preuves au-delà du SOPK.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

