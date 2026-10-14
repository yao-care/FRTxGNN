---
layout: default
title: Goserelin
parent: Prédiction du modèle uniquement (L5)
nav_order: 371
evidence_level: L5
indication_count: 3
---

# Goserelin
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

# Goséréline : De l'Endométriose à l'Aménorrhée

## Résumé en Une Phrase

La goséréline est un agoniste de la GnRH, initialement utilisé pour le traitement de l'endométriose.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**aménorrhée**, mais il s'agit surtout d'un effet pharmacodynamique recherché (suppression ovarienne réversible) plutôt que du traitement d'une aménorrhée pathologique.
Les données compilées pour ce rapport comptent **1 essai clinique** (de pertinence indirecte) et **15 publications**, dont quelques essais randomisés portant surtout sur le cancer du sein.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Endométriose (source : graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Aménorrhée |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L2 (selon l'évaluation des données ; preuve directe limitée, voir ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations structurées. Sur la base des connaissances pharmacologiques établies, la goséréline est un agoniste de la GnRH : une administration continue désensibilise les récepteurs de la GnRH de l'hypophyse, ce qui réduit la sécrétion de LH et de FSH puis la production d'œstradiol par les ovaires. Il en résulte une aménorrhée réversible.

Cet effet est bien documenté dans le cancer du sein de la femme non ménopausée (suppression ou ablation ovarienne) et dans l'endométriose, l'indication d'origine. L'aménorrhée est donc ici une conséquence attendue du traitement, et non une maladie que le médicament guérirait. Elle pourrait servir à supprimer les menstruations (saignements abondants, contexte de chimiothérapie, protection ovarienne).

Il faut en revanche noter que la goséréline ne traiterait pas les aménorrhées d'origine hypothalamique ou autres, qu'elle pourrait même aggraver. Le score élevé du modèle reflète donc surtout cette association pharmacodynamique, et non un bénéfice thérapeutique sur l'aménorrhée pathologique.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Inconnu | 300 | Torémifène adjuvant avec ou sans goséréline chez des femmes non ménopausées atteintes d'un cancer du sein à récepteurs hormonaux positifs, avec ou sans aménorrhée induite par la chimiothérapie. L'aménorrhée n'est pas le critère principal ; le soutien est indirect. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | ECR | J Clin Oncol | Goséréline versus CMF en adjuvant chez des patientes non ménopausées avec cancer du sein à ganglions positifs (étude ZEBRA) |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | ECR | J Natl Cancer Inst | Chimiothérapie suivie de goséréline versus chaque modalité seule (IBCSG Trial VIII) |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | ECR (analyse secondaire) | J Clin Oncol | Impact sur l'aménorrhée, les bouffées de chaleur et la qualité de vie (IBCSG VIII) |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | ECR | Fertil Steril | Agoniste de la GnRH versus contraceptif oral faiblement dosé pour la douleur pelvienne de l'endométriose |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Revue/Méta-analyse | Ann Oncol | Essai OPTION : agoniste de la GnRH pour protéger les ovaires pendant la chimiothérapie du cancer du sein précoce |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohorte | Cancer Res Treat | Ablation ovarienne par goséréline et survie en l'absence d'aménorrhée induite par la chimiothérapie |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohorte | J Clin Oncol | Faut-il surveiller l'œstradiol sous suppression ovarienne ? |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revue | J R Army Med Corps | Induction thérapeutique de l'aménorrhée ; la goséréline est présentée comme très efficace |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Revue | Breast Cancer Res Treat | Agonistes de la LHRH dans le cancer du sein précoce : ablation ovarienne réversible |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Revue | Br J Surg | Ablation ovarienne en adjuvant dans le cancer du sein |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66669173 | ZOLADEX 10,8 mg, implant en seringue préremplie pour voie sous-cutanée (AstraZeneca) | Implant | Non renseignée (AMM annulée) |
| 67037162 | ZOLADEX 3,6 mg, implant en seringue préremplie pour voie sous-cutanée (AstraZeneca) | Implant | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (à confirmer avec la notice, il ne s'agit pas du texte officiel) : hypertension artérielle, hyperglycémie, diabète, acidocétose diabétique, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, obésité (dont obésité monogénique), obstruction des voies urinaires.
- **Interactions médicamenteuses** : 371 interactions recensées. Parmi celles listées, une est **majeure** (dolasétron) ; les autres sont modérées, notamment avec les antidiabétiques (acarbose, metformine, glimépiride, chlorpropamide, inhibiteurs de la DPP-4, inhibiteurs du SGLT2, agonistes du GLP-1), la clarithromycine, le palonosétron, le famotidine, le lopéramide et plusieurs laxatifs (bisacodyl, acide picosulfurique, polyéthylène glycol).

Les mises en garde et contre-indications officielles de la notice n'ont pas été obtenues : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'aménorrhée est un effet pharmacodynamique attendu de la goséréline, et non une indication thérapeutique démontrée. Le seul essai clinique est indirect (critère oncologique) et aucune preuve directe n'étaye un traitement de l'aménorrhée pathologique.
- Les deux AMM françaises sont annulées et les données de sécurité officielles sont absentes, ce qui bloque le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice de l'ANSM (mises en garde, contre-indications).
- Compléter les données sur le mécanisme d'action (DrugBank).
- Définir précisément l'usage visé (suppression menstruelle induite plutôt que traitement de l'aménorrhée) et chercher des essais directs sur ce point.
- Clarifier le statut réglementaire en France (AMM annulées).

**Remarque sur les autres prédictions :** l'atrophie rénale congénitale (hypoplasie rénale, unilatérale et bilatérale) a des scores TxGNN élevés (environ 99 %), mais sans essai ni publication, sans lien mécanistique plausible (niveau L5, Hold). Ces prédictions sont probablement des artefacts du réseau de connaissances.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

