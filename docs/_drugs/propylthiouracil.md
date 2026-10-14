---
layout: default
title: Propylthiouracil
parent: Preuves modérées (L3-L4)
nav_order: 638
evidence_level: L4
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Propylthiouracile : De l'hyperthyroïdie à la résistance aux hormones thyroïdiennes (mutation du récepteur bêta)

## Résumé en Une Phrase

Le propylthiouracile (PTU) est un antithyroïdien de synthèse, initialement utilisé dans l'hyperthyroïdie, la maladie de Basedow, la thyrotoxicose et la crise thyrotoxique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **résistance aux hormones thyroïdiennes due à une mutation du récepteur bêta**, mais **aucun essai clinique** n'est enregistré et la littérature disponible (**4 publications**) se limite à des modèles murins et à des cas cliniques, sans évaluation du PTU comme traitement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperthyroïdie, maladie de Basedow, thyrotoxicose, crise thyrotoxique (le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Résistance aux hormones thyroïdiennes due à une mutation du récepteur bêta des hormones thyroïdiennes |
| Score de Prédiction TxGNN | 99,66 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances pharmacologiques générales, le PTU inhibe la thyroperoxydase, ce qui réduit la synthèse des hormones thyroïdiennes, et freine aussi la conversion périphérique de la T4 en T3.

Dans la résistance aux hormones thyroïdiennes de type bêta, des mutations du gène THRB rendent les tissus peu sensibles aux hormones, avec une élévation compensatoire de la TSH, de la T4 et de la T3. Le lien mécanistique est donc **faible, voire potentiellement délétère** : abaisser les hormones peut augmenter encore la TSH, favoriser un goitre et induire une hypothyroïdie tissulaire.

Le score très élevé du modèle reflète probablement une proximité dans le graphe de connaissances (gènes et phénotypes thyroïdiens communs) plutôt qu'un bénéfice thérapeutique réel. Cette prédiction doit être interprétée avec prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Préclinique (modèle murin) | Endocrinology | Rôle de la TSH dans le développement spontané de carcinome thyroïdien asymétrique chez des souris porteuses d'une mutation du récepteur bêta |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Préclinique (modèle murin) | Oncogene | Activation de la prolifération tumorale par l'hormone thyroïdienne dans un modèle murin de carcinome folliculaire |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Rapport de cas / étude familiale | Clinical Endocrinology | Thyrotoxicose néonatale et infertilité maternelle dans une résistance aux hormones thyroïdiennes (mutation M313T) |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Rapport de cas (génétique) | Endocrine Journal | Mutation de novo L330S chez une patiente thaïlandaise, préalablement traitée par PTU sur un diagnostic de thyrotoxicose ; le goitre s'est aggravé |

Aucune de ces publications n'évalue le PTU comme traitement de cette affection ; le cas de 1999 suggère même une aggravation du goitre sous PTU.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61397883 | PROPYLEX 50 mg, comprimé (AP-HP) | Comprimé | Non renseignée (AMM annulée) |

## Cytotoxicité

Le PTU n'est pas un médicament antinéoplasique ; cette section n'est pas applicable.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : thrombopénie, hypothyroïdie, myxœdème, hypothyroïdie congénitale, hyperbilirubinémie (dont formes héréditaires et syndrome de Gilbert), pneumopathie interstitielle, atteinte hépatique d'origine médicamenteuse, leucopénie, pancytopénie, agranulocytose et diverses formes de neutropénie (dont neutropénies congénitales sévères et idiopathique de l'adulte).
- **Interactions médicamenteuses** : 83 interactions recensées. Parmi les principales :
  - Majeure : défériprone
  - Modérées : naltrexone, iodure I-131, iodure I-123, macimoréline, warfarine, dicoumarol, théophylline, aminophylline, oxtriphylline
- Le profil du PTU comporte un risque connu d'atteinte hépatique grave, qui doit être pris en compte pour toute extension d'usage.

La notice officielle n'a pas pu être exploitée : veuillez la consulter pour les mises en garde et contre-indications réglementaires.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4 (modèles précliniques et cas isolés), sans essai clinique, et le mécanisme suggère un risque d'aggravation plutôt qu'un bénéfice dans cette affection.
- Le produit n'est plus commercialisé en France (AMM annulée) et le profil de sécurité (hépatotoxicité, atteintes hématologiques) est défavorable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Données détaillées sur le mécanisme d'action (DrugBank)
- Données cliniques montrant un bénéfice réel du PTU dans la résistance aux hormones thyroïdiennes (aucune actuellement)

---

### Note sur les autres prédictions

- **Thyrotoxicose néonatale** (score 99,40 %, niveau L4, « question de recherche ») : le mécanisme est cohérent avec l'indication d'origine, mais la littérature (revues et cohortes) porte sur l'usage maternel d'antithyroïdiens pendant la grossesse, soit une preuve indirecte. Aucun essai enregistré. Le PTU présente un avertissement d'hépatotoxicité sévère et, chez l'enfant, d'autres agents sont généralement préférés. Cela ne soutient pas un usage néonatal direct.
- **Hyperthyroxinémie** (score 99,08 %, niveau L5, Hold) : prédiction purement computationnelle, sans essai ni publication. Le libellé est non spécifique et recouvre des situations où réduire la T4 serait inapproprié ; l'indication devrait être redéfinie selon l'étiologie.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

