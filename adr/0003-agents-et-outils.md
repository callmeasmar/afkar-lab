# ADR-0003: Agents et outils pour Afkar Lab

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Orion a 9 agents (zed, architect, dev, os, qa, researcher, writer, curator,
remotion). Vérification faite : ils sont définis dans
`orion/.claude/agents/*.md`, **au niveau du projet Orion**, pas au niveau
utilisateur (`~/.claude/agents/` n'existe même pas). Leurs chartes sont
écrites pour le domaine d'Orion (manifest.json, briques, VPS HermesAgent) —
ils ne sont donc ni disponibles automatiquement dans Afkar Lab, ni
directement adaptés tels quels à son contexte.

Côté outils : les serveurs MCP (`memory`, `sequential-thinking`,
`filesystem`, `github`, `sqlite`, `fetch`, `context7`) sont configurés au
niveau utilisateur dans `~/.claude.json` — disponibles dans n'importe quel
projet ouvert avec ce compte, mais **pas versionnés** : une réinstallation
complète les efface et il faut les reconfigurer à la main.

## Décision

1. **Aucun agent dédié à Afkar pour l'instant.** La session principale
   (Claude Code générique) suffit au stade actuel (doc, structure,
   recherche). Ne pas copier un agent Orion tel quel : sa charte ne
   correspond pas au contexte Afkar.
2. **Si un besoin récurrent apparaît** (ex: veille hebdomadaire répétée,
   review systématique avant promotion Lab→Core), créer un agent **propre
   à Afkar**, scoped projet, dans `afkar-lab/.claude/agents/` — jamais en
   dehors du repo. Ça le rend versionné et reconstruit automatiquement au
   clone.
3. **Outils MCP** : réutiliser ceux déjà configurés (`memory`, `sqlite`,
   `fetch`, `sequential-thinking`) au cas par cas, sans en ajouter de
   nouveaux sans justification (règle "avant toute installation" du
   prompt de bootstrap). Documenter leur absence après reinstall dans
   [disaster-recovery.md](../docs/disaster-recovery.md).

## Alternatives considérées

- Réutiliser directement les agents Orion — rejeté : chartes non
  pertinentes (manifest, VPS Hermes), couplage indésirable entre Lab et
  Orion.
- Créer tout de suite des agents dédiés Afkar — rejeté : prématuré, pas de
  besoin récurrent identifié, irait contre "comprendre avant automatiser".

## Conséquences

- Afkar Lab reste autonome de l'écosystème d'agents Orion.
- Tout futur agent Afkar vit dans ce repo, donc survit à une réinstallation
  complète via `git clone`.
- Reconfigurer les MCP servers après reinstall reste une étape manuelle
  (pas de secret dans ce repo pour ça — voir disaster-recovery.md).
