# Research method and scope

[Back to Awesome BTCfi](../README.md) · Initial research snapshot: **2026-09-25**

## Scope

BTCfi here means financial uses of BTC and the infrastructure directly enabling them. Coverage includes Bitcoin contracts and asset protocols, payment layers, Bitcoin-oriented execution systems, BTC representations on other chains, lending, stablecoins, staking, shared security, trading, yield, wallets, developer tooling, analytics and selected centralized alternatives.

This is **not a claim to enumerate every BTCfi project**. The ecosystem is open-ended; deployments, product names and teams change. Networks, projects, distinct products, standards and research resources are all counted as **entries**, not as unique companies. A network and its separately described bridge asset can both appear. Searchable records keep the type explicit.

General-purpose DeFi is included when there is a documented Bitcoin connection. General Bitcoin businesses, every validator, every liquidity pool, individual meme tokens, individual NFT collections, all custodians, every exchange and all ETFs are outside the core catalog.

## Research process

1. Discover categories and candidates through Bitcoin Layers, DefiLlama, official ecosystem directories and web search.
2. Read project websites, documentation, code descriptions and official announcements. Prefer a technical page over marketing where practical.
3. Record the mechanism rather than copying superlatives. Identify what is native BTC, what is a representation, where execution occurs, and which questions the documentation leaves open.
4. Look for product changes and shutdown notices. Retain historical entries when their presence helps explain older BTCfi maps.
5. Attach at least one dated source to every catalog entry. Use a lighter `ecosystem-listed` status when only an official ecosystem description supports inclusion.
6. Run a separate HTTP reachability pass and structural checks. Neither is a protocol audit.

The review used public online sources and search-indexed material. Some pages were available in a web index when direct automated access failed. Index crawl dates vary, so **reviewed on September 25 is not a claim that every page was updated that day**. The repository intentionally preserves uncertainty instead of substituting an inferred operating status.

## Status labels

| Label | What it means | What it does not mean |
| --- | --- | --- |
| `documented` | A relevant primary description or documentation was reviewed | Deposits, withdrawals, live liquidity, code safety or solvency independently verified |
| `ecosystem-listed` | An official ecosystem page establishes identity/relevance | Detailed mechanics or current operating status independently reviewed |
| `mainnet-announced` | Official material explicitly advertises mainnet availability | The researcher executed a transaction or validated every component |
| `testnet` | Reviewed material identifies a testnet for the listed product | Mainnet availability inferred from the parent project's other products |
| `research` | A construction or research family, rather than a single deployment | Production readiness of all implementations |
| `changed` | Current material materially differs from common older descriptions | Every legacy position migrated or redeemed successfully |
| `status-unclear` | Relevant evidence exists but current service status remains unresolved | The project is necessarily inactive or malicious |
| `deprecated` | Public material points users to a retirement/deprecation flow | Every remaining contract is inaccessible |
| `discontinued` | A publisher explicitly announced closure or termination | On-chain contracts or all recovery routes have disappeared |

Labels describe the **evidence available for this review**, not a project's quality. `status_note` records qualifications. An entry with several products may have one live component and another in development; the note takes precedence over assumptions drawn from its label.

## Evidence and source hierarchy

- **Primary:** the project's own website, documentation, code repository, a network's official ecosystem listing, a protocol governance discussion, or the authors' research paper.
- **Secondary:** independent reporting or analysis, clearly identified if added. The current catalog primarily uses primary evidence; independent directories helped discover and frame the research.
- **Editorial review focus:** questions to investigate. These are not assertions that a vulnerability exists, and are not a complete security assessment.

Publisher statements can be incomplete, promotional or outdated. Sources establish what a project documents; they do not independently validate every security claim. No contracts were deployed, wallets connected, deposits made or withdrawals tested for this research.

## Dataset fields

The canonical source is [data/projects.json](../data/projects.json). Both the README listings and detailed catalog are generated from it.

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
| `status`, `status_note` | Evidence label and qualifications |
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

Candidates such as Rujira, Fiamma, DLC.link/dlcBTC, smaller Bitcoin layers and additional vault providers need deeper current-source review before receiving fuller entries. Their omission is a coverage limit, not a judgment. Community contributions should improve evidence quality as well as breadth.

No continuous monitoring or future research cadence is promised by this static snapshot. Repository checks catch structural mistakes; contributors must review changing financial and technical facts.
