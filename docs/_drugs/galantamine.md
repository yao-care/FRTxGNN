---
layout: default
title: Galantamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 354
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Galantamine : nouvelle indication prédite, Troubles du mouvement psychogènes (niveau de preuve L5). Indication d'origine : Maladie d'Alzheimer"
---

# Galantamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Galantamine : De la maladie d'Alzheimer aux troubles du mouvement psychogènes

## Résumé en Une Phrase

La galantamine est un inhibiteur de la cholinestérase, initialement utilisé dans le traitement de la maladie d'Alzheimer.
Le modèle TxGNN la prédit comme potentiellement efficace pour les **troubles du mouvement psychogènes**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement informatique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie d'Alzheimer (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Troubles du mouvement psychogènes |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 16 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la galantamine est un inhibiteur de la cholinestérase et un modulateur allostérique des récepteurs nicotiniques. Son efficacité symptomatique dans la maladie d'Alzheimer repose sur le renforcement de la transmission cholinergique.

Le lien avec les troubles du mouvement psychogènes (fonctionnels) n'est pas établi : aucune donnée ne relie la modulation cholinergique à cette pathologie. Le score élevé du modèle TxGNN reflète une proximité dans le graphe de connaissances, pas une preuve biologique ou clinique.

**Autres indications prédites (à titre indicatif, toutes en Hold) :**

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Tic chronique | 99,89 % | L5 | Hypothèse spéculative (interneurones cholinergiques striataux), sans données |
| 3 | Tremblement orthostatique primaire | 99,89 % | L5 | Aucun lien mécanistique démontré |
| 4 | Frissons bénins du nourrisson | 99,88 % | L5 | Affection bénigne, rapport bénéfice/risque défavorable |
| 5 | Maladies extrapyramidales et du mouvement | 99,88 % | L4 | Littérature surtout sur des mouvements anormaux *induits* par les inhibiteurs de cholinestérase (signal de sécurité) |
| 6 | Syndrome tremblement-nystagmus-ulcère duodénal | 99,88 % | L5 | Préoccupation théorique : risque ulcéreux gastro-intestinal |
| 7 | Dyskinésie linguo-faciale-buccale | 99,88 % | L4 | Données spécifiques à la galantamine uniquement précliniques, sauf un essai croisé randomisé sur la dyskinésie tardive |
| 8 | Élévation tonique paroxystique bénigne du regard avec ataxie | 99,88 % | L5 | Aucun mécanisme cholinergique connu |
| 9 | Porphyrie aiguë intermittente | 99,71 % | L5 | Aucun lien plausible ; sécurité en porphyrie non évaluée |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication principale (troubles du mouvement psychogènes).

---

## Informations de Marché en France

Les 16 AMM recensées sont annulées. Le texte d'indication approuvée n'est pas disponible dans les données compilées. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 62031593 | GALANTAMINE TEVA SANTE LP 8 mg | Gélule à libération prolongée | Annulée |
| 63358402 | GALANTAMINE BIOGARAN LP 8 mg | Gélule à libération prolongée | Annulée |
| 64679350 | GALANTAMINE KRKA LP 16 mg | Gélule à libération prolongée | Annulée |
| 61601453 | REMINYL 4 mg/mL | Solution buvable | Annulée |
| 61611472 | GALANTAMINE ZENTIVA LAB LP 24 mg | Gélule à libération prolongée | Annulée |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : syndrome du QT long familial, insuffisance hépatique, maladie hépatique, maladie rénale, épilepsie, bronchopneumopathie chronique obstructive (BPCO), asthme (intrinsèque et allergique), ulcère gastroduodénal et duodénal, maladie de la vésicule biliaire, obstruction du col vésical, pyo-uretère, bloc auriculo-ventriculaire.
- **Interactions médicamenteuses** : 173 interactions recensées. Parmi les principales :
  - **Majeure** : bupropion.
  - **Modérées** : anticholinergiques (atropine, hyoscyamine, dicyclomine, glycopyrronium, clidinium, trospium), antihistaminiques H2 (famotidine, ranitidine, cimétidine), clarithromycine, métronidazole, dolasétron, palonosétron, éliglustat, lopéramide, lorcasérine, et certains laxatifs/préparations coliques (acide picosulfurique, polyéthylène glycol avec électrolytes, sulfate de sodium).
- **Signaux de sécurité issus de la littérature** : les inhibiteurs de cholinestérase peuvent induire ou aggraver des mouvements anormaux (parkinsonisme, tremblement, syndrome de Pise), ce qui est défavorable pour les indications de type troubles du mouvement.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et sans lien mécanistique établi avec les troubles du mouvement psychogènes.
- Toutes les AMM françaises sont annulées, et les données de sécurité de la notice sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) pour le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Établir un lien mécanistique ou des données précliniques/cliniques pour l'indication ciblée.
- Si l'axe « troubles du mouvement » est poursuivi, évaluer d'abord le signal de sécurité des inhibiteurs de cholinestérase (aggravation de mouvements anormaux).
- Clarifier les raisons de l'annulation des AMM et la possibilité de disposer d'une formulation commercialisée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

