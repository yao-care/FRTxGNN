---
layout: default
title: Azathioprine
parent: Prédiction du modèle uniquement (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine : De l'Immunosuppression (indications d'AMM non renseignées) au Syndrome de Microphtalmie Colobomateuse-Dysplasie Rhizomélique

## Résumé en Une Phrase

L'azathioprine est un immunosuppresseur, antimétabolite des purines, commercialisé en France. Ses indications d'AMM ne figurent pas dans les données reçues.
Le modèle TxGNN classe en tête le **syndrome de microphtalmie colobomateuse-dysplasie rhizomélique**, mais **aucun essai clinique et aucune publication** ne soutiennent cette prédiction. Elle est très probablement un artefact du graphe de connaissances.
Dans ce même lot, les prédictions **maladie inflammatoire chronique de l'intestin (MICI)** et **rectocolite hémorragique** sont les seules à disposer d'essais cliniques directement pertinents (voir la Conclusion).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (aucun texte d'indication dans les AMM fournies) |
| Nouvelle Indication Prédite | Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 8 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, l'azathioprine est un antimétabolite des purines à effet immunosuppresseur et myélosuppresseur.

**Pour cette prédiction précise, aucun lien mécanistique plausible n'a été identifié.** Le syndrome de microphtalmie colobomateuse-dysplasie rhizomélique est un syndrome malformatif du développement, sans composante immunitaire connue que l'azathioprine pourrait corriger. Le score proche de 1,0 reflète très probablement un artefact du graphe de connaissances, et non une piste thérapeutique. La similarité avec l'indication d'origine n'a pas pu être évaluée.

Il faut donc considérer cette prédiction comme non étayée. Les pistes crédibles pour l'azathioprine figurent parmi les autres prédictions du lot (MICI, rectocolite hémorragique), où son rôle d'immunosuppresseur d'entretien épargneur de corticoïdes est cohérent.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Huit AMM sont recensées, dont cinq sont détaillées ci-dessous. Le texte de l'indication approuvée est vide dans les données reçues.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60211183 | AZATHIOPRINE TEVA 50 mg | Comprimé pelliculé | TEVA SANTE |
| 63935487 | IMUREL 50 mg | Poudre pour solution injectable (IV) | ASPEN PHARMA TRADING (Irlande) |
| 63479140 | AZATHIOPRINE VIATRIS 50 mg | Comprimé pelliculé sécable | VIATRIS SANTE |
| 66685747 | IMUREL 50 mg | Comprimé pelliculé | BB FARMA (Italie) |
| 64841852 | IMUREL 25 mg | Comprimé pelliculé | ASPEN PHARMA TRADING (Irlande) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction classée première n'a aucune preuve clinique ni bibliographique (L5). Le mécanisme de l'azathioprine ne correspond pas à une malformation du développement.

**Autres prédictions du lot (pour information) :**

| Rang | Indication prédite | Score TxGNN | Niveau | Décision |
|---|---|---|---|---|
| 1 | Microphtalmie colobomateuse-dysplasie rhizomélique | 99,999 % | L5 | Hold |
| 2 | Syndrome de brachydactylie-syndactylie | 99,999 % | L5 | Hold |
| 3 | Susceptibilité à l'arthrose | 99,70 % | L5 | Hold |
| 4 | Syndrome WHIM | 99,68 % | L5 | Hold (risque : aggravation de la neutropénie et de la lymphopénie) |
| 5 | Maladie inflammatoire chronique de l'intestin | 99,52 % | L1 | Proceed with Guardrails |
| 6 | Granulomatose chronique autosomique récessive 5 | 99,41 % | L5 | Hold |
| 7 | Arthrose | 99,40 % | L4 | Hold (correspondance jugée fallacieuse) |
| 8 | Granulomatose avec défaut de chimiotaxie des neutrophiles | 99,37 % | L5 | Hold |
| 9 | Rectocolite hémorragique | 99,33 % | L1 | Proceed with Guardrails |
| 10 | Dysplasie acromésomélique type Hunter-Thompson | 99,27 % | L5 | Hold |

Le niveau L1 des rangs 5 et 9 repose sur l'essai de Phase 3 [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) (azathioprine + allopurinol à faible dose versus azathioprine seule, rectocolite hémorragique, 84 patients). Son statut est « inconnu » et aucun résultat n'a été fourni. Ces deux prédictions sont donc plafonnées au stade S2 tant que les résultats ne sont pas vérifiés.

**Pour avancer, les éléments suivants sont nécessaires :**
- La notice ANSM (mises en garde, contre-indications, indications d'AMM) : lacune bloquante pour le criblage de sécurité.
- Les données sur le mécanisme d'action, à récupérer via DrugBank.
- Pour la MICI et la rectocolite hémorragique, des résultats d'essais vérifiés et un rapport dédié à ces indications. Les garde-fous prévus sont le génotypage TPMT/NUDT15 avant traitement, la surveillance de la NFS et de la fonction hépatique, et l'information sur le risque de syndrome lymphoprolifératif.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

