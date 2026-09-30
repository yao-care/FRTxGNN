---
layout: default
title: Nimodipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 215
evidence_level: L5
indication_count: 2
---

# Nimodipine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Nimodipine : De l'indication d'origine (non renseignée) à l'hypercholestérolémie familiale homozygote

## Résumé en Une Phrase

La nimodipine est un inhibiteur calcique de la famille des dihydropyridines, commercialisé en France sous le nom NIMOTOP en comprimé et en solution pour perfusion. Le texte d'indication figurant dans les AMM n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypercholestérolémie familiale homozygote**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale homozygote |
| Score de Prédiction TxGNN | 99,29 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, la nimodipine est un inhibiteur calcique de type dihydropyridine bloquant les canaux calciques de type L, avec une sélectivité cérébrovasculaire.

L'hypercholestérolémie familiale homozygote est due à des variants à perte de fonction du gène *LDLR* (plus rarement *APOB*, *PCSK9* ou *LDLRAP1*), qui altèrent fortement l'élimination du LDL-cholestérol. Aucun lien mécanistique direct n'est établi avec le blocage des canaux calciques. Certains inhibiteurs calciques ont montré des effets antiathérosclérotiques modestes en préclinique, mais aucun ne corrige le déficit en récepteur du LDL ni n'abaisse le LDL-C de façon cliniquement significative.

Le score élevé de TxGNN (0,993) est une prédiction issue d'un graphe de connaissances, sans confirmation clinique ni bibliographique. Les options déjà validées dans cette maladie (statines, ézétimibe, inhibiteurs de PCSK9, lomitapide, évinacumab, aphérèse des LDL) sont beaucoup mieux étayées.

Une seconde prédiction existe : le **syndrome d'antidiurèse inappropriée néphrogénique** (score 99,05 %, niveau L5, Hold). Elle repose sur des variants gain de fonction d'*AVPR2*, sans lien direct avec la cible de la nimodipine. Les effets vasodilatateur et hypotenseur du médicament pourraient en outre ajouter un risque chez un patient hyponatrémique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65726536 | NIMOTOP 30 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 61339638 | NIMOTOP 10 mg/50 ml, solution injectable pour perfusion | Solution injectable pour perfusion | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans la base interrogée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique plausible. Il existe déjà des traitements bien établis pour cette maladie. Les données de sécurité de la notice ANSM manquent également, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications) et le texte des indications approuvées
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank)
- Trouver des données précliniques ou de mécanisme reliant les inhibiteurs calciques au métabolisme des LDL ou à la voie AVPR2
- Vérifier la compatibilité des voies d'administration avec la maladie visée (actuellement en attente)

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

