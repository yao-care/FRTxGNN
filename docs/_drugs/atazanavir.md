---
layout: default
title: Atazanavir
parent: Prédiction du modèle uniquement (L5)
nav_order: 76
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Atazanavir : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (niveau de preuve L5). Indication d'origine : Infection par le VIH, SIDA"
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Atazanavir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Atazanavir : Du VIH/SIDA au Syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

Atazanavir est un inhibiteur de protéase du VIH, initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline** (score de 99,98 %), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.
Les données compilées pour ce rapport ne contiennent que des éléments indirects sur d'autres indications prédites (modèle du macaque SIV, grossesse chez les femmes infectées par le VIH).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (le texte de l'indication des AMM n'est pas renseigné ; source : indications du graphe de connaissances TxGNN) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'atazanavir fait partie de la classe des inhibiteurs de protéase du VIH ; son efficacité dans l'infection par le VIH est établie, et mécanistiquement il pourrait être applicable à d'autres lentivirus.

Le virus de l'immunodéficience féline (FIV) est un lentivirus dont la protéase est apparentée à celle du VIH-1. Un inhibiteur de protéase tel que l'atazanavir pourrait donc plausiblement agir sur lui. Le score élevé du modèle reflète probablement cette similarité avec le VIH.

Cette hypothèse reste une simple prédiction : aucun essai ni publication n'a été fourni, et la pertinence vétérinaire ainsi que la faisabilité ne sont pas évaluées. Le syndrome d'immunodéficience acquise féline est une maladie vétérinaire, et non une indication humaine.

**Autres indications prédites (pour information) :**

| Rang | Indication | Score | Niveau | Remarque |
|---|---|---|---|---|
| 2 | Infection par le virus de l'immunodéficience simienne | 99,98 % | L4 | Une seule étude préclinique chez le macaque (multithérapie), qui n'isole pas l'effet de l'atazanavir |
| 3 | Trouble neurodéveloppemental avec ataxie, absence de parole et diminution de la substance blanche corticale | 99,98 % | L5 | Aucun lien mécanistique plausible, probable artefact du graphe de connaissances |
| 4 | Hyperlipidémie familiale combinée (terme obsolète) | 99,82 % | L5 | Les inhibiteurs de protéase altèrent plutôt le profil lipidique ; bénéfice improbable |
| 5 | Complexe lié au SIDA | 99,71 % | L4 | Reformulation de l'usage existant, et non un véritable repositionnement |
| 6 | VIH congénital | 99,71 % | L3 | Extension de l'usage approuvé (grossesse, prévention de la transmission verticale) ; données observationnelles |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication principale (syndrome d'immunodéficience acquise féline).

À titre indicatif, les publications liées aux autres indications prédites les plus pertinentes sont :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohorte / pharmacocinétique | Antiviral Therapy | Étude de l'exposition à l'atazanavir pendant la grossesse : efficace indépendamment de l'utilisation du ténofovir (VIH congénital) |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Étude préclinique (primate non humain) | The Journal of Infectious Diseases | Chez les macaques infectés par le SIV et traités par multithérapie antirétrovirale, réduction de la réplication virale et de l'inflammation dans le SNC, mais persistance de l'ADN viral |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohorte | JAMA Pediatrics | Anomalies congénitales et exposition in utero aux antirétroviraux chez les nourrissons exposés non infectés |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Pharmacovigilance cas/non-cas | Eur J Clin Pharmacol | Risque d'anomalies congénitales après exposition fœtale aux antirétroviraux (registre européen) |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohorte | Frontiers in Immunology | Étude PHACS SMARTT : sécurité de l'exposition in utero aux antirétroviraux |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohorte | J Acquir Immune Defic Syndr | Schémas antirétroviraux courants et incidence des affections neurologiques définissant le SIDA |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | Préclinique / in vitro | Reproductive Toxicology | Interactions de l'atazanavir et du ritonavir avec les transporteurs ABCB1, ABCG2 et ABCC2 : effet sur la disposition transplacentaire chez le rat |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | Préclinique / in vitro | Antimicrob Agents Chemother | Nouveaux inhibiteurs de protéase fluorés ciblant le SNC, actifs contre le VIH-1 résistant (ne concerne pas l'atazanavir) |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohorte (sécurité) | AIDS Reviews | Facteurs de risque d'événements indésirables gastro-intestinaux chez les patients VIH traités ou non |

Ces études sont indirectes : aucun essai randomisé n'est disponible et aucune ne teste l'atazanavir dans une nouvelle indication. L'étude 31595301 (dolutégravir) et l'étude 28459118 (dépistage auditif) ont été écartées car peu pertinentes.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69443966 | REYATAZ 150 mg, gélule | Gélule | Non renseignée (AMM annulée) |
| 68301348 | REYATAZ 200 mg, gélule | Gélule | Non renseignée (AMM annulée) |
| 66745660 | REYATAZ 300 mg, gélule | Gélule | Non renseignée (AMM annulée) |

Les trois AMM, détenues par Bristol-Myers Squibb Pharma (Irlande), sont annulées : aucune AMM valide n'est actuellement recensée.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie TxGNN, et non texte de la notice) : insuffisance hépatique, maladie du foie, maladie de la vésicule biliaire, hyperglycémie, diabète, acidocétose diabétique, hépatite C chronique ou non, hépatite B chronique, hémophilie, hyperbilirubinémie (dont hyperbilirubinémie héréditaire et syndrome de Gilbert), néphrolithiase, néphropathie urique aiguë, bloc auriculo-ventriculaire, acidose lactique.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - *Majeures* : famotidine, ranitidine, rabéprazole, oméprazole (réduction de l'absorption de l'atazanavir par l'élévation du pH gastrique), lopéramide, triamcinolone, budésonide.
  - *Modérées* : acarbose, hydrocortisone, albiglutide, alogliptine, metformine, pioglitazone, alosétron, aprépitant, acétohexamide, hydroxyde d'aluminium, bétaméthasone, budésonide nasal, carbonate de calcium.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (VIH félin) repose uniquement sur le modèle (niveau L5), sans essai ni publication, et concerne une indication vétérinaire. Le lien mécanistique est plausible mais non démontré.
- La seule piste proche d'un usage humain (VIH congénital, niveau L3) prolonge l'indication VIH existante et ne constitue pas un nouveau domaine thérapeutique.
- Les AMM françaises sont toutes annulées et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (DrugBank)
- Mises en garde et contre-indications officielles issues de la notice ANSM
- Définition du cadre visé (vétérinaire ou humain) et évaluation de sa faisabilité
- Études précliniques ou in vitro de l'atazanavir sur la protéase du FIV
- Pour le VIH congénital : revue ciblée des données de sécurité et de pharmacocinétique de l'atazanavir pendant la grossesse
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

