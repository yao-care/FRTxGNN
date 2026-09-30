---
layout: default
title: Emtricitabine
parent: Preuves modérées (L3-L4)
nav_order: 117
evidence_level: L4
indication_count: 3
---

# Emtricitabine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Emtricitabine : De l'infection par le VIH au syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

L'emtricitabine est un inhibiteur nucléosidique de la transcriptase inverse, commercialisé en France seul (Emtriva) ou en association (Descovy, génériques emtricitabine/ténofovir). Il sert à traiter l'infection par le VIH chez l'humain, mais le texte d'indication des AMM n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace contre le **syndrome d'immunodéficience acquise féline** (infection par le FIV chez le chat), avec **4 essais cliniques** (tous chez l'humain, sans lien direct) et **1 publication** (étude préclinique chez le chat).
Cette prédiction relève de la médecine vétérinaire, et aucun essai clinique félin n'existe à ce jour.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH (déduite de la classe pharmacologique et des produits commercialisés ; texte d'AMM non renseigné) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées de DrugBank sur le mécanisme d'action ne sont pas disponibles. Selon les connaissances pharmacologiques établies, l'emtricitabine est un inhibiteur nucléosidique de la transcriptase inverse (INTI). Après phosphorylation intracellulaire, il interrompt la synthèse de l'ADN viral.

Le FIV est un lentivirus dont la transcriptase inverse est homologue à celle du VIH. Une activité des INTI contre ce virus est donc biologiquement plausible. Le FIV provoque chez le chat un dysfonctionnement immunitaire progressif comparable à celui du sida humain.

Il faut toutefois rester prudent. Le score TxGNN très élevé reflète probablement le lien entre les maladies VIH et FIV dans l'ontologie, plutôt qu'une preuve indépendante chez le chat. L'usage humain approuvé contre le VIH ne constitue pas une donnée d'efficacité chez le chat.

---

## Preuves d'Essais Cliniques

Les 4 essais enregistrés portent tous sur des patients humains infectés par le VIH-1. L'emtricitabine n'y figure que dans le bras comparateur ou dans le traitement de fond, jamais comme variable étudiée. Tous sont classés « faible pertinence » (grade C).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Terminé | 844 | Dolutégravir + abacavir/lamivudine vs Atripla (éfavirenz/emtricitabine/ténofovir) sur 96 semaines chez des adultes VIH-1 naïfs de traitement. Emtricitabine uniquement dans le bras comparateur. |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Terminé | 828 | Dolutégravir vs raltégravir, associés à une bithérapie d'INTI (abacavir/lamivudine ou ténofovir/emtricitabine) au choix de l'investigateur. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Terminé | 208 | Choix d'une dose quotidienne de dolutégravir associé à abacavir/lamivudine ou ténofovir/emtricitabine. |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Terminé | 145 | Darunavir boosté + lamivudine vs darunavir boosté + ténofovir/emtricitabine ou ténofovir/lamivudine chez des patients VIH-1 naïfs. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Étude préclinique chez l'animal (FIV) | Viruses | Évaluation de la pharmacocinétique et de l'évolution clinique d'une association antirétrovirale (dolutégravir 2,5 mg/kg, ténofovir 20 mg/kg, emtricitabine 40 mg/kg) chez des chats infectés par le FIV. |

L'emtricitabine n'est ici qu'un composant d'une trithérapie. L'effet propre de la molécule ne peut pas être isolé.

---

## Informations de Marché en France

Cinq AMM principales sur 20 sont listées ci-dessous. Le texte des indications approuvées n'est pas renseigné dans les données reçues.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 61294762 | EMTRIVA 200 mg, gélule | Gélule |
| 66717579 | EMTRIVA 10 mg/ml, solution buvable | Solution buvable |
| 62778588 | EMTRICITABINE/TENOFOVIR DISOPROXIL KRKA D.D. 200 mg/245 mg | Comprimé pelliculé |
| 66325208 | DESCOVY 200 mg/25 mg | Comprimé pelliculé |
| 68486060 | EMTRICITABINE/TENOFOVIR DISOPROXIL SANDOZ 200 mg/245 mg | Comprimé pelliculé |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un lien d'ontologie VIH/FIV et sur une seule étude préclinique chez le chat, portant sur une trithérapie. Aucun essai clinique félin n'existe, et les essais humains cités ne concernent pas cette indication.
- Le niveau de preuve est L4, avec un score TxGNN élevé mais non corroboré par des données cliniques félines.

**Pour avancer, les éléments suivants sont nécessaires :**
- Consulter la notice de l'ANSM (avertissements et contre-indications), lacune bloquante pour tout criblage de sécurité.
- Obtenir les données DrugBank sur le mécanisme d'action.
- Disposer de données de pharmacocinétique, de tolérance et d'efficacité de l'emtricitabine chez le chat, idéalement issues d'essais contrôlés.
- Clarifier le cadre réglementaire d'un usage vétérinaire d'un médicament humain.

À titre d'orientation, la prédiction voisine « infection par le virus de l'immunodéficience simienne » repose sur de nombreuses études sur macaques (prophylaxie emtricitabine/ténofovir). Son intérêt clinique reste toutefois indirect, car elle sert de modèle animal du VIH humain.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Toute piste de repositionnement doit être validée cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

