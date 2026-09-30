---
layout: default
title: Telmisartan
parent: Prédiction du modèle uniquement (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan : De l'hypertension artérielle (indication classique) à l'angor de Prinzmetal

## Résumé en une phrase

Telmisartan est un antagoniste des récepteurs de l'angiotensine II (ARA II), classiquement utilisé contre l'hypertension. Les données réglementaires fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**angor de Prinzmetal** (angor vasospastique), avec un score très élevé.
Cette prédiction repose sur le modèle seul : **0 essai clinique** et **0 publication** ne la soutiennent actuellement.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données réglementaires (texte d'indication vide pour les AMM listées) |
| Nouvelle indication prédite | Angor de Prinzmetal |
| Score de prédiction TxGNN | 99,98 % |
| Niveau de preuve | L5 |
| Statut de marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les éléments de raisonnement joints, telmisartan bloque le récepteur AT1 de l'angiotensine II. Il serait aussi un agoniste partiel de PPARγ, un récepteur qui intervient dans le métabolisme et la fonction de l'endothélium (la paroi interne des vaisseaux).

L'angor de Prinzmetal est causé par un spasme des artères coronaires. L'angiotensine II est un puissant vasoconstricteur, et son blocage, ou un effet favorable sur l'endothélium, pourrait donc réduire ces spasmes. Cette hypothèse est plausible, mais **aucune donnée fournie ne la teste**. Elle reste théorique.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

## Informations de marché en France

Sur les 20 AMM recensées, voici 5 exemples :

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 67169534 | TELMISARTAN TEVA SANTE 40 mg | Comprimé | Non renseignée |
| 69536527 | TELMISARTAN EG 80 mg | Comprimé pelliculé | Non renseignée |
| 62260706 | TELMISARTAN VIATRIS 80 mg | Comprimé | Non renseignée |
| 65179106 | TELMISARTAN BIOGARAN 40 mg | Comprimé | Non renseignée |
| 68369993 | PRITOR 20 mg | Comprimé | Non renseignée |

Les formes disponibles sont uniquement orales (comprimés, comprimés pelliculés, comprimés sécables).

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde et contre-indications de la notice ANSM n'ont pas pu être récupérées, et aucune interaction médicamenteuse n'a été trouvée dans les données.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'angor de Prinzmetal repose uniquement sur le score du modèle (niveau L5). Aucun essai ni aucune publication ne l'appuie, et le dossier de sécurité n'est pas disponible.
- D'autres indications prédites disposent de davantage de données que celle-ci. L'occlusion d'artère cérébrale (L3) repose surtout sur des études animales. L'hémorragie intracérébrale (L2) s'appuie sur l'essai de phase 3 TRIDENT (1 671 patients), mais il teste une association de trois médicaments, sans résultats fournis. Ces pistes pourraient être évaluées séparément.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indications autorisées), qui bloque actuellement l'évaluation de sécurité.
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Lancer une recherche ciblée dans les essais et la littérature sur telmisartan et l'angor vasospastique.
- Vérifier la pertinence clinique : l'angor de Prinzmetal se traite habituellement avec d'autres classes de médicaments, et l'intérêt d'un ARA II reste à démontrer.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

