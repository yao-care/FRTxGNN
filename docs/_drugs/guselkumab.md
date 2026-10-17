---
layout: default
title: Guselkumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Guselkumab : nouvelle indication prédite, Ostéoporose médicamenteuse (première prédiction) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées (textes d'indication…"
monitor_inn: "GUSELKUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "renal osteodystrophy", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
---

# Guselkumab
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

# Guselkumab : De l'indication d'origine non renseignée à l'ostéoporose médicamenteuse

## Résumé en Une Phrase

Guselkumab est un anticorps monoclonal inhibiteur de la sous-unité p19 de l'IL-23, commercialisé sous le nom de Tremfya. Les données réglementaires compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN place en tête de ses prédictions l'**ostéoporose médicamenteuse**, mais **aucun essai clinique ni aucune publication** ne soutient cette direction.

Deux autres prédictions de la liste disposent en revanche de preuves solides : le **psoriasis** (30 essais cliniques, 20 publications) et la **rectocolite hémorragique** (10 essais cliniques, 20 publications). Elles correspondent très probablement à des indications déjà connues du produit. Elles sont traitées dans la section suivante, car elles changent la lecture du dossier.

---

## Apercu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées (textes d'indication vides) |
| Nouvelle Indication Predite | Ostéoporose médicamenteuse (première prédiction) |
| Score de Prediction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

**Prédictions secondaires disposant de preuves (à vérifier avant d'y voir un repositionnement) :**

| Indication prédite | Score TxGNN | Niveau de preuve | Décision |
|------|------|------|------|
| Psoriasis | 99,75 % | L1 | Proceed with Guardrails |
| Rectocolite hémorragique | 99,70 % | L1 | Proceed with Guardrails |

Les sept autres prédictions du classement (rétinopathie diabétique sévère non proliférante, rétinopathie diabétique, ostéodystrophie rénale, hypotrichose congénitale avec dystrophie maculaire juvénile, trouble de libération plaquettaire primaire, thrombasthénie de Glanzmann, hyperparathyroïdie secondaire non rénale) sont au niveau L5 avec la décision Hold.

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances générales, guselkumab se lie à la sous-unité p19 de l'IL-23 et bloque l'axe IL-23/Th17, central dans plusieurs maladies inflammatoires à médiation immunitaire.

**Ostéoporose médicamenteuse (première prédiction).** La voie IL-23/IL-17 a été évoquée dans la résorption osseuse. Toutefois, aucune donnée fournie ne soutient un lien entre guselkumab et l'ostéoporose médicamenteuse. Le score élevé du modèle est une prédiction purement computationnelle et ne suffit pas à justifier une décision.

**Psoriasis et rectocolite hémorragique.** Ces deux prédictions s'appuient sur un mécanisme cohérent : le blocage de l'IL-23 réduit la signalisation Th17 pathogène dans la peau et la muqueuse intestinale. De nombreux essais de phase 3 le confirment. Comme le champ « indications d'origine » est vide et que le statut de marché est « annulé uniquement », il s'agit probablement d'un problème de complétude des données plutôt que d'un véritable repositionnement. Le statut réglementaire exact doit être vérifié avant de présenter ces résultats comme nouveaux.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour l'ostéoporose médicamenteuse.

Les essais ci-dessous concernent les deux prédictions disposant de preuves. Ils sont présentés à titre de contexte.

**Psoriasis (essais les plus pertinents)**

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03090100](https://clinicaltrials.gov/study/NCT03090100) | Phase 3 | Terminé | 1048 | Guselkumab versus sécukinumab dans le psoriasis en plaques modéré à sévère |
| [NCT03573323](https://clinicaltrials.gov/study/NCT03573323) | Phase 4 | Terminé | 1027 | Ixékizumab versus guselkumab sur 24 semaines dans le psoriasis en plaques |
| [NCT06039189](https://clinicaltrials.gov/study/NCT06039189) | Phase 3b | Terminé | 338 | Guselkumab versus placebo dans le psoriasis modéré à faible surface corporelle avec atteinte de sites spéciaux |
| [NCT02951533](https://clinicaltrials.gov/study/NCT02951533) | Phase 3b | Terminé | 119 | Guselkumab versus fumarates (Fumaderm) chez des patients naïfs de traitement systémique |
| [NCT02207244](https://clinicaltrials.gov/study/NCT02207244) | Phase 3 | Terminé | 992 | Efficacité et sécurité avec retrait randomisé et retraitement (VOYAGE 2) |
| [NCT02203032](https://clinicaltrials.gov/study/NCT02203032) | Phase 3 | Terminé | 872 | Guselkumab chez des patients en réponse inadéquate à l'ustékinumab |
| [NCT02207231](https://clinicaltrials.gov/study/NCT02207231) | Phase 3 | Terminé | 837 | Efficacité et sécurité versus placebo et comparateur actif |
| [NCT04914429](https://clinicaltrials.gov/study/NCT04914429) | Phase 4 | Terminé | 327 | Guselkumab versus placebo chez des participants chinois |

**Rectocolite hémorragique (essais les plus pertinents)**

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04033445](https://clinicaltrials.gov/study/NCT04033445) | Phase 2b/3 | Actif, hors recrutement | 1064 | Étude QUASAR : efficacité et sécurité versus placebo dans la RCH modérée à sévère |
| [NCT05528510](https://clinicaltrials.gov/study/NCT05528510) | Phase 3 | Actif, hors recrutement | 418 | Induction sous-cutanée versus placebo |
| [NCT05242484](https://clinicaltrials.gov/study/NCT05242484) | Phase 2b | Actif, hors recrutement | 577 | Association guselkumab + golimumab versus monothérapies |
| [NCT03662542](https://clinicaltrials.gov/study/NCT03662542) | Phase 2a | Terminé | 214 | Preuve de concept de l'association guselkumab + golimumab |
| [NCT06260163](https://clinicaltrials.gov/study/NCT06260163) | Phase 3 | Actif, hors recrutement | 112 | Efficacité chez des participants pédiatriques |
| [NCT06663332](https://clinicaltrials.gov/study/NCT06663332) | Phase 3 | En recrutement | 196 | Extension à long terme (sécurité) chez l'enfant |

---

## Preuves de la Litterature

Aucune littérature associée n'est disponible actuellement pour l'ostéoporose médicamenteuse.

**Psoriasis**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28057360](https://pubmed.ncbi.nlm.nih.gov/28057360/) | 2017 | ECR | J Am Acad Dermatol | VOYAGE 1 : guselkumab versus adalimumab dans le psoriasis modéré à sévère |
| [28057361](https://pubmed.ncbi.nlm.nih.gov/28057361/) | 2017 | ECR | J Am Acad Dermatol | VOYAGE 2 : retrait randomisé et retraitement |
| [28635018](https://pubmed.ncbi.nlm.nih.gov/28635018/) | 2018 | ECR | Br J Dermatol | NAVIGATE : guselkumab après réponse inadéquate à l'ustékinumab |
| [31583255](https://pubmed.ncbi.nlm.nih.gov/31583255/) | 2019 | Méta-analyse en réseau | J Immunol Res | Efficacité et sécurité à court terme des inhibiteurs d'IL-17, IL-12/23 et IL-23 |
| [37436070](https://pubmed.ncbi.nlm.nih.gov/37436070/) | 2023 | Méta-analyse en réseau | Cochrane Database Syst Rev | Traitements systémiques du psoriasis en plaques chronique |
| [32880909](https://pubmed.ncbi.nlm.nih.gov/32880909/) | 2021 | ECR | Br J Dermatol | Ixékizumab versus guselkumab, résultats à 24 semaines |

**Rectocolite hémorragique**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39706209](https://pubmed.ncbi.nlm.nih.gov/39706209/) | 2025 | ECR | Lancet | QUASAR : induction et maintenance de phase 3 contre placebo |
| [41544637](https://pubmed.ncbi.nlm.nih.gov/41544637/) | 2026 | ECR | Lancet Gastroenterol Hepatol | ASTRO : induction sous-cutanée de guselkumab |
| [37659673](https://pubmed.ncbi.nlm.nih.gov/37659673/) | 2023 | ECR | Gastroenterology | QUASAR, étude d'induction de phase 2b |
| [39425738](https://pubmed.ncbi.nlm.nih.gov/39425738/) | 2024 | Méta-analyse en réseau | Gastroenterology | Synthèse AGA 2024 sur l'efficacité comparée des thérapies avancées |
| [40407729](https://pubmed.ncbi.nlm.nih.gov/40407729/) | 2025 | Méta-analyse en réseau | Aliment Pharmacol Ther | Traitements d'entretien dans la RCH |
| [39572132](https://pubmed.ncbi.nlm.nih.gov/39572132/) | 2024 | Recommandations | Gastroenterology | Recommandations AGA sur la prise en charge pharmacologique de la RCH |

---

## Informations de Marche en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68372441 | TREMFYA 100 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM annulée) |
| 67296108 | TREMFYA 100 mg ONEPRESS, solution injectable en stylo prérempli | Solution injectable | Non renseignée (AMM annulée) |

Les deux AMM sont détenues par JANSSEN CILAG INTERNATIONAL NV et sont annulées. Aucune AMM valide n'apparaît dans les données compilées. Les essais enregistrés mentionnent pourtant une autorisation de mise sur le marché en France en 2018 pour le psoriasis en plaques, ce qui renforce l'hypothèse d'une source de données incomplète.

---

## Considerations de Securite

**Interactions médicamenteuses** (100 interactions recensées ; principales ci-dessous)

- **Majeure :** adalimumab (association de deux biothérapies immunomodulatrices).
- **Modérée :** simvastatine, apixaban, warfarine, rivaroxaban, dicoumarol, lidocaïne, hydrocodone, théophylline, aminophylline, oxtriphylline, roflumilast, tacrolimus, fentanyl, nifédipine, anatoxine tétanique.
- **Mineure :** sels de zinc (sulfate, acétate, gluconate, chlorure).

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Etapes

**Décision : Hold** (pour l'ostéoporose médicamenteuse, première prédiction)

**Justification :**
- La prédiction repose uniquement sur le score du modèle (99,84 %), sans essai ni publication, et aucun lien mécanistique n'est étayé par les données fournies. Le niveau de preuve est L5.
- Le psoriasis et la rectocolite hémorragique (niveau L1, Proceed with Guardrails) correspondent probablement à des indications déjà connues du produit. Il s'agit sans doute d'une lacune de données et non d'un repositionnement réel.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les notices ANSM (indications, mises en garde, contre-indications), car cette lacune bloque le criblage de sécurité.
- Vérifier le statut réglementaire réel de Tremfya en France, les AMM disponibles étant toutes annulées.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Pour l'ostéoporose médicamenteuse : mener une revue de littérature préclinique sur l'axe IL-23/IL-17 et le remodelage osseux avant toute étude clinique.
- Pour la rectocolite hémorragique et le psoriasis : confirmer s'il s'agit d'indications déjà approuvées afin de les écarter du périmètre du repositionnement.
- Pour une population à risque (grossesse, allaitement, infections chroniques), prévoir un plan de surveillance de sécurité.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

