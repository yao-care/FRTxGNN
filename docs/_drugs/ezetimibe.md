---
layout: default
title: Ezetimibe
parent: Preuves élevées (L1-L2)
nav_order: 314
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **4** 
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

# Ézétimibe : De l'Hyperlipidémie à l'Hyperlipoprotéinémie

## Résumé en Une Phrase

L'ézétimibe est un inhibiteur de l'absorption intestinale du cholestérol, initialement utilisé dans le traitement de l'hyperlipidémie, de l'hypercholestérolémie familiale (y compris homozygote) et de la sitostérolémie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperlipoprotéinémie**, avec **40 essais cliniques** et **19 publications** associés dans les données compilées pour ce rapport.
Il s'agit toutefois d'une indication très proche de l'indication d'origine : cette prédiction relève davantage d'un usage déjà établi que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperlipidémie (y compris hypercholestérolémie familiale et sitostérolémie) |
| Nouvelle Indication Prédite | Hyperlipoprotéinémie |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

*Remarque : les textes d'indication approuvée de l'ANSM sont vides dans les données compilées ; l'indication originale provient du graphe de connaissances TxGNN (PrimeKG).*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action issues de DrugBank ne sont pas disponibles. Sur la base des informations connues, l'ézétimibe inhibe la protéine NPC1L1, qui assure l'absorption intestinale du cholestérol alimentaire et biliaire. Cette inhibition réduit le LDL-cholestérol, seule ou en association avec une statine.

L'hyperlipoprotéinémie et l'hyperlipidémie désignent des troubles très voisins du métabolisme lipidique. La prédiction recoupe donc directement l'indication d'origine : on peut la considérer comme une utilisation dans l'indication déjà reconnue plutôt que comme un repositionnement au sens strict.

Plusieurs essais impliquent l'ézétimibe comme traitement de fond ou en association (statines, inhibiteurs de PCSK9, acide bempédoïque, obicétrapib). La contribution propre de l'ézétimibe doit donc être distinguée de celle du partenaire thérapeutique.

**Autres prédictions du modèle (preuves faibles, niveau L5, décision Hold) :**
- **Hypercholestérolémie par déficit en cholestérol 7α-hydroxylase** (score 99,25 %) : lien mécanistique plausible, mais aucun essai clinique ; une seule publication préclinique (PMID 34943976) sur la déficience en NPC1L1 chez la souris.
- **Déficit en protéine de transfert des esters de cholestérol (CETP)** (score 99,09 %) : aucun essai clinique ; seulement une revue générale et une étude animale, sans lien spécifique établi avec l'ézétimibe.

L'hypercholestérolémie familiale (score 99,38 %) est également prédite, mais fait déjà partie des indications d'origine ; elle est appuyée par des essais de phase 3 (niveau L1).

---

## Preuves d'Essais Cliniques

Sélection parmi les essais les plus pertinents pour l'hyperlipoprotéinémie :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminé prématurément | 49 | Étude ouverte d'usage compassionnel de l'ézétimibe 10 mg/j dans l'hypercholestérolémie familiale homozygote ou la sitostérolémie ; soutient la sécurité plus que l'efficacité |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Terminé | 50 | Ézétimibe 10 mg ajouté à l'atorvastatine ou la simvastatine dans l'HF homozygote |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Terminé | 1220 | Ézétimibe/simvastatine et niacine dans l'hyperlipidémie de type IIa/IIb |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Terminé | 576 | Fénofibrate + ézétimibe dans l'hyperlipidémie mixte |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Terminé | 611 | Ézétimibe/simvastatine + fénofibrate dans l'hyperlipidémie mixte |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Terminé | 511 | Évolocumab versus ézétimibe chez des patients intolérants aux statines ; l'ézétimibe est le comparateur |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Terminé | 40 | Ézétimibe seul versus statine dans l'hypercholestérolémie ; petite étude ouverte |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | Terminé | 127 | Association ézétimibe/rosuvastatine dans l'hypertension et l'hyperlipidémie |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Terminé | 1794 | Surveillance post-commercialisation de 52 semaines (Zetia) au Japon ; données de sécurité à long terme |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Terminé | 4105 | Surveillance post-commercialisation de l'ézétimibe aux Philippines |

Pour l'hypercholestérolémie familiale, des essais complémentaires de phase 3 existent, notamment [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) (sécurité à long terme, 44 patients), [NCT00867165](https://clinicaltrials.gov/study/NCT00867165) (ézétimibe versus placebo chez l'enfant, 138 patients, randomisé en double aveugle) et [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) (adolescents HeFH, 248 patients).

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECR (phase 3) | Lancet | Association fixe obicétrapib/ézétimibe (TANDEM) pour réduire le LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECR | JAMA | Inhibiteur oral de PCSK9 (enlicitide) dans l'HF hétérozygote ; ézétimibe non spécifique |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | ECR | Circulation | Inclisiran dans l'HF homozygote (ORION-5) ; ézétimibe non spécifique |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | ECR | Lancet | Évolocumab dans l'HF hétérozygote (RUTHERFORD-2), malgré statines ± ézétimibe |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohorte rétrospective | Lancet | Expérience mondiale de l'HF homozygote et résultats cliniques |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revue | Mol Med Rep | Avancées dans les médicaments ciblant l'hyperlipidémie |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revue | J Am Coll Cardiol | Thérapies nouvelles et émergentes de réduction du LDL-C, en complément des statines et de l'ézétimibe |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Mise à jour | Drug Ther Bull | Mise à jour sur l'ézétimibe ; réduction du LDL-C seul ou avec statine |
| [38338819](https://pubmed.ncbi.nlm.nih.gov/38338819/) | 2024 | Rapport de cas | Int J Mol Sci | Cas probable de sitostérolémie avec baisse marquée du LDL-C sous ézétimibe |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Revue | Cardiol Clin | L'ézétimibe figure parmi les traitements de l'hypercholestérolémie familiale |

La plupart des publications sont des revues ou des études portant sur d'autres molécules ; peu d'ECR évaluent l'ézétimibe isolément.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes **annulées** ; aucune AMM valide n'est enregistrée dans les données compilées. Les textes d'indication approuvée sont vides.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60981789 | EZETROL 10 mg, comprimé | Comprimé | Non renseignée |
| 60887592 | EZETIMIBE ALMUS 10 mg, comprimé | Comprimé | Non renseignée |
| 66718898 | EZETIMIBE SANDOZ 10 mg, comprimé | Comprimé | Non renseignée |
| 64518219 | TWICOR 10 mg/10 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 65237214 | LIPOROSA 10 mg/10 mg, gélule | Gélule | Non renseignée |

Les autres AMM (génériques EG, Crister(s), Zentiva, Krka, Viatris, Accord, Teva, Biogaran, Arrow, Zydus ; Twicor 20/10, Liporosa 20/10, Junaliza 20/10) sont également annulées. Le statut réel de commercialisation en France doit être vérifié auprès de l'ANSM.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : pancréatite, maladie hépatique, maladie de la vésicule biliaire, myopathie, maladies musculaires et du muscle squelettique, paralysie périodique familiale, abus/dépendance à une substance, rhabdomyolyse, fasciite nodulaire.
- **Interactions médicamenteuses** : 171 interactions recensées. Les interactions de niveau modéré concernent l'acide chénodésoxycholique, l'éluxadoline, la rosuvastatine et la simvastatine. D'autres interactions, de niveau non précisé, concernent notamment la calcitriol, le pantoprazole, la metformine, l'oméprazole, la morphine, la vancomycine et le lansoprazole.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'hyperlipoprotéinémie est étroitement liée aux indications d'origine de l'ézétimibe, et plusieurs essais de phase 3 (niveau L1) soutiennent son efficacité hypolipémiante. La prédiction est toutefois essentiellement une confirmation d'usage existant, et de nombreux essais sont menés en association, ce qui complique l'attribution de l'effet à l'ézétimibe seul.
- Les prédictions pour le déficit en cholestérol 7α-hydroxylase et le déficit en CETP (niveau L5) restent en **Hold**, faute de preuves cliniques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier le statut réglementaire réel en France, toutes les AMM étant annulées dans les données compilées.
- Obtenir les mises en garde et contre-indications officielles de la notice ANSM (données de sécurité manquantes).
- Compléter les données sur le mécanisme d'action (DrugBank).
- Séparer la contribution de l'ézétimibe de celle des traitements associés dans les essais en combinaison.
- Prêter attention aux risques hépatiques et musculaires signalés, notamment en association avec les statines.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

