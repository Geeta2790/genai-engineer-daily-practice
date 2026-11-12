import sys
from pathlib import Path

import pytest

# Allow importing day04's main.py as a module
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "day04-rag-retrieval"))

from main import retrieve, split_into_chunks  # noqa: E402


def test_retrieve_returns_top_k_results():
    results = retrieve("What is used for caching?", top_k=3)
    assert len(results) == 3
    assert all("document" in r and "score" in r for r in results)


def test_retrieve_top_result_is_most_relevant():
    results = retrieve("What is used for caching?", top_k=1)
    assert "Redis" in results[0]["document"]


def test_retrieve_scores_are_sorted_descending():
    results = retrieve("agent workflows", top_k=5)
    scores = [r["score"] for r in results]
    assert scores == sorted(scores, reverse=True)


def test_split_into_chunks_respects_chunk_size():
    text = " ".join([f"word{i}" for i in range(55)])
    chunks = split_into_chunks(text, chunk_size=20)
    assert len(chunks) == 3
    assert len(chunks[0].split()) == 20
    assert len(chunks[2].split()) == 15


def test_split_into_chunks_empty_input():
    assert split_into_chunks("") == []
