---
layout: default
title: Phenytoin
parent: Prédiction du modèle uniquement (L5)
nav_order: 601
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin : nouvelle indication prédite, Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Phenytoin
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

## Phenytoin: Néoplasme du nerf trijumeau (trigeminal nerve neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

La phénytoïne est un antiépileptique, utilisé à l'origine pour traiter l'épilepsie (crises tonico-cloniques généralisées, épilepsie partielle, état de mal épileptique, syndrome de Lennox-Gastaut).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **néoplasme du nerf trijumeau**, mais **aucun essai clinique** et **aucune publication pertinente** ne soutiennent cette prédiction : elle repose uniquement sur le modèle (niveau L5).
Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique, avec la névralgie du trijumeau, que la phénytoïne traite effectivement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, la phénytoïne bloque les canaux sodiques voltage-dépendants et limite les décharges neuronales répétitives soutenues, ce qui explique son efficacité dans l'épilepsie.

Ce mécanisme est pertinent pour la **névralgie du trijumeau** (douleur due à des décharges aberrantes de la racine nerveuse), pour laquelle la phénytoïne est utilisée comme option de recours, notamment par voie intraveineuse lors des crises aiguës. Le score élevé du modèle pour la tumeur du nerf trijumeau (0.9999) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique.

Rien n'indique cependant que la phénytoïne possède une activité antitumorale ni qu'elle traite la tumeur elle-même. Les deux publications retrouvées portent sur le traitement de la névralgie du trijumeau et sur le syndrome de Sturge-Weber, et non sur le néoplasme du nerf trijumeau. La prédiction est donc **peu convaincante** sur le plan mécanistique pour cette indication précise.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revue | Expert Rev Neurother | Panorama des traitements médicaux et chirurgicaux de la névralgie du trijumeau ; cause probable : compression vasculaire de la racine du nerf. Ne concerne pas le néoplasme. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Série de cas | An Esp Pediatr | Expérience de 14 cas de syndrome de Sturge-Weber (caractéristiques cliniques, évolution, réponse thérapeutique). Ne concerne pas le néoplasme. |

Aucune de ces publications ne soutient directement l'indication prédite.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62436200 | DILANTIN 250 mg/5 ml, solution injectable (ESTEVE PHARMACEUTICALS) | Solution injectable | Non renseignée (AMM active) |
| 66303560 | DI-HYDAN 100 mg, comprimé sécable (EFISCIENS) | Comprimé sécable | Non renseignée (AMM active) |

Les 2 AMM sur 2 sont valides : la phénytoïne est commercialisée dans ce pays.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : syndrome du QT long (y compris familial) et torsades de pointes ; insuffisance hépatique, maladie hépatique, coma et encéphalopathie hépatiques ; maladie rénale ; porphyries ; thrombopénie, neutropénie, agranulocytose ; diabète, hyperglycémie, acidocétose diabétique ; lupus érythémateux systémique ; hypotension ; troubles anxieux et dysthymiques ; abus ou dépendance à des substances ; syndromes d'apnée du sommeil et d'hypoventilation centrale congénitale (dont syndrome de Haddad).
- **Interactions médicamenteuses** : 390 interactions recensées. Parmi les principales, de niveau modéré : acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, métformine, pioglitazone, alogliptine, albiglutide, bupropion, aprépitant, morphine, oméprazole, métronidazole, cholécalciférol, calcifédiol. L'interaction avec l'acide acétylsalicylique est de niveau mineur.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice : ces informations n'ont pas pu être extraites pour ce rapport.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication spécifique, et semble résulter de la proximité avec la névralgie du trijumeau plutôt que d'un effet sur la tumeur.
- Les AMM françaises sont toutes annulées et le profil de sécurité est lourd (nombreuses contre-indications et interactions).

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données mécanistiques ou précliniques montrant une activité antitumorale de la phénytoïne sur les tumeurs du nerf trijumeau.
- Les données du mécanisme d'action détaillé (DrugBank) et la notice officielle (ANSM) pour l'analyse de sécurité.
- Une recherche bibliographique ciblée sur les néoplasmes du nerf trijumeau.

**Autres pistes issues des prédictions :** la **névralgie du trijumeau** (0.9997, niveau L3, question de recherche) est la piste la mieux étayée, avec des revues, une recommandation européenne et des études rétrospectives de phénytoïne intraveineuse comme traitement de recours ; elle reste toutefois proche de l'indication neurologique existante et sans essai de phase 3 confirmé. Le déficit en bêta-cétothiolase (0.9995) n'a aucun lien mécanistique crédible et correspond probablement à un artefact du modèle.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

