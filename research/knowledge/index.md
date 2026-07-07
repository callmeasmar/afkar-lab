# Knowledge management — recherche full-text vs sémantique

Objectif : vérifier si le choix FTS5-only d'ADR-0004 tient face à l'état
de l'art, avant que ça devienne un problème réel.

## Ce que dit la recherche (2026)

- **FTS5 seul suffit largement à l'échelle perso.** Le point de bascule
  où une base vectorielle dédiée devient plus rapide que SQLite se situe
  autour de 10 millions d'entrées avec requêtes multi-vecteurs complexes
  — aucun agent perso n'approche ce volume. À 10k-100k documents, SQLite
  reste très réactif. [(ZeroClaws)](https://zeroclaws.io/blog/zeroclaw-sqlite-fts5-vector-hybrid-memory-explained/)
- **FTS5 et recherche vectorielle répondent à des besoins différents,
  pas concurrents** : FTS5 gagne quand la précision compte (termes
  exacts, identifiants, code) ; le vectoriel gagne quand le rappel compte
  (recherche exploratoire, "je me souviens du concept pas des mots
  exacts"). [(dev.to)](https://dev.to/fex_beck_27bfd4dccd05f062/why-sqlitefts5-beats-vector-dbs-for-ai-agent-memory-4inj)
- **L'approche émergente est hybride, dans le même fichier SQLite** —
  l'extension `sqlite-vec` ajoute la recherche vectorielle sans nouveau
  service/serveur, cohabite avec FTS5 dans `vault.db`.
  [(Alex Garcia)](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html)

## Ce que ça change pour Afkar

**Rien dans l'immédiat** — 16 notes, aucune douleur de rappel flou
constatée. ADR-0004 validé par la recherche, pas juste par intuition.

**Chemin d'évolution identifié** (pas construit, juste noté) : si un
jour retrouver une note "par le concept, pas les mots" devient un vrai
problème, ajouter `sqlite-vec` au `vault.db` existant plutôt qu'une base
vectorielle externe — reste dans un seul fichier, zéro nouvelle
dépendance lourde. Voir addendum ADR-0004.

## Sources

- [ZeroClaw's Hybrid Memory — SQLite + FTS5 + Vectors](https://zeroclaws.io/blog/zeroclaw-sqlite-fts5-vector-hybrid-memory-explained/)
- [Why SQLite+FTS5 beats Vector DBs for AI Agent Memory](https://dev.to/fex_beck_27bfd4dccd05f062/why-sqlitefts5-beats-vector-dbs-for-ai-agent-memory-4inj)
- [Hybrid full-text + vector search with SQLite (sqlite-vec)](https://alexgarcia.xyz/blog/2024/sqlite-vec-hybrid-search/index.html)
