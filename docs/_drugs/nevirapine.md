---
layout: default
title: Nevirapine
parent: Preuves modérées (L3-L4)
nav_order: 533
evidence_level: L4
indication_count: 3
---

# Nevirapine
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

# Névirapine : Du VIH/SIDA au Syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

La névirapine est un inhibiteur non nucléosidique de la transcriptase inverse (INNTI), initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome d'immunodéficience acquise féline**, mais cette prédiction ne repose que sur **1 publication préclinique** et **aucun essai clinique**.
Il s'agit d'une indication vétérinaire, sans pertinence directe pour un développement clinique chez l'humain.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 11 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la névirapine appartient à la classe des INNTI, dont l'efficacité dans l'infection par le VIH-1 est établie. Elle se fixe sur une poche allostérique de la transcriptase inverse du VIH-1.

Le virus de l'immunodéficience féline (FIV) est un lentivirus doté lui aussi d'une transcriptase inverse, ce qui fournit une base mécanistique théorique à la prédiction. Le score très élevé du modèle (0,998) reflète probablement surtout la proximité entre cette maladie et le VIH/SIDA dans le graphe de connaissances.

Toutefois, les INNTI sont connus pour avoir une activité limitée sur les transcriptases inverses des lentivirus autres que le VIH-1, en raison de différences dans la poche de liaison. L'unique publication disponible (2023) compare, sur le plan biochimique et structural, plusieurs INNTI contre le FIV et le VIH, mais les données fournies ne permettent pas de confirmer si la névirapine est active ou inactive contre la transcriptase inverse du FIV.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Étude préclinique biochimique/structurale | Journal of Veterinary Science | Comparaison de la névirapine, de l'éfavirenz et de la rilpivirine contre les transcriptases inverses du FIV et du VIH ; l'activité propre de la névirapine contre le FIV n'est pas précisée dans les données disponibles |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|-----|
| 61512136 | NEVIRAPINE SANDOZ 200 mg | Comprimé | Non renseignée | Annulée |
| 60433166 | NEVIRAPINE SANDOZ LP 400 mg | Comprimé à libération prolongée | Non renseignée | Annulée |
| 69410368 | VIRAMUNE 400 mg | Comprimé à libération prolongée | Non renseignée | Annulée |
| 63791738 | VIRAMUNE 200 mg | Comprimé | Non renseignée | Annulée |
| 65256474 | NEVIRAPINE VIATRIS 200 mg | Comprimé | Non renseignée | Annulée |

Au total, 11 AMM sont répertoriées, toutes annulées ; seules les 5 principales sont listées ci-dessus.

---

## Cytotoxicité

Cette section est omise : la névirapine est un antirétroviral et non un médicament antinéoplasique.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie du foie, maladie de la vésicule biliaire, exanthème, infection chronique par le virus de l'hépatite C, infection par le virus de l'hépatite C, infection chronique par le virus de l'hépatite B, rhabdomyolyse, fasciite nodulaire, atteinte hépatique d'origine médicamenteuse, syndrome de Stevens-Johnson, nécrolyse épidermique toxique, syndrome de Lyell.
- **Interactions Médicamenteuses** : 207 interactions recensées. Parmi les principales, de niveau modéré : rabéprazole, bupropion, aprépitant, corticoïdes (triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone), clarithromycine, saxagliptine, linagliptine, éliglustat, naltrexone, naloxégol, naldémédine, cisapride, granisétron, ondansétron, nitisinone et orlistat.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle et sur une étude préclinique unique dont le résultat pour la névirapine n'est pas confirmé. Il s'agit d'une indication vétérinaire, sans pertinence pour un développement clinique chez l'humain. Le médicament n'a plus d'AMM valide en France et présente un profil de sécurité préoccupant (hépatotoxicité, réactions cutanées sévères).

**Pour avancer, les éléments suivants sont nécessaires :**
- Consulter le texte complet de la publication 38031646 afin de déterminer l'activité réelle de la névirapine sur la transcriptase inverse du FIV
- Obtenir les données détaillées sur le mécanisme d'action
- Récupérer les mises en garde et contre-indications officielles de la notice de l'ANSM
- Définir si un intérêt vétérinaire existe, avec des données d'efficacité et de sécurité chez le chat

---

### Note sur les autres prédictions

Deux autres prédictions ont été examinées et ne justifient pas d'avancer :
- **Infection par le virus de l'immunodéficience simienne** (score 99,85 %, niveau L4, Hold) : la littérature indique que le SIV est intrinsèquement résistant aux INNTI. Seules les chimères SHIV portant la transcriptase inverse du VIH-1 sont sensibles, ce qui les rend utiles comme modèles animaux. Plusieurs articles récupérés ne sont que faiblement liés au sujet.
- **Trouble neurodéveloppemental avec démarche ataxique, absence de parole et diminution de la substance blanche corticale** (score 99,82 %, niveau L5, Hold) : aucun lien mécanistique, aucun essai et aucune publication.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

