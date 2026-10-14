---
layout: default
title: Dexamethasone
parent: Preuves élevées (L1-L2)
nav_order: 229
evidence_level: L2
indication_count: 10
---

# Dexamethasone
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

# Dexaméthasone : Des maladies inflammatoires et endocriniennes à l'alopécie areata

## Résumé en Une Phrase

La dexaméthasone est un corticoïde de synthèse, utilisé à l'origine dans de nombreuses affections inflammatoires, hématologiques et endocriniennes (insuffisance surrénalienne, maladie de Crohn, leucémie aiguë lymphoblastique, hyperplasie congénitale des surrénales, etc.).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**alopécie areata**.
À ce jour, les données compilées pour ce rapport ne contiennent **aucun essai clinique enregistré** pour cette indication, mais **20 publications** ont été retrouvées, dont un essai randomisé pédiatrique, une méta-analyse en réseau et plusieurs études de cohorte.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM françaises (texte d'indication vide). Selon le graphe de connaissances : insuffisance surrénalienne, maladie de Crohn, leucémie aiguë lymphoblastique, hyperplasie congénitale des surrénales, etc. |
| Nouvelle Indication Prédite | Alopécie areata |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, la dexaméthasone est un glucocorticoïde puissant, dont l'efficacité anti-inflammatoire et immunosuppressive est établie dans de nombreuses maladies à composante immunitaire (maladie de Crohn, pneumonie à éosinophiles, etc.).

L'alopécie areata est une maladie auto-immune médiée par les lymphocytes T : des lymphocytes T CD8+ cytotoxiques attaquent le follicule pileux, qui bénéficie normalement d'un privilège immunitaire. La dexaméthasone freine l'activation des lymphocytes T, la production de cytokines et l'infiltrat inflammatoire péri-folliculaire. Son mécanisme immunosuppresseur correspond donc à la physiopathologie de la maladie.

Un schéma de « mini-pulses » oraux (par exemple 5 mg deux jours consécutifs par semaine) est déjà décrit dans la littérature. La sécurité demande toutefois une surveillance en raison de l'exposition cumulée aux corticoïdes, et les rechutes à l'arrêt sont fréquentes.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | ECR | Dermatologic Therapy | Étude randomisée ouverte (30 enfants) comparant les mini-pulses oraux de dexaméthasone à la sensibilisation de contact par DPCP dans l'alopécie areata sévère pédiatrique |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Revue systématique / méta-analyse en réseau | Arch Dermatol Res | Comparaison des corticoïdes systémiques, des inhibiteurs de JAK oraux et de l'immunothérapie de contact dans l'alopécie areata sévère |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Cohorte | J Clin Med | Cohorte prospective en vie réelle : efficacité et tolérance des mini-pulses de corticoïdes oraux, facteurs associés à la réponse |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Cohorte | Dermatologic Therapy | Étude multicentrique des mini-pulses de dexaméthasone orale dans l'alopécie areata modérée à sévère |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Cohorte | J Dermatol | Dexaméthasone orale 5 mg deux fois par semaine chez 30 patients atteints d'alopécie étendue |
| [41872082](https://pubmed.ncbi.nlm.nih.gov/41872082/) | 2026 | Cohorte rétrospective | Eur J Dermatol | Stratégie par étapes (corticoïdes topiques + baricitinib, puis pulses de dexaméthasone en rattrapage) chez 19 patients |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revue | Pediatr Dermatol | Revue des schémas de corticothérapie en pulses chez l'enfant et de leurs effets secondaires |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Cas clinique | J Dermatolog Treat | Rémission durable d'une alopécie areata sévère par mini-pulses de dexaméthasone lorsque les inhibiteurs de JAK ne sont pas envisageables |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Étude prospective | Dermatologic Therapy | Pulses intraveineux de dexaméthasone (1 jour vs 3 jours) associés à un corticoïde topique chez 73 enfants |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Étude de suivi | Dermatologic Therapy | Pulses oraux et corticoïde topique chez 65 enfants, suivi à long terme (médiane de 96 mois) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60833559 | AFLAVIS 1 mg/mL, collyre en solution | Collyre en solution | Non renseignée (AMM annulée) |
| 68106914 | DEXOCOL 1 mg/mL, collyre en solution | Collyre en solution | Non renseignée (AMM annulée) |
| 67392081 | OZURDEX 700 µg, implant intravitréen | Implant | Non renseignée (AMM annulée) |
| 68973246 | DEXAMETHASONE PANPHARMA 4 mg/mL | Solution injectable | Non renseignée (AMM annulée) |
| 62817482 | DECTANCYL 0,5 mg | Comprimé | Non renseignée (AMM annulée) |

Au total, 20 AMM sont enregistrées, toutes annulées ; aucune n'est actuellement valide.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, épilepsie, hyperglycémie, insuffisance cardiaque congestive, kératite herpétique, rougeole, certains déficits du cycle de l'urée (citrullinémie, hyperargininémie, déficit en carbamoyl-phosphate synthétase I), ainsi que divers déficits hypophysaires et hypogonadismes hypogonadotropes.
- **Interactions médicamenteuses** : 913 interactions recensées. Parmi elles, des interactions **majeures** avec le fentanyl et l'adalimumab ; des interactions modérées, par exemple avec le paclitaxel, l'ibuprofène, la nifédipine, l'acétazolamide, la zidovudine et l'isotrétinoïne ; des interactions mineures, par exemple avec le dolutégravir et la lidocaïne.
- **Points de vigilance spécifiques à l'indication** : exposition cumulée aux corticoïdes lors des pulses répétés et rechutes fréquentes à l'arrêt.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être récupérées.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'alopécie areata dispose d'un essai randomisé, d'une méta-analyse en réseau et de plusieurs cohortes appuyant les mini-pulses de dexaméthasone, avec un mécanisme immunosuppresseur cohérent. En revanche, aucun essai clinique enregistré n'existe, les données de sécurité officielles manquent et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles (notice ANSM), étape bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Définir la voie d'administration et le schéma posologique (mini-pulses oraux), et clarifier le statut réglementaire, aucune AMM valide n'étant en vigueur
- Prévoir un plan de surveillance de la sécurité (glycémie, tension artérielle, exposition cumulée) et de la rechute
- Idéalement, conduire un essai de phase 2/3 comparatif

**Autres indications prédites (rangs 2 à 10) :** alopécie mucineuse, effluvium télogène, folliculite décalvante de Quinquaud, déficit en anticorps avec alopécie, hypotrichose héréditaire avec vésicules cutanées récurrentes, syndrome alopécie-déficience intellectuelle-hypogonadisme hypergonadotrope, atrichie avec lésions papuleuses, alopécie universelle avec onychodystrophie et vitiligo, prolapsus de la glande lacrymale. Toutes sont au niveau de preuve L5 (prédiction du modèle seule) : les publications retrouvées pour l'effluvium télogène et le déficit en anticorps ne sont pas pertinentes (effets indésirables cutanés d'anticancéreux, actes de congrès), et aucune donnée n'existe pour les autres. Recommandation « Hold » pour la plupart, et « Research Question » pour l'alopécie universelle avec vitiligo, qui reste une extrapolation à partir de l'alopécie areata.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

