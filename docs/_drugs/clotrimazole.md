---
layout: default
title: Clotrimazole
parent: Preuves élevées (L1-L2)
nav_order: 191
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-14
description: "Clotrimazole : nouvelle indication prédite, Vulvovaginite (niveau de preuve L1). Indication d'origine : Mycoses cutanées (pied d'athlète, dermatophytoses)…"
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
---

# Clotrimazole
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **3** 
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

# Clotrimazole : De la candidose cutanéo-muqueuse à la vulvovaginite

## Résumé en Une Phrase

Clotrimazole est un antifongique azolé, initialement utilisé pour traiter les mycoses cutanées (pied d'athlète, dermatophytoses) et les candidoses cutanées, orales et vulvovaginales.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vulvovaginite**, avec **12 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit toutefois surtout de la confirmation d'un usage déjà établi (candidose vulvovaginale) plutôt que d'un véritable repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses cutanées (pied d'athlète, dermatophytoses), candidoses cutanées, orales et vulvovaginales (le texte d'indication des AMM n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Vulvovaginite |
| Score de Prédiction TxGNN | 99,59 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, le clotrimazole fait partie de la classe des antifongiques azolés ; il inhibe la synthèse de l'ergostérol fongique (enzyme CYP51), ce qui freine la croissance des champignons. Son efficacité dans les candidoses est établie.

La vulvovaginite, en particulier la candidose vulvovaginale, recoupe directement les indications d'origine du médicament (candidose vulvovaginale, candidose). Le mécanisme antifongique cible directement *Candida*, ce qui rend la prédiction cohérente.

Il faut noter que cette prédiction ne constitue pas un repositionnement au sens strict : elle confirme un usage existant. Elle ne vaut pas pour les vulvovaginites non fongiques (vaginose bactérienne, trichomonase).

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | Terminé | 466 | Non-infériorité d'un ovule de clotrimazole 500 mg par rapport au comprimé vaginal 500 mg dans la candidose vaginale |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | Terminé | 1524 | Tinidazole + fluconazole en dose unique vs métronidazole + clotrimazole vaginal chez des femmes avec pertes vaginales (Afrique de l'Ouest) |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | En recrutement | 264 | Clotrimazole + lactulose vs clotrimazole seul dans la vulvovaginite candidosique ; résultats non disponibles |
| [NCT03115073](https://clinicaltrials.gov/study/NCT03115073) | Phase 2/3 | Terminé | 84 | Candiplus® à trois doses vs crème vaginale de clotrimazole 1 % (comparateur actif) |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | Terminé | 150 | Dequalinium (Fluomizin®) vs clotrimazole 100 mg dans la candidose vulvovaginale |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | Terminé | 240 | Comprimé vaginal de clotrimazole vs fluconazole dans la candidose vulvovaginale sévère |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | Terminé | 140 | Clotrimazole avec ou sans Lactobacillus oral pour prévenir les récidives |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | Terminé | 100 | Suppositoires à l'extrait de graines de cumin dans la vulvovaginite candidosique (clotrimazole probablement comparateur) |
| [NCT03024502](https://clinicaltrials.gov/study/NCT03024502) | Phase 1/2 | Inconnu | 90 | Gel mucoadhésif à la propolis (EPP-AF) comparé à la crème de clotrimazole |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | Non applicable | Terminé | 1033 | Enquête de sécurité post-commercialisation de la crème Empecid L (clotrimazole 1 %) |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39362128](https://pubmed.ncbi.nlm.nih.gov/39362128/) | 2024 | Méta-analyse en réseau bayésienne | Eur J Obstet Gynecol Reprod Biol | Traitements d'entretien de la candidose vulvovaginale récidivante : risque de récidive précoce et tardive |
| [39907782](https://pubmed.ncbi.nlm.nih.gov/39907782/) | 2025 | Revue parapluie de revues systématiques | Naunyn-Schmiedeberg's Arch Pharmacol | Synthèse de l'efficacité et de la sécurité des traitements de la candidose vulvovaginale |
| [32992877](https://pubmed.ncbi.nlm.nih.gov/32992877/) | 2020 | Revue systématique | Pharmaceuticals (Basel) | Plus de 45 ans d'expérience clinique du clotrimazole dans la candidose vulvovaginale |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | ECR | Mycoses | Probiotiques et lactoferrine en traitement d'entretien de la candidose vulvovaginale récidivante |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | ECR | Obstet Gynecol | Suppositoires de clotrimazole 500 mg : rémission clinique chez 90,4 % des 42 patientes avec candidose récidivante |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | ECR | Am J Obstet Gynecol | Comprimé unique de 500 mg vs traitement de 6 jours à 100 mg dans la vulvovaginite candidosique (199 patientes) |
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | Essai comparatif | Complement Ther Med | Crème vaginale de *Prangos ferulacea* comparée à la crème de clotrimazole |
| [10394549](https://pubmed.ncbi.nlm.nih.gov/10394549/) | 1999 | Revue | J Reprod Med | Traitements en une journée de la candidose vaginale, dont le clotrimazole |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Revue | J Appl Microbiol | Clotrimazole : usages passés, présents et futurs |
| [41350226](https://pubmed.ncbi.nlm.nih.gov/41350226/) | 2025 | Cohorte | Pharmacoepidemiol Drug Saf | Risque de malformations congénitales majeures après exposition aux antifongiques topiques au premier trimestre |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67301480 | MYCOHYDRALIN 200 mg, comprimé vaginal | Comprimé | Non renseignée (AMM annulée) |
| 62633525 | CLOTRIMAZOLE EG LABO CONSEIL 1 %, crème | Crème | Non renseignée (AMM annulée) |
| 67933494 | MYCOHYDRALIN 500 mg, comprimé vaginal | Comprimé | Non renseignée (AMM annulée) |
| 67777579 | MYCOHYDRALIN, crème | Crème | Non renseignée (AMM annulée) |
| 60070359 | MYCOHYDRALIN 500 mg, capsule vaginale | Capsule | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance corticosurrénale, maladie d'Addison, atrophie cutanée, télangiectasies, maladies capillaires, maladie de Rendu-Osler, maladie vasculaire périphérique, claudication intermittente, artériopathie périphérique.
- **Interactions médicamenteuses** (100 interactions recensées ; extrait des principales) :
  - **Majeures** : fentanyl, alfentanil, amiodarone, hydrocodone.
  - **Modérées** : abémaciclib, paclitaxel, acalabrutinib, nifédipine, lévonorgestrel, alfuzosine, aliskirène, estradiol, alprazolam, noréthistérone, amlodipine, apixaban, aprépitant.
  - **Mineures** : dolutégravir, amphotéricine B.
- **Points de vigilance issus de la littérature** : sécurité au premier trimestre de grossesse (étude récente sur le risque de malformations et étude sur la stéroïdogenèse placentaire), vulvovaginites non candidosiques, formes récidivantes nécessitant un traitement d'entretien.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de Phase 3 et de nombreuses revues soutiennent l'usage du clotrimazole dans la vulvovaginite candidosique, ce qui correspond à une indication déjà connue. Les preuves sont solides pour cette indication, mais les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice officielle (ANSM), actuellement indisponibles et bloquantes pour l'évaluation de sécurité.
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Une clarification du statut réglementaire en France (AMM annulées) et de la voie d'administration requise.
- Un encadrement de l'usage pendant la grossesse, et un diagnostic différentiel des vulvovaginites non fongiques.
- Les résultats de l'essai en cours NCT06835361.

## Autres Indications Prédites (à titre d'information)

- **Acné** (score 99,86 %, niveau L4, décision **Hold**) : le seul essai disponible (NCT01244256, Phase 2/3, suspendu, 80 patients) teste une association fixe (bêclométasone + gentamicine + clotrimazole), ce qui empêche d'attribuer un effet au clotrimazole. Le lien mécanistique est indirect.
- **Vaginite atrophique post-ménopausique** (score 99,46 %, niveau L5, décision **Hold**) : prédiction fondée uniquement sur le modèle. Cette affection est liée à une carence en œstrogènes et non à une infection fongique ; aucun essai ni publication ne la soutient.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

