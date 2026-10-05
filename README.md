# Argos (working name)

A proof-of-concept architecture for a public affairs and political relations analytics platform.

Argos ingests news, social posts, public records, prediction-market data and aggregate demographics, tags every record with consistent keys (date, source, geography), scores language with a **campaign-tunable, LLM-assisted aspect sentiment layer**, and exposes the result through SQL for analysis and visualization.

> **Status: architecture only.** This repository shows how the system would be built. Modules are stubs with docstrings describing intent. Nothing here is runnable yet.

## Core ideas

1. **Metadata at the door.** Every record gets `doc_id`, `published_at`, `source`, `geo_id` (census tract / ZIP) at ingestion, so any two datasets can be joined later.
2. **Immutable raw data, derived everything else.** `data/raw` is never edited. Cleaned, enriched and aggregated layers are rebuilt from it.
3. **Parquet + DuckDB + SQL.** Parquet datasets partitioned by date; DuckDB queries them in place.
4. **Keywords and sentiment live in separate tables**, not as columns, so adding a keyword never changes the schema.
5. **Campaign-tunable weights.** Each campaign defines the terms it cares about (housing, encampment, gentrification...) and how much they matter. The LLM scores; the weights are applied afterwards, in plain code, so results are auditable.
6. **Demographics are aggregate and sourced.** Tract/ZIP attributes come from census (ACS) and aggregated voter-file statistics, with provenance. They describe places, never individual authors.

## Pipeline

```
sources -> ingest -> data/raw -> clean -> data/interim -> enrich (geo, LLM sentiment, demographics)
        -> data/processed (Parquet) -> DuckDB views (sql/) -> analysis -> viz / reports
```

## Layout

See [docs/architecture.md](docs/architecture.md) for the full walkthrough and [docs/data-model.md](docs/data-model.md) for table definitions.

## Responsible use

Read [docs/compliance.md](docs/compliance.md) before connecting real data. Voter files, social platform terms and privacy law constrain what this tool may do.
