---
layout: default
title: Moxonidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Moxonidine
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

# Moxonidine : De l'Hypertension Artérielle à l'Hypotrichose Simple du Cuir Chevelu

## Résumé en Une Phrase

La moxonidine est un antihypertenseur à action centrale (agoniste des récepteurs imidazolines I1 et alpha-2), commercialisé en France. L'indication d'origine n'est pas renseignée dans les données d'AMM fournies ; elle est déduite de la classe pharmacologique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (hypertension artérielle, déduite de la classe pharmacologique) |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 10 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la moxonidine appartient à la classe des antihypertenseurs à action centrale. Elle réduit l'activité sympathique en stimulant les récepteurs imidazolines I1 et alpha-2. Rien dans le dossier ne relie ce mécanisme à la biologie du follicule pileux.

**Cette prédiction est donc peu convaincante sur le plan biologique.** Le score très élevé (99,95 %) reflète probablement une proximité dans le graphe de connaissances, et non un mécanisme réel. Les autres prédictions capillaires du même médicament (hypotrichose congénitale avec milia, alopécie areata diffuse, alopécie) obtiennent des scores voisins et présentent le même problème. Cela suggère un artefact de topologie du graphe partagé entre elles. L'alopécie areata, par exemple, est auto-immune (effondrement du privilège immunitaire, voie JAK/IFN-γ), sans lien apparent avec l'action sympatholytique de la moxonidine.

À titre de comparaison, deux prédictions plus loin dans la liste sont plus cohérentes avec la pharmacologie du médicament : la **maladie rénale hypertensive maligne** et l'**hypertension rénovasculaire maligne** (score 99,67 %, classées « Question de recherche »). Elles restent toutefois sans données cliniques. L'urgence hypertensive relève en général de traitements parentéraux, et un agent oral à action centrale n'y a pas de rôle démontré.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés dans les données d'AMM fournies. Cinq AMM sur les 10 recensées sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62425307 | MOXONIDINE TEVA SANTE 0,4 mg | Comprimé pelliculé | RATIOPHARM (Allemagne) |
| 64771724 | MOXONIDINE BIOGARAN 0,2 mg | Comprimé pelliculé | BIOGARAN |
| 62036633 | MOXONIDINE BIOGARAN 0,4 mg | Comprimé pelliculé | BIOGARAN |
| 68782718 | PHYSIOTENS 0,4 mg | Comprimé pelliculé | VIATRIS MEDICAL |
| 63708322 | MOXONIDINE TEVA SANTE 0,2 mg | Comprimé pelliculé | RATIOPHARM (Allemagne) |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette prédiction repose uniquement sur le score du modèle (niveau L5). Il n'existe ni essai clinique ni publication, et aucun lien mécanistique plausible n'a été identifié entre la moxonidine et la pousse des cheveux.
- Les données de sécurité issues de la notice ANSM sont absentes, ce qui empêche toute évaluation de sécurité (critère bloquant).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications) afin de lever le blocage sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank).
- Renseigner l'indication d'origine à partir des textes d'AMM.
- Réaliser une recherche ciblée de littérature préclinique sur la moxonidine (ou les agonistes alpha-2/I1) et le follicule pileux avant tout investissement.
- Envisager de réorienter l'évaluation vers les prédictions cardio-rénales (hypertension maligne, atteinte rénale hypertensive), plus cohérentes sur le plan pharmacologique, en recherchant des données de devenir rénal.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

