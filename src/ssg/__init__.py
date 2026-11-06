"""SSG reference core."""
__version__ = "0.5.0"

from .git_ingest import GitIngestionError, ingest_git_history

__all__ = ["GitIngestionError", "ingest_git_history", "__version__"]
