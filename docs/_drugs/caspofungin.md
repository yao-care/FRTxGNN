---
layout: default
title: Caspofungin
parent: Prédiction du modèle uniquement (L5)
nav_order: 145
evidence_level: L5
indication_count: 1
---

# Caspofungin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Caspofungine : De la candidose œsophagienne à l'anomalie de sécrétion de la gastrine

## Résumé en Une Phrase

La caspofungine est un antifongique de la classe des échinocandines, initialement utilisé pour traiter la candidose œsophagienne et la candidémie.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**anomalie de sécrétion de la gastrine**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Candidose œsophagienne, candidémie (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Anomalie de sécrétion de la gastrine |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 12 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, la caspofungine fait partie des échinocandines : elle inhibe la β-(1,3)-D-glucane synthase, une enzyme fongique absente des cellules de mammifères. Son efficacité est établie dans la candidose œsophagienne et la candidémie.

**Aucun lien mécanistique plausible n'est actuellement soutenu par les données.** Aucune voie connue ne relie cette activité antifongique à la régulation de la gastrine (fonction des cellules G, sécrétion d'acide gastrique, signalisation du récepteur CCK2). Le score élevé (99,44 %) reflète probablement une proximité dans le réseau du graphe de connaissances (voisins communs, tels que d'autres médicaments ou gènes associés à des affections gastro-intestinales) plutôt qu'une causalité biologique.

Cette prédiction doit donc être considérée comme une hypothèse purement computationnelle, à interpréter avec une grande prudence.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Toutes les AMM recensées sont annulées ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63197689 | Caspofungine Stragen 70 mg | Poudre pour solution à diluer pour perfusion | Stragen France |
| 60140010 | Caspofungine Stragen 50 mg | Poudre pour solution à diluer pour perfusion | Stragen France |
| 66400785 | Caspofungine Lorien 70 mg | Poudre pour solution à diluer pour perfusion | Laboratorios Lorien (Espagne) |
| 64566502 | Caspofungine Lorien 50 mg | Poudre pour solution à diluer pour perfusion | Laboratorios Lorien (Espagne) |
| 63609267 | Caspofungine Tillomed 70 mg | Poudre pour solution à diluer pour perfusion | Tillomed Pharma (Allemagne) |

*Cinq AMM principales sur 12 affichées.*

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie du graphe, et non le texte de la notice) : maladie du foie, maladie de la vésicule biliaire, carence en potassium.
- **Interactions médicamenteuses** : 81 interactions recensées.
  - **Majeure** : dexaméthasone.
  - **Modérée** : naltrexone.
  - Les autres interactions listées (par ex. pantoprazole, oméprazole, lansoprazole, vancomycine, amphotéricine B, nystatine, simvastatine, prednisone, hydrocortisone, prednisolone, chlorure de potassium) ont un niveau de gravité non précisé.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible ; de plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice de l'ANSM (mises en garde et contre-indications), indispensable avant tout criblage de sécurité.
- Compléter les données sur le mécanisme d'action (par ex. via DrugBank) et évaluer s'il existe un lien biologique avec la sécrétion de la gastrine.
- Rechercher dans la littérature et les registres d'essais toute preuve préclinique ou clinique concernant cette indication.
- Évaluer la compatibilité des voies d'administration (la forme actuelle est une perfusion intraveineuse) et la similarité avec l'indication d'origine.
- Clarifier le statut réglementaire en France, toutes les AMM étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

