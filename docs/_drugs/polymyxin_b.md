---
layout: default
title: Polymyxin B
parent: Preuves modérées (L3-L4)
nav_order: 615
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-20
monitor_inn: "polymyxin b"
predicted_indications: ["bronchitis", "laryngotracheitis"]
description: "Polymyxin B : nouvelle indication prédite, Bronchite (bronchitis) (niveau de preuve L4). En France, AMM dans la BDPM : 9 (valides : 9)"
---

# Polymyxin B
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

## Polymyxin B: Bronchite (bronchitis)
{: .text-alpha }

## Résumé en Une Phrase

La polymyxine B est un antibiotique polypeptidique actif contre les bactéries à Gram négatif. Elle est présente dans plusieurs spécialités françaises à usage local (gynécologique, auriculaire, ophtalmique), toutes aujourd'hui radiées.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **bronchite**, mais aucun essai clinique n'est enregistré et la littérature disponible est surtout indirecte ou porte sur des signaux de sécurité respiratoire.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Bronchite (bronchitis) |
| Score de Prédiction TxGNN | 0.9987 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 9) |
| Nombre d'AMM | 9 (valides : 9) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Polymyxin B (traduction non officielle) : « Le sulfate de polymyxine B exerce une action bactéricide contre presque tous les bacilles à Gram négatif, à l'exception du groupe Proteus. Les polymyxines augmentent la perméabilité de la membrane cellulaire bactérienne, entraînant la mort de la cellule. Toutes les bactéries à Gram positif, les champignons et les cocci à Gram négatif sont résistants à la polymyxine B. Pour des informations spécifiques concernant les critères d'interprétation des tests de sensibilité ainsi que les méthodes d'essai et les normes de contrôle de qualité associées reconnues par la FDA pour ce médicament, veuillez consulter : www.fda.gov/STIC. » Texte original en anglais : "Polymyxin B sulfate has a bactericidal action against almost all gram-negative bacilli except the Proteus group. Polymyxins increase the permeability of bacterial cell membrane leading to death of the cell. All gram positive bacteria, fungi, and gram-negative cocci are resistant to polymyxin B. For specific information regarding susceptibility test criteria and associated test methods and quality control standards recognized by FDA for this drug, please see: www.fda.gov/STIC." ([DailyMed: Polymyxin B (polymyxin b sulfate) prescribing information, Xellia Pharmaceuticals USA LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b56f18c0-ef5e-4ed9-a5af-f79f3cd189b6), version du 2026-06-22 ; consulté le 2026-11-19). D'après les connaissances générales, la polymyxine B agit en désorganisant la membrane externe des bactéries à Gram négatif et possède une activité bactéricide.

Un lien plausible existe donc avec les bronchites ou trachéo-bronchites bactériennes dues à des germes à Gram négatif multirésistants (*Pseudomonas aeruginosa*, *Acinetobacter baumannii*). Des séries de cas et des études de cohorte portent sur la polymyxine B inhalée dans ces infections respiratoires, mais elles concernent surtout des pneumopathies ou des trachéo-bronchites associées à la ventilation, et non la bronchite au sens large.

Le score élevé de TxGNN n'est pas conforté par des données cliniques favorables. Plusieurs publications (1971, 1979, 1985) décrivent une bronchoconstriction et une provocation bronchique non spécifique après inhalation de polymyxine B chez des patients asthmatiques ou atteints de bronchite chronique. Des modèles animaux montrent aussi une accumulation d'éosinophiles dans les voies aériennes. Ce signal de sécurité pèse lourd face au bénéfice théorique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Les publications ci-dessous sont celles qui concernent la bronchite ou les atteintes bronchiques. Elles sont classées selon le niveau de preuve, le plus élevé en premier.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Cohorte comparative | Infection | Comparaison de la polymyxine B à d'autres antimicrobiens dans la pneumonie et la trachéo-bronchite associées à la ventilation (*P. aeruginosa*, *A. baumannii*) |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Série de cas | Diagn Microbiol Infect Dis | Polymyxine B inhalée chez 19 patients atteints d'infections respiratoires à bacilles à Gram négatif multirésistants (pneumonies et trachéo-bronchites) |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Non classé | J Kans Med Soc | Trachéo-bronchite à *Pseudomonas* : gentamicine par voie générale et aérosol de polymyxine B |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Observation expérimentale | Chest | Polymyxine B endobronchique : observations expérimentales dans la bronchite chronique |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Étude physiologique | Lung | Réactivité bronchique à la polymyxine B inhalée dans l'asthme et la bronchite chronique obstructive (signal de sécurité) |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Étude physiologique | Orvosi Hetilap | Provocation bronchique non spécifique induite par le sulfate de polymyxine B (signal de sécurité) |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Commentaire de sécurité | Ann Intern Med | Danger de l'inhalation de polymyxine B |
| [11359434](https://pubmed.ncbi.nlm.nih.gov/11359434/) | 2001 | Étude animale | Clin Exp Allergy | Chez le cobaye, l'accumulation d'éosinophiles induite par la polymyxine B réduit la réactivité bronchique |
| [8054833](https://pubmed.ncbi.nlm.nih.gov/8054833/) | 1994 | Étude animale (indirecte) | Clin Auton Res | Modèle de bronchite à éosinophiles induit chez le cobaye par la polymyxine B, utilisé pour tester un antagoniste de la neurokinine |
| [28441858](https://pubmed.ncbi.nlm.nih.gov/28441858/) | 2017 | Étude animale (indirecte) | Zhonghua Yi Xue Za Zhi | Modèle murin de bronchite à éosinophiles induit par la polymyxine B |

---

## Informations de Marché en France

Les 9 AMM sont radiées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66085108 | POLYGYNAX, capsule vaginale | Capsule | Non renseignée |
| 62067340 | MAXIDROL, pommade ophtalmique | Pommade | Non renseignée |
| 66129490 | POLYDEXA, solution auriculaire, gouttes | Solution gouttes | Non renseignée |
| 68739115 | POLYGYNAX VIRGO, capsule vaginale | Capsule | Non renseignée |
| 60798567 | ANTIBIO SYNALAR, solution pour instillation auriculaire | Solution pour instillation | Non renseignée |

---

## Considérations de Sécurité

- **Signaux respiratoires (littérature)** : l'inhalation ou l'administration endobronchique de polymyxine B a été associée à une bronchoconstriction et à une réactivité bronchique accrue chez des patients asthmatiques ou atteints de bronchite chronique.
- **Interactions médicamenteuses** : 73 interactions sont recensées. Parmi les interactions de niveau majeur figurent l'amikacine, la toxine botulique de type A, le cisatracurium, le cidofovir, le déférasirox, l'acide iothalamique, le diatrizoate et plusieurs immunoglobulines humaines. Parmi les interactions de niveau modéré figurent l'éthinylestradiol, l'estradiol, la mésalazine, le balsalazide, l'ibandronate, la capréomycine et la clofarabine.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais le niveau de preuve est L4 : aucun essai clinique n'est enregistré, la littérature est surtout indirecte et elle signale des risques respiratoires lors de l'inhalation. Aucune spécialité n'est actuellement autorisée en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (données ANSM manquantes, ce qui bloque l'étape d'évaluation de sécurité).
- Les données sur le mécanisme d'action, à compléter depuis DrugBank.
- Une évaluation de la voie d'administration, car le médicament n'a aucune forme respiratoire autorisée et la voie inhalée pose un problème de sécurité.
- Une revue ciblée des infections bactériennes à Gram négatif des voies respiratoires basses, afin de distinguer ce cas d'une bronchite en général.

### Autres indications prédites (pour information)

- **Laryngotrachéite** (score 0,9962, niveau L5, Hold) : seule la prédiction du modèle la soutient, sans essai ni publication. Cette pathologie est surtout virale, donc l'intérêt d'un antibactérien actif sur les Gram négatifs est faible.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Polymyxin B (polymyxin b sulfate) prescribing information, Xellia Pharmaceuticals USA LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b56f18c0-ef5e-4ed9-a5af-f79f3cd189b6) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

