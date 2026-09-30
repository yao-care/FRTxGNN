---
layout: default
title: Propofol
parent: Preuves élevées (L1-L2)
nav_order: 251
evidence_level: L2
indication_count: 5
---

# Propofol
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **5** 
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

# Propofol : De l'anesthésie à la migraine

## Résumé en Une Phrase

Le propofol est un agent anesthésique intraveineux commercialisé en France sous forme d'émulsion injectable. Le texte de ses indications d'AMM n'est pas renseigné dans le dossier, et son usage d'anesthésie/sédation relève ici de la connaissance générale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine (migraine disorder)**, avec **5 essais cliniques** (dont 3 directement pertinents) et **20 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM du dossier (usage connu : anesthésie/sédation) |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,69 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 11 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Le propofol est toutefois décrit comme un modulateur allostérique positif du récepteur GABA-A. À faible dose (dose sous-anesthésique), il pourrait interrompre une crise de migraine en atténuant l'hyperexcitabilité trigémino-vasculaire et corticale.

Le lien avec l'indication d'origine est pharmacologique plutôt que thérapeutique. Le même effet dépresseur sur le système nerveux central, qui sert à l'anesthésie, pourrait calmer les circuits neuronaux impliqués dans la crise migraineuse. Des travaux précliniques montrent que le propofol supprime la dépression corticale envahissante, considérée comme le corrélat neuronal de l'aura migraineuse.

Le signal clinique provient d'un essai randomisé de phase 2/3 et d'un essai pédiatrique sur la perfusion de faible dose aux urgences. S'y ajoutent une revue systématique et l'inclusion dans la mise à jour 2025 des lignes directrices de l'American Headache Society pour les urgences. Les essais sont de petite taille et le risque de sédation est réel. L'usage devrait donc rester limité à un environnement surveillé, pour les cas réfractaires ou de recours.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Terminé | 74 | Propofol à faible dose comme traitement de la crise migraineuse pédiatrique aux urgences. Directement pertinent. |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | Non applicable | Terminé | 40 | Perfusion de propofol à faible dose contre la crise migraineuse de l'enfant. Directement pertinent, mais phase non classée et échantillon réduit. |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | Non applicable | Arrêté prématurément | 12 | Propofol à faible dose pour la migraine sévère réfractaire aux urgences. Pertinent, mais arrêté avec 12 participants, il apporte peu de preuves. |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | Non applicable | Inconnu | 130 | Sévoflurane vs propofol pour l'entretien de l'anesthésie et la survenue de céphalées postopératoires. Le propofol est un comparateur, l'objectif n'est pas de traiter la migraine. |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | Non applicable | Terminé | 315 | Combinaisons de points d'acupuncture par électroacupuncture lors d'un pontage coronarien à cœur battant. Lien seulement indirect. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | ECR | J Emerg Med | Propofol à faible dose dans la migraine pédiatrique aux urgences. Évalue efficacité, effets indésirables et durée de séjour. |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | ECR (double insu) | Arch Acad Emerg Med | Propofol + granisétron vs propofol + métoclopramide dans la prise en charge des symptômes de la migraine aiguë. |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | ECR pilote | Emerg Med Australas | Propofol à dose de sédation procédurale vs traitement standard en première intention de la migraine aux urgences. |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | ECR | Arch Acad Emerg Med | Association sumatriptan + propofol comparée au sumatriptan seul dans la migraine aiguë. |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revue systématique | Acad Emerg Med | Sécurité et efficacité du propofol dans la migraine aiguë aux urgences. Les données disponibles restent limitées. |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revue systématique et analyse en réseau | Headache | Efficacité des agents parentéraux pour réduire les rechutes après une migraine aiguë sévère. |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revue systématique et recommandations | Cephalalgia | Recommandations de la Société canadienne des céphalées pour le traitement de la migraine en urgence. |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Revue systématique qualitative | Headache | Sécurité et efficacité des traitements de la migraine pédiatrique aux urgences. |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Lignes directrices | Headache | Mise à jour 2025 des lignes directrices de l'American Headache Society sur les traitements parentéraux de la migraine aux urgences. |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Revue | Expert Rev Neurother | Profil du propofol à dose sous-anesthésique dans les migraines réfractaires. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63558577 | PROPOFOL BAXTER 10 mg/ml, émulsion injectable/pour perfusion | Émulsion injectable pour perfusion | Baxter Holding (Pays-Bas) |
| 62010414 | DIPRIVAN 20 mg/mL, émulsion injectable en seringue pré-remplie | Émulsion injectable | Aspen Pharma Trading (Irlande) |
| 66093051 | PROPOFOL BAXTER 20 mg/ml, émulsion injectable/pour perfusion | Émulsion injectable pour perfusion | Baxter Holding (Pays-Bas) |
| 66110981 | PROPOFOL KABI 10 mg/mL, émulsion injectable/pour perfusion | Émulsion injectable ou pour perfusion | Fresenius Kabi France |
| 66701952 | PROPOFOL LIPURO 2 % (20 mg/ml), émulsion injectable ou pour perfusion | Émulsion injectable ou pour perfusion | B. Braun Melsungen |

Le texte des indications approuvées n'est pas renseigné pour ces AMM dans le dossier. Aucune indication migraineuse n'y apparaît.

## Considérations de Sécurité

- **Sédation** : le risque de sédation est réel, y compris à faible dose. L'usage doit être limité à un environnement surveillé, pour les cas réfractaires ou de recours.
- **Angor vasospastique** : des cas rapportés font état de spasmes coronaires survenus lors d'une anesthésie induite par le propofol (PMID 19364017 et 20339883). Ils ne prouvent pas un lien de causalité, mais appellent à la prudence chez les patients atteints d'angor de Prinzmetal ou de vasospasme connu.

Veuillez consulter la notice pour les informations de sécurité complètes (mises en garde, contre-indications, interactions médicamenteuses).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Un essai randomisé de phase 2/3 terminé et un essai pédiatrique terminé soutiennent l'usage du propofol à faible dose dans la migraine aiguë. Une revue systématique et la mise à jour 2025 des lignes directrices de l'American Headache Society vont dans le même sens. Les essais restent de petite taille et le risque de sédation impose un cadre de surveillance strict.

Les autres prédictions, à savoir la migraine avec aura du tronc cérébral (extrapolation, question de recherche), l'angor de Prinzmetal, le syndrome néphrogénique d'antidiurèse inappropriée et le syndrome de Gilles de la Tourette, ne sont pas étayées par des preuves thérapeutiques. Elles sont classées en attente (Hold) ou en question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- La notice ANSM (mises en garde et contre-indications), indispensable pour le criblage de sécurité
- Les données détaillées sur le mécanisme d'action (MOA)
- Le texte des indications approuvées pour les AMM françaises
- Des essais de phase 3 confirmatoires, de plus grande taille, chez l'adulte et l'enfant
- Un protocole d'usage encadré : environnement surveillé, dose et critères de sélection des patients (exclusion des patients atteints d'angor vasospastique)

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

