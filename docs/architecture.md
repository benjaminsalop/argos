# Architecture

## Stages

| Stage | Package | Input | Output |
|---|---|---|---|
| Ingest | `argos.ingest` | external sources (news, social, crime reports, prediction markets, voter file) | `data/raw/<source>/date=YYYY-MM-DD/*.jsonl` (immutable) |
| Clean | `argos.clean` | raw | `data/interim/documents/` Parquet, with `doc_id`, timestamps in UTC, normalized text, dedupe |
| Geo-tag | `argos.geo` | interim documents | adds `geo_id` (tract / ZIP) via gazetteer + crosswalks |
| Keywords | `argos.enrich.keywords` | documents + campaign YAML | `document_keywords` table |
| Sentiment | `argos.enrich.sentiment` + `argos.llm` | documents + campaign weights | `document_aspect_scores` table |
| Demographics | `argos.enrich.demographics` | ACS + aggregated voter file | `geo_demographics` table (tract/ZIP level) |
| Storage | `argos.storage` | all of the above | Parquet datasets under `data/processed/`, DuckDB catalog |
| Analysis | `argos.analysis` | SQL views in `sql/` | tables, model results |
| Viz / reports | `argos.viz` | analysis output | HTML/PNG charts, campaign reports |

## Campaign-tunable weights

The LLM is asked to do one thing: for each document, return the relevant **aspects** (e.g. `housing_affordability`, `encampments`) with a sentiment in [-1, 1] and a relevance in [0, 1], plus a short evidence span.

Campaign weights are applied **after** the LLM call, in `argos.llm.weights`:

```
weighted_score = sentiment * relevance * campaign_weight(aspect)
```

Why post-hoc: weights stay visible, adjustable without re-running the LLM, and explainable to a client. Changing a weight only recomputes a view. Terms with high campaign weight are also injected into the prompt (as the aspect list and aliases) so the model looks for them.

Weights live in `configs/campaigns/<campaign>.yaml` and can be edited by hand, through the CLI (`argos weights set`), or in the local Streamlit editor (`app/weights_editor.py`).

A small hand-labeled validation set per campaign (`examples/validation/`) is used to check LLM scores before anyone trusts them.

## Geography

Everything resolves to a `geo_id`:
- `tract` (11-digit FIPS) preferred
- `zip` (ZCTA) where only ZIP is known
- Neighborhood names (e.g. Rockridge) are mapped through `data/reference/neighborhood_crosswalk.csv` to tract sets.

HUD/Census crosswalks handle ZIP <-> tract.

## Demographics and the voter file

Voter file records are processed locally and **aggregated to tract/ZIP** in `enrich/demographics.py`. Only aggregates leave that step. Small cells are suppressed (`privacy/aggregation.py`). Place-level attributes describe areas, not authors or readers of any document.

## Prediction markets vs. news

`analysis/lead_lag.py` aligns market price series with news-sentiment series on a common UTC time grid and tests lead/lag relationships (cross-correlation, Granger tests, event studies). It reports association, not proof of cause.

## VS Code extension

`vscode-extension/` is a thin shell: it edits campaign YAML (with JSON Schema validation), triggers CLI runs, and renders results. All logic stays in the Python package.
