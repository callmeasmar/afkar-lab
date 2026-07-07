# ADR-0005: Mémoire (agent + décisions)

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 2. Deux formes de "mémoire" à distinguer :
1. **Mémoire agent** — ce que Claude Code retient d'une session à l'autre
   sur l'utilisateur, ses préférences, le contexte du projet.
2. **Mémoire de contenu/décisions** — idées, sources, choix structurants.

Vérification faite : Claude Code fournit déjà un système de mémoire
automatique **scoped par projet**, dans
`~/.claude/projects/<slug-du-dossier>/memory/` (celui utilisé par Orion
dans `~/.claude/projects/-home-hermesagent-orion/memory/`). Il n'existe
pas encore de dossier équivalent pour `afkar-lab` — il se créera de
lui-même à la première session ouverte dans ce dossier.

## Décision

1. **Mémoire agent : réutiliser le système auto de Claude Code, aucun
   développement nécessaire.** Le harness crée et gère
   `~/.claude/projects/<slug-afkar-lab>/memory/` automatiquement.
2. **Mémoire de contenu/décisions : déjà couverte par ADR-0004** (vault
   research/learning/observatory + index FTS5) et par les ADR eux-mêmes
   (`adr/`, historique des décisions dans ce repo Git).
3. **Aucun système de mémoire custom pour Afkar** — pas de justification
   à en construire un tant que le système existant suffit (cohérent avec
   "avant toute installation").

## Conséquences

- ⚠️ **Gap de portabilité identifié** : la mémoire agent
  (`~/.claude/projects/.../memory/`) vit **hors de ce repo Git**, au
  niveau utilisateur de la machine. Une réinstallation complète du VPS la
  perd. Ajouté à `docs/disaster-recovery.md`.
- Pas de nouvelle brique à maintenir : la mémoire "recommence à zéro" et
  se reconstruit à l'usage après une réinstallation — acceptable, cette
  mémoire est un accélérateur, pas une source de vérité (les ADR et le
  vault le sont).
