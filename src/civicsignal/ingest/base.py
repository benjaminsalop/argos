"""Connector interface.

class Connector(Protocol):
    name: str
    def fetch(self, since: datetime) -> Iterator[RawRecord]: ...

RawRecord holds the untouched payload plus source, source_id, fetched_at.
Writers append to data/raw/<source>/date=YYYY-MM-DD/ and never modify existing files.
"""
