---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Hydrocortisone : Du Traitement Anti-inflammatoire à la Pelade (Alopecia Areata)

## Résumé en Une Phrase

L'hydrocortisone est un glucocorticoïde de référence, largement utilisé comme traitement anti-inflammatoire et immunosuppresseur ainsi que dans la substitution de l'insuffisance surrénalienne.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Alopecia Areata (Pelade)**,
avec **4 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---------|---------|
| Indication Originale | Non renseignée dans le registre TFDA (médicament non commercialisé) |
| Nouvelle Indication Prédite | Alopecia Areata (Pelade) |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L1 |
| Statut de Marché (TFDA) | ✗ Non commercialisé |
| Nombre d'AMM TFDA | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

L'hydrocortisone est un glucocorticoïde endogène et médicamenteux agissant via les récepteurs aux glucocorticoïdes (GR). En se liant aux GR, il inhibe le facteur de transcription NF-κB, supprime la production de cytokines pro-inflammatoires (IL-2, IFN-γ, TNF-α) et atténue l'activation des lymphocytes T CD8+. Ces mécanismes sont bien établis dans la littérature pharmacologique, même si les données détaillées de mécanisme d'action ne sont pas disponibles dans le présent dossier réglementaire TFDA.

L'alopecia areata est une maladie auto-immune médiée par les lymphocytes T CD8+, qui attaquent les follicules pileux et détruisent leur « privilège immunologique ». Cette convergence mécanistique est directe : l'hydrocortisone peut restaurer le micro-environnement périfolliculaire en supprimant l'infiltrat lymphocytaire responsable de la chute de cheveux. L'application topique ou l'injection intralésionnelle permettent une action locale ciblée, limitant l'exposition systémique.

Ce lien n'est pas uniquement théorique. Dès 1956, des séries cliniques rapportaient l'utilisation de l'hydrocortisone dans la pelade, et un essai randomisé contrôlé de Phase 3 publié dans *JAMA Dermatology* en 2014 a directement comparé la crème hydrocortisone 1 % à la crème clobétasol 0,05 % chez l'enfant atteint de pelade. L'usage des corticoïdes topiques dans la pelade est aujourd'hui une pratique clinique courante dans de nombreux pays.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|----------------|-------|--------|-------------|----------------------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Terminé | 41 | ECR comparant hydrocortisone 1 % crème vs clobétasol 0,05 % crème chez l'enfant atteint de pelade ; résultats publiés (PMID 24226568). Preuve directe de la plus haute pertinence. |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Terminé | 18 | Impact des injections intralésionnelles de triamcinolone sur la fonction surrénalienne dans la pelade ; l'hydrocortisone sert d'indicateur de la réponse de l'axe HPA, données de sécurité pertinentes. |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Pas encore recruté | 72 | Étude dose-réponse en quadruple bras sur des produits de croissance capillaire dans l'alopécie androgénétique légère à modérée ; pertinence indirecte pour la dose. |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Terminé | 380 | Étude du métabolome stéroïdien anormal sur la qualité osseuse dans le contexte d'adénomes surrénaliens (MACS) ; fournit des données de contexte sur le métabolisme des stéroïdes. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|----------------------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | ECR | JAMA Dermatology | ECR Phase 3 comparant directement hydrocortisone 1 % vs clobétasol 0,05 % chez l'enfant atteint de pelade ; résultat primaire publié, preuve de la plus haute pertinence. |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Revue systématique / Étude clinique | Clinical and Experimental Dermatology | Efficacité et sécurité des corticoïdes topiques sous occlusion pour la pelade sévère (AT/AU) chez l'enfant ; analyse rétrospective monocentrique, résultats sur corticoïdes de différentes puissances. |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Revue systématique et méta-analyse | Journal of Cosmetic Dermatology | Revue des lasers fractionnés seuls ou en association dans la pelade ; mentionne les associations avec corticoïdes comme traitement de référence de comparaison. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Série clinique précoce | Medical Times | Première série clinique documentant le traitement de la pelade (partialis, totalis) par cortisone, hydrocortisone et analogues (prednisone, prednisolone) ; référence historique fondatrice. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Rapport clinique | Der Hautarzt | Repousse capillaire dans la pelade areata et maligna après injection intracutanée d'hydrocortisone ; preuve directe du bénéfice de la voie intralésionnelle. |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Étude clinique | Vestnik Dermatologii | Traitement de la pelade et de l'alopécie totale par injections intracutanées d'hydrocortisone ; série de cas avec suivi. |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Rapport clinique | Actas Dermo-Sifiliográficas | Injections intradermiques d'hydrocortisone dans la pelade ; preuve clinique directe supplémentaire de la voie locale. |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Revue | JEADV | Hyperactivité de l'axe HPA dans la pelade : évaluation du rôle du cortisol et de la MSH ; fournit le contexte neuroendocrinien de la pathophysiologie. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Rapport de cas | JAAD | Quatre cas de pelade congénitale avec suivi de 3 à 5 ans ; les traitements utilisés incluent la gamme des corticoïdes topiques, dont l'hydrocortisone. |
| [39506493](https://pubmed.ncbi.nlm.nih.gov/39506493/) | 2025 | Étude clinique exploratoire | Journal of Cosmetic Dermatology | Impact du stress psychologique chronique sur le vieillissement cutané ; décrit le déclenchement de la pelade via la libération de cortisol et d'épinéphrine, contextualisant le rôle de l'axe HPA. |

---

## Considerations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans le dossier réglementaire TFDA actuel pour ce médicament.

> Veuillez consulter la notice pour les informations de sécurité complètes. Une attention particulière est recommandée pour l'usage prolongé de corticoïdes topiques (risque d'atrophie cutanée, suppression de l'axe HPA avec les formulations de forte puissance).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Un essai randomisé contrôlé de Phase 3 (NCT01453686 / PMID 24226568) a directement évalué l'hydrocortisone dans la pelade chez l'enfant, et de multiples séries cliniques historiques ainsi qu'une revue systématique récente (2024) soutiennent l'usage des corticoïdes topiques comme traitement établi de la pelade. Le lien mécanistique est bien documenté et cohérent. Le niveau de preuve L1 justifie une progression sous conditions.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données détaillées de mécanisme d'action (MOA) via DrugBank API (DG002)
- Télécharger et analyser la notice TFDA pour les mises en garde et contre-indications (DG001)
- Vérifier la disponibilité des formulations appropriées (crème topique 1 %, solution injectable intralésionnelle) pour l'indication pelade
- Définir le plan de surveillance de sécurité : risque de suppression surrénalienne (axe HPA) avec l'usage prolongé, surtout chez l'enfant
- Évaluer la comparaison d'efficacité avec les corticoïdes de forte puissance (clobétasol) et les nouveaux inhibiteurs de JAK (baricitinib, ritlecitinib) désormais approuvés dans la pelade sévère, afin de positionner l'hydrocortisone dans l'algorithme thérapeutique actuel
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

