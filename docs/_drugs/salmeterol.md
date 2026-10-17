---
layout: default
title: Salmeterol
parent: Preuves élevées (L1-L2)
nav_order: 692
evidence_level: L1
indication_count: 7
last_modified_at: 2026-10-14
description: "Salmeterol : nouvelle indication prédite, Bronchite (niveau de preuve L1). Indication d'origine : Emphysème pulmonaire, asthme intrinsèque, asthme allergique"
monitor_inn: "salmeterol"
predicted_indications: ["bronchitis", "respiratory malformation", "obstructive lung disease", "Rienhoff syndrome", "asthma-related traits, susceptibility to", "atopic eczema"]
---

# Salmeterol
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **7** 
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

# Salmétérol : De l'emphysème pulmonaire et de l'asthme à la bronchite

## Résumé en Une Phrase

Le salmétérol est un bêta-2-agoniste de longue durée d'action, initialement utilisé pour le traitement de l'emphysème pulmonaire et de l'asthme (intrinsèque et allergique).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, avec **8 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit toutefois d'une extension très proche des usages d'origine (bronchite chronique et BPCO) plutôt que d'un repositionnement éloigné.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Emphysème pulmonaire, asthme intrinsèque, asthme allergique (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base. Sur la base des informations connues, le salmétérol est un agoniste des récepteurs bêta-2-adrénergiques à action prolongée. Il induit une bronchodilatation durable par relaxation du muscle lisse bronchique, via l'AMP cyclique.

Il favorise aussi la clairance muco-ciliaire, ce qui est pertinent dans la bronchite chronique. Une étude clinique a d'ailleurs évalué son effet aigu sur la clairance muco-ciliaire et la toux chez des patients atteints de bronchite chronique.

La bronchite chronique est un phénotype de la BPCO et partage sa physiopathologie avec l'emphysème et l'asthme, indications d'origine. La prédiction est donc mécanistiquement cohérente : c'est une extension proche, non un repositionnement distant.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | Terminé | 130 | Salmétérol/fluticasone 50/500 µg vs placebo sur l'inflammation bronchique dans la BPCO (13 semaines) |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | Terminé | 584 | Tiotropium vs salmétérol en aérosol vs placebo dans la BPCO (6 mois) |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | Terminé | 122 | Étude de tolérance à long terme (56 semaines) de salmétérol/fluticasone dans la BPCO (bronchite chronique, emphysème) |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Terminé | 741 | Arformotérol vs placebo et comparateur actif dans la BPCO (12 semaines) ; le salmétérol est vraisemblablement le comparateur |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Terminé | 799 | Sécurité à 12 mois de l'arformotérol dans la BPCO ; données indirectes pour le salmétérol |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | Terminé | 150 | Comparaison de deux médicaments dans la BPCO (18 semaines) ; lien avec le salmétérol plausible mais non vérifié |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | Terminé | 457 | Recherche de dose fluticasone/formotérol par rapport à Advair Diskus (salmétérol) dans la BPCO |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | Inconnu | 20 | Arformotérol nébulisé vs salmétérol en poudre sèche (Serevent) dans la BPCO ; petit effectif |
| [NCT00233051](https://clinicaltrials.gov/study/NCT00233051) | Non applicable | Arrêté | 20 | Biomarqueurs inflammatoires dans les expectorations induites dans la BPCO ; exploratoire |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17557771](https://pubmed.ncbi.nlm.nih.gov/17557771/) | 2007 | ECR | Thorax | Effet de salmétérol/fluticasone sur l'inflammation des voies aériennes dans la BPCO |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | Étude clinique | Chest | Efficacité et sécurité de fluticasone 250 µg/salmétérol 50 µg (Diskus) vs placebo et composants seuls dans la BPCO |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Méta-analyse | Respir Res | Résultats améliorés dans la BPCO sous salmétérol 50 µg deux fois par jour vs placebo/traitement habituel |
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | Étude clinique | Pulm Pharmacol Ther | Effet aigu du salmétérol sur la clairance muco-ciliaire et de la toux dans la bronchite chronique (n = 14) |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Étude clinique | Ther Adv Respir Dis | Sécurité et tolérance à un an de l'arformotérol et du salmétérol dans la BPCO |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte (base de remboursements) | Curr Med Res Opin | Recours aux soins et coûts chez les patients atteints de bronchite chronique initiant fluticasone/salmétérol vs autres traitements inhalés |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Revue | Drugs | Revue de l'usage de salmétérol/fluticasone dans la BPCO |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | Étude ouverte | Clin Ther | Salmétérol inhalé vs théophylline orale dans la BPCO légère à modérée |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Recommandations | Basic Clin Pharmacol Toxicol | Recommandations finlandaises sur la BPCO stable |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | Revue | Br J Clin Pharmacol | Antagonisme de l'effet des bêta-2-agonistes de longue durée d'action |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69163238 | SEREVENT DISKUS 50 microgrammes/dose | Poudre pour inhalation | Non renseignée (AMM annulée) |
| 67274478 | SEREVENT 25 microgrammes/dose | Suspension pour inhalation en flacon pressurisé | Non renseignée (AMM annulée) |
| 67546191 | SERETIDE DISKUS 100/50 microgrammes/dose | Poudre pour inhalation | Non renseignée (AMM annulée) |
| 69505268 | SERETIDE 125/25 microgrammes/dose | Suspension pour inhalation en flacon pressurisé | Non renseignée (AMM annulée) |
| 64587838 | SERETIDE 50/25 microgrammes/dose | Suspension pour inhalation en flacon pressurisé | Non renseignée (AMM annulée) |

Au total, 20 AMM sont recensées (monothérapie Serevent, Seretide et génériques de l'association propionate de fluticasone/salmétérol). Toutes sont annulées ; aucune n'est actuellement valide.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, syndrome du QT long (dont forme familiale), épilepsie, hyperglycémie, kératite herpétique, déficits hypophysaires (dont déficit en hormone de croissance et hypogonadisme hypogonadotrope), syndrome de Kallmann, syndrome de Sheehan, maladies du thymus et ostéoporose.
- **Interactions médicamenteuses** : 600 interactions recensées. La plus importante est **majeure** avec la clarithromycine. Des interactions modérées concernent notamment l'épinéphrine, la famotidine, l'isométheptène, la dolasétron, la diéthylpropion, ainsi que des antidiabétiques (acarbose, alogliptine, canagliflozine, chlorpropamide, dapagliflozine, empagliflozine, albiglutide, dulaglutide). Des interactions mineures concernent les corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, béclométasone, bétaméthasone, budésonide).
- **Point d'attention clé (asthme)** : les revues Cochrane signalent un risque d'événements indésirables graves avec les bêta-2-agonistes de longue durée d'action ; leur usage dans l'asthme doit se faire en association avec un corticoïde inhalé.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être obtenues ; veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés et des études publiées soutiennent l'usage du salmétérol dans la BPCO avec bronchite chronique, ce qui correspond à un niveau de preuve L1. L'extension est proche des indications d'origine.
- Aucune AMM n'est actuellement valide en France, et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (ANSM) : mises en garde, contre-indications, indications autorisées. Cette lacune est bloquante pour le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Clarifier la situation réglementaire : vérifier si des spécialités à base de salmétérol (notamment les associations) sont encore disponibles en France.
- Définir des garde-fous : association à un corticoïde inhalé dans l'asthme, surveillance cardiovasculaire (QT, tension) et gestion de l'interaction majeure avec la clarithromycine.
- Distinguer, dans les essais, les données propres au salmétérol de celles où il n'est que comparateur ou fait partie d'une association.

**Autres indications prédites (non retenues à ce stade) :**
- Obstructive lung disease (maladie pulmonaire obstructive) : niveau L1, mais il s'agit d'un usage déjà couvert par les indications d'origine.
- Asthme : niveau L1, avec les garde-fous ci-dessus.
- Malformation respiratoire, syndrome de Rienhoff, asthme (traits de susceptibilité) et eczéma atopique : Hold, preuves absentes ou insuffisantes (L4 à L5).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

