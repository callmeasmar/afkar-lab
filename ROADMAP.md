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

## Ordre retenu pour la suite du backlog

Mémoire (fait) → Infra & hébergement → Sécurité & secrets →
Automatisation → Interface/UX → Règle de promotion Lab→Core
(logique de dépendances : fondations avant automatisation/UX construites dessus)

## TODO

- Infra & hébergement (backlog #4)
