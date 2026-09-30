---
layout: default
title: Acyclovir
parent: Prédiction du modèle uniquement (L5)
nav_order: 16
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Aciclovir : Des Infections Herpétiques à la Kératoconjonctivite Ponctuée Épithéliale

## Résumé en Une Phrase

L'aciclovir est un antiviral actif sur les virus herpétiques (HSV, VZV), commercialisé en France sous forme de crème, comprimé, suspension buvable et préparations injectables.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératoconjonctivite ponctuée épithéliale**.
Cette prédiction repose sur **0 essai clinique** et **2 publications**, deux séries de cas indirectes qui ne testent pas l'aciclovir dans cette maladie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Kératoconjonctivite ponctuée épithéliale |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances établies, l'aciclovir est activé par la thymidine kinase virale : il n'agit donc que sur les virus qui en codent une, comme HSV et VZV.

La kératoconjonctivite ponctuée épithéliale a plusieurs causes possibles : adénovirale, herpétique, microsporidienne, etc. Un bénéfice de l'aciclovir ne serait envisageable que dans les cas d'origine herpétique. Il n'y a pas de lien mécanistique clair pour les autres causes.

Le score du modèle (0,997) n'est donc pas étayé par des données cliniques. Il doit être lu comme un signal de recherche, pas comme une preuve d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Série de cas | Indian J Pathol Microbiol | Caractéristiques de la kératoconjonctivite microsporidienne dans une cohorte de l'est de l'Inde. Aucun traitement par aciclovir n'est décrit dans le résumé. |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Série de cas | Am J Ophthalmol | Lipidose cornéenne d'origine médicamenteuse chez deux patients atteints du SIDA, traités pour des infections opportunistes. Aucun lien démontré avec l'aciclovir dans le résumé. |

Ces deux articles décrivent des atteintes oculaires, mais aucun ne fournit de données d'efficacité de l'aciclovir.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 67344332 | ACICLOVIR CRISTERS 5 %, crème | Crème |
| 60418673 | ACICLOVIR EG 200 mg, comprimé | Comprimé |
| 64941728 | ACICLOVIR ZENTIVA 5 %, crème | Crème |
| 60618154 | ZOVIRAX 800 mg/10 mL, suspension buvable en flacon | Suspension buvable |
| 68102563 | ACICLOVIR BIOGARAN CONSEIL 5 %, crème | Crème |

Le texte des indications approuvées n'est pas renseigné dans les données reçues. Le dossier signale aussi des formes en poudre pour solution injectable et pour perfusion parmi les 20 AMM.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score du modèle est très élevé, mais aucun essai clinique ni aucune publication ne soutient l'usage de l'aciclovir dans cette maladie. Le niveau de preuve est L5.
- Le lien mécanistique n'existe que pour une cause herpétique, sous-ensemble non identifié dans les données.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM. C'est un prérequis bloquant pour tout examen de sécurité.
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Cibler la kératoconjonctivite herpétique plutôt que la forme ponctuée générale, puis mener une recherche bibliographique dédiée.
- Vérifier l'indication d'origine dans le texte des AMM françaises.

À titre d'orientation, la prédiction classée n° 2, la **verrue commune**, dispose de plusieurs essais et d'un ECR publié (niveau L2). Elle mérite une évaluation séparée.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

