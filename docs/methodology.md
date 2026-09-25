# Research method and scope

[Back to Awesome BTCFi](../README.md) · Initial research snapshot: **2026-09-25**

## Scope

BTCFi here means financial uses of BTC and the infrastructure directly enabling them. Coverage includes Bitcoin contracts and asset protocols, payment layers, Bitcoin-oriented execution systems, BTC representations on other chains, lending, stablecoins, staking, shared security, trading, yield, wallets, developer tooling, analytics and selected centralized alternatives.

This is **not a claim to enumerate every BTCFi project**. The ecosystem is open-ended; deployments, product names and teams change. Networks, projects, distinct products, standards and research resources are all counted as **entries**, not as unique companies. A network and its separately described bridge asset can both appear. Searchable records keep the type explicit.

General-purpose DeFi is included when there is a documented Bitcoin connection. General Bitcoin businesses, every validator, every liquidity pool, individual meme tokens, individual NFT collections, all custodians, every exchange and all ETFs are outside the core catalog.

## Research process

1. Discover categories and candidates through Bitcoin Layers, DefiLlama, official ecosystem directories and web search.
2. Read project websites, documentation, code descriptions and official announcements. Prefer a technical page over marketing where practical.
3. Record the mechanism rather than copying superlatives. Identify what is native BTC, what is a representation, where execution occurs, and which questions the documentation leaves open.
4. Look for product changes and shutdown notices. Retain historical entries when their presence helps explain older BTCFi maps.
5. Attach at least one dated source to every catalog entry. Use `ecosystem-only` evidence when only an official ecosystem description supports inclusion.
6. Run a separate HTTP reachability pass and structural checks. Neither is a protocol audit.

The review used public online sources and search-indexed material. Some pages were available in a web index when direct automated access failed. Index crawl dates vary, so **reviewed on September 25 is not a claim that every page was updated that day**. The repository intentionally preserves uncertainty instead of substituting an inferred operating status.

## Evidence and lifecycle

These are **independent dimensions**, not a rating scale. Every entry has both. A project can have a direct source and still have unverified availability, or have a well-documented shutdown.

| Evidence label | Meaning |
| --- | --- |
| `direct-source` | A publisher description, original technical document, research paper or other direct evidence was reviewed; depth varies |
| `ecosystem-only` | Inclusion rests on an ecosystem/partner listing, without direct product documentation reviewed |
| `code-only` | The cited evidence is source repositories; it does not establish a deployed service |

| Lifecycle label | Meaning |
| --- | --- |
| `unverified` | Current end-to-end operation was not established; this is the default, not a finding of inactivity |
| `mainnet-announced` | Publisher material explicitly advertises mainnet availability; not transaction-tested |
| `testnet` | Reviewed material identifies testnet for the listed product |
| `research` | A construction/research family rather than one deployed product |
| `changed` | Current material differs materially from older product descriptions; old liabilities may remain |
| `deprecated` | Publisher material points to retirement/deprecation |
| `discontinued` | Publisher explicitly announced closure; contracts or recovery routes may remain |
| `not-applicable` | A standard, developer tool, research or reference resource rather than a financial service |

`review_note` explains qualifications and product-specific exceptions. The README suppresses default labels for readability; the detailed catalog and browse index show the full classification. None of these labels verifies solvency, successful withdrawals or code safety.

## Evidence and source hierarchy

- **Primary:** the project's own website, documentation, code repository, a network's official ecosystem listing, an auditor's own scoped report, or the authors' research paper. A governance post is primary for its own proposal or decision, not automatically primary for every third-party product claim it repeats.
- **Secondary:** independent reporting or analysis, clearly identified if added. The current catalog primarily uses primary evidence; independent directories helped discover and frame the research.
- **Editorial review focus:** questions to investigate. These are not assertions that a vulnerability exists, and are not a complete security assessment.

Publisher statements can be incomplete, promotional or outdated. Sources establish what a project documents; they do not independently validate every security claim. No contracts were deployed, wallets connected, deposits made or withdrawals tested for this research.

## Dataset fields

The canonical source is [data/projects.json](../data/projects.json). The README listings, detailed catalog, browse indexes and evidence-coverage report are generated from it.

| Field | Meaning |
| --- | --- |
| `id` | Stable lowercase identifier used by catalog links |
| `name` | Project, product, protocol or resource name |
| `category` | One primary category; use descriptions and network tags for cross-category discovery |
| `website` | Canonical resource link; can be documentation where that is more useful |
| `networks` | Relevant ecosystems, not an exhaustive or certified deployment list |
| `kind` | Network, asset, application, protocol, standard, infrastructure, wallet, platform, tool or research resource |
| `description` | Short neutral explanation of relevance |
| `bitcoin_mechanism` | How BTC or a Bitcoin-linked claim is involved |
| `review_focus` | Important implementation/economic questions for further diligence |
| `evidence`, `lifecycle`, `review_note` | Separate evidence basis, availability/lifecycle qualification and explanatory note |
| `sources` | Source URLs, source type and review date; optional descriptive `title` |
| `last_reviewed` | Date of the directory's most recent substantive review of that record |

The dataset's `as_of` is the snapshot date. Change it deliberately when publishing a new research snapshot; do not make all entries look newly reviewed by changing dates in bulk.

## Link checking

[The report](../data/link-health.json) stores public URL status, redirects and the time of the HTTP check. It is reproducible with [the checker](../scripts/check_links.py).

- A `200` response can be a landing page, JavaScript shell, soft 404, parked site or historical notice.
- A `403`, timeout, DNS or TLS failure can reflect access protection or the checking environment.
- Link-check status is therefore independent of catalog status. Failures require human review, not automatic deletion.

## Maintenance priorities and known gaps

First recheck changed products, shutdowns, redemption notices, bridge parameters and newly deployed vaults. Then expand coverage of Liquid asset issuance, RGB applications, smaller sidechain ecosystems, Solana/Sui Bitcoin markets, oracle providers and institution-specific infrastructure.

Rujira, Fiamma and iBTC / DLC.link were added after direct-source review. The [generated review queue](coverage.md) keeps the remaining thinly sourced entries visible. Smaller Bitcoin layers and additional vault providers still need research. Community contributions should improve evidence quality as well as breadth.

No continuous monitoring or future research cadence is promised by this static snapshot. Repository checks catch structural mistakes; contributors must review changing financial and technical facts.

## Schema 2 migration

The first edition used one `status` field for both evidence and lifecycle. Schema 2 replaces it with `evidence` and `lifecycle`, and renames `status_note` to `review_note`. Previously `documented` records now default to unverified lifecycle rather than implying an operating service. The search script uses `--evidence` and `--lifecycle` instead of `--status`. Consumers of the original JSON should update those field names; stable entry IDs are preserved.
