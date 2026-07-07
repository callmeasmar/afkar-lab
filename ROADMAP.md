# Roadmap

## Fait

- Bootstrap du Lab (structure, ADR, visuels squelettes)
- Repo poussé sur GitHub (`callmeasmar/afkar-lab`, privé)
- ADR-0003 : décision agents/outils (aucun agent dédié pour l'instant)
- Backlog de brainstorm structuré (voir `docs/brainstorm-backlog.md`)
- Procédure de reprise après réinstallation (`docs/disaster-recovery.md`)
- ADR-0004 : architecture de connaissances v1 (vault existant + index SQLite FTS5)
- `scripts/index-vault.py` — indexe research/learning/observatory, testé (16 notes, recherche full-text OK)
- ADR-0005 : mémoire (agent = système auto Claude Code, contenu = ADR-0004)
- ADR-0006 : infra & hébergement (même VPS qu'Orion, pas de backup vault.db)
- ADR-0007 : sécurité & secrets + tool-adoption-checklist.md
- ADR-0008 : automatisation (rien à automatiser maintenant, seuil défini)
- ADR-0009 : interface/UX (Claude Code CLI uniquement)
- ADR-0010 : règle de promotion Lab→Core + promotion-checklist.md
- **Backlog de brainstorm initial (9 points) entièrement tranché.**

## À venir

- Premier prototype réel dans `experiments/` (ex: enrichir index-vault.py
  avec un vrai usage, ou attaquer un sujet dans `research/`)
- Nouveaux points de brainstorm à ajouter au backlog au fil de l'usage

## TODO

- Choisir le premier sujet concret à creuser (pas juste architectural)
