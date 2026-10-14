---
layout: default
title: Eptifibatide
parent: Prédiction du modèle uniquement (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide : Du Syndrome Coronarien Aigu à la Polyarthrite Rhumatoïde

## Résumé en Une Phrase

L'eptifibatide est un antagoniste des récepteurs GPIIb/IIIa (antiagrégant plaquettaire injectable), initialement utilisé dans le **syndrome coronarien aigu**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polyarthrite rhumatoïde**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome coronarien aigu (d'après le graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM abrogées (non commercialisé) |
| Nombre d'AMM | 2 (0 valide, 2 abrogées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, l'eptifibatide bloque le récepteur GPIIb/IIIa (intégrine αIIbβ3) des plaquettes et empêche leur agrégation. Cette action explique son utilité dans le syndrome coronarien aigu.

Le lien avec la polyarthrite rhumatoïde reste **spéculatif**. L'inflammation d'origine plaquettaire et la signalisation des intégrines pourraient jouer un rôle dans l'inflammation synoviale, mais aucune donnée clinique ou bibliographique n'a été trouvée pour étayer cette hypothèse. La similarité entre l'indication d'origine (maladie cardiovasculaire thrombotique) et la nouvelle indication (maladie auto-immune articulaire) n'a pas pu être évaluée.

À titre d'information, parmi les autres indications prédites, l'**hémoglobinopathie** (drépanocytose) est la mieux documentée (niveau L2, voir la conclusion). Elle repose sur le rôle de l'activation plaquettaire dans les crises vaso-occlusives.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut | Indication Approuvée |
|---------|------|------|------|-----------|
| 67185951 | EPTIFIBATIDE ACCORD 2 mg/ml | Solution injectable | Abrogée | Non renseignée |
| 61707499 | EPTIFIBATIDE ACCORD 0,75 mg/ml | Solution pour perfusion | Abrogée | Non renseignée |

Les deux AMM appartiennent à ACCORD HEALTHCARE (Espagne) et concernent des spécialités à base d'eptifibatide seul. Aucune n'est actuellement valide.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : thrombocytopénie, maladie de la coagulation, insuffisance rénale.
- **Interactions médicamenteuses** (100 interactions recensées, principales citées) :
  - **Majeures** : déférasirox, ibritumomab tiuxétan, tositumomab (I-131).
  - **Modérées** : acide acétylsalicylique, dexfenfluramine, fenfluramine, sibutramine.
  - D'autres interactions, de niveau non précisé, concernent notamment les inhibiteurs de la pompe à protons (oméprazole, pantoprazole, lansoprazole), la morphine, la simvastatine et la prednisone.

Le risque hémorragique inhérent à tout antiagrégant doit être pris en compte. Pour les mises en garde officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la polyarthrite rhumatoïde repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le profil de risque hémorragique, et les contre-indications relevées dans le graphe de connaissances, pèsent contre une avancée sans données solides.
- L'eptifibatide n'a plus d'AMM valide en France, ce qui complique tout développement local.
- L'hémoglobinopathie (drépanocytose) est la piste la mieux étayée, avec un essai de phase 1/2 randomisé (NCT00834899, arrêté prématurément après 13 patients) et trois études pilotes ou de phase I. L'efficacité n'y est pas démontrée, et aucune donnée de phase 3 n'existe. Elle mérite d'être traitée comme une question de recherche à part entière.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice (mises en garde, contre-indications, indications) auprès de l'ANSM, pour permettre un premier examen de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Réaliser une revue de la littérature ciblée sur le rôle des plaquettes et de GPIIb/IIIa dans la polyarthrite rhumatoïde, puis des études précliniques si elle est concluante.
- Clarifier la situation réglementaire (abrogation des AMM) et la disponibilité du produit en France.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

