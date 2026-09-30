---
layout: default
title: Ciprofibrate
parent: Prédiction du modèle uniquement (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Ciprofibrate
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

# Ciprofibrate : Vers l'Hyperlipoprotéinémie (indication d'origine non renseignée)

## Résumé en Une Phrase

Le ciprofibrate est un fibrate hypolipémiant commercialisé en France, mais le dossier ne précise pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperlipoprotéinémie**,
avec **0 essai clinique enregistré** et **20 publications** soutenant actuellement cette direction.
Cette prédiction est en fait proche de l'usage connu du médicament : elle relève davantage de la confirmation que d'un repositionnement à proprement parler.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Hyperlipoprotéinémie |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L2 (selon le classement du dossier ; il repose sur des études anciennes, dont des essais comparatifs en double aveugle, et non sur un essai de phase 2/3 enregistré) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. Sur la base des informations connues, le ciprofibrate appartient à la classe des fibrates, agonistes de PPAR-alpha. Il augmente l'activité de la lipoprotéine lipase et réduit la synthèse hépatique des VLDL. Il abaisse ainsi les triglycérides et le cholestérol non-HDL, et élève le HDL-cholestérol.

Les publications rapportent aussi un déplacement vers des sous-fractions de LDL moins athérogènes. L'hyperlipoprotéinémie (types IIa, IIb et IV) correspond directement à ce mécanisme, ce qui rend la prédiction cohérente.

Il faut toutefois rester prudent. Le dossier ne renseigne aucune indication d'origine, ni dans DrugBank ni dans les AMM françaises. On ne peut donc pas évaluer la « distance » entre l'indication d'origine et la nouvelle indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6753860](https://pubmed.ncbi.nlm.nih.gov/6753860/) | 1982 | ECR en double aveugle contre placebo | Atherosclerosis | Hypercholestérolémie de type II : 50 ou 100 mg/j de ciprofibrate contre placebo pendant 12 semaines. Le traitement a été bien toléré (20 patients ayant terminé l'étude). |
| [3994783](https://pubmed.ncbi.nlm.nih.gov/3994783/) | 1985 | Essai comparatif en double aveugle | Atherosclerosis | Ciprofibrate 100 mg/j contre fénofibrate 300 mg/j sur 3 mois : baisse du cholestérol total, du LDL, du VLDL et de l'apoB, et hausse du HDL et de l'apoA. |
| [9015467](https://pubmed.ncbi.nlm.nih.gov/9015467/) | 1996 | Essai comparatif ouvert, multicentrique | Postgrad Med J | 174 patients avec hyperlipidémie de type II : ciprofibrate 100 mg/j contre bézafibrate LP 400 mg/j pendant 8 semaines (efficacité et sécurité comparées). |
| [2289217](https://pubmed.ncbi.nlm.nih.gov/2289217/) | 1990 | Étude clinique multicentrique | Clin Ther | 127 patients, 100 mg/j pendant 12 semaines : baisse significative du cholestérol total, du LDL, des VLDL, des triglycérides et de l'apoB, et hausse du HDL et de l'apoA-I. |
| [8831920](https://pubmed.ncbi.nlm.nih.gov/8831920/) | 1996 | Synthèse d'efficacité et de sécurité | Atherosclerosis | Efficace dans les types IIa, IIb et IV. À 100 mg/j chez environ 3 000 patients de type IIa, baisse du cholestérol total, des triglycérides, de l'apoB et du LDL. |
| [11048518](https://pubmed.ncbi.nlm.nih.gov/11048518/) | 2000 | Étude observationnelle multicentrique | Vnitrni Lekarstvi | 633 patients (23 centres, République tchèque), 3 mois : cholestérol −13 %, triglycérides −41 %, HDL +15 %. |
| [6951582](https://pubmed.ncbi.nlm.nih.gov/6951582/) | 1982 | Étude dose-réponse | Atherosclerosis | 50 patients (types IIA, IIB, IV) à 50, 100 et 200 mg/j : effet hypolipémiant maximal à 200 mg/j, sans effet indésirable subjectif. |
| [12915663](https://pubmed.ncbi.nlm.nih.gov/12915663/) | 2003 | Étude clinique mécanistique | J Clin Endocrinol Metab | 10 patients de type IIb : forte baisse des VLDL-1 (−40 %) et VLDL-2 (−25 %), et stimulation de l'efflux de cholestérol médié par le HDL. |
| [17414592](https://pubmed.ncbi.nlm.nih.gov/17414592/) | 2007 | Étude clinique | Am J Ther | Dyslipidémie de type IV : baisse du cholestérol non-HDL et des triglycérides, hausse du HDL. |
| [6421601](https://pubmed.ncbi.nlm.nih.gov/6421601/) | 1984 | Étude clinique (lipides biliaires) | Eur J Clin Invest | 19 patients traités 6 semaines à 100 mg/j : analyse des lipides sériques et biliaires, en lien avec le risque de lithiase des fibrates. |

## Informations de Marché en France

Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 66475325 | LIPANOR 100 mg, gélule | Gélule | SANOFI WINTHROP INDUSTRIE |
| 66866758 | CIPROFIBRATE BIOGARAN 100 mg, gélule | Gélule | BIOGARAN |
| 62938313 | CIPROFIBRATE ARROW 100 mg, gélule | Gélule | ARROW GENERIQUES |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs études cliniques, dont des essais comparatifs en double aveugle, montrent que le ciprofibrate améliore le profil lipidique, ce qui est cohérent avec son mécanisme de fibrate. En revanche, ces données sont anciennes et de taille modeste, aucun essai clinique n'est enregistré, et la notice de l'ANSM n'a pas encore été analysée, ce qui bloque l'examen de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), étape bloquante pour l'évaluation de sécurité
- Compléter les données sur le mécanisme d'action (par exemple via l'API DrugBank)
- Confirmer l'indication d'origine dans les AMM françaises, afin de savoir s'il s'agit d'un véritable repositionnement
- Rechercher des données récentes ou des critères cliniques forts (événements cardiovasculaires), et situer le ciprofibrate par rapport aux statines
- Prévoir un suivi de sécurité pour les populations particulières et les associations (statines, anticoagulants), en tenant compte du risque musculaire et biliaire des fibrates

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

