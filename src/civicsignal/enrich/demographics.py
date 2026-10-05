"""Build geo_demographics.

Inputs: ACS (geo.census) and the local voter file (ingest.voter_file).
Voter-file records are aggregated to tract/ZIP counts and shares, then passed through
privacy.aggregation.suppress_small_cells before being written. Each row carries source and cell size.
"""
