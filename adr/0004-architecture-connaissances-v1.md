# ADR-0004: Architecture de connaissances v1

**Statut**: accepted
**Date**: 2026-07-07

## Contexte

Backlog point 1. Priorités exprimées par l'utilisateur : recherche
full-text rapide, base requêtable par les agents, liens/graphe entre
idées. Habitude actuelle : fichiers markdown / Obsidian.

Orion a déjà un système proche — `apps/vault-factory` (vault Obsidian
séparé `orion-vault` + index SQLite `entries`, cf. ADR-009 d'Orion).
Analyse :
- ✅ Base requêtable par les agents (SQLite)
- ⚠️ Pas de full-text réel : la table indexe titre/tags/résumé, pas le
  corps des notes, et n'utilise pas `FTS5`
- ⚠️ Pas de génération de liens/wikilinks — rien ne crée de `[[liens]]`
  automatiquement

## Décision

1. **Pas de dépendance au vault d'Orion.** Cohérent avec ADR-0001/0003 :
   Afkar Lab reste autonome. On reprend le *pattern* (vault markdown +
   index SQLite), pas le code ni la base d'Orion.
2. **Pas de repo `afkar-vault` séparé pour l'instant.** `research/`,
   `learning/`, `observatory/` sont déjà un vault markdown minimal,
   déjà versionné dans ce repo. Volume actuel trop faible pour justifier
   un découpage — à revisiter si ça grossit (même clause de sortie
   qu'Orion ADR-003/ADR-009).
3. **Index local SQLite avec `FTS5` dès le départ** — corrige le point
   faible identifié chez Orion plutôt que de le reproduire. Un seul
   fichier `scripts/index-vault.py`, stdlib uniquement (`sqlite3`),
   rebuild complet à chaque exécution (volume trop faible pour justifier
   un suivi incrémental par mtime).
4. **Pas de génération automatique de wikilinks en v1** — aucun besoin
   réel constaté. À réévaluer si le volume de notes grossit.

## Alternatives considérées

- Notion (déjà connecté via MCP) — écarté : l'utilisateur note déjà en
  markdown/Obsidian, pas de bénéfice à changer d'habitude, et moins
  portable qu'un dossier de fichiers plats (cf. disaster-recovery.md).
- Réutiliser tel quel `apps/vault-factory` d'Orion — écarté : coupling
  entre deux projets qu'on a explicitement voulu garder séparés.

## Conséquences

- `data/vault.db` est local, gitignored (recréable par
  `scripts/index-vault.py`, jamais source de vérité — les `.md` le sont).
- Recherche full-text possible dès maintenant via `sqlite3 data/vault.db
  "SELECT path, title FROM notes WHERE notes MATCH '...'"`.
- Si le volume grossit fortement ou qu'un besoin de graphe apparaît,
  reconsidérer un vault Obsidian séparé + wikilinks (repasser par un ADR).

## Addendum — recherche 2026-07-07 (validation du choix FTS5)

Creusé dans `research/knowledge/index.md` : à l'échelle perso (10k-100k
notes), SQLite/FTS5 reste plus rapide qu'une base vectorielle dédiée — le
point de bascule est ~10M entrées. **Choix FTS5-only confirmé, pas
seulement une intuition.**

Nuance retenue : FTS5 gagne en précision (termes exacts), le vectoriel
gagne en rappel flou ("je me souviens du concept, pas des mots"). Chemin
d'évolution si ce besoin apparaît un jour : ajouter l'extension
`sqlite-vec` au `vault.db` existant (même fichier, pas de nouveau
service) — pas construit maintenant, aucune douleur constatée (16 notes).
