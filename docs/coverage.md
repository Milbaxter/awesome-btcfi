# Evidence coverage and review queue

Snapshot: **2026-10-15** · [Method](methodology.md) · [Browse](browse.md) · [Editorial review](editorial-review.md)

Generated from the dataset. Counts describe research coverage, not project quality or safety. Several sources from one publisher are not independent corroboration.

| Measure | Count |
| --- | ---: |
| Total entries | 131 |
| Entries with one cited source | 109 |
| Entries citing only their listed website/resource URL | 77 |
| Evidence: code-only | 3 |
| Evidence: direct-source | 124 |
| Evidence: ecosystem-only | 4 |

A website/resource URL can be a technical document or repository, so the URL-only count is a triage signal, not a claim that all those sources are marketing pages.

## Entries needing stronger direct evidence

| Entry | Evidence | Specific unresolved point |
| --- | --- | --- |
| [Alkanes](directory.md#alkanes) | code-only | Contract execution is not Bitcoin Core executing a general-purpose VM. |
| [PumpBTC](directory.md#pumpbtc) | code-only | Code reviewed; current user-facing service availability was not established. |
| [ALEX](directory.md#alex) | ecosystem-only | Ecosystem listing establishes identity, not present operational health. |
| [Curve](directory.md#curve) | ecosystem-only | WBTC's official site lists Curve among supported trading venues; verify the particular pool. |
| [JuiceSwap](directory.md#juiceswap) | ecosystem-only | Listed from the network's official directory; no execution testing performed. |
| [Uniswap](directory.md#uniswap) | ecosystem-only | BTC trading uses a representation such as WBTC, not native Bitcoin settlement. |
| [Metashrew](directory.md#metashrew) | code-only | Indexing a contract is different from Bitcoin consensus enforcing its full semantics. |

## Coverage still missing

Deeper coverage is still needed for Solana/Sui Bitcoin markets, Liquid asset issuance, smaller RGB applications, oracle providers, and institutional infrastructure. The list also lacks a systematic deployment-by-deployment audit and incident history. These gaps remain open; entry count is not a measure of completeness.

## Next review priorities

1. Resolve the ecosystem-only and code-only entries above with dated product documentation.
2. Recheck redemptions, changed strategies, closures and permissioned bridge roles.
3. Add deployment-specific audit scope and incident/recovery sources where independently verified.
4. Review the HTTP failures in [link health](../data/link-health.json), without inferring closure from access errors.
