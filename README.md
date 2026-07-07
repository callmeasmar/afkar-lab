# 🧠 Afkar Lab

**Afkar** (أفكار — pensées, idées) : Personal Operations System en
construction. Laboratoire privé — expérimentations, recherche, erreurs
autorisées. La version publique et stable (**Afkar Core**) viendra plus
tard, une fois le projet mûr (voir [ADR-0001](adr/0001-lab-et-core.md)).

> Comprendre avant d'automatiser. Documenter avant de construire.
> Explorer avant d'optimiser.

![status](https://img.shields.io/badge/statut-backlog%20initial%20tranch%C3%A9-brightgreen)
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
| Architecture de connaissances | ✅ Fait | [ADR-0004](adr/0004-architecture-connaissances-v1.md) · `scripts/index-vault.py` |
| Système de mémoire | ✅ Fait | [ADR-0005](adr/0005-memoire.md) |
| Infrastructure & hébergement | ✅ Fait | [ADR-0006](adr/0006-infrastructure-hebergement.md) |
| Sécurité & secrets | ✅ Fait | [ADR-0007](adr/0007-securite-secrets.md) |
| Automatisation | ✅ Fait | [ADR-0008](adr/0008-automatisation.md) |
| Interface / UX | ✅ Fait | [ADR-0009](adr/0009-interface-ux.md) |
| Règle de promotion Lab → Core | ✅ Fait | [ADR-0010](adr/0010-promotion-lab-core.md) |

Détail complet de la reprise : [BOOTSTRAP_STATE.md](BOOTSTRAP_STATE.md) ·
Historique : [CHANGELOG.md](CHANGELOG.md)

## 📖 Documents clés

- [AFKAR.md](AFKAR.md) — identité et vision du projet
- [PROJECT_CHARTER.md](PROJECT_CHARTER.md) — principes directeurs
- [CLAUDE.md](CLAUDE.md) — règles de travail dans ce repo
- [ROADMAP.md](ROADMAP.md) — état d'avancement
- [docs/brainstorm-backlog.md](docs/brainstorm-backlog.md) — grandes questions (backlog initial tranché)
- [docs/tool-adoption-checklist.md](docs/tool-adoption-checklist.md) — avant d'adopter un outil
- [docs/promotion-checklist.md](docs/promotion-checklist.md) — avant de promouvoir Lab → Core
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
