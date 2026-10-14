---
layout: default
title: Esomeprazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Ésoméprazole : De l'Ulcère Peptique au Reflux Duodénogastrique

## Résumé en Une Phrase

L'ésoméprazole est un inhibiteur de la pompe à protons, initialement utilisé pour les maladies liées à l'acidité gastrique (ulcère peptique, reflux gastro-œsophagien, œsophagite, syndrome de Zollinger-Ellison).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **reflux duodénogastrique**, mais cette prédiction repose sur **0 essai clinique** et **1 publication** de portée générale, qui ne traite pas directement de cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ulcère peptique, reflux gastro-œsophagien, œsophagite, syndrome de Zollinger-Ellison (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Reflux duodénogastrique |
| Score de Prédiction TxGNN | 99,53 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'ésoméprazole fait partie de la classe des inhibiteurs de la pompe à protons (H+/K+ ATPase). Son efficacité a été établie dans les pathologies liées à l'acidité gastrique.

Dans le reflux duodénogastrique, le contenu duodénal (bile, sécrétions pancréatiques) remonte dans l'estomac. En réduisant l'acidité, l'ésoméprazole pourrait diminuer la composante acide du liquide refluant et soulager l'irritation de la muqueuse et les symptômes.

**Le lien reste toutefois indirect et, au mieux, symptomatique.** Ce reflux est principalement dû à la bile, aux sécrétions pancréatiques et à des troubles de la motricité, que la suppression acide ne traite pas directement. Le score TxGNN très élevé (99,53 %) reflète probablement le chevauchement du médicament avec des indications voisines (reflux, maladies acido-dépendantes) plutôt qu'une preuve directe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revue | European Journal of Clinical Pharmacology | Mise à jour sur l'usage clinique et la pharmacocinétique des inhibiteurs de la pompe à protons (ulcère peptique, infection à *H. pylori*, RGO, lésions liées aux AINS, syndrome de Zollinger-Ellison). Ne traite pas directement du reflux duodénogastrique. |

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Voici les 5 premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|------|
| 62358997 | ESOMEPRAZOLE ARROW LAB 40 mg | Gélule gastro-résistante | Annulée |
| 62824142 | INEXIUM 40 mg | Comprimé gastro-résistant | Annulée |
| 67972216 | ESOMEPRAZOLE EG 40 mg | Gélule gastro-résistante | Annulée |
| 66628995 | ESOMEPRAZOLE ZENTIVA 40 mg | Gélule gastro-résistante | Annulée |
| 64359642 | ESOMEPRAZOLE ETHYPHARM 20 mg | Gélule gastro-résistante | Annulée |

Les autres formes recensées sont les granulés pour suspension buvable (INEXIUM 10 mg) et la poudre pour solution injectable ou pour perfusion.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, ostéoporose, ostéoporose post-ménopausique, fracture osseuse, gastrite atrophique chronique.
- **Interactions médicamenteuses** : 168 interactions recensées. Parmi celles listées, deux sont de niveau **majeur** : l'acalabrutinib et l'atazanavir. Plusieurs sont de niveau modéré, par exemple l'hydrochlorothiazide, l'atorvastatine, le fénofibrate, l'amphotéricine B, l'amikacine, l'amphétamine, l'apalutamide, le bosutinib, la bendamustine et le bumétanide. D'autres sont de niveau mineur, par exemple l'acide acétylsalicylique, la cyanocobalamine, l'axitinib et le bortézomib.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni publication spécifique ne soutient l'usage de l'ésoméprazole dans le reflux duodénogastrique.
- Le lien mécanistique est indirect, et le score élevé du modèle ne remplace pas des preuves réelles.
- Toutes les AMM françaises recensées sont annulées.

À titre de contexte, la prédiction « ulcère duodénal » (rang 3) est bien étayée par des essais de phase 3 et des études randomisées. Elle correspond toutefois à un usage déjà établi du médicament et ne constitue pas un véritable repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données cliniques ou observationnelles spécifiques au reflux duodénogastrique (ou reflux biliaire) : essais contrôlés, études sur le soulagement des symptômes
- Les données détaillées sur le mécanisme d'action
- Les informations officielles de sécurité (mises en garde et contre-indications de la notice ANSM)
- La clarification du statut réglementaire actuel en France, puisqu'aucune AMM n'est valide dans les données disponibles
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

