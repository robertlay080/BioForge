"""
BioForge Data Module
--------------------
Handles loading, saving, and managing biological datasets such as genomes
and reaction simulation logs.
"""
from pathlib import Path
import json
import csv

DATA_DIR = Path(__file__).resolve().parent
GENOMES_DIR = DATA_DIR / "genomes"
LOGS_DIR = DATA_DIR / "reaction_logs"


def load_genome(name: str) -> dict:
    """Load genome data by name (without .json extension)."""
    path = GENOMES_DIR / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(f"Genome '{name}' not found in {GENOMES_DIR}")
    with open(path, "r") as f:
        return json.load(f)


def save_reaction_log(filename: str, data: list[dict]):
    """Save reaction results to CSV for analysis."""
    path = LOGS_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
