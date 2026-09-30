---
layout: default
title: Iloprost
parent: Prédiction du modèle uniquement (L5)
nav_order: 148
evidence_level: L5
indication_count: 9
---

# Iloprost
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

# Iloprost : De l'hypertension artérielle pulmonaire à l'hypotrichose simple du cuir chevelu

## Résumé en Une Phrase

L'iloprost est un analogue de la prostacycline (agoniste du récepteur IP), commercialisé en France sous forme de solution à diluer pour perfusion. Les données ANSM disponibles ne précisent pas son indication d'origine. Le dossier le rattache toutefois à l'hypertension artérielle pulmonaire (HTAP).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**, mais **aucun essai clinique et aucune publication** ne soutiennent cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données ANSM (texte d'indication vide pour les 3 AMM). Le dossier mentionne l'HTAP comme usage établi. |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu |
| Score de Prédiction TxGNN | 99,45 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, l'iloprost est un analogue de la prostacycline qui active le récepteur IP. Son efficacité dans l'HTAP est établie, et le lien avec le cycle pilaire reste hypothétique.

La signalisation des prostanoïdes a certains liens avec la biologie du cycle du cheveu, ce qui donne un point de départ plausible. En revanche, l'hypotrichose simple du cuir chevelu est un trouble pileux d'origine monogénique. Le lien avec une voie vasodilatatrice reste donc **spéculatif**. Le score élevé reflète probablement la proximité dans le graphe de connaissances, et non une preuve biologique.

Autre point de prudence : les AMM françaises concernent des solutions pour perfusion. Le dossier ne renseigne pas de voie d'administration compatible avec un usage sur le cuir chevelu (compatibilité des voies : en attente).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69133241 | ILOPROST TEVA 100 microgrammes/mL (TEVA, Pays-Bas) | Solution à diluer pour perfusion | Non précisée dans les données disponibles |
| 64341103 | ILOPROST ZENTIVA 100 microgrammes/mL (Zentiva France) | Solution à diluer pour perfusion | Non précisée dans les données disponibles |
| 62386427 | ILOMEDINE 0,1 mg/1 ml (Bayer Healthcare) | Solution à diluer pour perfusion | Non précisée dans les données disponibles |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et le mécanisme reste spéculatif pour un trouble pileux monogénique. Les données de sécurité ANSM sont absentes, ce qui bloque le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications), qui bloque la suite du processus
- Compléter les données sur le mécanisme d'action (DrugBank) et l'indication d'origine
- Trouver des données précliniques ou mécanistiques reliant la voie IP/prostanoïdes à la pilosité
- Évaluer une voie d'administration adaptée au cuir chevelu

**Autres indications prédites, mieux documentées que le rang 1 :**

| Indication prédite | Score TxGNN | Niveau | Preuves | Recommandation |
|------|------|------|------|------|
| HTAP associée à une cardiopathie congénitale | 99,33 % | L3 | 1 essai (NCT01383083, N/A, statut inconnu, 42 patients) et 19 publications | Question de recherche |
| HTAP associée à une connectivite | 99,21 % | L3 | 19 publications, dont une cohorte de suivi à long terme de l'iloprost IV (PMID 27651181) | Question de recherche |
| HTAP associée au VIH | 99,21 % | L4 | 1 essai de phase 3 terminé (NCT00709956, 64 patients), dont la population VIH-HTAP reste à confirmer, et 4 publications | Question de recherche |

Ces trois indications relèvent de l'HTAP, pour laquelle l'iloprost est déjà établi. Elles constituent donc davantage des sous-groupes de l'indication connue que de véritables repositionnements. Les cinq autres indications prédites (malformation artérioveineuse pulmonaire, HTAP liée à la schistosomiase, HTAP liée à l'anémie hémolytique chronique, hypotrichose congénitale avec milia, alopécie areata diffuse) restent à L4-L5 avec la décision Hold.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

