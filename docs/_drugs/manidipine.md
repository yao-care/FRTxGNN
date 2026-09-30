---
layout: default
title: Manidipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 185
evidence_level: L5
indication_count: 9
---

# Manidipine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Manidipine : D'un inhibiteur calcique de la classe des dihydropyridines à la migraine

## Résumé en Une Phrase

La manidipine est un inhibiteur calcique de la classe des dihydropyridines, commercialisé en France sous forme de comprimés.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **migraine (migraine disorder)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,80 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 16 |
| Décision Recommandée | Hold |

Le texte de l'indication approuvée n'est renseigné pour aucune des AMM fournies, donc la ligne « Indication Originale » est omise.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, la manidipine est un inhibiteur calcique de type dihydropyridine, avec une activité sur les canaux calciques de type L et de type T. Mécanistiquement, elle pourrait être applicable à la migraine.

D'autres inhibiteurs calciques, comme la flunarizine, sont utilisés en prophylaxie de la migraine. Le lien est donc plausible. Cependant, aucun essai ni aucune publication spécifique à la manidipine n'a été fourni. Le score élevé du modèle (99,80 %) reste une prédiction et ne remplace pas une preuve clinique.

Le modèle a aussi proposé d'autres pistes, toutes au niveau L5 :
- **Angor de Prinzmetal** : bon ajustement mécanistique (les inhibiteurs calciques traitent le vasospasme coronaire). Elle est classée « Research Question », avec une revue ciblée de la littérature comme prochaine étape raisonnable.
- **Hypertension pulmonaire** : la vasodilatation est plausible. Les trois articles retrouvés n'apportent aucun soutien clinique, et l'un d'eux est un cas de pneumopathie interstitielle attribuée à la manidipine (voir Considérations de Sécurité).
- **Migraine avec aura du tronc cérébral** et **susceptibilité à la migraine avec ou sans aura** : sous-types ou phénotypes génétiques de la migraine, à intégrer à la question générale de la migraine.
- **Autres pistes** (syndrome néphrogénique d'antidiurèse inappropriée, atrophodermie vermiculée) : aucun lien mécanistique plausible. Les scores proviennent probablement d'artefacts du graphe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la migraine.

Pour la prédiction voisine « susceptibilité à la migraine avec ou sans aura », les 20 références retrouvées (10 affichées) portent sur les mécanismes génétiques et moléculaires communs à l'épilepsie et à la migraine, par exemple les gènes de canaux ioniques comme SCN1A. Aucune ne mentionne la manidipine, et elles ne soutiennent qu'un raisonnement général de canalopathie.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|------|
| 67985231 | MANIDIPINE ZYDUS 20 mg, comprimé | Comprimé | ZYDUS FRANCE |
| 60165857 | MANIDIPINE BIOGARAN 10 mg, comprimé | Comprimé | BIOGARAN |
| 63426700 | MANIDIPINE ZENTIVA 10 mg, comprimé | Comprimé | ZENTIVA FRANCE |
| 67302931 | MANIDIPINE ARROW 10 mg, comprimé sécable | Comprimé sécable | ARROW GENERIQUES |
| 66582900 | MANIDIPINE VIATRIS 10 mg, comprimé | Comprimé | VIATRIS SANTE |

Ces 5 AMM sont affichées sur un total de 16. Le texte des indications approuvées n'est pas renseigné dans les données.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée de mise en garde, de contre-indication ou d'interaction médicamenteuse n'a pu être extraite.

Un signal issu de la littérature est à noter : un cas rapporté au Japon en 1997 décrit une pneumopathie interstitielle après la prise de manidipine 10 mg/jour chez une patiente ayant une atteinte pulmonaire rhumatoïde préexistante. Les symptômes se sont améliorés après l'arrêt du médicament et l'instauration d'une corticothérapie. Il s'agit d'un rapport de cas isolé.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction pour la migraine repose uniquement sur le modèle (L5), sans essai clinique ni publication propre à la manidipine. Le lien mécanistique est plausible, mais la sécurité n'a pas pu être examinée faute de notice ANSM analysée, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications), point bloquant
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank
- Réaliser une revue de la littérature sur les inhibiteurs calciques (flunarizine, dihydropyridines) dans la prophylaxie de la migraine, puis rechercher des données propres à la manidipine
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine (actuellement non évaluées)
- Regrouper les pistes « migraine avec aura du tronc cérébral » et « susceptibilité à la migraine » dans la question générale de la migraine
- Traiter séparément l'angor de Prinzmetal comme question de recherche prioritaire

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat de repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

