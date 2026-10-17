---
layout: default
title: Insulin Lispro
parent: Prédiction du modèle uniquement (L5)
nav_order: 404
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Insulin Lispro : nouvelle indication prédite, Ovarite auto-immune (niveau de preuve L5). Indication d'origine : Diabète de type 2"
monitor_inn: "insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Insuline lispro : Du diabète de type 1 et 2 à la polyendocrinopathie auto-immune (ovarite auto-immune)

## Résumé en Une Phrase

L'insuline lispro est un analogue de l'insuline à action rapide, initialement utilisé pour le traitement du diabète de type 1 et de type 2 ainsi que de l'acidocétose diabétique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**ovarite auto-immune**, mais cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2 (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances TxGNN) |
| Nouvelle Indication Prédite | Ovarite auto-immune |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'insuline lispro est un analogue de l'insuline humaine. Son efficacité dans le diabète est établie : elle remplace ou complète l'insuline endogène pour contrôler la glycémie.

Le lien avec l'ovarite auto-immune est probablement indirect. Cette maladie coexiste souvent avec les syndromes polyendocriniens auto-immuns, dont fait partie le diabète de type 1. L'association du graphe de connaissances reflète donc plus vraisemblablement une **co-occurrence de maladies** qu'un effet thérapeutique. On ne s'attend pas à ce que l'insuline traite le processus auto-immun ovarien lui-même.

**Autres prédictions du modèle (toutes de niveau L5, sauf mention contraire, décision Hold) :**

| Maladie prédite | Score TxGNN | Interprétation |
|------|------|------|
| Syndrome de dysfonctionnement répondant à la thiamine | 99,37 % | Prise en charge symptomatique du diabète associé ; le traitement principal est la thiamine |
| Syndrome de l'homme raide classique | 99,36 % | Probable comorbidité avec le diabète de type 1 (auto-immunité anti-GAD65) |
| Syndrome du membre raide focal | 99,36 % | Même explication que ci-dessus |
| Opsismodysplasie | 99,34 % | Lien hypothétique via INPPL1 (SHIP2), régulateur de la voie insuline/PI3K |
| Lipodystrophie localisée d'origine médicamenteuse | 99,09 % | Probable effet indésirable connu des injections d'insuline, donc probable faux positif |
| Agénésie pancréatique | 99,09 % | Substitution hormonale rationnelle (niveau L4), mais ce n'est pas un vrai repositionnement |
| Lipodystrophie centrifuge | 99,04 % | Aucun mécanisme clair |
| Lipoatrophie localisée induite par la pression | 99,03 % | Non étayée ; l'insuline est aussi associée à la lipoatrophie au site d'injection |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'ovarite auto-immune.

Pour information, une seule publication a été identifiée pour une autre prédiction (agénésie pancréatique) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Revue | J Am Pharm Assoc | Revue générale de l'insulinothérapie dans le diabète de type 2 et de sa mise en place pratique ; preuve indirecte uniquement |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 69727429 | LYUMJEV 100 unités/mL, solution injectable en flacon | Solution injectable | Non renseignée | Annulée |
| 66817088 | LYUMJEV 100 unités/mL, solution injectable en cartouche | Solution injectable | Non renseignée | Annulée |
| 66537912 | HUMALOG 100 unités/ml JUNIOR KWIKPEN, stylo prérempli | Solution injectable | Non renseignée | Annulée |
| 67759549 | HUMALOG 200 UI/ml KWIKPEN, stylo prérempli | Solution injectable | Non renseignée | Annulée |
| 62000441 | LYUMJEV 100 unités/mL, Junior KwikPen, stylo prérempli | Solution injectable | Non renseignée | Annulée |

Une sixième AMM (66599764, LYUMJEV 200 unités/mL KwikPen) est également annulée. Les six AMM sont détenues par ELI LILLY NEDERLAND BV.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 352 interactions sont recensées. Celles affichées dans les données compilées sont surtout de niveau modéré :
  - Agents hyperglycémiants ou antagonisant l'effet de l'insuline : corticoïdes (hydrocortisone), œstrogènes et progestatifs (estradiol, éthinylestradiol, lévonorgestrel), diurétiques thiazidiques (hydrochlorothiazide), acétazolamide
  - Sympathomimétiques et bêta-agonistes : épinéphrine, phényléphrine, pseudoéphédrine, salbutamol, formotérol
  - Autres antidiabétiques (risque d'effet additif et d'hypoglycémie) : metformine, alogliptine, albiglutide
  - Autres : acébutolol (bêtabloquant pouvant masquer les signes d'hypoglycémie), doxycycline, alpélisib, éthanol
  - Les corticoïdes topiques (hydrocortisone, alclométasone) sont de niveau mineur.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les prédictions reposent uniquement sur le modèle (niveau L5) : aucun essai clinique ni publication ne les soutient. Elles reflètent surtout des comorbidités avec le diabète ou des effets indésirables connus (lipodystrophie), et non un effet thérapeutique.
- Toutes les AMM françaises sont annulées, et les données de sécurité de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Téléchargement et analyse des notices ANSM (mises en garde, contre-indications)
- Données sur le mécanisme d'action issues de DrugBank
- Recherche ciblée de littérature et d'essais pour l'ovarite auto-immune, en vérifiant si le signal vient d'une simple comorbidité
- Pour l'agénésie pancréatique, des données spécifiques à l'insuline lispro (cette indication relève d'une substitution hormonale et non d'un repositionnement)
- Vérification de la situation réglementaire actuelle (raisons de l'annulation des AMM) et de la compatibilité de voie d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

