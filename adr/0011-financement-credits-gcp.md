# ADR-0011: Financement via crédits Google Cloud (Vertex AI)

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 19. ~260€ de crédits Google Cloud, expirant dans 88 jours
(~2026-10-03 environ). Vérifié : Claude Code supporte nativement Google
Cloud Vertex AI comme backend (variables `CLAUDE_CODE_USE_VERTEX`,
`ANTHROPIC_VERTEX_PROJECT_ID`, `CLOUD_ML_REGION`), et les crédits GCP
standards couvrent l'inférence Vertex AI comme n'importe quel service GCP.

GLM (Z.ai) est aussi disponible sur Vertex AI Model Garden en tant que
"partner model" MaaS (`vertex_ai/zai-org/glm-5-maas`) — facturé par
Google, donc éligible aux mêmes crédits. Différent de l'API directe
Z.ai (`api.z.ai`) qu'utilise déjà Orion (`sm glm`), qui reste facturée
par Z.ai, hors crédits GCP.

## Décision

1. **Tout passe par les crédits Vertex.** Claude Code sera configuré
   pour router via Vertex AI (au lieu de l'API Anthropic directe) tant
   que les crédits durent.
2. **GLM via Z.ai (`sm glm` chez Orion) reste inchangé** — pas facturé
   par GCP, pas concerné par cette décision. Une bascule éventuelle de
   `sm glm` vers GLM-via-Vertex serait une décision Orion séparée, pas
   traitée ici.
3. **Cursor écarté** — pas sur Vertex, pas de crédits GCP applicables.

## Alternatives considérées

- Utiliser les crédits sur Cursor/GLM directement — écarté : ces crédits
  sont explicitement exclus pour les services tiers hors GCP natif
  (règle générale des crédits promo GCP).

## Conséquences

- Claude Code (utilisé pour Orion ET Afkar, même VPS) change de backend
  d'authentification — impact partagé, pas propre à Afkar seul.
- Nécessite : ID de projet GCP, région, méthode d'auth (login interactif
  `gcloud` ou clé de compte de service) — détails pratiques à finaliser
  avec l'utilisateur avant modification de `~/.claude/settings.json`.
- À revisiter (repasser en API Anthropic directe) une fois les crédits
  épuisés ou expirés.
