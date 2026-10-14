---
layout: default
title: Pyrazinamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide : De la tuberculose pulmonaire à l'otite moyenne infectieuse

## Résumé en Une Phrase

Pyrazinamide est un antituberculeux de première ligne, utilisé à l'origine dans le traitement de la tuberculose pulmonaire et des tuberculoses méningées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**otite moyenne infectieuse**, mais **aucun essai clinique** ni **aucune publication** ne soutient directement cette prédiction. Les 3 publications trouvées pour des indications voisines (oreille moyenne, otite chronique) sont des cas cliniques de tuberculose de l'oreille.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tuberculose pulmonaire (les textes d'indication des AMM françaises ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Otite moyenne infectieuse |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le pyrazinamide fait partie des schémas antituberculeux multimédicamenteux. Il est actif contre *Mycobacterium tuberculosis* : son efficacité repose sur un pH acide et sur sa conversion en acide pyrazinoïque par la pyrazinamidase mycobactérienne.

Le lien avec l'otite moyenne est donc **limité** : il n'existe que pour la forme tuberculeuse, rare. Le pyrazinamide n'est pas actif contre les agents habituels de l'otite moyenne (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*). Le score élevé du modèle semble refléter la proximité, dans le graphe de connaissances, entre la tuberculose et les maladies de l'oreille, plutôt qu'un mécanisme démontré.

Les autres prédictions du même groupe sont soit une extension de l'indication d'origine à un autre site anatomique (tuberculose de l'oreille moyenne ou otite tuberculeuse chronique), soit dépourvues de justification plausible (granulome cholestérolique, otite allergique, otite non suppurée).

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature n'est disponible pour l'otite moyenne infectieuse. Les publications ci-dessous concernent des indications voisines (oreille moyenne, otite chronique et suppurée), toutes classées comme preuves de faible niveau.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Cas clinique | Int J Mycobacteriol | Tuberculose nasale et de l'oreille moyenne chez une femme de 55 ans, traitée 9 mois par rifampicine, isoniazide et pyrazinamide ; pas de récidive après un an |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Cas clinique | Am J Kidney Dis | Otite moyenne tuberculeuse chez un greffé rénal, après otites chroniques traitées plusieurs fois par antibiothérapie empirique |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Cas clinique | Cureus | Otite moyenne tuberculeuse à présentation insidieuse, diagnostic retardé dans une région à faible prévalence |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Observation clinique | Laryngo-Rhino-Otologie | 12 patients avec tuberculose de la tête et du cou, dont un cas d'atteinte de l'oreille moyenne |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Étude animale | J Am Assoc Lab Anim Sci | Torticolis chez des souris infectées par *M. tuberculosis*, y compris sous traitements associant pyrazinamide (lien indirect) |

Remarque : les publications sur la sacro-iliite et la tuberculose orbito-faciale, également retrouvées, sont hors sujet et n'ont pas été retenues.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66454982 | PIRILENE 500 mg, comprimé (AMM annulée) | Comprimé | Non renseignée |
| 64208131 | RIFATER, comprimé enrobé (AMM annulée) | Comprimé enrobé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications ou maladies à risque (graphe de connaissances, hors notice)** : insuffisance hépatique (y compris aiguë), maladie du foie, hépatite, porphyries (héréditaire, troubles du métabolisme des porphyrines), maladie de la vésicule biliaire, diabète et acidocétose diabétique, goutte, neuropathie périphérique et maladies du système nerveux périphérique, abus ou dépendance à une substance, acétylation lente.
- **Interactions médicamenteuses** : 56 interactions recensées. Les deux de niveau modéré sont l'acide picosulfurique et la naltrexone. Parmi les autres, de niveau non précisé : pantoprazole, oméprazole, lansoprazole, ranitidine, famotidine, prednisone, prednisolone, vancomycine, amphotéricine B, métronidazole, glibenclamide, amoxicilline, streptomycine, acide acétylsalicylique, sulfasalazine, mésalazine, morphine et chlorure de potassium.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) pour l'otite moyenne infectieuse : aucun essai, aucune littérature, et un mécanisme non applicable aux pathogènes habituels. Les seules données concernent des cas de tuberculose de l'oreille, où le pyrazinamide fait déjà partie du traitement standard, ce qui ne constitue pas une nouvelle indication.
- Le médicament n'a plus d'AMM valide en France (2 AMM annulées), et les données de sécurité de la notice sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de sécurité de la notice (mises en garde, contre-indications) auprès de l'ANSM, indispensables avant tout examen de sécurité
- Les données détaillées sur le mécanisme d'action
- Si la piste est poursuivie, la restreindre à l'otite moyenne tuberculeuse confirmée, avec une revue systématique des cas publiés
- Une évaluation du statut réglementaire, puisque toutes les AMM françaises sont annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

