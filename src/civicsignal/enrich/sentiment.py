"""Aspect-based sentiment orchestration.

For each document in scope: build prompt from campaign aspects (llm.prompts), call llm.client,
validate output, store raw aspect scores (sentiment, relevance, evidence) in document_aspect_scores.
Weights are NOT applied here; see llm.weights and the v_weighted_scores SQL view.
Results are cached by (doc_id, campaign version, prompt version, model).
"""
