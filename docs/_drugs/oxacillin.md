---
layout: default
title: Oxacillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 562
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "oxacillin"
predicted_indications: ["epiglottitis", "laryngitis", "bacterial arthritis", "urinary tract infection (disease)"]
description: "Oxacillin : nouvelle indication prédite, Épiglottite (epiglottitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Oxacillin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Oxacillin: Épiglottite (epiglottitis)
{: .text-alpha }

## Résumé en Une Phrase

L'oxacilline est une pénicilline résistante aux pénicillinases, initialement utilisée contre les infections à *Staphylococcus aureus* et d'autres infections staphylococciques (pharyngite, pneumonie staphylococcique, sinusite).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**épiglottite**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.
Pour information, l'indication classée en 3e position, l'arthrite bactérienne, dispose de 20 publications indirectes (aucune étude contrôlée spécifique à l'oxacilline).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Épiglottite (epiglottitis) |
| Score de Prédiction TxGNN | 0.9990 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'oxacilline est une bêta-lactamine résistante aux pénicillinases qui inhibe la synthèse de la paroi bactérienne et est active sur les *S. aureus* sensibles à la méticilline.

L'épiglottite peut être provoquée par *S. aureus*, ce qui crée un lien plausible mais indirect avec l'indication d'origine. En revanche, les germes habituellement en cause (*Haemophilus influenzae* de type b, streptocoques) ne sont pas bien couverts par l'oxacilline.

Le score élevé de TxGNN (0,999) est une prédiction purement computationnelle. Il doit être interprété avec prudence en l'absence de toute donnée clinique ou bibliographique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'épiglottite.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 64323500 | OXACILLINE PANPHARMA 1 g, poudre pour solution injectable (IV) | Poudre pour solution injectable | Active |
| 69443560 | ISTOPEN 1 g/5 ml, poudre et solvant pour solution injectable (IV) | Poudre et solvant pour solution injectable | Active |

Le texte de l'indication approuvée n'est pas renseigné pour ces deux AMM.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, mononucléose infectieuse, syndrome d'infection chronique à virus d'Epstein-Barr.
- **Interactions médicamenteuses** : 41 interactions recensées. Les principales de niveau modéré concernent la doxycycline, la tétracycline, la minocycline, l'acide picosulfurique et l'iode I-131. La clarithromycine présente une interaction mineure. Plusieurs autres (morphine, oméprazole, vancomycine, prednisone, métronidazole, etc.) sont de niveau non classé.
- **Signal de sécurité dans la littérature** : un cas de syndrome DRESS induit par l'oxacilline (2017) et deux cas de leucopénie/granulocytopénie après un traitement intraveineux à forte dose (1977).

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'épiglottite repose uniquement sur le modèle (L5), sans essai ni publication. Le spectre de l'oxacilline couvre mal les principaux agents de cette infection, et les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) sur le site de l'ANSM, un point bloquant pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Rechercher des données microbiologiques et cliniques sur l'épiglottite à *S. aureus*
- Vérifier la disponibilité réelle du produit en France
- Piste à approfondir : l'arthrite bactérienne (score 0,9950, niveau L4), étroitement liée à l'indication staphylococcique existante, mérite d'être traitée comme question de recherche, tandis que la laryngite et l'infection urinaire (probabilité clinique limitée) restent en attente
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

