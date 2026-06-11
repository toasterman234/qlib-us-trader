"""Built-in US large-cap stock universe.

Returns the list of tickers the app trades/researches by default (`us-core-100`).
Override it at runtime by pointing ``US_UNIVERSE_FILE`` at a text file with one
ticker per line (blank lines and ``#`` comments are ignored).
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

# Curated US large-cap universe (~100 names across mega-cap tech, financials,
# healthcare, energy, consumer, and industrials). Used as the default when no
# US_UNIVERSE_FILE override is provided.
US_CORE_100: list[str] = [
    # Mega-cap tech / communication
    "AAPL", "MSFT", "NVDA", "GOOGL", "GOOG", "AMZN", "META", "TSLA", "AVGO", "ORCL",
    "ADBE", "CRM", "AMD", "INTC", "CSCO", "QCOM", "TXN", "IBM", "NFLX", "INTU",
    "AMAT", "MU", "NOW", "PANW", "LRCX",
    # Communication / media
    "DIS", "CMCSA", "T", "VZ", "TMUS",
    # Financials
    "BRK-B", "JPM", "BAC", "WFC", "GS", "MS", "C", "SCHW", "AXP", "BLK",
    "SPGI", "CB", "PGR", "USB", "PNC",
    # Healthcare
    "UNH", "JNJ", "LLY", "PFE", "MRK", "ABBV", "TMO", "ABT", "DHR", "BMY",
    "AMGN", "MDT", "GILD", "ISRG", "CVS",
    # Consumer staples
    "PG", "KO", "PEP", "WMT", "COST", "MDLZ", "CL", "MO", "PM", "TGT",
    # Consumer discretionary
    "HD", "LOW", "MCD", "NKE", "SBUX", "BKNG", "TJX", "GM", "F", "ORLY",
    # Energy
    "XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "OXY",
    # Industrials
    "CAT", "BA", "HON", "GE", "UPS", "RTX", "LMT", "DE", "UNP", "MMM",
    # Materials / utilities / real estate
    "LIN", "NEE", "DUK", "AMT", "PLD",
]


@lru_cache(maxsize=1)
def get_us_universe_tickers() -> list[str]:
    """Return the active US universe tickers.

    If ``US_UNIVERSE_FILE`` is set and points to a readable file, its tickers are
    used (one per line; blank lines and ``#`` comments ignored). Otherwise the
    built-in ``US_CORE_100`` list is returned.
    """
    override = os.getenv("US_UNIVERSE_FILE")
    if override:
        path = Path(override).expanduser()
        if path.is_file():
            tickers: list[str] = []
            for raw in path.read_text().splitlines():
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                tickers.append(line.upper())
            if tickers:
                # De-duplicate while preserving order.
                seen: set[str] = set()
                return [t for t in tickers if not (t in seen or seen.add(t))]

    return list(US_CORE_100)
