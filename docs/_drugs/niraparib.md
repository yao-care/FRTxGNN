---
layout: default
title: Niraparib
parent: Prédiction du modèle uniquement (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Niraparib : nouvelle indication prédite, Néoplasme de l'épiglotte (niveau de preuve L5). Indication d'origine : Carcinome épithélial malin de l'ovaire et cancers du péritoine"
monitor_inn: "niraparib"
predicted_indications: ["epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of hypopharynx", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "tumor of testis and paratestis", "inner ear neoplasm", "pre-malignant neoplasm", "schwannoma of jugular foramen"]
---

# Niraparib
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

# Niraparib : Du Cancer Épithélial de l'Ovaire et du Péritoine au Néoplasme de l'Épiglotte

## Résumé en Une Phrase

Le niraparib est un inhibiteur de PARP, utilisé à l'origine dans les cancers de l'ovaire et du péritoine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **néoplasme de l'épiglotte**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome épithélial malin de l'ovaire et cancers du péritoine (d'après le graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Néoplasme de l'épiglotte |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 3 (aucune valide) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le niraparib appartient à la classe des inhibiteurs de PARP1/2. Ces médicaments exploitent la « létalité synthétique » : les cellules tumorales dont la réparation de l'ADN par recombinaison homologue est déficiente ne survivent pas lorsque PARP est bloquée.

Les indications d'origine (cancer de l'ovaire, carcinome péritonéal primitif, tumeur desmoplastique à petites cellules rondes) sont des tumeurs pour lesquelles cette vulnérabilité est bien décrite. Le passage vers une tumeur de l'épiglotte reposerait sur l'hypothèse que certaines tumeurs de la tête et du cou présenteraient aussi un déficit de réparation de l'ADN.

Cette hypothèse reste plausible mais non validée. Les données compilées ne documentent rien sur les tumeurs des muqueuses de la tête et du cou. Le score élevé du modèle ne remplace donc pas une preuve réelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les trois AMM sont annulées. Le texte d'indication approuvée n'est pas renseigné pour ces autorisations.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61096104 | ZEJULA 100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 67707919 | ZEJULA 100 mg, gélule | Gélule | Non renseignée |
| 69324990 | AKEEGA 100 mg/500 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de PARP) |
| Risque de Myélosuppression | Non documenté dans les données compilées. Les cytopénies (thrombopénie, anémie, neutropénie) sont un effet connu de la classe : veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS (numération formule sanguine) en priorité ; fonctions hépatique et rénale selon la notice |
| Protection de Manipulation | Veuillez consulter la notice pour les précautions de manipulation |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 351 interactions sont recensées. Parmi celles listées, les plus importantes sont :
  - **Majeures** : déféprone, lexidronam de samarium (¹⁵³Sm).
  - **Modérées** :
    - antithrombotiques et anticoagulants : acide acétylsalicylique, abciximab, alteplase, antithrombine III, apixaban, dipyridamole, bétrixaban, bivalirudine, cangrelor, caplacizumab, cilostazol ;
    - radiopharmaceutiques et anticorps radiomarqués : iobenguane (I-131), ibritumomab tiuxétan, tositumomab (avec ou sans I-131), chlorure de strontium Sr-89 ;
    - autres : rolapitant, palifermine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le néoplasme de l'épiglotte repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ni mécanisme documenté.
- Les AMM françaises sont toutes annulées.
- Les mises en garde et contre-indications de la notice ne sont pas disponibles : le dépistage de sécurité ne peut donc pas être mené.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Mener une revue ciblée de la littérature sur les inhibiteurs de PARP dans les cancers de la tête et du cou, avec recherche de biomarqueurs de déficience de réparation de l'ADN (HRD).
- Clarifier la situation réglementaire : les AMM sont annulées.

**Remarque :** parmi les autres prédictions, la « tumeur kystique » (2ᵉ rang, niveau L2) dispose de données plus solides. Elle est soutenue par un essai de phase 2 en recrutement (NCT04716686, niraparib en monothérapie dans le carcinome séreux de l'endomètre). Il s'agit toutefois surtout d'une extension des indications ovariennes existantes plutôt que d'une indication réellement nouvelle. Elle pourrait être évaluée séparément.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

