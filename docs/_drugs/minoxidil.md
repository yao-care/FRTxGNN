---
layout: default
title: Minoxidil
parent: Preuves modérées (L3-L4)
nav_order: 503
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Minoxidil : nouvelle indication prédite, Hypotrichose simple du cuir chevelu (niveau de preuve L3). Indication d'origine : Hypertension artérielle et alopécie"
monitor_inn: "MINOXIDIL"
predicted_indications: ["congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "primary hereditary glaucoma"]
---

# Minoxidil
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **10** 
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

# Minoxidil : De l'Hypertension et de l'Alopécie à l'Hypotrichose Simple du Cuir Chevelu

## Résumé en Une Phrase

Minoxidil est un vasodilatateur ouvreur des canaux potassiques, initialement utilisé pour traiter l'hypertension artérielle (par voie orale) et l'alopécie (par voie cutanée).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**, une maladie génétique rare.
Aucun essai clinique n'est enregistré, mais **3 publications** (séries et rapports de cas) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle et alopécie (le texte d'indication des AMM n'est pas renseigné ; source : graphe de connaissances) |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 19 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, le minoxidil ouvre les canaux potassiques sensibles à l'ATP et prolonge la phase anagène du follicule pileux. Il favorise aussi la vasodilatation et la prolifération folliculaire, ce qui est cohérent avec son usage dans l'alopécie.

L'hypotrichose simple héréditaire est un trouble non cicatriciel de raréfaction pilaire, lié notamment à des variants du gène *CDSN* (cornéodesmosine). Son mécanisme est donc proche de celui des alopécies non cicatricielles déjà traitées par le minoxidil, et l'effet stimulant sur la croissance du cheveu pourrait s'y appliquer.

Une réserve importante : dans les trois publications identifiées, le minoxidil (oral ou topique) était associé à des facteurs de croissance, à des extraits botaniques ou à du plasma riche en plaquettes (PRP). Sa contribution propre ne peut donc pas être isolée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Série de cas | Dermatologic Therapy | Traitement de l'hypotrichose simple héréditaire du cuir chevelu par minoxidil oral et facteurs de croissance (résumé non disponible) |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Cas clinique | Frontiers in Genetics | Cas familial d'un garçon de 8 ans porteur d'une mutation de *CDSN*, traité par extraits botaniques et minoxidil |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Cas clinique | Journal of Dermatological Treatment | Patient de 14 ans traité avec succès par injection de PRP associée au minoxidil topique à 2 % |

## Informations de Marché en France

Les 19 AMM recensées sont annulées. Les cinq premières sont présentées ci-dessous ; le texte d'indication n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64473959 | Minoxidil Sandoz Conseil 5 % | Solution pour application cutanée | Non renseignée |
| 69250554 | Alostil 5 % | Mousse pour application cutanée | Non renseignée |
| 69301899 | Alopexy 50 mg/ml | Solution pour application cutanée | Non renseignée |
| 69871657 | Unipexil 2 % | Solution pour application cutanée | Non renseignée |
| 67395654 | Lonoten 10 mg | Comprimé sécable | Non renseignée |

## Considérations de Sécurité

**Contre-indications issues du graphe de connaissances** (ce ne sont pas des données de notice) : hypotension orthostatique, atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, maladie rénale, accident vasculaire cérébral et maladies cérébrovasculaires, infarctus du myocarde, maladies cardiovasculaires, phéochromocytome et paragangliome, péricardite, épanchement péricardique et tamponnade, hémoglobinopathie, ainsi que dermatose du cuir chevelu.

**Interactions médicamenteuses** (100 interactions recensées, dont les principales sont de niveau modéré) :
- Corticoïdes : hydrocortisone, prednisone, prednisolone, dexaméthasone, bétaméthasone, budésonide, triamcinolone
- Inhibiteurs du SGLT2 : canagliflozine, dapagliflozine, empagliflozine, ertugliflozine
- Autres : bupropion, morphine, opium, dronabinol, nabilone, saproptérine

Pour les mises en garde et la notice officielle, veuillez consulter la notice : les données de l'ANSM n'ont pas pu être exploitées.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le score TxGNN est très élevé et le mécanisme est plausible, mais les preuves se limitent à trois cas cliniques en association thérapeutique (niveau L3), sans essai enregistré.
- Le profil de sécurité, en particulier cardiovasculaire en cas d'usage systémique, impose des précautions, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action issues de DrugBank
- Mises en garde et contre-indications de la notice ANSM
- Études contrôlées isolant l'effet du minoxidil en monothérapie
- Évaluation de la voie d'administration (topique ou orale à faible dose) et de la sécurité cardiovasculaire, notamment chez l'enfant
- Clarification du statut réglementaire, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

