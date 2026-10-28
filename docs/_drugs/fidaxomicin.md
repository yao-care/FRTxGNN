---
layout: default
title: Fidaxomicin
parent: Prédiction du modèle uniquement (L5)
nav_order: 325
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "fidaxomicin"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis"]
description: "Fidaxomicin : nouvelle indication prédite, Syndrome de la peau ébouillantée staphylococcique (staphylococcal scalded skin syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans l…"
---

# Fidaxomicin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Fidaxomicin: Syndrome de la peau ébouillantée staphylococcique (staphylococcal scalded skin syndrome)
{: .text-alpha }

## Résumé en Une Phrase

La fidaxomicine est un antibiotique macrocyclique à spectre étroit, initialement utilisé pour traiter la colite à *Clostridium difficile*.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la peau ébouillantée staphylococcique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome de la peau ébouillantée staphylococcique (staphylococcal scalded skin syndrome) |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la fidaxomicine est un antibiotique macrocyclique à spectre étroit qui inhibe l'ARN polymérase bactérienne. Son efficacité dans la colite à *C. difficile* est établie. Une activité *in vitro* contre certains germes à Gram positif, dont certaines souches de *Staphylococcus aureus*, est plausible, ce qui pourrait expliquer le lien établi par le modèle.

Toutefois, cette prédiction reste fragile. La fidaxomicine est très peu absorbée par voie systémique : elle agit dans la lumière digestive et il est peu probable qu'elle atteigne les sites d'infection producteurs de toxines ou la circulation sanguine, ce qui serait nécessaire dans le syndrome de la peau ébouillantée staphylococcique. Aucune preuve clinique ou bibliographique ne vient étayer cet usage.

### Autres indications prédites (pour information)

Le modèle propose également plusieurs autres indications, toutes au niveau de preuve L5 et toutes en décision « Hold » :

| Rang | Indication prédite | Score TxGNN | Remarque principale |
|------|------|------|------|
| 2 | Impétigo bulleux | 0,9970 | Absorption faible, pas de forme topique |
| 3 | Botulisme par inhalation | 0,9969 | Un antibiotique ne neutralise pas la toxine préformée |
| 4 | Impétigo | 0,9968 | Pas de forme topique ; alternatives établies (ex. mupirocine) |
| 5 | Botulisme infectieux à médiation toxinique | 0,9966 | Hypothèse purement théorique (portage digestif) |
| 6 | Candidose vulvovaginale | 0,9965 | Pas d'activité antifongique reconnue |
| 7 | Orgelet | 0,9964 | Pas de forme ophtalmique ; guérison spontanée fréquente |
| 8 | Pneumonie à *Staphylococcus aureus* | 0,9921 | Exposition systémique insuffisante pour une infection pulmonaire |
| 9 | Kératoconjonctivite épithéliale ponctuée | 0,9902 | Origine souvent virale ou inflammatoire |

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature directement associée à l'indication principale (syndrome de la peau ébouillantée staphylococcique) n'est disponible actuellement.

Pour information, une seule publication a été retrouvée pour une autre indication prédite (pneumonie à *S. aureus*) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) | 2019 | Revue | Journal of Hospital Medicine | Synthèse générale de la littérature en médecine hospitalière ; mentionne la vancomycine ou la fidaxomicine comme traitements de première intention de l'infection à *C. difficile*, sans apporter de preuve pour la pneumonie à *S. aureus* |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62629288 | DIFICLIR 40 mg/ml, granulés pour suspension buvable (statut : active) | Granulés pour suspension buvable | Non renseignée |
| 61973350 | DIFICLIR 200 mg, comprimé pelliculé (statut : active) | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

**Interactions médicamenteuses** : 79 interactions ont été recensées. Parmi celles listées dans les données compilées :
- **Majeure** : vaccin vivant contre le choléra (*Vibrio cholerae* souche CVD 103-HgR)
- **Modérées** : alpélisib, apalutamide, binimétinib, acide picosulfurique
- **Mineures** : nifédipine, amiodarone, diltiazem, vérapamil, ciclosporine, clarithromycine, érythromycine, spironolactone, dronédarone, daclatasvir, ivacaftor, elagolix, brigatinib, cabozantinib, capmatinib

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Par ailleurs, la faible absorption systémique de la fidaxomicine rend peu plausible une efficacité dans une affection toxinique d'origine cutanée. De plus, les deux AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Données de pharmacocinétique tissulaire et d'activité *in vitro* contre les souches de *S. aureus* productrices de toxines exfoliatives
- Évaluation de la faisabilité d'une voie d'administration adaptée (aucune forme topique ou systémique appropriée n'est disponible)
- Études précliniques, puis éventuellement un essai exploratoire, avant toute reconsidération
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

