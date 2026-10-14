---
layout: default
title: Aminophylline
parent: Preuves modérées (L3-L4)
nav_order: 57
evidence_level: L4
indication_count: 10
---

# Aminophylline
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Aminophylline : De l'indication non renseignée à la migraine

## Résumé en Une Phrase

Aminophylline est un dérivé de la théophylline (méthylxanthine), commercialisé en France sous forme de solution pour perfusion ; le texte de l'indication d'origine n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine** (*migraine disorder*), mais **aucun essai clinique** n'est enregistré et seules **4 publications** indirectes (une revue, deux rapports de cas, une note clinique historique) soutiennent cette piste.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Autorisation annulée uniquement |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, l'aminophylline est un antagoniste non sélectif des récepteurs de l'adénosine et un inhibiteur des phosphodiestérases. Son usage historique concerne le bronchospasme, et elle a aussi été utilisée dans les céphalées post-ponction durale.

Le lien avec la migraine repose sur la signalisation de l'adénosine, impliquée dans la vasodilatation cérébrale et la nociception trigémino-vasculaire. Un cas d'épisode de migraine hémiplégique déclenché par le régadénoson (agoniste A2A de l'adénosine) va dans ce sens. Une revue de 2023 discute aussi l'aminophylline dans la douleur et la migraine.

Cette plausibilité reste toutefois **indirecte** : aucun essai clinique n'est enregistré, et la littérature se limite à une revue, un rapport de cas, une note clinique de 1964 et un cas de syndrome X lié à un excès d'adénosine. Le rapport de similarité avec l'indication d'origine n'a pas pu être évalué, faute d'indication d'origine renseignée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour la migraine.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Revue | Pain Management | La migraine pourrait être liée à un métabolisme énergétique cérébral altéré avec adénosine élevée ; l'aminophylline, antagoniste de l'adénosine, soulagerait la douleur, notamment les céphalées post-ponction durale |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Rapport de cas | J Nucl Cardiol | Épisode de migraine hémiplégique déclenché par le régadénoson (agoniste de l'adénosine) |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Rapport de cas | Can J Cardiol | Patiente avec syndrome X lié à un excès d'effet de l'adénosine (« migraine myocardique ») |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Article clinique historique | Aggiorn Clin Ter | Article historique sur les céphalées, sans résumé disponible |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69586398 | AMINOPHYLLINE RENAUDIN 250 mg/10 ml, solution pour perfusion (statut : annulée) | Solution pour perfusion | Non renseignée |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été identifiées dans la base DDInter. Parmi celles listées :
  - **Majeure** : bupropion (risque accru de convulsions).
  - **Modérées** : antihistaminiques H2 (famotidine, ranitidine, cimétidine, nizatidine), tétracyclines (doxycycline, minocycline, tétracycline), clarithromycine, corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide), préparations de lavage colique (acide picosulfurique, polyéthylène glycol avec électrolytes, sulfate de sodium), acide obéticholique, métréleptine.
  - **Mineure** : lansoprazole.
- **Signaux de sécurité issus de la littérature** : dans l'angor de Prinzmetal, l'arrêt d'un test au dipyridamole par l'aminophylline a déclenché des vasospasmes coronariens. Dans l'hyperthyroïdie, les méthylxanthines peuvent aggraver tachycardie et tremblements.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4 : aucun essai clinique n'est enregistré pour la migraine, la littérature est indirecte, et la seule AMM française est annulée. La donnée de sécurité de la notice, bloquante, manque également.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications, indication d'origine), donnée bloquante pour le dépistage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action via DrugBank.
- Évaluer la faisabilité d'un essai exploratoire (Phase 2) ou d'une revue systématique ciblée sur la migraine et les céphalées post-ponction durale.
- Définir la voie d'administration (la forme actuelle est une perfusion, peu adaptée à un usage chronique dans la migraine) et le plan de gestion des interactions, notamment avec le bupropion.

---

### Autres indications prédites (pour information)

| Maladie | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|
| Hypertension pulmonaire | 99,23 % | L3 | Question de recherche : 1 essai de Phase 1 (sécurité avec l'ambrisentan, 18 volontaires sains) et des études hémodynamiques anciennes ou précliniques ; aucun essai d'efficacité de Phase 2/3 |
| Migraine avec aura du tronc cérébral | 99,84 % | L5 | Hold : aucune preuve spécifique |
| Migraine avec ou sans aura, susceptibilité | 99,82 % | L4 | Hold : doublon de la migraine, sans preuve indépendante |
| Angor de Prinzmetal | 99,33 % | L4 | Hold : signal de sécurité plutôt que bénéfice |
| Neuropathie sciatique | 99,07 % | L5 | Hold : étude préclinique unique |
| Hyperthyroïdie | 99,06 % | L4 | Hold : risque de sécurité plus plausible qu'un bénéfice |

Les autres prédictions (atrophodermie vermiculée, ulérythème ophryogène, cardiopathie cyphoscoliotique) sont de niveau L5 (prédiction du modèle seule) et restent en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

