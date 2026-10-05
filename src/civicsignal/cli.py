"""Command-line entry point.

Planned commands:
    argos ingest <source>            pull from a configured source into data/raw
    argos clean                      raw -> interim
    argos enrich --campaign <id>     geo-tag, keywords, LLM aspect scoring, demographics
    argos weights show|set           view or edit campaign weights
    argos query "<sql>"              run SQL against the DuckDB catalog
    argos report --campaign <id>     build a campaign report
"""
import typer

app = typer.Typer(help="argos CLI (stub)")

# TODO: implement commands
