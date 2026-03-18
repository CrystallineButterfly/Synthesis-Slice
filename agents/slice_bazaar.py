"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Agent Bazaar Hooks",
  "track": "Slice",
  "pitch": "An agent storefront that models dynamic pricing, checkout policy, and identity-aware access for ENS and Locus-powered commerce.",
  "overlap_targets": [
    "PayWithLocus",
    "ENS",
    "Lido stETH Treasury",
    "Virtuals",
    "ERC-8004 Receipts",
    "Celo"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
