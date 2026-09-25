# Editorial review and improvements

Reviewed **2026-09-25**. [Awesome BTCFi](../README.md) · [Remaining evidence gaps](coverage.md)

The first edition had useful breadth and dated sources, but breadth made the research look more uniform than it was. Its strongest features were the asset-mechanism explanations, explicit shutdown notes, and refusal to rank projects by advertised returns. Its weaknesses needed concrete changes:

| Critique of the first edition | Improvement made | Remaining limit |
| --- | --- | --- |
| The display name used inconsistent BTCFi capitalization | Standardized authored prose and dataset title to **Awesome BTCFi** | Existing lowercase URLs and file paths are retained |
| One `status` field mixed evidence quality, deployment claims and product changes | Split evidence basis and lifecycle in schema 2; default lifecycle is `unverified` | No live transaction testing was performed |
| Several entries relied on ecosystem listings despite available product docs | Reviewed direct sources for Hermetica, Bitflow and Satsuma; improved mechanisms and qualifications | Four other ecosystem-only entries remain visible in the queue |
| cbBTC relied on a third-party assessment classified as primary evidence | Added Coinbase's own documentation and reclassified the external assessment | Issuer statements are not an independent reserve audit |
| Network browsing required a command-line script | Added generated, clickable network/evidence/lifecycle/type indexes | Network tags indicate relevance, not certified deployments |
| Known omissions were listed but unresolved | Added Rujira, Fiamma Bridge/fiaBTC and iBTC / DLC.link after direct-source research | Coverage remains selective |
| Trust questions were generic and mostly publisher-framed | Added scoped auditor evidence for Fiamma and explicit custody/redemption paths for the newly reviewed products | Audit coverage is not systematic across the directory |
| Research-depth differences were buried in individual entries | Added a generated evidence-coverage report and named review queue | Source count measures coverage, not truth or independence |

## Specific research corrections

- **Hermetica:** replaced the broad USDh/hBTC ecosystem summary with a focused USDh/sUSDh entry. The [minting documentation](https://docs.hermetica.fi/usdh/how-it-works/mint) describes eligibility checks, custodian/venue dependencies and redemption-pause conditions. hBTC availability is not inferred from USDh docs.
- **Rujira:** the [secured-assets explanation](https://rujira.network/secured-assets) makes THORChain vault custody part of the path. Native BTC deposits do not imply the user's sole key control throughout application use.
- **Fiamma:** the [bridge status page](https://docs.fiammalabs.io/our-product-suite/pragmatically-trustless-bitvm-bitcoin-bridge/bridge-test) claims mainnet modules, while [OpenZeppelin's audit](https://www.openzeppelin.com/news/fiamma-bridge-audit) identifies off-chain dependencies and privileged roles for its reviewed version. Neither the audit nor a mainnet announcement verifies every current deployment.

## What a stronger next edition would require

The list is still a discovery and research starting point. A deployment-level comparison would need contract/version identifiers, precise signer and upgrade powers, redemption eligibility, audit scope, incidents and recovery status for each individual deployment. Those facts cannot be inferred reliably from project names or filled in through blanket labels. The [coverage report](coverage.md) distinguishes completed improvements from work still open.
