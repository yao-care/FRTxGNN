---
layout: default
title: Azathioprine
parent: Preuves élevées (L1-L2)
nav_order: 86
evidence_level: L1
indication_count: 10
---

# Azathioprine
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Azathioprine : De la polyarthrite rhumatoïde à la maladie inflammatoire chronique de l'intestin (MICI)

## Résumé en Une Phrase

Azathioprine est un immunosuppresseur (analogue des purines, promédicament de la 6-mercaptopurine), initialement associé au traitement de la polyarthrite rhumatoïde.
Le modèle TxGNN classe en tête de ses prédictions exploitables la **maladie inflammatoire chronique de l'intestin (MICI)**. Cette prédiction s'appuie sur **25 essais cliniques** et **20 publications** pour la MICI. La rectocolite hémorragique, une forme de MICI, est également prédite, avec 15 essais et 20 publications.
Il s'agit toutefois d'un usage déjà bien établi plutôt que d'un véritable repositionnement.

> **Remarque sur le classement :** les deux premières prédictions du modèle (syndrome de microphtalmie colobomateuse-dysplasie rhizomélique et syndrome de brachydactylie-syndactylie) ont des scores TxGNN très élevés, mais sans aucune preuve ni lien mécanistique plausible. Elles relèvent très probablement d'artefacts du graphe de connaissances. Ce rapport se concentre donc sur la première prédiction étayée par des données, la MICI (rang 5), complétée par la rectocolite hémorragique (rang 9).

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Predite | Maladie inflammatoire chronique de l'intestin (MICI) |
| Score de Prediction TxGNN | 99,52 % |
| Niveau de Preuve | L1 |
| Statut de Marche en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 8 (8 annulées) |
| Decision Recommandee | Proceed with Guardrails |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. D'après les analyses compilées pour ce rapport, l'azathioprine est un promédicament de la 6-mercaptopurine. Ses métabolites, les nucléotides de thioguanine, inhibent la synthèse des purines et induisent l'apoptose des lymphocytes T (via l'inhibition de Rac1). Cela atténue la réponse immunitaire muqueuse dérégulée observée dans les MICI.

La polyarthrite rhumatoïde et les MICI sont toutes deux des maladies inflammatoires à médiation immunitaire. Un immunomodulateur qui freine la prolifération lymphocytaire est donc mécanistiquement applicable aux deux. L'azathioprine est d'ailleurs un immunomodulateur établi pour le maintien de la rémission dans les MICI, et les revues Cochrane le soutiennent dans la rectocolite hémorragique. La prédiction est donc cohérente, mais elle reflète un usage clinique existant plutôt qu'une découverte nouvelle.

À l'inverse, les autres prédictions à score élevé (dysplasies squelettiques, malformations des membres, ostéoarthrite, syndrome WHIM, granulomatoses chroniques) n'ont aucun lien mécanistique crédible, voire un rapport bénéfice-risque défavorable (par exemple, une myélosuppression dans le syndrome WHIM).

---

## Preuves d'Essais Cliniques

Sélection des essais les plus pertinents pour la MICI (dont la rectocolite hémorragique) :

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminé (arrêt anticipé) | 242 | Infliximab seul ou associé à l'azathioprine versus azathioprine seule dans la rectocolite hémorragique modérée à sévère ; résultats non fournis |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | En recrutement | 300 | Mirikizumab d'emblée versus traitement standard par azathioprine dans la rectocolite hémorragique récente ; résultats en attente |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | Terminé | 211 | Association infliximab-antimétabolites versus monothérapies dans la maladie de Crohn en rémission sans corticoïdes |
| [NCT02247258](https://clinicaltrials.gov/study/NCT02247258) | Phase 2 | Terminé prématurément | 63 | Azathioprine systématique versus guidée par l'endoscopie pour prévenir la récidive postopératoire de la maladie de Crohn iléale |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Terminé | 83 | Azathioprine versus mésalazine pour prévenir la récidive postopératoire de la maladie de Crohn |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | Terminé prématurément | 31 | Étude de dose d'Imuran dans la maladie de Crohn active sous prednisone |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | Terminé prématurément | 28 | Traitement conventionnel progressif (dont azathioprine) versus infliximab seul dans la rectocolite hémorragique ; très faible effectif |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | Inconnu | 84 | Azathioprine à faible dose + allopurinol versus azathioprine seule dans la rectocolite hémorragique |
| [NCT00521950](https://clinicaltrials.gov/study/NCT00521950) | Non applicable | Terminé | 853 | Dépistage du génotype TPMT avant traitement par thiopurines : soutient les mesures de sécurité plutôt que l'efficacité |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | Terminé | 65 | Azathioprine + infliximab précoces versus corticoïdes + azathioprine dans la colite aiguë sévère |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | ECR | Gut | Essai ACTIVE : infliximab + azathioprine d'emblée versus azathioprine seule dans la colite aiguë sévère répondant aux corticoïdes IV |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Mise à jour de l'efficacité de l'azathioprine et de la 6-mercaptopurine pour le maintien de la rémission dans la rectocolite hémorragique |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Version antérieure de la revue Cochrane sur le maintien de la rémission dans la rectocolite hémorragique |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Méta-analyse | Aliment Pharmacol Ther | Efficacité de l'azathioprine et de la mercaptopurine dans la rectocolite hémorragique |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Revue clinique | J Crohns Colitis | Synthèse sur les thiopurines dans les MICI : maintien de la rémission sans corticoïdes |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Revue | J Gastroenterol Hepatol | Pharmacogénétique et suivi des métabolites de l'azathioprine et de la 6-MP dans les MICI |
| [15177535](https://pubmed.ncbi.nlm.nih.gov/15177535/) | 2004 | Revue | Gastroenterol Clin North Am | Revue critique de l'efficacité et de la toxicité de la 6-MP et de l'azathioprine |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Préclinique/mécanistique | Cell Rep Med | Des bactéries commensales favorisent l'échec de l'azathioprine en réduisant la biodisponibilité de la 6-MP |
| [35501287](https://pubmed.ncbi.nlm.nih.gov/35501287/) | 2022 | Cohorte | J Gastroenterol Hepatol | Risque minime de lymphome et de cancer cutané non mélanocytaire sous thiopurines au long cours (Inde du Nord) |
| [34287682](https://pubmed.ncbi.nlm.nih.gov/34287682/) | 2021 | Revue | J Gastroenterol | Pharmacogénomique des thiopurines et grossesse dans les MICI (variant NUDT15) |

---

## Informations de Marche en France

Toutes les AMM recensées sont annulées. Le texte d'indication approuvée n'est pas renseigné.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60211183 | Azathioprine Teva 50 mg | Comprimé pelliculé | Non renseignée |
| 63935487 | Imurel 50 mg | Poudre pour solution injectable (IV) | Non renseignée |
| 63479140 | Azathioprine Viatris 50 mg | Comprimé pelliculé sécable | Non renseignée |
| 66685747 | Imurel 50 mg (BB Farma) | Comprimé pelliculé | Non renseignée |
| 64841852 | Imurel 25 mg | Comprimé pelliculé | Non renseignée |

---

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Immunosuppresseur antimétabolite (analogue des purines) ; non classé comme antinéoplasique dans les données disponibles |
| Risque de Myelosuppression | Élevé : anémie, thrombocytopénie et leucopénie figurent parmi les maladies associées en contre-indication dans le graphe de connaissances ; le risque est accru en cas de déficit en TPMT/NUDT15 |
| Classification d'Emetogenicite | Données non disponibles |
| Elements de Surveillance | NFS, fonction hépatique et rénale, génotypage TPMT/NUDT15, dosage des métabolites |
| Protection de Manipulation | Consulter la notice et les recommandations locales de manipulation |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : pancréatite, thrombopénie, anémie (dont macrocytaire), insuffisance rénale, infections (dont mycoses et dermatophytoses), lymphomes (dont lymphome primitif du système nerveux central, lymphosarcome et lymphome T hépatosplénique), thrombose des veines hépatiques et syndrome de Budd-Chiari.
- **Interactions médicamenteuses** (100 interactions recensées) : les principales de niveau modéré concernent les aminosalicylés (mésalazine, balsalazide, olsalazine, sulfasalazine). Des interactions mineures existent avec les sels de zinc. Plusieurs autres sont de niveau inconnu (par exemple amphotéricine B, acide acétylsalicylique, metformine, oméprazole). Une revue de la charge d'interactions est recommandée, notamment pour l'allopurinol et les autres myélosuppresseurs.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

---

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 et 4, deux revues Cochrane et un essai randomisé récent (ACTIVE, 2025) soutiennent l'usage de l'azathioprine dans les MICI. Il s'agit toutefois d'un usage déjà établi, et non d'un repositionnement nouveau.
- Les autres prédictions à score élevé (rangs 1 à 4, 6, 8 et 10) sont sans support clinique ou mécanistique et sont maintenues en Hold. L'ostéoarthrite (rang 7) est également en Hold, avec un rapport bénéfice-risque défavorable.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer le texte officiel de la notice (mises en garde, contre-indications, indications) auprès de l'ANSM : donnée bloquante pour le dépistage de sécurité.
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Clarifier la situation réglementaire : les 8 AMM sont annulées, ce qui nécessite de vérifier la disponibilité réelle du produit en France.
- Mettre en place le génotypage TPMT/NUDT15, le suivi des métabolites, la surveillance hématologique et hépatique, ainsi que la surveillance du risque de lymphome et d'infection.
- Examiner l'interaction avec l'allopurinol et les autres myélosuppresseurs.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

