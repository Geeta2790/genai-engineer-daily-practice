# day04 rag retrieval

## Goal
Load sample text, split it into chunks, retrieve relevant chunks for a query, and discuss top-k and relevance.

## Your checklist
- [x] Understand the concept
- [x] Write the implementation yourself
- [x] Run the code locally
- [x] Test a success case and an error case
- [x] Commit your work with a meaningful message

## Learning notes
- TF-IDF scores a term by how often it appears in a doc (TF) weighted down by how common it is across the corpus (IDF). Rare informative words dominate the score.
- `stop_words="english"` strips filler like "how / is / in" so queries line up on the signal words.
- Cosine similarity is unit-length dot product — it measures direction, not magnitude. Longer docs don't automatically win.
- Top-k retrieval is just `argsort` on the similarity vector; the retrieve step is cheap once the index is built.
- Weakness seen in the output: `api` vs `apis` don't match without a stemmer. Real RAG uses embeddings so morphology/synonyms are handled automatically.
