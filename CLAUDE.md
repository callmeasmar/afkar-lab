# Afkar Lab

> Laboratoire privé du Personal Operations System Afkar. Voir AFKAR.md et
> PROJECT_CHARTER.md pour la vision et les principes.

## Règles

- **Langue** : français pour les notes internes (Lab). Anglais possible
  pour Afkar Core (public, futur).
- **ADR obligatoire** pour toute décision structurante — voir `adr/`.
- **Documentation avant implémentation** : comprendre → documenter →
  décider → construire. Pas de code sans doc préalable minimale.
- **Économie de tokens** : privilégier des stubs courts et évolutifs à la
  documentation verbeuse. Ne pas répéter ce qui est déjà écrit ailleurs.
- **Promotion Lab → Core** : une idée ne passe dans Afkar Core que si elle
  est mûre — doc propre + ADR + testée. Jamais de code Lab poussé tel quel
  vers Core.

## Agents

Aucun agent dédié à Afkar pour l'instant. Les 9 agents Orion existent dans
un autre projet (`orion/`) et ne sont pas automatiquement pertinents ici —
à évaluer au cas par cas si un besoin (recherche, review, doc) apparaît.

## Périmètre

Ce CLAUDE.md ne s'applique qu'à `~/projects/afkar-lab/`. Ne pas toucher au
VPS, à `orion/`, ni à la config système depuis ce projet.
