---
layout: default
title: Bupivacaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 123
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Bupivacaine : nouvelle indication prédite, Acrodermatite chronique atrophiante (niveau de preuve L5). Indication d'origine : Dermatite (selon la base de connaissances TxGNN"
monitor_inn: "bupivacaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
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

## Bupivacaïne : De la dermatite à la acrodermatite chronique atrophiante
{: .text-alpha }

## Résumé en Une Phrase

La bupivacaïne est un anesthésique local de type amide, dont l'indication d'origine retenue dans la base de connaissances est la dermatite.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**acrodermatite chronique atrophiante**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatite (selon la base de connaissances TxGNN ; aucun texte d'indication n'est renseigné dans les AMM) |
| Nouvelle Indication Prédite | Acrodermatite chronique atrophiante |
| Score de Prédiction TxGNN | 0,9923 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 6) |
| Nombre d'AMM | 6 (valides : 4) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la bupivacaïne est un anesthésique local de type amide qui bloque les canaux sodiques voltage-dépendants et inhibe ainsi la conduction nerveuse.

Cette prédiction est **difficile à justifier sur le plan mécanistique**. L'acrodermatite chronique atrophiante est une manifestation cutanée tardive de l'infection par *Borrelia*, traitée par antibiotiques. Un bloqueur des canaux sodiques n'a pas de rôle plausible de modification de la maladie. Le score élevé (0,9923) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Les autres prédictions du modèle (dermatomyosite néonatale, dermatomyosite amyopathique, pneumopathie interstitielle de l'enfant associée à une maladie du tissu conjonctif) présentent le même constat : aucun lien mécanistique n'est étayé et aucune preuve clinique n'est disponible. Pour la dermatomyosite néonatale, la myotoxicité locale connue de la bupivacaïne constitue en outre une préoccupation de sécurité.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Parmi les 6 AMM ci-dessous, 4 sont valides ; le médicament est commercialisé.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61578015 | BUPIVACAINE VIATRIS 20 mg/4 ml, voie intrarachidienne (ampoule) | Solution injectable | Non renseignée |
| 66563273 | BUPIVACAINE AGUETTANT 2,5 mg/ml | Solution injectable | Non renseignée |
| 62837780 | BUPIVACAINE POUR RACHIANESTHESIE AGUETTANT 5 mg/ml (voie intrarachidienne) | Solution injectable | Non renseignée |
| 63699439 | BUPIVACAINE ACCORD 2,5 mg/mL | Solution injectable | Non renseignée |
| 61201295 | BUPIVACAINE ACCORD 5 mg/mL | Solution injectable | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, insuffisance hépatique, maladie hépatique, maladie rénale, épilepsie, BPCO, insuffisance respiratoire, hypothyroïdie, myxœdème, maladie inflammatoire de l'intestin, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, fibrillation auriculaire, coronaropathie, infarctus du myocarde, arrêt cardiaque soudain, maladie de la conduction cardiaque, hypotension, hémoglobinopathie, carence en potassium, abus/dépendance de substances, glaucome à angle fermé, entre autres.
- **Interactions médicamenteuses** : 56 interactions recensées. Parmi les principales de niveau modéré : aprépitant et morphine (liposomale). Les autres (par exemple pantoprazole, oméprazole, lansoprazole, vancomycine, atropine, corticoïdes, simvastatine, ondansétron, métoclopramide, naloxone) ont un niveau de gravité non précisé.
- **Risques liés à une exposition systémique** : risque de cardiotoxicité, sans bénéfice démontré dans les indications prédites.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible avec une infection tardive à *Borrelia*.
- Sur les 6 AMM françaises, 4 sont valides, et les données de sécurité de la notice sont manquantes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications) afin de permettre le criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Recherche ciblée d'études précliniques ou observationnelles justifiant un lien avec l'indication prédite
- Vérification de la compatibilité de la voie d'administration avec la nouvelle indication
- Clarification de la pertinence de l'indication d'origine « dermatite » (aucun texte d'indication dans les AMM)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

