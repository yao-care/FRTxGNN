---
layout: default
title: Sotalol
parent: Prédiction du modèle uniquement (L5)
nav_order: 287
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Sotalol : Des Arythmies Cardiaques au Syndrome du Sinus Malade Autosomique Dominant de Type 2

## Résumé en Une Phrase

Le sotalol est un antiarythmique (bêtabloquant qui bloque aussi les canaux potassiques IKr/hERG), utilisé pour le contrôle du rythme cardiaque, notamment dans la fibrillation auriculaire. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome du sinus malade 2, autosomique dominant**. **Aucun essai clinique et aucune publication** ne soutient actuellement cette prédiction, et le sotalol est généralement déconseillé dans cette pathologie sans pacemaker.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données AMM (texte d'indication vide) ; antiarythmique |
| Nouvelle Indication Prédite | Syndrome du sinus malade 2, autosomique dominant |
| Score de Prédiction TxGNN | 99,76 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations d'évaluation, le sotalol associe un blocage bêta-adrénergique et un blocage des canaux potassiques IKr/hERG, ce qui ralentit la fréquence sinusale et la conduction auriculo-ventriculaire.

Le lien avec le syndrome du sinus malade n'est donc, au mieux, qu'une association plausible au niveau des canaux ioniques. Le rythme sinusal et la conduction sont précisément ce que le sotalol ralentit.

**Cette prédiction est probablement un artefact du graphe de connaissances, voire le signe d'un risque.** Le sotalol est généralement mis en garde ou contre-indiqué en cas de syndrome du sinus malade sans pacemaker, à cause du risque de bradycardie et de pauses sinusales.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62193524 | SOTALOL SANDOZ 160 mg, comprimé sécable | Comprimé sécable | SANDOZ |
| 62519799 | SOTALEX 80 mg, comprimé sécable | Comprimé sécable | CHEPLAPHARM ARZNEIMITTEL (Allemagne) |
| 64820630 | SOTALEX 160 mg, comprimé sécable | Comprimé sécable | CHEPLAPHARM ARZNEIMITTEL (Allemagne) |

Le texte de l'indication approuvée n'est pas renseigné pour ces trois AMM.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le profil pharmacologique du sotalol (bradycardie, ralentissement de la conduction) va plutôt à l'encontre de cette indication.
- À titre indicatif, une autre prédiction du même dossier, « accident vasculaire cérébral », présente des essais et des publications. Ils portent sur la prise en charge de la fibrillation auriculaire, où le sotalol n'est qu'un comparateur, et non sur un bénéfice propre du sotalol.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une recherche de littérature ciblée sur le sotalol et le syndrome du sinus malade, avec une évaluation explicite du risque de bradycardie
- L'indication approuvée de chaque AMM, à compléter pour documenter l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

