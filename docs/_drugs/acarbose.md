---
layout: default
title: Acarbose
parent: Prédiction du modèle uniquement (L5)
nav_order: 14
evidence_level: L5
indication_count: 9
---

# Acarbose
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

# Acarbose : Du Diabète de Type 2 au Syndrome de la Personne Raide Classique

## Résumé en Une Phrase

L'acarbose est un inhibiteur des alpha-glucosidases intestinales, qui ralentit l'absorption des glucides. Il est habituellement utilisé pour contrôler la glycémie après les repas dans le diabète de type 2 (le texte d'indication des AMM françaises n'est pas renseigné dans les données reçues).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la personne raide classique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue uniquement du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2 (connaissance générale ; texte d'indication des AMM non renseigné) |
| Nouvelle Indication Prédite | Syndrome de la personne raide classique |
| Score de Prédiction TxGNN | 99,65 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 13 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank pour ce dossier. D'après les informations connues, l'acarbose inhibe les alpha-glucosidases de l'intestin, ce qui ralentit la digestion des glucides et atténue les pics de glycémie après les repas.

Le syndrome de la personne raide est un trouble neurologique auto-immun, souvent associé à des anticorps anti-GAD65 et à une atteinte du système GABAergique. **Aucun lien mécanistique plausible n'a été identifié** avec l'inhibition des alpha-glucosidases. Le score élevé de TxGNN (0,996) vient d'une prédiction fondée sur le graphe de connaissances. Il pourrait refléter un lien indirect, par exemple la comorbidité avec le diabète ou l'auto-immunité anti-GAD, mais cette hypothèse n'est pas vérifiée.

Les autres prédictions du même modèle (forme focale du syndrome de la personne raide, syndrome de dysfonction répondant à la thiamine, opsismodysplasie, lipodystrophies localisées, agénésie pancréatique) n'ont pas non plus de preuve clinique. Seule l'agénésie pancréatique dispose de quelques publications, mais elles portent sur le diabète en général et non sur cette maladie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 5 AMM principales sont listées ci-dessous, sur un total de 13. Le texte d'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60989978 | ACARBOSE VIATRIS 50 mg, comprimé | Comprimé | VIATRIS SANTE |
| 65803331 | ACARBOSE EG 100 mg, comprimé | Comprimé | EG LABO - LABORATOIRES EUROGENERICS |
| 69771614 | ACARBOSE SANDOZ 50 mg, comprimé | Comprimé | SANDOZ |
| 60946941 | ACARBOSE VIATRIS 100 mg, comprimé sécable | Comprimé sécable | VIATRIS SANTE |
| 67901945 | ACARBOSE ZENTIVA 100 mg, comprimé sécable | Comprimé sécable | ZENTIVA FRANCE |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, texte des indications approuvées)
- Obtenir les données de mécanisme d'action depuis DrugBank
- Mener une recherche bibliographique ciblée sur l'acarbose et le syndrome de la personne raide (auto-immunité anti-GAD65, diabète associé)
- Documenter une hypothèse mécanistique testable avant toute étude préclinique ou clinique

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

