---
layout: default
title: Benralizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 54
evidence_level: L5
indication_count: 5
---

# Benralizumab
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

# Benralizumab : De l'Asthme Éosinophilique Sévère à la Thrombopénie par Destruction Immune

## Résumé en Une Phrase

Le benralizumab est un anticorps monoclonal anti-IL-5Rα, utilisé dans l'asthme éosinophilique sévère (d'après le contexte des essais cliniques du dossier ; le texte d'indication de l'ANSM n'est pas renseigné).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombopénie par destruction immune**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme éosinophilique sévère (texte d'indication ANSM non renseigné ; déduit du contexte des essais) |
| Nouvelle Indication Prédite | Thrombopénie par destruction immune |
| Score de Prédiction TxGNN | 99,34 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le benralizumab est un anticorps dirigé contre la chaîne α du récepteur de l'IL-5. Il élimine les éosinophiles et les basophiles par cytotoxicité cellulaire dépendante des anticorps (ADCC). Les données détaillées sur le mécanisme d'action ne sont pas fournies par DrugBank dans ce dossier. Cette description provient de l'analyse de plausibilité mécanistique associée à la prédiction.

Le lien avec la nouvelle indication est **faible**. La thrombopénie par destruction immune repose surtout sur des auto-anticorps et sur la clairance des plaquettes via les récepteurs Fc. Aucun lien établi n'existe avec les éosinophiles ou avec la voie IL-5. Le score TxGNN élevé (0,993) reflète une proximité dans le graphe de connaissances, pas une preuve biologique ou clinique.

La prédiction doit donc être considérée comme une simple hypothèse générée par le modèle. Aucune donnée réelle ne permet de la confirmer ou de l'infirmer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63562134 | FASENRA 30 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée dans les données ANSM |
| 63094493 | FASENRA 30 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée dans les données ANSM |

Les deux AMM sont détenues par ASTRAZENECA AB.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible entre la déplétion des éosinophiles et la destruction immune des plaquettes.
- Les données de sécurité de la notice ANSM manquent également, ce qui bloque le passage à l'étape de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réaliser une recherche bibliographique ciblée sur les anti-IL-5 dans les thrombopénies immunes, afin de vérifier s'il existe un signal, même faible.
- Définir un argument biologique reliant l'IL-5Rα à la destruction plaquettaire avant d'envisager tout essai.

**Remarque sur les autres candidats du dossier :** la dermatite (rang 2) est la seule indication prédite avec des preuves réelles, mais elles sont négatives. L'essai de phase 2 HILLIER (NCT04605094, 194 patients) a montré l'absence d'effet clinique du benralizumab dans la dermatite atopique modérée à sévère. Cette piste est également en Hold. Les dermatoses éosinophiliques (par exemple DRESS, syndromes hyperéosinophiliques) paraissent plus plausibles, mais les essais correspondants n'en sont qu'à un stade précoce ou n'ont pas démarré.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

