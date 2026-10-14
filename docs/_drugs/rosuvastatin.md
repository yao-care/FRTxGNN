---
layout: default
title: Rosuvastatin
parent: Preuves élevées (L1-L2)
nav_order: 681
evidence_level: L1
indication_count: 10
---

# Rosuvastatin
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Rosuvastatine : Des Dyslipidémies et de l'Athérosclérose à l'Hypercholestérolémie Familiale

## Résumé en Une Phrase

La rosuvastatine est une statine, initialement utilisée pour traiter les dyslipidémies (hypertriglycéridémie, hyperlipoprotéinémie, hypercholestérolémie familiale homozygote) et pour prévenir les complications athéroscléreuses, dont l'accident vasculaire cérébral.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypercholestérolémie familiale** (classée en 2e position des prédictions), avec **12 essais cliniques** et **12 publications** recensés dans les données compilées pour ce report.
Il s'agit toutefois d'une indication très proche de l'indication d'origine : l'évaluation relève davantage de la confirmation que d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertriglycéridémie, hyperlipoprotéinémie, hypercholestérolémie familiale homozygote, athérosclérose, accident vasculaire cérébral (source : graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

> **Remarque** : la première prédiction du classement (déficit en protéine de transfert des esters de cholestérol, score 99,54 %) ne repose sur aucun essai ni publication (niveau L5, Hold). L'hypercholestérolémie familiale, deuxième du classement avec un score quasi identique, est retenue ici car c'est la première prédiction réellement documentée.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, la rosuvastatine fait partie de la classe des statines (inhibiteurs de l'HMG-CoA réductase). En bloquant la synthèse hépatique du cholestérol, elle augmente l'expression des récepteurs hépatiques des LDL et abaisse le LDL-cholestérol.

L'hypercholestérolémie familiale résulte le plus souvent d'un déficit fonctionnel du récepteur des LDL. Le mécanisme de la statine est donc directement pertinent. La forme homozygote figure déjà parmi les indications d'origine du médicament, ce qui explique le score très élevé du modèle.

Cette prédiction est donc plausible, mais elle est surtout proche d'une indication déjà établie. Pour la forme hétérozygote et pour les enfants, les essais disponibles apportent des preuves directes.

---

## Preuves d'Essais Cliniques

Sélection des essais les plus pertinents pour l'hypercholestérolémie familiale (13 essais recensés, dont 10 présentés ici) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | Terminé | 20 | Étude croisée randomisée en double aveugle contre placebo de la rosuvastatine chez l'enfant et l'adolescent (6 à <18 ans) atteints d'HF homozygote |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | Terminé | 9 | Extension ouverte à long terme évaluant la sécurité chez l'enfant atteint d'HF homozygote ; effectif très limité |
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | Terminé | 315 | Étude ouverte de 2 ans sur l'efficacité et la sécurité de la rosuvastatine chez l'enfant et l'adolescent atteints d'HF |
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3b | Terminé | 173 | Étude de 12 semaines en double aveugle contre placebo, puis 40 semaines ouvertes, chez des enfants de 10 à 17 ans atteints d'HF hétérozygote |
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3b | Terminé | 1500 | Étude ouverte non comparative de 48 semaines dans les dyslipidémies de type IIa/IIb, y compris l'HF hétérozygote |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3b | Terminé | 442 | Étude randomisée ouverte de 6 semaines comparant les effets rénaux de la rosuvastatine et de la simvastatine |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Terminé | 249 | Alirocumab versus placebo dans l'HF hétérozygote insuffisamment contrôlée sous traitement hypolipémiant (la rosuvastatine n'est pas le produit étudié) |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Terminé | 153 | Alirocumab chez l'enfant atteint d'HF hétérozygote, sous statine stable ; rôle exact de la rosuvastatine non précisé |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | Terminé | 135 | Sécurité à long terme de l'association ézétimibe + rosuvastatine chez des patients japonais hypercholestérolémiques |
| [NCT07474649](https://clinicaltrials.gov/study/NCT07474649) | Phase 3 | Pas encore en recrutement | 103 | Triple association acide bempédoïque/ézétimibe/statine de forte intensité ; la rosuvastatine est un traitement de fond, sans résultats |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | ECR | J Am Coll Cardiol | Efficacité et sécurité de la rosuvastatine chez l'enfant atteint d'HF |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohorte | J Am Coll Cardiol | Efficacité de la rosuvastatine chez l'enfant atteint d'HF homozygote et lien avec les mutations génétiques sous-jacentes |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Recommandations | Endocr Pract | Recommandations AACE/ACE pour la prise en charge des dyslipidémies et la prévention cardiovasculaire |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Revue | Drugs | Profil de la rosuvastatine : supériorité sur l'atorvastatine, la simvastatine et la pravastatine sur le profil lipidique, faible propension aux interactions |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Revue | Clin Ther | Place de la rosuvastatine dans la prise en charge de l'hyperlipidémie, y compris l'HF homozygote |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | Modélisation pharmacocinétique | Eur J Clin Pharmacol | Pharmacocinétique de population de la rosuvastatine chez l'enfant atteint d'HF hétérozygote |
| [36928267](https://pubmed.ncbi.nlm.nih.gov/36928267/) | 2023 | Données en vie réelle | J Atheroscler Thromb | Taux d'atteinte des cibles de LDL-C chez des patients à haut risque au Japon |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Étude mécanistique | Toxicology | Myotoxicité des statines lipophiles et hydrophiles sur des cellules musculaires dérivées de patients atteints d'HF |
| [20531065](https://pubmed.ncbi.nlm.nih.gov/20531065/) | 2010 | Rapport de cas | South Med J | Thrombopénie sévère induite par la rosuvastatine (complication rare) |
| [42137960](https://pubmed.ncbi.nlm.nih.gov/42137960/) | 2026 | Essai de phase 1 | Circulation | Laroprovstat, inhibiteur oral de PCSK9 (autre molécule, contexte thérapeutique) |

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Les 5 premières sont présentées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 61543911 | ROSUVASTATINE BGR 20 mg | Comprimé pelliculé | Annulée |
| 64675900 | ROSUVASTATINE CRISTERS 10 mg | Comprimé pelliculé | Annulée |
| 61062358 | ROSUVASTATINE EVOLUGEN 20 mg | Comprimé pelliculé | Annulée |
| 65148032 | ROSUVASTATINE CRISTERS 20 mg | Comprimé pelliculé | Annulée |
| 65227063 | ROSUVASTATINE EG 10 mg | Comprimé pelliculé | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie du foie, maladie de la vésicule biliaire, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), myopathie et maladies musculaires, paralysie périodique familiale, abus de substances/dépendance, rhabdomyolyse, fasciite nodulaire, traumatisme, protéinurie.
- **Interactions médicamenteuses** : 524 interactions recensées. Parmi celles présentées :
  - **Majeures** : fénofibrate, atazanavir.
  - **Modérées** : amiodarone, atorvastatine, ézétimibe, acide bempédoïque, paclitaxel, alpélisib, apalutamide, éthanol, zidovudine, adalimumab, auranofine, entre autres.
  - **Mineures** : lévonorgestrel, noréthistérone, désogestrel.
- **Signal de sécurité rapporté dans la littérature** : un cas de thrombopénie sévère sous rosuvastatine (PMID 20531065).

Les mises en garde et contre-indications issues de la notice de l'ANSM ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés (dont des essais randomisés contre placebo chez l'enfant) et un essai randomisé publié soutiennent l'efficacité et la tolérance de la rosuvastatine dans l'hypercholestérolémie familiale. Le niveau de preuve est L1.
- L'indication est quasi identique à l'indication d'origine : il s'agit d'une confirmation plus que d'un repositionnement. Les autres prédictions à fort score sans preuve (déficit en CETP, déficit en lipase hépatique, amylose ABri, trouble neurodéveloppemental rare) restent en « Hold ».

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de sécurité de la notice ANSM (mises en garde, contre-indications), actuellement manquantes et bloquantes pour le criblage de sécurité.
- Les données détaillées sur le mécanisme d'action.
- La vérification de la disponibilité réelle des produits, les 20 AMM étant toutes annulées.
- Un plan de surveillance : CPK, transaminases, fonction rénale, gestion des interactions (notamment fénofibrate et atazanavir), et posologie adaptée à l'enfant.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

