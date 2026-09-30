---
layout: default
title: Milrinone
parent: Prédiction du modèle uniquement (L5)
nav_order: 195
evidence_level: L5
indication_count: 10
---

# Milrinone
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

# Milrinone : De l'insuffisance cardiaque aiguë à l'alopécie

## Résumé en Une Phrase

La milrinone est un inhibiteur de la PDE3 (« inodilatateur »), utilisé par voie injectable en milieu hospitalier. Son indication d'origine n'est pas renseignée dans les données ANSM fournies, mais l'usage connu est l'insuffisance cardiaque aiguë.
Le modèle TxGNN prédit qu'elle pourrait être efficace contre l'**alopécie**, avec un score très élevé, mais **aucun essai clinique et aucune publication** ne soutient cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (usage connu : insuffisance cardiaque aiguë) |
| Nouvelle Indication Prédite | Alopécie |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, la milrinone inhibe la PDE3, ce qui augmente l'AMPc. Il en résulte une meilleure contractilité cardiaque et une vasodilatation.

Le lien avec l'alopécie est **spéculatif**. On pourrait imaginer un effet de type vasodilatateur sur le follicule pileux, mais aucune donnée ne l'étaye. Le score élevé reflète probablement un artefact du graphe de connaissances : plusieurs termes voisins (hypotrichose, alopécie en plaques) obtiennent des scores similaires, ce qui suggère une simple proximité dans le graphe. Il ne s'agit pas d'un signal biologique démontré. L'alopécie en plaques est auto-immune, et les hypotrichoses sont des atteintes folliculaires héréditaires. Aucune n'a de lien plausible avec la PDE3.

## Autres Indications Prédites

Le modèle a produit 10 prédictions. Les plus solides ne concernent pas les cheveux.

| Rang | Indication | Score TxGNN | Niveau | Décision |
|------|------|------|------|------|
| 1 | Alopécie | 99,91 % | L5 | Hold |
| 2 | Hypotrichose simple du cuir chevelu | 99,90 % | L5 | Hold |
| 3 | Hypotrichose congénitale avec milia | 99,89 % | L5 | Hold |
| 4 | Alopécie en plaques diffuse | 99,88 % | L5 | Hold |
| 5 | Céphalée (cas de syndrome de vasoconstriction cérébrale réversible) | 99,46 % | L4 | Research Question |
| 6 | Insuffisance cardiaque congestive | 99,45 % | L2 | Proceed with Guardrails |
| 7 | Migraine | 99,45 % | L5 | Hold |
| 8 | Migraine avec aura du tronc cérébral | 99,38 % | L5 | Hold |
| 9 | Céphalée autonomique trigéminale | 99,25 % | L5 | Hold |
| 10 | Cœur pulmonaire aigu | 99,19 % | L3 | Research Question |

- **Insuffisance cardiaque congestive** : c'est un usage déjà établi de la milrinone, donc pas un vrai repositionnement. Le dossier compte des méta-analyses milrinone vs dobutamine et des études de cohorte. Il ne contient pas d'ECR de phase 3 spécifique à la milrinone, d'où le niveau L2.
- **Céphalée** : la littérature se limite à des cas de syndrome de vasoconstriction cérébrale réversible (dont une administration intra-artérielle), un syndrome vasospastique. Elle ne concerne pas les céphalées primaires.
- **Cœur pulmonaire aigu** : les données portent surtout sur la milrinone inhalée, avec de petites études hémodynamiques et des revues.

## Preuves d'Essais Cliniques

Aucun essai clinique associé à l'alopécie n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée à l'alopécie n'est disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61448776 | COROTROPE 10 mg/10 ml | Solution injectable IV | Sanofi Winthrop Industrie |
| 61412965 | MILRINONE TILLOMED 1 mg/mL | Solution injectable ou pour perfusion | Tillomed Pharma (Allemagne) |
| 65725263 | MILRINONE CARINOPHARM 1 mg/ml | Solution injectable ou pour perfusion | Carinopharm (Allemagne) |
| 64507226 | MILRINONE STRAGEN 1 mg/ml | Solution injectable | Stragen France |

Le texte d'indication approuvée n'est pas fourni pour ces AMM. Toutes les présentations sont injectables, sans forme topique ni orale.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde, contre-indications et interactions ne sont pas disponibles dans le dossier.

Point de vigilance d'ordre général, tiré de l'analyse du modèle : hypotension, arythmies et adaptation de la dose à la fonction rénale. Une éventuelle application capillaire nécessiterait en outre une étude de tolérance systémique spécifique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication prédite en rang 1 (alopécie) repose uniquement sur le score du modèle (L5). Il n'y a ni essai, ni publication, ni mécanisme plausible.
- Les prédictions capillaires (rangs 1 à 4) semblent être un artefact de proximité dans le graphe.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications), lacune bloquante pour le criblage de sécurité
- Obtenir les données de mécanisme d'action via DrugBank
- Recentrer l'évaluation sur les pistes mieux documentées : syndrome de vasoconstriction cérébrale réversible et milrinone inhalée dans l'hypertension pulmonaire et la défaillance ventriculaire droite
- Pour l'alopécie, aucune étape n'est justifiée tant qu'aucune donnée préclinique n'existe

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

