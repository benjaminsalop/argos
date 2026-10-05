# Data model

Fixed metadata columns; keywords, sentiment and demographics are separate tables joined on keys.

## `documents` (Parquet, partitioned by `published_date`)
| column | type | notes |
|---|---|---|
| doc_id | string | stable hash of source + source_id |
| source | string | e.g. `oaklandside`, `x`, `oakland_pd` |
| source_type | string | news, social, crime_report, market, ... |
| source_id | string | id/URL at origin |
| published_at | timestamp (UTC) | |
| ingested_at | timestamp (UTC) | |
| geo_id | string | tract FIPS or ZCTA |
| geo_level | string | tract, zip |
| title | string | nullable |
| text | string | cleaned text |
| lang | string | |

## `document_keywords`
| doc_id | keyword | aspect | match_type (exact, alias, llm) |

## `document_aspect_scores`
| column | notes |
|---|---|
| doc_id | |
| campaign_id | scores are per campaign config version |
| aspect | e.g. `housing_affordability` |
| sentiment | LLM output, [-1, 1] |
| relevance | LLM output, [0, 1] |
| evidence | short span from the text |
| model | model id + prompt version |
| scored_at | |

Weighted scores are computed in the SQL view `v_weighted_scores` using the campaign weights table, not stored.

## `campaign_weights` (loaded from YAML)
| campaign_id | aspect | term | weight | version |

## `geo_demographics`
| geo_id | geo_level | year | metric | value | source | n (cell size) |

Metrics come from ACS and aggregated voter-file statistics. Cells below the suppression threshold are dropped.

## `market_series`
| market_id | ts | price | volume | source |

## `reference` tables
`neighborhood_crosswalk`, `zip_tract_crosswalk`, `lexicon_terms` (base sentiment lexicon with provenance).
