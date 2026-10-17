---
layout: default
title: Cefpodoxime
parent: Prédiction du modèle uniquement (L5)
nav_order: 148
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cefpodoxime : nouvelle indication prédite, Susceptibilité à l'arthrose (osteoarthritis susceptibility) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données (texte d'indicatio…"
monitor_inn: "cefpodoxime"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis"]
---

# Cefpodoxime
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Céfpodoxime : D'une indication antibiotique non documentée à l'arthrose

## Résumé en Une Phrase

La céfpodoxime est une céphalosporine de troisième génération, un antibiotique dont le texte d'indication d'origine n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **susceptibilité à l'arthrose** (les prédictions suivantes concernent l'arthrose et la polyarthrite rhumatoïde).
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données (texte d'indication vide pour toutes les AMM) |
| Nouvelle Indication Prédite | Susceptibilité à l'arthrose (osteoarthritis susceptibility) |
| Score de Prédiction TxGNN | 99,35 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 18 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la céfpodoxime fait partie des céphalosporines de troisième génération, qui inhibent la synthèse de la paroi cellulaire bactérienne en se liant aux protéines de liaison à la pénicilline. Son usage est antibactérien.

**Aucun lien mécanistique n'est étayé par les données disponibles.** La « susceptibilité à l'arthrose » est un phénotype de risque génétique et non un état pathologique traitable, ce qui en fait une cible thérapeutique peu adaptée pour un antibiotique. Aucune voie plausible (anti-inflammatoire, chondroprotectrice) n'est documentée.

Les trois indications prédites (susceptibilité à l'arthrose 99,35 %, arthrose 99,25 %, polyarthrite rhumatoïde 99,24 %) ont des scores presque identiques. Cela suggère un signal non spécifique issu de voisins arthritiques partagés dans le graphe de connaissances, plutôt qu'un mécanisme propre au médicament. La polyarthrite rhumatoïde est une maladie auto-immune traitée par des immunomodulateurs ; aucune activité immunomodulatrice n'est documentée pour la céfpodoxime.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 18 AMM sont annulées. Les 5 premières sont listées ci-dessous ; les textes d'indication ne sont pas renseignés.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 68474866 | Cefpodoxime Viatris Enfants et Nourrissons 40 mg/5 mL | Poudre pour suspension buvable | Annulée |
| 63386914 | Cefpodoxime Zydus 100 mg | Comprimé pelliculé | Annulée |
| 68951100 | Cefpodoxime Viatris 100 mg | Comprimé pelliculé | Annulée |
| 68497014 | Cefpodoxime Biogaran Enfants et Nourrissons 40 mg/5 mL | Poudre pour suspension buvable | Annulée |
| 69170898 | Cefpodoxime Sandoz Enfants et Nourrissons 40 mg/5 mL | Poudre pour suspension buvable | Annulée |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 78 interactions sont recensées. Les 20 premières, toutes de niveau modéré, concernent notamment :
  - les anti-acides et inhibiteurs de la sécrétion gastrique : famotidine, ranitidine, cimétidine, nizatidine, oméprazole, ésoméprazole, lansoprazole, dexlansoprazole, pantoprazole, rabéprazole ;
  - les sels d'aluminium, de calcium et de magnésium : hydroxyde d'aluminium, carbonate de calcium, magaldrate, carbonate, hydroxyde et oxyde de magnésium ;
  - les aminosides : kanamycine, néomycine ;
  - le balsalazide.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Aucun mécanisme plausible n'est identifié, la cible « susceptibilité à l'arthrose » n'est pas traitable, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications), actuellement manquante et bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Formuler une hypothèse mécanistique (anti-inflammatoire, chondroprotectrice) et la tester par des études précliniques
- Clarifier les indications d'origine des AMM annulées
- Évaluer la faisabilité pratique du développement, compte tenu de l'absence de produit commercialisé
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

