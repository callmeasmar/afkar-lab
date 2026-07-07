# 🧠 Afkar Lab

**Afkar** (أفكار — pensées, idées) : Personal Operations System en
construction. Laboratoire privé — expérimentations, recherche, erreurs
autorisées. La version publique et stable (**Afkar Core**) viendra plus
tard, une fois le projet mûr (voir [ADR-0001](adr/0001-lab-et-core.md)).

> Comprendre avant d'automatiser. Documenter avant de construire.
> Explorer avant d'optimiser.

![status](https://img.shields.io/badge/statut-bootstrap%20termin%C3%A9-brightgreen)
![visibility](https://img.shields.io/badge/visibilit%C3%A9-priv%C3%A9-lightgrey)
![lang](https://img.shields.io/badge/langue-fran%C3%A7ais-blue)

---

## 📍 Suivi

| Chantier | Statut | Détail |
|---|---|---|
| Bootstrap du Lab (structure, ADR, docs) | ✅ Fait | [CHANGELOG](CHANGELOG.md) |
| Push GitHub | ✅ Fait | `callmeasmar/afkar-lab` (privé) |
| Écosystème agents/outils | 🔄 Décidé, à réévaluer | [ADR-0003](adr/0003-agents-et-outils.md) |
| Portabilité / reprise après reinstall | 🔄 1er jet fait | [disaster-recovery.md](docs/disaster-recovery.md) |
| Architecture de connaissances | ⬜ À faire | [backlog #1](docs/brainstorm-backlog.md#1-architecture-de-connaissances) |
| Système de mémoire | ⬜ À faire | [backlog #2](docs/brainstorm-backlog.md#2-système-de-mémoire-agent--perso) |
| Infrastructure & hébergement | ⬜ À faire | [backlog #4](docs/brainstorm-backlog.md#4-infrastructure--hébergement) |
| Automatisation | ⬜ À faire | [backlog #5](docs/brainstorm-backlog.md#5-automatisation--quand-et-comment) |
| Interface / UX | ⬜ À faire | [backlog #6](docs/brainstorm-backlog.md#6-interface--ux-quotidienne) |
| Sécurité & secrets | ⬜ À faire | [backlog #7](docs/brainstorm-backlog.md#7-sécurité--secrets) |
| Règle de promotion Lab → Core | ⬜ À faire | [backlog #9](docs/brainstorm-backlog.md#9-règle-de-promotion-lab--core) |

Détail complet de la reprise : [BOOTSTRAP_STATE.md](BOOTSTRAP_STATE.md) ·
Historique : [CHANGELOG.md](CHANGELOG.md)

## 📖 Documents clés

- [AFKAR.md](AFKAR.md) — identité et vision du projet
- [PROJECT_CHARTER.md](PROJECT_CHARTER.md) — principes directeurs
- [CLAUDE.md](CLAUDE.md) — règles de travail dans ce repo
- [ROADMAP.md](ROADMAP.md) — état d'avancement
- [docs/brainstorm-backlog.md](docs/brainstorm-backlog.md) — grandes questions à trancher
- [docs/disaster-recovery.md](docs/disaster-recovery.md) — survivre à une réinstallation complète
- [adr/](adr/) — décisions d'architecture (ADR)

## 🗂️ Structure

```
adr/            décisions d'architecture
docs/           documentation (architecture, backlog, recovery)
visuals/        diagrammes Mermaid (système, infra, flux, agents)
research/       veille et notes par domaine
observatory/    rapports hebdomadaires de veille
learning/       notes d'apprentissage technique
experiments/    code exploratoire, non stable
prototypes/     ébauches plus abouties qu'un experiment
scripts/        scripts utilitaires
stack/          stack technique réelle du VPS
```

## 🔒 Règles

Aucun secret en clair, ADR obligatoire pour toute décision structurante,
documentation avant implémentation. Détail complet : [CLAUDE.md](CLAUDE.md).
