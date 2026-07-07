#!/usr/bin/env python3
"""Reconstruit l'index full-text de research/ + learning/ + observatory/.

Usage:
    python3 scripts/index-vault.py
    python3 -c "import sqlite3; c=sqlite3.connect('data/vault.db'); \
        print(c.execute(\"SELECT path,title FROM notes WHERE notes MATCH 'ta-recherche'\").fetchall())"

(pas de CLI `sqlite3` sur ce VPS — même constat que le vault-factory d'Orion)

Rebuild complet à chaque run (pas de suivi incrémental, cf. ADR-0004) :
le volume actuel ne justifie pas la complexité d'un diff par mtime.
"""

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT_DIRS = ["research", "learning", "observatory"]
DB_PATH = ROOT / "data" / "vault.db"


def extract_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return fallback


def iter_notes():
    for vault_dir in VAULT_DIRS:
        base = ROOT / vault_dir
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            content = path.read_text(encoding="utf-8")
            rel_path = str(path.relative_to(ROOT))
            title = extract_title(content, fallback=path.stem)
            yield rel_path, title, content


def main():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DROP TABLE IF EXISTS notes")
    conn.execute(
        """
        CREATE VIRTUAL TABLE notes USING fts5(
            path UNINDEXED,
            title,
            content,
            tokenize = 'porter unicode61'
        )
        """
    )
    rows = list(iter_notes())
    conn.executemany(
        "INSERT INTO notes (path, title, content) VALUES (?, ?, ?)", rows
    )
    conn.commit()
    conn.close()
    print(f"{len(rows)} notes indexées dans {DB_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
