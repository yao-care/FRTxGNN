---
layout: default
title: Exemestane
parent: Prédiction du modèle uniquement (L5)
nav_order: 313
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Exemestane : nouvelle indication prédite, Déficience en antithrombine de type 2 (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "exemestane"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura"]
---

# Exemestane
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Exémestane : Du Cancer du Sein à la Déficience en Antithrombine de Type 2
{: .text-alpha }

## Résumé en Une Phrase

L'exémestane est un inhibiteur stéroïdien irréversible de l'aromatase, qui réduit les taux d'œstrogènes. Les données compilées pour ce rapport ne précisent pas d'indication originale dans les AMM françaises.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **déficience en antithrombine de type 2**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Déficience en antithrombine de type 2 |
| Score de Prédiction TxGNN | 0,9983 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 16 sur 16) |
| Nombre d'AMM | 16 (valides : 16) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances générales, l'exémestane est un inhibiteur stéroïdien irréversible de l'aromatase : il bloque la conversion des androgènes en œstrogènes et abaisse ainsi les taux d'œstradiol.

La déficience en antithrombine de type 2 est un trouble héréditaire de la coagulation, lié à des variants du gène SERPINC1. **Aucun lien mécanistique n'a été identifié** : l'abaissement des œstrogènes n'est pas connu pour corriger la fonction de l'antithrombine. Le score élevé (0,9983) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Les autres prédictions du modèle se situent dans la même zone (coagulation et thrombophilie) ou concernent des pathologies sans lien démontré :

| Rang | Maladie prédite | Score | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Aménorrhée | 0,9982 | L4 | Littérature indirecte (l'aménorrhée est un état lié au traitement du cancer du sein, pas une cible thérapeutique) |
| 3 | Excès de facteur V avec thrombose spontanée | 0,9982 | L5 | Aucun rationnel mécanistique |
| 4 | Déficit en cofacteur II de l'héparine | 0,9982 | L5 | Aucun lien identifié |
| 5 | Thrombophilie | 0,9967 | L5 | Les inhibiteurs de l'aromatase comportent plutôt un risque thromboembolique |
| 6 | Migraine | 0,9902 | L5 | Lien hormonal hypothétique, sens de l'effet incertain |
| 7 | Migraine avec aura du tronc cérébral | 0,9901 | L5 | Spéculatif, sans données |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la déficience en antithrombine de type 2.

À titre indicatif, 5 publications ont été retrouvées pour la 2ᵉ prédiction (aménorrhée). Elles sont indirectes : l'aménorrhée y est un contexte ou un critère de suivi du cancer du sein, et non une maladie traitée par l'exémestane.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohorte | Annals of Oncology | Récupération de la fonction ovarienne chez des patientes avec aménorrhée induite par la chimiothérapie, passées du tamoxifène à l'exémestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Revue | Oncology (Williston Park) | Rôle de la suppression ovarienne chez les femmes préménopausées avec cancer du sein précoce RH+ |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Revue | Journal of Clinical Oncology | Nécessité du suivi de l'œstradiol sous suppression ovarienne dans le cancer du sein |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Revue | Recenti Progressi in Medicina | Place des analogues de la LHRH dans le cancer du sein chez les patientes préménopausées |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Revue | Klinicka Onkologie | Inhibiteurs de l'aromatase chez les femmes ménopausées avec cancer du sein et gestion des effets indésirables |

---

## Informations de Marché en France

Les 16 AMM sur 16 sont valides. Le texte d'indication n'est pas renseigné dans les données compilées. Principales AMM (5 sur 16) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66922032 | EXEMESTANE TEVA 25 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 69225138 | AROMASINE 25 mg (Pfizer) | Comprimé enrobé | Non renseignée (AMM active) |
| 64144682 | EXEMESTANE ZENTIVA 25 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 69233035 | AROMASINE 25 mg (Difarmed) | Comprimé enrobé | Non renseignée (AMM active) |
| 61396272 | EXEMESTANE ZYDUS FRANCE 25 mg | Comprimé enrobé | Non renseignée (AMM active) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Hormonothérapie (inhibiteur stéroïdien de l'aromatase), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible (pas de donnée de toxicité compilée ; à vérifier dans la notice) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 203 interactions recensées. Les plus notables, de niveau modéré : **dexaméthasone** et **troglitazone**. Les autres interactions listées (pantoprazole, morphine, metformine, oméprazole, lansoprazole, simvastatine, chlorure de potassium, ranitidine, ondansétron, métronidazole, famotidine, acide acétylsalicylique, sucralfate, rosiglitazone, lactulose, rosuvastatine, orlistat, rabéprazole) ont un niveau de gravité non précisé.
- **Point d'attention thromboembolique** : les inhibiteurs de l'aromatase s'accompagnent d'une alerte thromboembolique ; ce point est particulièrement critique pour les prédictions touchant la coagulation et la thrombophilie.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5), sans essai clinique, sans publication et sans lien mécanistique plausible. Les AMM françaises sont toutes annulées, et le profil de risque thromboembolique des inhibiteurs de l'aromatase va à l'encontre d'un usage dans les troubles de la coagulation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) détaillées
- Notice officielle (mises en garde et contre-indications), indispensable pour le dépistage de sécurité
- Indication originale d'après les textes d'AMM
- Preuves précliniques ou mécanistiques reliant l'inhibition de l'aromatase à la fonction de l'antithrombine
- Évaluation de sécurité thromboembolique avant toute poursuite
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

