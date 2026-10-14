---
layout: default
title: Natalizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 527
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

# Natalizumab : De la maladie de Crohn à la bronchite

## Résumé en Une Phrase

Natalizumab est un anticorps monoclonal bloquant l'intégrine alpha-4, initialement utilisé pour le traitement de la maladie de Crohn, des maladies inflammatoires chroniques de l'intestin et de la sclérose en plaques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Crohn (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,46 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, natalizumab bloque l'intégrine alpha-4 et réduit la migration des leucocytes vers les tissus enflammés. Cet effet est à l'origine de son efficacité dans la maladie de Crohn et la sclérose en plaques.

En théorie, ce blocage pourrait atténuer le recrutement de cellules inflammatoires dans les voies respiratoires. Toutefois, cette hypothèse reste purement spéculative : natalizumab est aussi immunosuppresseur et pourrait augmenter le risque d'infections respiratoires. Un bénéfice dans la bronchite est donc peu plausible sans données supplémentaires. Le score TxGNN est très élevé, mais il s'agit uniquement d'une prédiction computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les trois AMM recensées sont toutes annulées ; le texte de l'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60779570 | TYRUKO 300 mg (Sandoz) | Solution à diluer pour perfusion | Annulée |
| 61863110 | TYSABRI 150 mg (Biogen) | Solution injectable en seringue préremplie | Annulée |
| 68722564 | TYSABRI 300 mg (Biogen) | Solution à diluer pour perfusion | Annulée |

## Considérations de Sécurité

- **Contre-indication issue du graphe de connaissances** (et non du texte de la notice) : leucoencéphalopathie multifocale progressive (LEMP).
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - **Majeures** : corticoïdes (hydrocortisone, prednisone, prednisolone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), mercaptopurine, lévamisole, triméthrexate, ibritumomab tiuxétan, tositumomab, iobenguane (I-131).
  - **Modérée** : naltrexone.
  - **Mineures** : sels de zinc (sulfate, acétate, gluconate, chlorure).
- Les signalements de la littérature associent également natalizumab à un risque de LEMP et à des cas de psoriasis induit ou aggravé.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la bronchite repose uniquement sur le modèle (L5), sans essai ni publication. Le risque d'infection respiratoire et de LEMP rend un bénéfice peu plausible. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (ANSM), actuellement manquantes et bloquantes pour l'évaluation de sécurité
- Les données détaillées sur le mécanisme d'action
- Des données précliniques ou cliniques sur natalizumab dans la bronchite
- Une clarification du statut réglementaire en France (AMM annulées)

---

### Annexe : autres indications prédites (non retenues)

| Rang | Maladie | Score TxGNN | Niveau | Décision | Commentaire |
|---|---|---|---|---|---|
| 2 | Parapsoriasis | 99,37 % | L4 | Hold | Un seul cas clinique rapportant des effets indésirables dermatologiques (avec fingolimod) ; signal de sécurité, pas de bénéfice |
| 3 | Psoriasis | 99,19 % | L4 | Hold | Données contradictoires : une série de 18 patients rapporte une amélioration, mais plusieurs cas décrivent un psoriasis induit ou aggravé ; aucun essai |
| 4 | Rétinopathie diabétique non proliférante sévère | 99,18 % | L5 | Hold | Aucune donnée ; risque de LEMP en usage systémique |
| 5 | Pityriasis lichénoïde aigu | 99,04 % | L4 | Hold | Même cas clinique que ci-dessus, confondu par l'exposition au fingolimod ; aucun soutien |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

