---
layout: default
title: Indomethacin
parent: Prédiction du modèle uniquement (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
description: "Indomethacin : nouvelle indication prédite, Brachydactyly-syndactyly syndrome (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Indomethacin
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

## Indomethacin: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## Résumé en Une Phrase

L'indométacine est un anti-inflammatoire non stéroïdien (AINS) utilisé à l'origine dans les affections rhumatismales et inflammatoires (polyarthrite rhumatoïde, spondylarthrite ankylosante, goutte, arthrose, bursite, ténosynovite) ainsi que pour la fermeture du canal artériel persistant.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome brachydactylie-syndactylie**, mais **aucun essai clinique et aucune publication** ne soutiennent cette prédiction, qui repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Brachydactyly-syndactyly syndrome |
| Score de Prédiction TxGNN | 0.9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'indométacine est un inhibiteur non sélectif des cyclooxygénases (COX-1 et COX-2) : elle réduit la synthèse des prostaglandines, médiateurs de l'inflammation, de la douleur et de la fièvre. Son efficacité dans les rhumatismes inflammatoires repose sur ce mécanisme.

**Pour la prédiction principale, aucun lien mécanistique n'est établi.** Le syndrome brachydactylie-syndactylie est une malformation squelettique du développement des membres. Rien dans les données disponibles ne relie l'inhibition des prostaglandines à la physiopathologie de cette malformation.

Les autres prédictions du top 10 sont du même ordre : syndromes développementaux rares (colobomateuse-microphtalmie, dysplasie acromésomélique de type Hunter-Thompson, syndrome WHIM, brachyolmie, myosclérose) sans lien mécanistique démontré. À titre de comparaison, les prédictions les plus plausibles sont l'**arthrite juvénile idiopathique** (rang 8, niveau L3) et ses sous-types, qui prolongent l'usage connu des AMM dans les arthropathies inflammatoires. Elles relèvent toutefois davantage d'une extension de l'usage de la classe des AMM que d'un repositionnement véritablement nouveau.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le syndrome brachydactylie-syndactylie.

À titre indicatif, pour l'arthrite juvénile idiopathique (prédiction alternative de rang 8), les publications les plus pertinentes sont :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | ECR | S Afr Med J | Comparaison en double aveugle croisée kétoprofène vs indométacine chez 30 enfants atteints d'arthrite chronique juvénile : les deux sûrs et efficaces, l'indométacine étant le produit préféré |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Revue | Br J Rheumatol | Usage des AINS en rhumatologie pédiatrique ; salicylates et indométacine pas plus efficaces mais plus toxiques que d'autres AINS |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Revue | Drugs | Prise en charge pharmacologique de l'arthrite rhumatoïde juvénile, dont les AINS (indométacine incluse) |
| [19078081](https://pubmed.ncbi.nlm.nih.gov/19078081/) | 1996 | Enquête/Revue | J Clin Rheumatol | Enquête auprès de rhumatologues pédiatres : indométacine utilisée chez 11 % des patients |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Revue | Clin Pharmacokinet | Pharmacocinétique des médicaments utilisés dans l'arthrite juvénile |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60921824 | INDOCOLLYRE 0,1 %, collyre en solution (active) | Collyre en solution | Non renseignée |
| 68142440 | INDOCID 100 mg, suppositoire (active) | Suppositoire | Non renseignée |
| 61914124 | INDOCOLLYRE 0,1 %, collyre unidose (active) | Collyre en solution | Non renseignée |
| 66664685 | INDOCID 25 mg, gélule (active) | Gélule | Non renseignée |
| 69829455 | CHRONO-INDOCID 75 mg, gélule (active) | Gélule | Non renseignée |

Une sixième AMM (69668450, INDOBIOTIC, collyre unidose) est également annulée.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, épilepsie, ulcère gastrique et duodénal, ulcère peptique actif, maladie rénale, maladie hépatique, thrombopénie, troubles de la coagulation, asthme, infarctus du myocarde et maladies cardiovasculaires, maladies inflammatoires de l'intestin (dont la rectocolite hémorragique), entérocolite nécrosante, hémorragie intracérébrale, troubles anxieux et dysthymiques, maladie de la vésicule biliaire, hémoglobinopathies.
- **Interactions médicamenteuses** : 252 interactions recensées. Parmi les principales, de niveau modéré : acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), metformine, glimépiride, chlorpropamide, aprépitant, mésalazine, balsalazide, sels de potassium et préparations de lavage colique. De niveau mineur : famotidine, ranitidine, cimétidine, linaclotide.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (syndrome brachydactylie-syndactylie) n'a ni essai, ni publication, ni lien mécanistique plausible : elle relève très probablement d'un artefact du modèle (niveau L5).
- L'arthrite juvénile idiopathique (niveau L3) est la piste la plus crédible, mais elle prolonge un usage ancien des AINS, désormais supplanté par les traitements de fond et les biothérapies.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Un lien biologique plausible entre l'inhibition des COX et la physiopathologie du syndrome ciblé, avant toute étude précliniques
- Si la piste de l'arthrite juvénile est retenue : une revue comparative avec les traitements actuels, et une clarification du statut réglementaire (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

