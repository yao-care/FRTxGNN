---
layout: default
title: Acitretin
parent: Preuves modérées (L3-L4)
nav_order: 23
evidence_level: L3
indication_count: 4
---

# Acitretin
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **4** 
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

# Acitrétine : De l'indication d'origine non renseignée à l'Acné (Disease)

## Resume en Une Phrase

L'acitrétine est un rétinoïde systémique de deuxième génération, commercialisé en France sous le nom de SORIATANE (gélules), dont le texte d'indication d'origine n'est pas disponible dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**acné**, avec **1 essai clinique** et **17 publications** associés à cette piste.
Ces preuves concernent toutefois surtout l'**hidradénite suppurée (acné inversée)**, et non l'acné vulgaire.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données d'AMM |
| Nouvelle Indication Predite | Acné (disease) |
| Score de Prediction TxGNN | 99,94 % |
| Niveau de Preuve | L3 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. Sur la base des informations connues, l'acitrétine est un rétinoïde systémique de deuxième génération (métabolite de l'étrétinate). Elle module la différenciation et la prolifération des kératinocytes et exerce un effet anti-inflammatoire via les récepteurs RAR/RXR. Sa principale réussite clinique documentée dans la littérature est le psoriasis.

L'acné repose notamment sur l'activité des glandes sébacées et l'hyperkératinisation folliculaire, deux processus sur lesquels les rétinoïdes agissent. Cela donne un fondement mécanistique plausible à la prédiction.

Il faut cependant nuancer : l'effet sébosuppresseur de l'acitrétine est plus faible que celui de l'isotrétinoïne. Les données soutiennent surtout son usage dans l'hidradénite suppurée (acné inversée) et dans certains cas d'acné réfractaire, plutôt que dans l'acné vulgaire. Le nœud « acné » de TxGNN semble recouvrir celui d'« acné inversée ».

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT07708480](https://clinicaltrials.gov/study/NCT07708480) | Phase 4 | Terminé | 70 | Aprémilast (30 mg 2 fois/jour) vs acitrétine (25 mg 2 fois/jour) pendant 12 semaines dans l'hidradénite suppurée modérée à sévère ; critère principal : score IHS4. Aucun résultat disponible ; l'acitrétine sert de comparateur. |

---

## Preuves de la Litterature

Sélection des publications les plus pertinentes parmi celles compilées (aucun ECR identifié).

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Recommandation | JEADV | Recommandations européennes S1 pour le traitement de l'hidradénite suppurée/acné inversée |
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Revue Cochrane | Cochrane Database Syst Rev | Médicaments du lupus érythémateux discoïde |
| [40888828](https://pubmed.ncbi.nlm.nih.gov/40888828/) | 2025 | Revue systématique | Am J Clin Dermatol | Différences ethniques dans la pustulose palmo-plantaire |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Série/étude clinique | Br J Dermatol | Résultats à long terme de l'acitrétine dans l'hidradénite suppurée |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Rapport de cas | Cutis | Acné nodulokystique et hidradénite suppurée traitées par acitrétine |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Revue | Hautarzt | Traitements médicamenteux de l'acné inversée (antibiotiques, anti-TNF-α) |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Revue | Clin Dermatol | Vitamine A et rétinoïdes en dermatologie |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Revue | Dermatology | Rétinoïdes et activité des glandes sébacées |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Revue | Drugs | Usage actuel et rôle potentiel des rétinoïdes en dermatologie |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Revue | Skin Pharmacol Appl Skin Physiol | Indications dermatologiques futures des rétinoïdes |

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 64225999 | SORIATANE 25 mg, gélule (annulée) | Gélule | Non renseignée |
| 60292349 | SORIATANE 10 mg, gélule (annulée) | Gélule | Non renseignée |

---

## Cytotoxicite

Cette section est omise : l'acitrétine est un rétinoïde, et non un médicament antinéoplasique.

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de la notice) : insuffisance hépatique, lésion hépatique d'origine médicamenteuse, pancréatite, diabète, acidocétose diabétique, hypertriglycéridémie, obésité (dont obésité monogénique), hypoalphalipoprotéinémie, troubles anxieux, troubles névrotiques, trouble dysthymique, abus/dépendance aux substances, pseudotumeur cérébrale, hypertension intracrânienne, troubles de la vision, cécité, héméralopie (dont cécité nocturne congénitale stationnaire et maladie d'Oguchi) et hyperostose.
- **Interactions médicamenteuses** (113 interactions recensées) :
  - Majeures : doxycycline, minocycline, tétracycline, vitamine A.
  - Modérées : sulfamides hypoglycémiants (acétohexamide, chlorpropamide, glimépiride, glipizide, glibenclamide, tolazamide, tolbutamide) et naltrexone.
  - Niveau non précisé (extrait) : pantoprazole, oméprazole, lansoprazole, simvastatine, rosuvastatine, morphine, vancomycine, triamcinolone.
- **Points d'attention issus des données** : l'acitrétine est un puissant tératogène, absolument contre-indiqué pendant la grossesse. Une toxicité osseuse est également décrite (fermeture épiphysaire prématurée chez l'enfant en cas d'usage prolongé).

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Le niveau de preuve est L3, fondé sur un seul essai de phase 4 comparant l'acitrétine à un autre traitement dans l'hidradénite suppurée (sans résultats disponibles) et sur des revues ou rapports de cas. Aucune preuve directe ne concerne l'acné vulgaire.
- Le profil de sécurité est lourd (tératogénicité, toxicité hépatique, osseuse et lipidique), les AMM françaises sont toutes annulées, et la notice n'a pas pu être exploitée, ce qui bloque le passage à l'étape de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir et analyser la notice ANSM (mises en garde, contre-indications), élément bloquant.
- Compléter les données sur le mécanisme d'action, par exemple via DrugBank.
- Obtenir les résultats de l'essai NCT07708480 et rechercher des ECR spécifiques à l'acné vulgaire ou à l'hidradénite suppurée.
- Préciser s'il faut cibler l'acné vulgaire ou l'hidradénite suppurée, puisque le nœud TxGNN recouvre les deux.
- Définir un programme de prévention de la grossesse et un plan de surveillance (bilans hépatique et lipidique) avant toute évaluation clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

