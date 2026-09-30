---
layout: default
title: Quinapril
parent: Prédiction du modèle uniquement (L5)
nav_order: 255
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Quinapril : D'un inhibiteur de l'ECA (indication originale non renseignée) à l'hypertension rénovasculaire maligne

## Résumé en une phrase

Le quinapril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC). Les données fournies ne précisent pas son indication originale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données réglementaires fournies |
| Nouvelle indication prédite | Hypertension rénovasculaire maligne |
| Score de prédiction TxGNN | 99,86 % |
| Niveau de preuve | L5 |
| Statut de marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le quinapril appartient à la classe des inhibiteurs de l'ECA. Il agit sur le système rénine-angiotensine et pourrait, mécanistiquement, être applicable à l'hypertension rénovasculaire.

L'hypertension rénovasculaire est en grande partie due à l'activation du système rénine-angiotensine, généralement en aval d'une sténose de l'artère rénale. Un blocage de ce système est donc biologiquement plausible. Cependant, l'indication originale n'étant pas renseignée, la relation entre l'ancienne et la nouvelle indication ne peut pas être analysée plus en détail.

Cette prédiction demande de la prudence. Chez un patient avec sténose bilatérale des artères rénales ou rein fonctionnel unique, un IEC peut provoquer une insuffisance rénale aiguë. Le profil de sécurité doit donc être examiné séparément. Le score TxGNN (0,9986) est une prédiction informatique et ne remplace pas une preuve clinique.

Les quatre autres indications prédites (hypertension rénale maligne, deux formes d'hypertension pulmonaire et syndrome de Braddock) sont toutes de niveau L5, avec une recommandation Hold. L'hypertension rénale maligne a exactement le même score que l'entrée rénovasculaire. Les deux prédictions proviennent donc probablement du même voisinage dans le graphe et ne constituent pas deux signaux indépendants. Les 20 publications récupérées pour l'hypertension pulmonaire liée à l'hypoxie portent sur l'hypoxie en général (vieillissement cérébral, cancer, sclérose en plaques, altitude). Aucune ne mentionne le quinapril, elles ne fournissent donc aucun élément de preuve.

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 62206135 | ACUITEL 5 mg, comprimé enrobé sécable (PFIZER HOLDING FRANCE) | Comprimé enrobé sécable | Non renseignée dans les données fournies |
| 62927128 | ACUITEL 20 mg, comprimé enrobé sécable (PFIZER HOLDING FRANCE) | Comprimé enrobé sécable | Non renseignée dans les données fournies |

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité.

Les données de sécurité de l'ANSM (mises en garde, contre-indications) ne sont pas encore disponibles, et aucune interaction médicamenteuse n'a été trouvée. À noter toutefois, d'après l'analyse mécanistique : les inhibiteurs de l'ECA peuvent provoquer une insuffisance rénale aiguë en cas de sténose bilatérale des artères rénales ou de rein fonctionnel unique, ce qui concerne directement l'indication prédite.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique ni aucune publication pertinente ne la soutient.
- Les données de sécurité de l'ANSM manquent, ce qui bloque le passage à l'étape suivante de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde et contre-indications), en priorité car elle bloque la suite
- Obtenir les données sur le mécanisme d'action (MOA) et l'indication originale via l'API DrugBank
- Rechercher des essais cliniques et des publications spécifiques au quinapril (ou aux IEC) dans l'hypertension rénovasculaire
- Réaliser une revue de sécurité dédiée au risque rénal (sténose bilatérale des artères rénales, rein fonctionnel unique)

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Toute piste de repositionnement doit être validée cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

