# Detailed BTCfi directory

Snapshot: **2026-09-25**. [Method and status definitions](methodology.md) · [Awesome list](../README.md)

Descriptions summarize publisher documentation. Review focuses are editorial questions, not completed security assessments. Network tags describe relevance, not a certified list of live deployments.

## Bitcoin contracts and asset protocols

<a id="alkanes"></a>
### Alkanes

**Type:** protocol · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

WASM-based metaprotocol supporting programmable assets and DeFi logic.

- **Bitcoin mechanism:** Bitcoin witness data interpreted by a metaprotocol runtime and indexer.
- **Review focus:** Runtime correctness, indexer agreement and upgrade rules.
- **Status evidence / qualification:** Contract execution is not Bitcoin Core executing a general-purpose VM.
- **Project/resource:** [Alkanes](https://github.com/kungfuflex/alkanes-rs)
- **Source 1:** [Primary source](https://github.com/kungfuflex/alkanes-rs) — primary; reviewed 2026-09-25.

<a id="ark"></a>
### Ark

**Type:** protocol · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Shared-UTXO payment design with virtual UTXOs and a coordinating server.

- **Bitcoin mechanism:** Prearranged Bitcoin transaction trees and off-chain transfers.
- **Review focus:** Server availability, refresh deadlines, transfer assumptions and unilateral exit costs.
- **Status evidence / qualification:** Implementations differ; see Arkade and Second.
- **Project/resource:** [Ark](https://ark-protocol.org/)
- **Source 1:** [Primary source](https://ark-protocol.org/) — primary; reviewed 2026-09-25.

<a id="bitvm"></a>
### BitVM

**Type:** research · **Networks:** Bitcoin · **Status:** `research` · **Reviewed:** 2026-09-25

Off-chain computation with Bitcoin-enforced dispute mechanisms, used in bridge and rollup designs.

- **Bitcoin mechanism:** Fraud-proof constructions using existing Bitcoin scripting capabilities.
- **Review focus:** Version-specific challengers, setup, liquidity and dispute assumptions.
- **Status evidence / qualification:** BitVM is a construction family; its existence does not prove a particular bridge is deployed or safe.
- **Project/resource:** [BitVM](https://bitvm.org/)
- **Source 1:** [Primary source](https://bitvm.org/) — primary; reviewed 2026-09-25.

<a id="brc-20"></a>
### BRC-20

**Type:** standard · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Inscription-based token experiment with off-chain balance interpretation.

- **Bitcoin mechanism:** Deploy, mint and transfer inscriptions interpreted by indexers.
- **Review focus:** Indexer agreement, evolving protocol rules and token liquidity.
- **Status evidence / qualification:** Original specification is historical; it points to Layer 1 Foundation for evolving documentation.
- **Project/resource:** [BRC-20](https://domo-2.gitbook.io/brc-20-experiment)
- **Source 1:** [Primary source](https://domo-2.gitbook.io/brc-20-experiment) — primary; reviewed 2026-09-25.

<a id="discreet-log-contracts-dlcs"></a>
### Discreet Log Contracts (DLCs)

**Type:** standard · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Oracle-attested Bitcoin contracts for contingent payments, derivatives and collateral arrangements.

- **Bitcoin mechanism:** Bitcoin transactions with outcomes selected using oracle signatures.
- **Review focus:** Oracle accuracy and availability, contract construction and refund paths.
- **Status evidence / qualification:** A contract family, not a single lending platform.
- **Project/resource:** [Discreet Log Contracts (DLCs)](https://dlc.wiki/)
- **Source 1:** [Primary source](https://dlc.wiki/) — primary; reviewed 2026-09-25.
- **Source 2:** [DLC specifications](https://github.com/discreetlogcontracts/dlcspecs) — primary; reviewed 2026-09-25.

<a id="lightning-network"></a>
### Lightning Network

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Payment channels that route BTC off-chain and can settle to Bitcoin.

- **Bitcoin mechanism:** Bitcoin channel transactions and timelocked settlement.
- **Review focus:** Channel backups, online monitoring, liquidity and on-chain exit fees.
- **Status evidence / qualification:** Protocol overview reviewed; individual wallet custody varies.
- **Project/resource:** [Lightning Network](https://lightning.network/)
- **Source 1:** [Primary source](https://lightning.network/) — primary; reviewed 2026-09-25.

<a id="op-net"></a>
### OP_NET

**Type:** protocol · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Smart-contract execution system that embeds contract data in Bitcoin transactions.

- **Bitcoin mechanism:** Additional execution and verification rules applied to Bitcoin witness data.
- **Review focus:** Execution consensus, indexing, contract security and network-specific deployment stage.
- **Status evidence / qualification:** Documentation reviewed; this entry does not certify mainnet deployment or inherit marketing security claims.
- **Project/resource:** [OP_NET](https://docs.opnet.org/)
- **Source 1:** [Primary source](https://docs.opnet.org/getting-started/introduction-to-op-net/bitcoin-smart-contracts-explained) — primary; reviewed 2026-09-25.

<a id="ordinals"></a>
### Ordinals

**Type:** standard · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Satoshi indexing and inscriptions underlying collectible markets and collateral use cases.

- **Bitcoin mechanism:** Bitcoin transactions interpreted by ordinal-aware software.
- **Review focus:** Indexer conventions, UTXO handling, fees and collectible liquidity.
- **Status evidence / qualification:** Adjacent infrastructure, not an intrinsic BTC yield mechanism.
- **Project/resource:** [Ordinals](https://docs.ordinals.com/)
- **Source 1:** [Primary source](https://docs.ordinals.com/) — primary; reviewed 2026-09-25.

<a id="rgb"></a>
### RGB

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Client-validated contracts and asset issuance anchored to Bitcoin outputs.

- **Bitcoin mechanism:** Off-chain contract state and proofs associated with Bitcoin ownership.
- **Review focus:** Proof backups, wallet interoperability and issuer terms.
- **Status evidence / qualification:** Issued assets are distinct from native BTC.
- **Project/resource:** [RGB](https://rgb.tech/)
- **Source 1:** [Primary source](https://rgb.tech/) — primary; reviewed 2026-09-25.

<a id="rgb-plus-plus"></a>
### RGB++

**Type:** protocol · **Networks:** Bitcoin, Nervos CKB · **Status:** `documented` · **Reviewed:** 2026-09-25

Asset protocol connecting Bitcoin UTXOs and CKB cells through isomorphic bindings.

- **Bitcoin mechanism:** Asset ownership bindings across Bitcoin and CKB.
- **Review focus:** CKB dependencies and the separate custody model of any BTC wrapper.
- **Status evidence / qualification:** Distinct from RGB; token movement does not by itself make native BTC bridge-free.
- **Project/resource:** [RGB++](https://github.com/utxostack/rgbpp-sdk)
- **Source 1:** [Primary source](https://talk.nervos.org/t/rgb-protocol-light-paper-translation/7790) — primary; reviewed 2026-09-25.

<a id="runes"></a>
### Runes

**Type:** standard · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Fungible-token metaprotocol with balances assigned to Bitcoin outputs.

- **Bitcoin mechanism:** Runestones encoded in Bitcoin transactions.
- **Review focus:** Indexer correctness, token economics, market liquidity and fee costs.
- **Status evidence / qualification:** Rune tokens are separate assets, not bitcoin.
- **Project/resource:** [Runes](https://docs.ordinals.com/runes.html)
- **Source 1:** [Primary source](https://docs.ordinals.com/runes.html) — primary; reviewed 2026-09-25.

<a id="taproot-assets"></a>
### Taproot Assets

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Asset issuance and transfers using Taproot, including Lightning-based transfers.

- **Bitcoin mechanism:** Bitcoin commitments, client-side asset proofs and Lightning channels.
- **Review focus:** Issuer backing, proof availability, wallet compatibility and channel liquidity.
- **Status evidence / qualification:** An issuance protocol; a dollar token adds its own issuer risk.
- **Project/resource:** [Taproot Assets](https://docs.lightning.engineering/the-lightning-network/taproot-assets)
- **Source 1:** [Primary source](https://docs.lightning.engineering/the-lightning-network/taproot-assets) — primary; reviewed 2026-09-25.

## Execution networks and Bitcoin layers

<a id="alpen"></a>
### Alpen

**Type:** network · **Networks:** Bitcoin, Alpen · **Status:** `testnet` · **Reviewed:** 2026-09-25

EVM-compatible validity-rollup project for programmable Bitcoin applications.

- **Bitcoin mechanism:** Validity proofs with Bitcoin consensus and data availability in the documented design.
- **Review focus:** Testnet limitations, bridge construction and eventual mainnet controls.
- **Status evidence / qualification:** Docs explicitly describe a work-in-progress rollup on Bitcoin signet; mainnet is a future release.
- **Project/resource:** [Alpen](https://www.alpen.org/)
- **Source 1:** [Primary source](https://docs.alpen.org/) — primary; reviewed 2026-09-25.

<a id="arch-network"></a>
### Arch Network

**Type:** network · **Networks:** Bitcoin, Arch · **Status:** `documented` · **Reviewed:** 2026-09-25

Financial application infrastructure designed around native Bitcoin settlement.

- **Bitcoin mechanism:** External execution and signing infrastructure connected to Bitcoin transactions.
- **Review focus:** Validator or signer control, settlement guarantees and the current application design.
- **Status evidence / qualification:** Native settlement language does not eliminate the need to review the execution and signing layer.
- **Project/resource:** [Arch Network](https://www.arch.network/)
- **Source 1:** [Primary source](https://www.arch.network/) — primary; reviewed 2026-09-25.

<a id="b2-network"></a>
### B2 Network

**Type:** network · **Networks:** Bitcoin, B2 · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin extension ecosystem with rollup infrastructure, bridges and application products.

- **Bitcoin mechanism:** B2 Hub, execution network and separate asset bridges.
- **Review focus:** Bridge control, data availability, proof verification and current product scope.
- **Status evidence / qualification:** Official product navigation includes B2 Hub, Rollup and BTC Bridge.
- **Project/resource:** [B2 Network](https://www.bsquared.network/)
- **Source 1:** [Primary source](https://www.bsquared.network/) — primary; reviewed 2026-09-25.

<a id="bitcoinos"></a>
### BitcoinOS

**Type:** infrastructure · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

BitSNARK and Grail-related infrastructure for Bitcoin proofs, bridges and interoperable applications.

- **Bitcoin mechanism:** Proof and bridge constructions intended to connect external computation to Bitcoin.
- **Review focus:** Implementation maturity, custody, proof challenge assumptions and each integration's deployment.
- **Status evidence / qualification:** Infrastructure claims reviewed; no blanket mainnet or trustlessness assertion.
- **Project/resource:** [BitcoinOS](https://www.bitcoinos.build/)
- **Source 1:** [Primary source](https://www.bitcoinos.build/) — primary; reviewed 2026-09-25.

<a id="bitlayer"></a>
### Bitlayer

**Type:** network · **Networks:** Bitcoin, Bitlayer · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin execution ecosystem associated with BitVM infrastructure and the YBTC product family.

- **Bitcoin mechanism:** Separate execution and product-specific Bitcoin bridge arrangements.
- **Review focus:** Current deployment versus whitepaper design, custody and withdrawal conditions.
- **Status evidence / qualification:** Homepage now emphasizes YBTC; distinguish the network from individual products.
- **Project/resource:** [Bitlayer](https://www.bitlayer.org/)
- **Source 1:** [Primary source](https://static.bitlayer.org/Bitlayer-Technical-Whitepaper.pdf) — primary; reviewed 2026-09-25.
- **Source 2:** [Current Bitlayer products](https://www.bitlayer.org/) — primary; reviewed 2026-09-25.

<a id="bob"></a>
### BOB

**Type:** network · **Networks:** Bitcoin, Ethereum, BOB · **Status:** `documented` · **Reviewed:** 2026-09-25

Hybrid-chain ecosystem with Bitcoin intents, DeFi access and Bitcoin vault development.

- **Bitcoin mechanism:** EVM execution plus route-dependent bridging, intents and BitVM-related infrastructure.
- **Review focus:** Current chain stage, privileged roles and the exact bridge or vault used.
- **Status evidence / qualification:** Docs describe several products; do not assign one security model to all of them.
- **Project/resource:** [BOB](https://docs.gobob.xyz/)
- **Source 1:** [Primary source](https://docs.gobob.xyz/) — primary; reviewed 2026-09-25.

<a id="citrea"></a>
### Citrea

**Type:** network · **Networks:** Bitcoin, Citrea · **Status:** `mainnet-announced` · **Reviewed:** 2026-09-25

Bitcoin rollup project with EVM applications and the Clementine cBTC bridge.

- **Bitcoin mechanism:** Validity proofs and a BitVM-based bridge architecture.
- **Review focus:** Bridge challengers and operators, exit liquidity, sequencer and upgrade controls.
- **Status evidence / qualification:** Official homepage states that mainnet is live; no transaction testing performed.
- **Project/resource:** [Citrea](https://citrea.xyz/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.
- **Source 2:** [Citrea architecture and getting started](https://docs.citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="fractal-bitcoin"></a>
### Fractal Bitcoin

**Type:** network · **Networks:** Bitcoin, Fractal · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-code-based scaling ecosystem supporting asset protocols and applications.

- **Bitcoin mechanism:** Separate SHA256d network with its own asset and consensus arrangements.
- **Review focus:** Separate-chain security and the custody of any asset bridged from Bitcoin.
- **Status evidence / qualification:** FB is not BTC; compatibility with Bitcoin software does not imply identical security.
- **Project/resource:** [Fractal Bitcoin](https://docs.fractalbitcoin.io/)
- **Source 1:** [Primary source](https://docs.fractalbitcoin.io/getting-started/introduction) — primary; reviewed 2026-09-25.

<a id="goat-network"></a>
### GOAT Network

**Type:** network · **Networks:** Bitcoin, GOAT · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-oriented execution ecosystem advertising BTC fee income and programmable applications.

- **Bitcoin mechanism:** Separate execution network, bridge and operator arrangements.
- **Review focus:** BTC entry and exit path, operators, upgrades and fees versus token incentives.
- **Status evidence / qualification:** BTC-denominated fees and GOATED rewards are distinct reward sources.
- **Project/resource:** [GOAT Network](https://www.goat.network/)
- **Source 1:** [Primary source](https://www.goat.network/) — primary; reviewed 2026-09-25.

<a id="hemi"></a>
### Hemi

**Type:** network · **Networks:** Bitcoin, Ethereum, Hemi · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin and Ethereum ecosystem offering programmable BTC-related finance and institutional access.

- **Bitcoin mechanism:** Hemi execution with product-specific Bitcoin access and custody paths.
- **Review focus:** Settlement architecture, bridge or custody route and strategy dependencies.
- **Status evidence / qualification:** HEMI token staking is not the same thing as staking BTC.
- **Project/resource:** [Hemi](https://hemi.xyz/)
- **Source 1:** [Primary source](https://hemi.xyz/) — primary; reviewed 2026-09-25.

<a id="liquid-network"></a>
### Liquid Network

**Type:** network · **Networks:** Bitcoin, Liquid · **Status:** `documented` · **Reviewed:** 2026-09-25

Federated Bitcoin sidechain for confidential transfers, asset issuance and capital markets.

- **Bitcoin mechanism:** BTC is represented as L-BTC on a federation-operated sidechain.
- **Review focus:** Federation control, peg-out access and issuer risk for non-BTC assets.
- **Status evidence / qualification:** Sidechain settlement has additional trust assumptions beyond Bitcoin.
- **Project/resource:** [Liquid Network](https://www.liquid.net/)
- **Source 1:** [Primary source](https://www.liquid.net/) — primary; reviewed 2026-09-25.

<a id="merlin-chain"></a>
### Merlin Chain

**Type:** network · **Networks:** Bitcoin, Merlin · **Status:** `documented` · **Reviewed:** 2026-09-25

EVM-compatible ecosystem supporting Bitcoin-linked assets and applications.

- **Bitcoin mechanism:** A separate network with bridged Bitcoin assets and proof infrastructure.
- **Review focus:** Bridge custody, oracle and data availability assumptions, upgrades and exits.
- **Status evidence / qualification:** Rollup branding is not treated as proof of Bitcoin-enforced withdrawals.
- **Project/resource:** [Merlin Chain](https://merlinchain.io/)
- **Source 1:** [Primary source](https://merlinchain.io/) — primary; reviewed 2026-09-25.

<a id="rootstock"></a>
### Rootstock

**Type:** network · **Networks:** Bitcoin, Rootstock · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-oriented EVM sidechain hosting lending, stablecoins and trading.

- **Bitcoin mechanism:** RBTC peg and a separate smart-contract execution network.
- **Review focus:** Powpeg custody, bridge delays, network consensus and application contracts.
- **Status evidence / qualification:** The official site identifies Rootstock as a Bitcoin sidechain.
- **Project/resource:** [Rootstock](https://rootstock.io/)
- **Source 1:** [Primary source](https://rootstock.io/) — primary; reviewed 2026-09-25.

<a id="stacks"></a>
### Stacks

**Type:** network · **Networks:** Bitcoin, Stacks · **Status:** `documented` · **Reviewed:** 2026-09-25

Smart-contract network for Bitcoin applications, including lending and exchanges using sBTC.

- **Bitcoin mechanism:** Separate execution with Bitcoin anchoring and an sBTC signer-based peg.
- **Review focus:** Signer custody, execution rules, upgrades and withdrawal mechanics.
- **Status evidence / qualification:** Treat Stacks execution and sBTC custody as separate review questions.
- **Project/resource:** [Stacks](https://www.stacks.co/)
- **Source 1:** [Primary source](https://www.stacks.co/sbtc) — primary; reviewed 2026-09-25.

## Bitcoin representations and bridges

<a id="btc-b"></a>
### BTC.b

**Type:** asset · **Networks:** Bitcoin, Multichain · **Status:** `changed` · **Reviewed:** 2026-09-25

Non-yield BTC representation operated by Lombard, originally launched by Ava Labs.

- **Bitcoin mechanism:** BTC backing with Lombard consortium and chain-specific transfer infrastructure.
- **Review focus:** Consortium custody, supported-chain changes and redemption paths.
- **Status evidence / qualification:** Lombard docs report acquisition in October 2025; September 2026 chain support changes require separate review.
- **Project/resource:** [BTC.b](https://docs.lombard.finance/learn/products/assets)
- **Source 1:** [Primary source](https://docs.lombard.finance/learn/products/assets) — primary; reviewed 2026-09-25.
- **Source 2:** [September 2026 chain support and bridging](https://docs.lombard.finance/use/bridging) — primary; reviewed 2026-09-25.

<a id="btcb"></a>
### BTCB

**Type:** asset · **Networks:** Bitcoin, BNB Chain · **Status:** `documented` · **Reviewed:** 2026-09-25

Binance-issued Bitcoin representation used in the BNB Chain ecosystem.

- **Bitcoin mechanism:** Custodial BTC backing and destination-chain tokens.
- **Review focus:** Binance custody, reserve verification, redemption and smart-contract permissions.
- **Status evidence / qualification:** BTCB is distinct from native BTC and from unrelated similarly named tokens.
- **Project/resource:** [BTCB](https://www.bnbchain.org/en/blog/empowering-btcfi-on-bnb-chain-the-role-of-btcb-in-building-trust)
- **Source 1:** [Primary source](https://www.bnbchain.org/en/blog/empowering-btcfi-on-bnb-chain-the-role-of-btcb-in-building-trust) — primary; reviewed 2026-09-25.

<a id="cbbtc"></a>
### cbBTC

**Type:** asset · **Networks:** Bitcoin, Ethereum, Base, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Coinbase-backed BTC representation for on-chain collateral and trading.

- **Bitcoin mechanism:** BTC held by Coinbase with tokens issued on supported networks.
- **Review focus:** Custody, issuer controls, redemption eligibility and chain-specific bridge design.
- **Status evidence / qualification:** The cited technical assessment distinguishes canonical cbBTC from a bridged deployment.
- **Project/resource:** [cbBTC](https://www.coinbase.com/cbbtc)
- **Source 1:** [Primary source](https://governance.aave.com/t/coinbase-wrapped-btc-cbbtc-on-aave-monad-assessments/25257) — primary; reviewed 2026-09-25.

<a id="ckbtc"></a>
### ckBTC

**Type:** asset · **Networks:** Bitcoin, Internet Computer · **Status:** `documented` · **Reviewed:** 2026-09-25

Chain-key BTC representation managed by Internet Computer canisters.

- **Bitcoin mechanism:** Threshold signatures, ICP subnets and minter/ledger canisters.
- **Review focus:** ICP consensus and governance, canister upgrades, transaction screening and redemption.
- **Status evidence / qualification:** No traditional single custodian does not mean no additional trust assumptions.
- **Project/resource:** [ckBTC](https://dashboard.internetcomputer.org/bitcoin)
- **Source 1:** [Primary source](https://docs.internetcomputer.org/concepts/chain-fusion/bitcoin/) — primary; reviewed 2026-09-25.

<a id="clementine-and-cbtc"></a>
### Clementine and cBTC

**Type:** bridge · **Networks:** Bitcoin, Citrea · **Status:** `documented` · **Reviewed:** 2026-09-25

Citrea's bridge and BTC representation for its application environment.

- **Bitcoin mechanism:** BitVM-based optimistic verification in the documented bridge design.
- **Review focus:** Operator and challenger requirements, withdrawal liquidity and dispute windows.
- **Status evidence / qualification:** The whitepaper specifies an honest watchtower assumption within a permissioned set; implementation and deployed configuration require separate review.
- **Project/resource:** [Clementine and cBTC](https://citrea.xyz/)
- **Source 1:** [Clementine whitepaper](https://citrea.xyz/clementine_whitepaper.pdf) — primary; reviewed 2026-09-25.

<a id="fbtc"></a>
### FBTC

**Type:** asset · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin representation connecting custodial BTC reserves to destination-chain tokens.

- **Bitcoin mechanism:** On-chain contracts combined with off-chain custody operations.
- **Review focus:** Custody policy, pausing, upgrades and safety-committee emergency powers.
- **Status evidence / qualification:** Distinct from the FBTC ticker used by a Bitcoin ETF.
- **Project/resource:** [FBTC](https://fbtc.com/)
- **Source 1:** [Primary source](https://docs.fbtc.com/security/risk-management/custody) — primary; reviewed 2026-09-25.

<a id="l-btc"></a>
### L-BTC

**Type:** asset · **Networks:** Bitcoin, Liquid · **Status:** `documented` · **Reviewed:** 2026-09-25

Liquid's Bitcoin-pegged settlement asset.

- **Bitcoin mechanism:** BTC locked under the Liquid federation's peg arrangements.
- **Review focus:** Federation behavior, peg-out access and network liveness.
- **Status evidence / qualification:** Holding L-BTC is not identical to holding a Bitcoin L1 UTXO.
- **Project/resource:** [L-BTC](https://www.liquid.net/)
- **Source 1:** [Primary source](https://www.liquid.net/) — primary; reviewed 2026-09-25.

<a id="sbtc"></a>
### sBTC

**Type:** asset · **Networks:** Bitcoin, Stacks · **Status:** `documented` · **Reviewed:** 2026-09-25

BTC-backed asset used by applications on Stacks.

- **Bitcoin mechanism:** Bitcoin deposits controlled through the sBTC signer system.
- **Review focus:** Signer threshold, withdrawals, upgrades and application-level risk.
- **Status evidence / qualification:** Distinct from Synthetix's historical sBTC ticker.
- **Project/resource:** [sBTC](https://www.stacks.co/sbtc)
- **Source 1:** [Primary source](https://www.stacks.co/sbtc) — primary; reviewed 2026-09-25.

<a id="strkbtc"></a>
### strkBTC

**Type:** asset · **Networks:** Bitcoin, Starknet · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin representation on Starknet with optional shielded balances and staking integrations.

- **Bitcoin mechanism:** Bitcoin bridging plus Starknet token and privacy infrastructure.
- **Review focus:** Bridge backing, shielding controls, recovery and staking dependencies.
- **Status evidence / qualification:** Privacy features do not remove the bridge's custody assumptions.
- **Project/resource:** [strkBTC](https://www.starknet.io/blog/strkbtc-user-guide/)
- **Source 1:** [Primary source](https://www.starknet.io/blog/strkbtc-user-guide/) — primary; reviewed 2026-09-25.

<a id="tbtc"></a>
### tBTC

**Type:** asset · **Networks:** Bitcoin, Ethereum, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Threshold Network's Bitcoin bridge asset for DeFi.

- **Bitcoin mechanism:** Threshold-signing custody rather than a single traditional custodian.
- **Review focus:** Signer thresholds, bridge governance, redemption and destination-chain contracts.
- **Status evidence / qualification:** Review the current tBTC version, not assumptions from the earlier v1 system.
- **Project/resource:** [tBTC](https://www.threshold.network/)
- **Source 1:** [Primary source](https://docs.threshold.network/tbtc-v2) — primary; reviewed 2026-09-25.

<a id="wbtc"></a>
### WBTC

**Type:** asset · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Custodially backed Bitcoin representation used across DeFi markets.

- **Bitcoin mechanism:** BTC reserves, authorized merchants and token contracts on destination chains.
- **Review focus:** Custodian arrangements, mint and redemption access, freeze controls and additional bridge layers.
- **Status evidence / qualification:** A BTC wrapper, not a yield product by itself.
- **Project/resource:** [WBTC](https://www.wbtc.network/)
- **Source 1:** [Primary source](https://www.wbtc.network/) — primary; reviewed 2026-09-25.

## Staking and shared security

<a id="babylon-bitcoin-staking"></a>
### Babylon Bitcoin Staking

**Type:** protocol · **Networks:** Bitcoin, Babylon · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin collateral used to provide security to external proof-of-stake systems.

- **Bitcoin mechanism:** Bitcoin staking scripts and finality-provider delegation.
- **Review focus:** Slashing conditions, unbonding time, covenant rules and reward denomination.
- **Status evidence / qualification:** This does not change Bitcoin consensus from proof of work to proof of stake.
- **Project/resource:** [Babylon Bitcoin Staking](https://babylonlabs.io/)
- **Source 1:** [Primary source](https://babylonlabs.io/institutional-staking) — primary; reviewed 2026-09-25.

<a id="core"></a>
### Core

**Type:** network · **Networks:** Bitcoin, Core · **Status:** `documented` · **Reviewed:** 2026-09-25

EVM network with BTC timelock-based delegation and CORE rewards.

- **Bitcoin mechanism:** Bitcoin CLTV timelocks help elect Core validators.
- **Review focus:** Lock duration, validator performance, CORE exposure and separate risks when using Core DeFi.
- **Status evidence / qualification:** Official description distinguishes BTC timelocking from bridging; dual staking also requires CORE.
- **Project/resource:** [Core](https://coredao.org/)
- **Source 1:** [Primary source](https://coredao.org/) — primary; reviewed 2026-09-25.

<a id="endur"></a>
### Endur

**Type:** protocol · **Networks:** Starknet · **Status:** `mainnet-announced` · **Reviewed:** 2026-09-25

Liquid staking infrastructure for BTC representations and STRK on Starknet.

- **Bitcoin mechanism:** Receipt tokens backed by product-specific staking positions.
- **Review focus:** Underlying wrapper, staking contracts, token exchange rate and redemption.
- **Status evidence / qualification:** Official site states Starknet mainnet availability; BTC and STRK products are distinct.
- **Project/resource:** [Endur](https://www.endur.fi/)
- **Source 1:** [Primary source](https://www.endur.fi/) — primary; reviewed 2026-09-25.

<a id="pell-network"></a>
### Pell Network

**Type:** protocol · **Networks:** Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Restaking platform using BTC representations and liquid staking derivatives for shared security.

- **Bitcoin mechanism:** Restaked collateral securing decentralized validated services.
- **Review focus:** Underlying wrapper custody, operators, service-specific slashing and reward tokens.
- **Status evidence / qualification:** Terms depend on the particular asset and service selected.
- **Project/resource:** [Pell Network](https://pell.network/)
- **Source 1:** [Primary source](https://docs.pell.network/) — primary; reviewed 2026-09-25.

<a id="pumpbtc"></a>
### PumpBTC

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `status-unclear` · **Reviewed:** 2026-09-25

Liquid Bitcoin staking contracts minting pumpBTC from supported BTC representations.

- **Bitcoin mechanism:** Operator-mediated conversion and Babylon staking in the published contract description.
- **Review focus:** Operator custody, wrapper backing, upgrade roles and unstaking terms.
- **Status evidence / qualification:** Code reviewed; current user-facing service availability was not established.
- **Project/resource:** [PumpBTC](https://github.com/pumpbtc/pumpbtc-contract)
- **Source 1:** [Primary source](https://github.com/pumpbtc/pumpbtc-contract) — primary; reviewed 2026-09-25.

<a id="satlayer"></a>
### SatLayer

**Type:** protocol · **Networks:** Babylon, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Shared-security contracts on Babylon for Bitcoin Validated Services.

- **Bitcoin mechanism:** Wrapped BTC or BTC liquid staking tokens allocated to service security.
- **Review focus:** Underlying assets, operators, contracts and whether a given vault enables slashing.
- **Status evidence / qualification:** Do not assume every displayed vault has the same slashing configuration.
- **Project/resource:** [SatLayer](https://docs.satlayer.xyz/)
- **Source 1:** [Primary source](https://docs.satlayer.xyz/) — primary; reviewed 2026-09-25.

<a id="stacking-dao"></a>
### Stacking DAO

**Type:** protocol · **Networks:** Stacks, Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Liquid staking products for BTC and STX, including stBTC, stSTX and stSTXbtc.

- **Bitcoin mechanism:** Stacks staking mechanisms and liquid receipt tokens.
- **Review focus:** Asset identity, signer or contract dependencies, redemption and yield source.
- **Status evidence / qualification:** Current homepage offers BTC/sBTC deposits into stBTC; older STX-only descriptions are incomplete.
- **Project/resource:** [Stacking DAO](https://www.stackingdao.com/)
- **Source 1:** [Primary source](https://www.stackingdao.com/) — primary; reviewed 2026-09-25.

<a id="starknet-bitcoin-staking"></a>
### Starknet Bitcoin staking

**Type:** protocol · **Networks:** Starknet · **Status:** `documented` · **Reviewed:** 2026-09-25

Staking supported tokenized BTC on Starknet to receive STRK rewards.

- **Bitcoin mechanism:** BTC wrapper tokens locked in Starknet staking contracts.
- **Review focus:** Wrapper and bridge security, validator rules, unbonding and STRK price exposure.
- **Status evidence / qualification:** Starknet is an Ethereum L2; this is not staking an unwrapped Bitcoin L1 UTXO.
- **Project/resource:** [Starknet Bitcoin staking](https://www.starknet.io/staking/)
- **Source 1:** [Primary source](https://www.starknet.io/staking/) — primary; reviewed 2026-09-25.

## Lending and Bitcoin collateral

<a id="aave"></a>
### Aave

**Type:** application · **Networks:** Ethereum, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Money markets supporting Bitcoin representations as collateral or supplied assets in selected markets.

- **Bitcoin mechanism:** Destination-chain contracts using tokens such as WBTC and cbBTC.
- **Review focus:** Market-specific collateral factors, oracles, liquidations and wrapper custody.
- **Status evidence / qualification:** BTC exposure on Aave generally adds wrapper and chain dependencies; separate native-collateral pilots need separate review.
- **Project/resource:** [Aave](https://aave.com/)
- **Source 1:** [Primary source](https://aave.com/) — primary; reviewed 2026-09-25.

<a id="avalon-labs"></a>
### Avalon Labs

**Type:** application · **Networks:** Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-focused on-chain money markets, USDa borrowing and separate institutional credit products.

- **Bitcoin mechanism:** Product-specific smart contracts and, for CeDeFi loans, custodial collateral.
- **Review focus:** Identify on-chain versus institutional terms, custody, rates and liquidation controls.
- **Status evidence / qualification:** The site's On-Chain and CeDeFi products are separate trust models.
- **Project/resource:** [Avalon Labs](https://www.avalonfinance.xyz/)
- **Source 1:** [Primary source](https://www.avalonfinance.xyz/) — primary; reviewed 2026-09-25.

<a id="babylon-trustless-bitcoin-vaults"></a>
### Babylon Trustless Bitcoin Vaults

**Type:** infrastructure · **Networks:** Bitcoin, Ethereum · **Status:** `testnet` · **Reviewed:** 2026-09-25

Native BTC collateral infrastructure targeting applications such as external-chain borrowing.

- **Bitcoin mechanism:** BTCVault construction with external recognition of Bitcoin collateral.
- **Review focus:** Actual testnet/mainnet stage, liquidation path, proof system and recovery conditions.
- **Status evidence / qualification:** Homepage's TBV access link points to a testnet app; the Aave integration is not labeled as a verified live lending market here.
- **Project/resource:** [Babylon Trustless Bitcoin Vaults](https://babylonlabs.io/)
- **Source 1:** [Primary source](https://babylonlabs.io/) — primary; reviewed 2026-09-25.

<a id="debifi"></a>
### Debifi

**Type:** application · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Connects Bitcoin borrowers with institutional lenders for fiat and stablecoin loans.

- **Bitcoin mechanism:** Dedicated 3-of-4 Bitcoin multisignature collateral escrow.
- **Review focus:** Key-holder roles, lender terms, identity checks and liquidation processes.
- **Status evidence / qualification:** Institutional lending marketplace; not an autonomous Bitcoin L1 money market.
- **Project/resource:** [Debifi](https://debifi.com/)
- **Source 1:** [Primary source](https://debifi.com/) — primary; reviewed 2026-09-25.

<a id="firefish"></a>
### Firefish

**Type:** application · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Marketplace for fiat or stablecoin loans secured by Bitcoin.

- **Bitcoin mechanism:** On-chain multisignature escrow with off-chain loan settlement.
- **Review focus:** Escrow roles, default procedures, liquidation execution and legal counterparties.
- **Status evidence / qualification:** Combines Bitcoin collateral infrastructure with contractual lending relationships.
- **Project/resource:** [Firefish](https://firefish.io/)
- **Source 1:** [Primary source](https://docs.firefish.io/) — primary; reviewed 2026-09-25.

<a id="fluid"></a>
### Fluid

**Type:** application · **Networks:** Ethereum, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Liquidity and lending infrastructure with WBTC-related markets.

- **Bitcoin mechanism:** Smart-contract vaults and a shared liquidity architecture.
- **Review focus:** Liquidations, oracle behavior, contract architecture and BTC wrapper custody.
- **Status evidence / qualification:** The cited proposal establishes WBTC market design; current live market parameters need app verification.
- **Project/resource:** [Fluid](https://fluid.io/)
- **Source 1:** [Primary source](https://gov.fluid.io/t/launch-wbtc-markets-on-fluid/787) — primary; reviewed 2026-09-25.

<a id="granite"></a>
### Granite

**Type:** application · **Networks:** Stacks · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-backed borrowing with isolated collateral and partial liquidations.

- **Bitcoin mechanism:** sBTC collateral in Stacks smart contracts.
- **Review focus:** sBTC peg, price oracles, liquidation execution and contract controls.
- **Status evidence / qualification:** The protocol says posted collateral is not re-lent; that does not remove liquidation risk.
- **Project/resource:** [Granite](https://www.granite.world/)
- **Source 1:** [Primary source](https://www.granite.world/) — primary; reviewed 2026-09-25.

<a id="lava"></a>
### Lava

**Type:** application · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-collateralized dollar borrowing and related spending services.

- **Bitcoin mechanism:** BTC collateral arrangements linked to external loan and payment infrastructure.
- **Review focus:** Contract and key control, liquidation, funding counterparties and card eligibility.
- **Status evidence / qualification:** Self-custody marketing is not used here as an independent security certification.
- **Project/resource:** [Lava](https://www.lava.xyz/)
- **Source 1:** [Primary source](https://www.lava.xyz/) — primary; reviewed 2026-09-25.

<a id="lend-at-hodl-hodl"></a>
### Lend at Hodl Hodl

**Type:** application · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Marketplace for crypto loans secured by Bitcoin multisignature escrow.

- **Bitcoin mechanism:** BTC collateral in a multisig contract; loan currency moves separately.
- **Review focus:** Counterparty performance, dispute resolution, LTV thresholds and contract recovery.
- **Status evidence / qualification:** Lenders need to inspect the loan currency; BTC collateral does not mean BTC-denominated lending.
- **Project/resource:** [Lend at Hodl Hodl](https://lend.hodlhodl.com/)
- **Source 1:** [Primary source](https://lend.hodlhodl.com/) — primary; reviewed 2026-09-25.

<a id="lendasat"></a>
### Lendasat

**Type:** application · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Peer-to-peer loans with Bitcoin collateral and fiat or stablecoin settlement.

- **Bitcoin mechanism:** 2-of-3 multisignature collateral with a dispute-resolution participant.
- **Review focus:** Counterparty repayment, dispute process, liquidation and recovery tools.
- **Status evidence / qualification:** Shared control is different from unilateral self-custody.
- **Project/resource:** [Lendasat](https://lendasat.com/docs)
- **Source 1:** [Primary source](https://lendasat.com/docs/p2p-loans/faq) — primary; reviewed 2026-09-25.

<a id="liquidium"></a>
### Liquidium

**Type:** application · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

BTC loans secured by supported Ordinals or Runes, with lenders exposed to the collateral on default.

- **Bitcoin mechanism:** Bitcoin-native collateral contracts for the Bitcoin product.
- **Review focus:** Repayment deadlines, collectible valuation, collateral transfer and illiquidity.
- **Status evidence / qualification:** The site also has another-chain product; this listing covers Bitcoin loans.
- **Project/resource:** [Liquidium](https://liquidium.wtf/)
- **Source 1:** [Primary source](https://liquidium.wtf/) — primary; reviewed 2026-09-25.

<a id="morpho"></a>
### Morpho

**Type:** application · **Networks:** Ethereum, Base, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Isolated lending markets and curated vaults, including cbBTC collateral markets.

- **Bitcoin mechanism:** Token collateral in market-specific smart contracts.
- **Review focus:** Oracle selection, liquidation parameters, wrapper custody and vault-curator allocation.
- **Status evidence / qualification:** A market can exist permissionlessly without being endorsed by Morpho or this list.
- **Project/resource:** [Morpho](https://morpho.org/)
- **Source 1:** [Primary source](https://morpho.org/blog/cbbtc-lending-markets-deployed-on-morpho) — primary; reviewed 2026-09-25.

<a id="sovryn"></a>
### Sovryn

**Type:** application · **Networks:** Rootstock · **Status:** `documented` · **Reviewed:** 2026-09-25

Rootstock lending, collateralized borrowing and trading suite.

- **Bitcoin mechanism:** RBTC and other supported assets in smart contracts.
- **Review focus:** Rootstock peg, contract governance, oracles and liquidation rules.
- **Status evidence / qualification:** Includes several subprotocols with different economics.
- **Project/resource:** [Sovryn](https://sovryn.app/)
- **Source 1:** [Primary source](https://sovryn.app/) — primary; reviewed 2026-09-25.

<a id="venus"></a>
### Venus

**Type:** application · **Networks:** BNB Chain, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Money-market protocol with BTCB and other Bitcoin-related collateral markets.

- **Bitcoin mechanism:** Wrapped assets in destination-chain lending contracts.
- **Review focus:** Wrapper backing, oracle configuration, liquidations and governance.
- **Status evidence / qualification:** Supported assets differ by pool and chain; check current limits and pause flags.
- **Project/resource:** [Venus](https://venus.io/)
- **Source 1:** [Primary source](https://docs-v4.venus.io/risk) — primary; reviewed 2026-09-25.

<a id="vesu"></a>
### Vesu

**Type:** application · **Networks:** Starknet · **Status:** `documented` · **Reviewed:** 2026-09-25

Starknet lending pools and curated vault infrastructure within the Bitcoin staking ecosystem.

- **Bitcoin mechanism:** Pool-specific collateral contracts on Starknet.
- **Review focus:** Accepted BTC representation, oracle, liquidation and curator configuration.
- **Status evidence / qualification:** Endur lists Vesu as an integration; no individual BTC market or rate is certified here.
- **Project/resource:** [Vesu](https://vesu.xyz/)
- **Source 1:** [Primary source](https://docs.vesu.xyz/) — primary; reviewed 2026-09-25.

<a id="zest-protocol"></a>
### Zest Protocol

**Type:** application · **Networks:** Stacks, Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Stacks lending markets and a separately described Bitcoin Collateral Vault initiative.

- **Bitcoin mechanism:** sBTC-based lending; proposed/native-vault paths have different mechanics.
- **Review focus:** Liquidations, price oracles, sBTC signers and the deployment stage of each vault product.
- **Status evidence / qualification:** Existing Stacks markets must not be conflated with new vault architecture.
- **Project/resource:** [Zest Protocol](https://www.zestprotocol.com/)
- **Source 1:** [Primary source](https://www.zestprotocol.com/) — primary; reviewed 2026-09-25.

## Stablecoins and synthetic dollars

<a id="arkadiko"></a>
### Arkadiko

**Type:** application · **Networks:** Stacks · **Status:** `documented` · **Reviewed:** 2026-09-25

Stablecoin and DeFi system whose USDA vaults are described as STX-collateralized.

- **Bitcoin mechanism:** Stacks collateral contracts and oracle-dependent debt positions.
- **Review focus:** STX volatility, collateral ratios, liquidations and contract controls.
- **Status evidence / qualification:** Bitcoin-ecosystem inclusion does not mean USDA is directly backed by BTC.
- **Project/resource:** [Arkadiko](https://arkadiko.finance/)
- **Source 1:** [Primary source](https://arkadiko.finance/) — primary; reviewed 2026-09-25.

<a id="btcfi-bifrost"></a>
### BTCFi (Bifrost)

**Type:** application · **Networks:** Bitcoin, Bifrost, Base · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-collateralized borrowing service and related BtcUSD ecosystem.

- **Bitcoin mechanism:** Product-specific collateral arrangements supporting native BTC and BTC representations.
- **Review focus:** Collateral custody, supported routes, liquidation rules and stablecoin redemption.
- **Status evidence / qualification:** A specific product brand, distinct from the general term BTCfi; the source lists BTC, WBTC, BTCB and cbBTC collateral.
- **Project/resource:** [BTCFi (Bifrost)](https://www.btcfi.one/)
- **Source 1:** [Primary source](https://ecosystem.btcfi.one/) — primary; reviewed 2026-09-25.

<a id="ctusd"></a>
### ctUSD

**Type:** asset · **Networks:** Citrea · **Status:** `documented` · **Reviewed:** 2026-09-25

Dollar stablecoin within the Citrea ecosystem described as backed by cash and short-term Treasury bills.

- **Bitcoin mechanism:** External fiat reserves and tokens on Citrea.
- **Review focus:** Issuer, reserves, redemption eligibility and chain risk.
- **Status evidence / qualification:** Not BTC-collateralized despite use in Bitcoin capital markets.
- **Project/resource:** [ctUSD](https://citrea.xyz/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="ducat-unit"></a>
### Ducat / UNIT

**Type:** protocol · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

BTC-backed stablecoin design using collateral vaults and MPC-coordinated rules.

- **Bitcoin mechanism:** Native BTC collateral plus external guardians, oracles and protocol nodes.
- **Review focus:** Guardian/signing assumptions, liquidation path, oracle integrity and deployment stage.
- **Status evidence / qualification:** BTC-native branding is not a claim that Bitcoin alone enforces every stablecoin rule.
- **Project/resource:** [Ducat / UNIT](https://docs.ducatprotocol.com/)
- **Source 1:** [Primary source](https://docs.ducatprotocol.com/how-ducat-works/vaults) — primary; reviewed 2026-09-25.

<a id="hermetica"></a>
### Hermetica

**Type:** application · **Networks:** Stacks, Bitcoin · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

USDh synthetic-dollar product and hBTC Bitcoin yield strategies.

- **Bitcoin mechanism:** Strategy-managed financial exposure delivered through ecosystem assets.
- **Review focus:** Hedging and custody arrangements, counterparties, liquidity and product-specific redemption.
- **Status evidence / qualification:** Included from Stacks' official ecosystem report; current detailed product mechanics need direct-document review.
- **Project/resource:** [Hermetica](https://www.stacks.co/bitcoin-native-finance)
- **Source 1:** [Primary source](https://www.stacks.co/blog/q1-2026-snapshot) — primary; reviewed 2026-09-25.

<a id="mezo"></a>
### Mezo

**Type:** application · **Networks:** Bitcoin, Mezo · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin finance platform with BTC-backed MUSD borrowing and yield-vault access.

- **Bitcoin mechanism:** Bitcoin-linked collateral on Mezo and application-specific debt/vault contracts.
- **Review focus:** Collateral bridge, liquidation and redemption rules; vaults add curator risk.
- **Status evidence / qualification:** MUSD's dollar target is distinct from holding BTC; Upshift-powered vaults are a separate product.
- **Project/resource:** [Mezo](https://mezo.org/)
- **Source 1:** [Primary source](https://mezo.org/) — primary; reviewed 2026-09-25.

<a id="money-on-chain"></a>
### Money On Chain

**Type:** application · **Networks:** Rootstock · **Status:** `documented` · **Reviewed:** 2026-09-25

DOC dollar exposure and BPRO Bitcoin exposure within a shared collateral system.

- **Bitcoin mechanism:** Bitcoin-linked collateral on Rootstock with risk allocated between token classes.
- **Review focus:** RBTC peg, collateral model, oracles and BPRO exposure.
- **Status evidence / qualification:** BPRO is a risk-bearing product, not a plain BTC deposit.
- **Project/resource:** [Money On Chain](https://moneyonchain.com/)
- **Source 1:** [Primary source](https://moneyonchain.com/) — primary; reviewed 2026-09-25.

<a id="sovryn-zero"></a>
### Sovryn Zero

**Type:** application · **Networks:** Rootstock · **Status:** `documented` · **Reviewed:** 2026-09-25

BTC-backed stablecoin borrowing within the Sovryn ecosystem.

- **Bitcoin mechanism:** RBTC collateral, stablecoin debt and a liquidation stability pool.
- **Review focus:** Origination fees, redemptions, collateral ratio and liquidation.
- **Status evidence / qualification:** The page includes DLLR and older ZUSD language; verify the current app and docs before interpreting terms.
- **Project/resource:** [Sovryn Zero](https://sovryn.com/zero)
- **Source 1:** [Primary source](https://sovryn.com/zero) — primary; reviewed 2026-09-25.

## Exchanges and trading

<a id="alex"></a>
### ALEX

**Type:** application · **Networks:** Stacks · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

Stacks DeFi suite with liquidity and exchange functionality.

- **Bitcoin mechanism:** Stacks contracts and associated ecosystem assets.
- **Review focus:** Incident history, paused functions, contract versions and current recovery information.
- **Status evidence / qualification:** Ecosystem listing establishes identity, not present operational health.
- **Project/resource:** [ALEX](https://alexlab.co/)
- **Source 1:** [Primary source](https://www.stacks.co/explore/ecosystem) — primary; reviewed 2026-09-25.

<a id="bitflow"></a>
### Bitflow

**Type:** application · **Networks:** Stacks · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

Exchange and liquidity infrastructure for Stacks assets including sBTC pairs.

- **Bitcoin mechanism:** Stacks smart-contract liquidity pools.
- **Review focus:** sBTC backing, pool design, price ranges, impermanent loss and contract risk.
- **Status evidence / qualification:** Official Stacks source describes sBTC/USDCx liquidity activity.
- **Project/resource:** [Bitflow](https://www.bitflow.finance/)
- **Source 1:** [Primary source](https://www.stacks.co/blog/stacks-90-day-defi-incentive-program-announced-with-zest-and-bitflow) — primary; reviewed 2026-09-25.

<a id="curve"></a>
### Curve

**Type:** application · **Networks:** Ethereum, Multichain · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

Liquidity pools and related DeFi infrastructure used with tokenized Bitcoin.

- **Bitcoin mechanism:** Automated market makers on destination chains.
- **Review focus:** Pool composition, wrapper depegs, liquidity, impermanent loss and contracts.
- **Status evidence / qualification:** WBTC's official site lists Curve among supported trading venues; verify the particular pool.
- **Project/resource:** [Curve](https://curve.finance/)
- **Source 1:** [Primary source](https://www.wbtc.network/) — primary; reviewed 2026-09-25.

<a id="flashnet"></a>
### Flashnet

**Type:** infrastructure · **Networks:** Bitcoin, Spark, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin trading and payment orchestration infrastructure with native-asset routing.

- **Bitcoin mechanism:** Route-dependent exchange, bridge and settlement integrations.
- **Review focus:** Route composition, provider trust, underlying payment layer and settlement recovery.
- **Status evidence / qualification:** Spark identifies Flashnet as an ecosystem integration; route guarantees should be checked individually.
- **Project/resource:** [Flashnet](https://www.flashnet.xyz/)
- **Source 1:** [Primary source](https://www.flashnet.xyz/) — primary; reviewed 2026-09-25.

<a id="juiceswap"></a>
### JuiceSwap

**Type:** application · **Networks:** Citrea · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

Exchange listed among Citrea's Bitcoin applications.

- **Bitcoin mechanism:** Citrea application contracts and assets.
- **Review focus:** Pool deployment, liquidity, contract review and bridge dependencies.
- **Status evidence / qualification:** Listed from the network's official directory; no execution testing performed.
- **Project/resource:** [JuiceSwap](https://bapp.juiceswap.com/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="ln-markets"></a>
### LN Markets

**Type:** application · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin derivatives interface using Lightning and external exchange liquidity.

- **Bitcoin mechanism:** Lightning funding combined with platform-managed trading infrastructure.
- **Review focus:** Margin liquidation, platform custody, execution and exchange counterparties.
- **Status evidence / qualification:** Lightning deposits do not turn a derivatives venue into a self-custodial protocol.
- **Project/resource:** [LN Markets](https://lnmarkets.com/)
- **Source 1:** [Primary source](https://lnmarkets.com/) — primary; reviewed 2026-09-25.

<a id="satsuma"></a>
### Satsuma

**Type:** application · **Networks:** Citrea · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

Exchange listed in Citrea's application ecosystem.

- **Bitcoin mechanism:** Citrea application contracts and assets.
- **Review focus:** Pool deployment, liquidity, contract review and cBTC bridge dependencies.
- **Status evidence / qualification:** Identity and category confirmed by Citrea; detailed product due diligence remains open.
- **Project/resource:** [Satsuma](https://www.satsuma.exchange/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="sideswap"></a>
### SideSwap

**Type:** application · **Networks:** Liquid · **Status:** `documented` · **Reviewed:** 2026-09-25

Peer-to-peer swaps and settlement tools for Liquid assets.

- **Bitcoin mechanism:** Liquid asset transactions and L-BTC peg access.
- **Review focus:** Liquid federation, individual asset issuers and market liquidity.
- **Status evidence / qualification:** Non-custodial trading does not remove the underlying Liquid peg assumptions.
- **Project/resource:** [SideSwap](https://sideswap.io/)
- **Source 1:** [Primary source](https://sideswap.io/) — primary; reviewed 2026-09-25.

<a id="unisat"></a>
### UniSat

**Type:** application · **Networks:** Bitcoin, Fractal · **Status:** `documented` · **Reviewed:** 2026-09-25

Wallet, marketplace and data tools for Bitcoin asset protocols.

- **Bitcoin mechanism:** Ordinal, BRC-20, Rune and Alkane-aware transaction and indexing systems.
- **Review focus:** Asset-indexer correctness, signing, UTXO selection and marketplace liquidity.
- **Status evidence / qualification:** Features on Fractal use a different network from Bitcoin mainnet.
- **Project/resource:** [UniSat](https://unisat.io/)
- **Source 1:** [Primary source](https://unisat.io/) — primary; reviewed 2026-09-25.

<a id="uniswap"></a>
### Uniswap

**Type:** application · **Networks:** Ethereum, Multichain · **Status:** `ecosystem-listed` · **Reviewed:** 2026-09-25

General-purpose exchange infrastructure with tokenized BTC markets.

- **Bitcoin mechanism:** Version-specific automated market makers and, in v4, optional hooks.
- **Review focus:** Token authenticity, LP price ranges, wrapper risk and any pool-specific hook.
- **Status evidence / qualification:** BTC trading uses a representation such as WBTC, not native Bitcoin settlement.
- **Project/resource:** [Uniswap](https://uniswap.org/)
- **Source 1:** [Primary source](https://www.wbtc.network/) — primary; reviewed 2026-09-25.

## Yield markets and managed strategies

<a id="bedrock"></a>
### Bedrock

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `changed` · **Reviewed:** 2026-09-25

uniBTC and brBTC alongside a broader Bitcoin yield-vault product suite.

- **Bitcoin mechanism:** BTC representations routed into product-specific strategies.
- **Review focus:** Custody, token backing, contracts and off-chain strategy dependencies.
- **Status evidence / qualification:** Current site describes Bedrock 2.0, including lending, derivatives and RWA strategies beyond staking.
- **Project/resource:** [Bedrock](https://www.bedrock.technology/)
- **Source 1:** [Primary source](https://www.bedrock.technology/) — primary; reviewed 2026-09-25.

<a id="lombard-lbtc"></a>
### Lombard LBTC

**Type:** asset · **Networks:** Bitcoin, Multichain · **Status:** `changed` · **Reviewed:** 2026-09-25

Yield-bearing BTC asset now tied to a Bitwise-managed covered-call strategy.

- **Bitcoin mechanism:** Custodied BTC backing and non-rebasing tokens with an exchange rate.
- **Review focus:** Options losses, counterparties, custody and redemption delays.
- **Status evidence / qualification:** Docs say Babylon backing ended in August 2026 and the new strategy started August 17; do not describe today's LBTC as simply a Babylon LST.
- **Project/resource:** [Lombard LBTC](https://docs.lombard.finance/use/lbtc)
- **Source 1:** [Primary source](https://docs.lombard.finance/learn/products/assets) — primary; reviewed 2026-09-25.
- **Source 2:** [Current LBTC yield mechanics](https://docs.lombard.finance/use/lbtc) — primary; reviewed 2026-09-25.

<a id="lorenzo-protocol"></a>
### Lorenzo Protocol

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin liquidity and asset-management infrastructure, including stBTC-related designs.

- **Bitcoin mechanism:** Tokenized BTC principal or yield exposure and strategy-specific backing.
- **Review focus:** Current product scope, custody, receipt-token rights and redemption availability.
- **Status evidence / qualification:** Public Bitcoin-liquidity documentation exists; current front-end availability is not certified.
- **Project/resource:** [Lorenzo Protocol](https://www.lorenzo-protocol.xyz/)
- **Source 1:** [Primary source](https://lorenzo-protocol.gitbook.io/docs/bitcoin-liquidity-layer) — primary; reviewed 2026-09-25.

<a id="pendle"></a>
### Pendle

**Type:** application · **Networks:** Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Yield tokenization and trading usable with supported Bitcoin yield assets.

- **Bitcoin mechanism:** Principal and yield claims on an underlying yield-bearing token.
- **Review focus:** Underlying protocol and wrapper risk, maturity, liquidity and yield-token decay.
- **Status evidence / qualification:** BTC market availability changes; inspect the specific underlying asset and expiry.
- **Project/resource:** [Pendle](https://www.pendle.finance/)
- **Source 1:** [Primary source](https://www.pendle.finance/pendle) — primary; reviewed 2026-09-25.

<a id="solv-protocol"></a>
### Solv Protocol

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

SolvBTC representation, xSolvBTC yield exposure and managed BTC strategies.

- **Bitcoin mechanism:** Product-specific custody, reserve and strategy arrangements.
- **Review focus:** Backing composition, manager permissions, counterparties and redemption terms.
- **Status evidence / qualification:** SolvBTC, xSolvBTC and BTC+ should not be treated as identical products.
- **Project/resource:** [Solv Protocol](https://solv.finance/)
- **Source 1:** [Primary source](https://solv.finance/) — primary; reviewed 2026-09-25.

<a id="spectra"></a>
### Spectra

**Type:** application · **Networks:** Multichain, Hemi · **Status:** `documented` · **Reviewed:** 2026-09-25

Permissionless yield markets and vault infrastructure, including Bitcoin-related ecosystem use.

- **Bitcoin mechanism:** Separate principal/yield claims and interest-rate markets.
- **Review focus:** Underlying backing, maturity, curator choices and secondary-market liquidity.
- **Status evidence / qualification:** Hemi is among the networks shown; each BTC market needs independent verification.
- **Project/resource:** [Spectra](https://www.spectra.finance/)
- **Source 1:** [Primary source](https://www.spectra.finance/) — primary; reviewed 2026-09-25.

<a id="yieldbasis"></a>
### YieldBasis

**Type:** protocol · **Networks:** Ethereum · **Status:** `documented` · **Reviewed:** 2026-09-25

Liquidity strategy designed to offset impermanent loss for tokenized BTC and ETH.

- **Bitcoin mechanism:** Leveraged liquidity positions rather than Bitcoin consensus rewards.
- **Review focus:** Leverage, borrowing costs, rebalancing, wrapper backing and pool losses.
- **Status evidence / qualification:** The design's leverage is economically material; claims of eliminating IL do not eliminate all losses.
- **Project/resource:** [YieldBasis](https://yieldbasis.com/)
- **Source 1:** [Primary source](https://docs.yieldbasis.com/pdf/mica-whitepaper.pdf) — primary; reviewed 2026-09-25.

## Cross-chain and atomic swaps

<a id="atomiq"></a>
### Atomiq

**Type:** protocol · **Networks:** Bitcoin, Lightning, Solana, Starknet · **Status:** `documented` · **Reviewed:** 2026-09-25

Atomic swaps between Bitcoin and supported smart-contract chains.

- **Bitcoin mechanism:** Escrow contracts, Bitcoin light-client verification and refund paths.
- **Review focus:** Light-client implementation, swap expiry, smart contracts and counterparty liquidity.
- **Status evidence / qualification:** The site documents both on-chain Bitcoin and Lightning routes.
- **Project/resource:** [Atomiq](https://www.atomiq.exchange/)
- **Source 1:** [Primary source](https://www.atomiq.exchange/) — primary; reviewed 2026-09-25.

<a id="boltz"></a>
### Boltz

**Type:** application · **Networks:** Bitcoin, Lightning, Liquid, Rootstock, Arkade · **Status:** `documented` · **Reviewed:** 2026-09-25

Submarine and chain swaps across Bitcoin payment layers, with additional stablecoin routes.

- **Bitcoin mechanism:** Atomic-swap contracts and route-specific execution legs.
- **Review focus:** Refund backups, timeouts, fees and any extra DEX or bridge used by a route.
- **Status evidence / qualification:** Stablecoin routes can compose additional components beyond a basic BTC-to-Lightning swap.
- **Project/resource:** [Boltz](https://boltz.exchange/)
- **Source 1:** [Primary source](https://api.docs.boltz.exchange/lifecycle.html) — primary; reviewed 2026-09-25.

<a id="chainflip"></a>
### Chainflip

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Native-asset cross-chain swaps with liquidity, Boost and lending products.

- **Bitcoin mechanism:** Validator MPC custody and cross-chain execution.
- **Review focus:** Validator security, custody, confirmation risk and product-specific lending terms.
- **Status evidence / qualification:** Swap, Boost and lending exposures have different risk profiles.
- **Project/resource:** [Chainflip](https://chainflip.io/)
- **Source 1:** [Primary source](https://chainflip.io/) — primary; reviewed 2026-09-25.

<a id="garden"></a>
### Garden

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Atomic-swap infrastructure and APIs connecting Bitcoin with other networks.

- **Bitcoin mechanism:** Chain-specific swap contracts and liquidity providers.
- **Review focus:** Timeouts, refund implementation, provider liquidity and destination-chain contracts.
- **Status evidence / qualification:** Swap contracts and supported chain routes are documented separately.
- **Project/resource:** [Garden](https://garden.finance/docs/)
- **Source 1:** [Primary source](https://docs.garden.finance/) — primary; reviewed 2026-09-25.

<a id="lendaswap"></a>
### LendaSwap

**Type:** application · **Networks:** Bitcoin, Lightning, Arkade, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin-to-stablecoin swaps associated with Lendasat.

- **Bitcoin mechanism:** Route-specific swaps using Bitcoin payment layers.
- **Review focus:** Exact route, timeout/recovery behavior and stablecoin issuer.
- **Status evidence / qualification:** Product directory describes Lightning and Arkade integration; distinct from Lendasat loans.
- **Project/resource:** [LendaSwap](https://lendasat.com/docs)
- **Source 1:** [Primary source](https://lendasat.com/docs) — primary; reviewed 2026-09-25.

<a id="thorchain"></a>
### THORChain

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Cross-chain exchange and liquidity infrastructure for native assets including BTC.

- **Bitcoin mechanism:** Threshold-controlled network vaults and pool-based exchange.
- **Review focus:** Validator economics, vault custody, pool exposure and network halts.
- **Status evidence / qualification:** Native-asset swaps still have network custody assumptions; distinguish swap pools from historical lending products.
- **Project/resource:** [THORChain](https://thorchain.org/)
- **Source 1:** [Primary source](https://thorchain.org/) — primary; reviewed 2026-09-25.

## Payments, Lightning liquidity and ecash

<a id="amboss"></a>
### Amboss

**Type:** infrastructure · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin payment infrastructure and integration tooling.

- **Bitcoin mechanism:** Lightning-connected payment routes and receiving-wallet integrations.
- **Review focus:** Wallet custody choice, route support and service availability.
- **Status evidence / qualification:** Current homepage emphasizes payment APIs; legacy product names need separate verification.
- **Project/resource:** [Amboss](https://amboss.tech/)
- **Source 1:** [Primary source](https://amboss.tech/) — primary; reviewed 2026-09-25.

<a id="arkade"></a>
### Arkade

**Type:** infrastructure · **Networks:** Bitcoin, Ark · **Status:** `documented` · **Reviewed:** 2026-09-25

Ark-based toolkit for payments, programmable transaction flows and asset exchange.

- **Bitcoin mechanism:** Bitcoin transaction structures coordinated through Arkade.
- **Review focus:** Operator availability, committed recovery paths and implementation-specific assumptions.
- **Status evidence / qualification:** Homepage labels Intents as developer preview; do not treat every feature as production-ready.
- **Project/resource:** [Arkade](https://arkadeos.com/)
- **Source 1:** [Primary source](https://arkadeos.com/) — primary; reviewed 2026-09-25.

<a id="cashu"></a>
### Cashu

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Open Chaumian ecash protocol with Bitcoin-linked mints and wallets.

- **Bitcoin mechanism:** Bearer claims issued by mints, commonly funded over Lightning.
- **Review focus:** Mint solvency, issuer trust and token loss or double spending.
- **Status evidence / qualification:** Each mint is its own trust relationship.
- **Project/resource:** [Cashu](https://cashu.space/)
- **Source 1:** [Primary source](https://cashu.space/) — primary; reviewed 2026-09-25.

<a id="fedimint"></a>
### Fedimint

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Federated ecash for Bitcoin payments and community custody.

- **Bitcoin mechanism:** Federation custody backing private ecash notes.
- **Review focus:** Guardian collusion, solvency, federation availability and exit liquidity.
- **Status evidence / qualification:** Privacy and distributed custody do not make ecash self-custodial BTC.
- **Project/resource:** [Fedimint](https://fedimint.org/)
- **Source 1:** [Primary source](https://fedimint.org/) — primary; reviewed 2026-09-25.

<a id="lightning-loop"></a>
### Lightning Loop

**Type:** application · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Submarine swaps for moving value between Lightning and on-chain Bitcoin.

- **Bitcoin mechanism:** HTLC-based swaps and refund conditions.
- **Review focus:** Fees, timeout handling, liquidity and transaction monitoring.
- **Status evidence / qualification:** Channel management service; not a passive yield product.
- **Project/resource:** [Lightning Loop](https://docs.lightning.engineering/lightning-network-tools/loop)
- **Source 1:** [Primary source](https://docs.lightning.engineering/lightning-network-tools/loop) — primary; reviewed 2026-09-25.

<a id="lightning-pool"></a>
### Lightning Pool

**Type:** application · **Networks:** Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Marketplace for leasing Lightning channel liquidity.

- **Bitcoin mechanism:** Bitcoin allocated to payment-channel capacity.
- **Review focus:** Channel demand, node uptime, lease terms, fees and operational costs.
- **Status evidence / qualification:** Liquidity fees are a different source of return from lending or staking.
- **Project/resource:** [Lightning Pool](https://docs.lightning.engineering/lightning-network-tools/pool)
- **Source 1:** [Primary source](https://docs.lightning.engineering/lightning-network-tools/pool) — primary; reviewed 2026-09-25.

<a id="mercury-layer"></a>
### Mercury Layer

**Type:** infrastructure · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Statechain implementation using blinded co-signing and key updates.

- **Bitcoin mechanism:** UTXO ownership transfers supported by a key-share service.
- **Review focus:** Server key deletion/update assumptions, backup transactions and exit timelocks.
- **Status evidence / qualification:** Implementation documentation reviewed; current service availability not transaction-tested.
- **Project/resource:** [Mercury Layer](https://mercurylayer.com/)
- **Source 1:** [Primary source](https://mercurylayer.com/) — primary; reviewed 2026-09-25.

<a id="second"></a>
### Second

**Type:** infrastructure · **Networks:** Bitcoin, Ark, Lightning · **Status:** `mainnet-announced` · **Reviewed:** 2026-09-25

Ark implementation and SDKs connecting Ark, Lightning and on-chain payments.

- **Bitcoin mechanism:** Ark virtual UTXOs and implementation-specific transfer/recovery paths.
- **Review focus:** Server availability, VTXO expiry, backups and exit fees.
- **Status evidence / qualification:** Official homepage announces mainnet; no payment testing performed.
- **Project/resource:** [Second](https://second.tech/)
- **Source 1:** [Primary source](https://second.tech/) — primary; reviewed 2026-09-25.

<a id="spark"></a>
### Spark

**Type:** infrastructure · **Networks:** Bitcoin, Spark, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin and asset payment infrastructure with Lightning connectivity.

- **Bitcoin mechanism:** Statechain-style transfers and an operator-assisted Bitcoin ownership system.
- **Review focus:** Operator and key-share assumptions, unilateral exit details and issued-asset backing.
- **Status evidence / qualification:** Distinct from the Spark DeFi lending/savings brand on Ethereum.
- **Project/resource:** [Spark](https://www.spark.money/)
- **Source 1:** [Primary source](https://www.spark.money/) — primary; reviewed 2026-09-25.

## Wallets and access

<a id="bitlight-wallet"></a>
### Bitlight Wallet

**Type:** wallet · **Networks:** Bitcoin, RGB, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Wallet for Bitcoin and RGB assets, with asset issuance tooling.

- **Bitcoin mechanism:** Client-side RGB state and Bitcoin wallet functionality.
- **Review focus:** Asset proofs, issuer authenticity, backups and version compatibility.
- **Status evidence / qualification:** RGB assets require more than a BTC-only recovery assumption.
- **Project/resource:** [Bitlight Wallet](https://bitlightlabs.com/wallet)
- **Source 1:** [Primary source](https://bitlightlabs.com/wallet) — primary; reviewed 2026-09-25.

<a id="leather"></a>
### Leather

**Type:** wallet · **Networks:** Bitcoin, Stacks · **Status:** `documented` · **Reviewed:** 2026-09-25

Wallet for Bitcoin, Stacks assets and ecosystem applications.

- **Bitcoin mechanism:** Bitcoin and Stacks transaction signing.
- **Review focus:** Backups, hardware-wallet compatibility and application approvals.
- **Status evidence / qualification:** Access layer rather than an independent source of yield.
- **Project/resource:** [Leather](https://leather.io/)
- **Source 1:** [Primary source](https://leather.io/) — primary; reviewed 2026-09-25.

<a id="xverse"></a>
### Xverse

**Type:** wallet · **Networks:** Bitcoin, Stacks, Spark, Starknet · **Status:** `documented` · **Reviewed:** 2026-09-25

Wallet and application gateway for Bitcoin assets and connected financial services.

- **Bitcoin mechanism:** User signing plus integrations with distinct Bitcoin-related networks.
- **Review focus:** Recovery, signing permissions and the trust model of each connected service.
- **Status evidence / qualification:** Wallet self-custody does not guarantee self-custody after depositing into an application.
- **Project/resource:** [Xverse](https://www.xverse.app/)
- **Source 1:** [Primary source](https://www.xverse.app/) — primary; reviewed 2026-09-25.

## Developer tools and infrastructure

<a id="bitcoin-dev-kit"></a>
### Bitcoin Dev Kit

**Type:** developer-tool · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Libraries for Bitcoin wallet and transaction applications.

- **Bitcoin mechanism:** Bitcoin descriptors, transaction construction and chain access.
- **Review focus:** Key handling, dependency versions and application security.
- **Status evidence / qualification:** Developer infrastructure, not a financial service.
- **Project/resource:** [Bitcoin Dev Kit](https://bitcoindevkit.org/)
- **Source 1:** [Primary source](https://bitcoindevkit.org/) — primary; reviewed 2026-09-25.

<a id="bitcoin-s"></a>
### Bitcoin-S

**Type:** developer-tool · **Networks:** Bitcoin, Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Scala libraries and tooling for Bitcoin transaction applications.

- **Bitcoin mechanism:** Bitcoin and Lightning data structures and transaction APIs.
- **Review focus:** Application design, signing and maintained library versions.
- **Status evidence / qualification:** Useful building block for Bitcoin financial software.
- **Project/resource:** [Bitcoin-S](https://bitcoin-s.org/)
- **Source 1:** [Primary source](https://bitcoin-s.org/) — primary; reviewed 2026-09-25.

<a id="breez-sdk"></a>
### Breez SDK

**Type:** developer-tool · **Networks:** Bitcoin, Lightning, Spark, Liquid · **Status:** `documented` · **Reviewed:** 2026-09-25

SDKs for embedding Bitcoin payments into applications.

- **Bitcoin mechanism:** Implementation-dependent Bitcoin payment-layer integrations.
- **Review focus:** Which SDK implementation is used, recovery, providers and payment liquidity.
- **Status evidence / qualification:** Different SDK backends have different trust and availability properties.
- **Project/resource:** [Breez SDK](https://breez.technology/)
- **Source 1:** [Primary source](https://breez.technology/) — primary; reviewed 2026-09-25.

<a id="elements"></a>
### Elements

**Type:** developer-tool · **Networks:** Liquid, Sidechains · **Status:** `documented` · **Reviewed:** 2026-09-25

Sidechain-capable software with confidential transactions and asset issuance.

- **Bitcoin mechanism:** Independent or pegged chains with configurable consensus.
- **Review focus:** Operator model, peg construction and issued-asset obligations.
- **Status evidence / qualification:** Software capability does not certify any chain built from it.
- **Project/resource:** [Elements](https://elementsproject.org/)
- **Source 1:** [Primary source](https://elementsproject.org/) — primary; reviewed 2026-09-25.

<a id="layeredge"></a>
### LayerEdge

**Type:** infrastructure · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Proof aggregation and anchoring infrastructure for external applications.

- **Bitcoin mechanism:** Aggregated proofs anchored to underlying networks.
- **Review focus:** Anchoring versus actual enforcement, verifier design and deployment stage.
- **Status evidence / qualification:** Do not equate publishing a proof commitment with inheriting all Bitcoin security properties.
- **Project/resource:** [LayerEdge](https://www.layeredge.io/)
- **Source 1:** [Primary source](https://www.layeredge.io/) — primary; reviewed 2026-09-25.

<a id="lightning-dev-kit"></a>
### Lightning Dev Kit

**Type:** developer-tool · **Networks:** Lightning · **Status:** `documented` · **Reviewed:** 2026-09-25

Modular Lightning implementation and SDK for applications.

- **Bitcoin mechanism:** Payment-channel logic integrated into the host application.
- **Review focus:** Persistence, channel monitoring and integration correctness.
- **Status evidence / qualification:** Developers choose their own operational architecture.
- **Project/resource:** [Lightning Dev Kit](https://lightningdevkit.org/)
- **Source 1:** [Primary source](https://lightningdevkit.org/) — primary; reviewed 2026-09-25.

<a id="metashrew"></a>
### Metashrew

**Type:** developer-tool · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

WASM-powered indexing framework for Bitcoin metaprotocols.

- **Bitcoin mechanism:** Block processing and application-defined indexer logic.
- **Review focus:** Indexer implementation, reorg handling and state agreement.
- **Status evidence / qualification:** Indexing a contract is different from Bitcoin consensus enforcing its full semantics.
- **Project/resource:** [Metashrew](https://github.com/kungfuflex/metashrew)
- **Source 1:** [Primary source](https://github.com/kungfuflex/metashrew) — primary; reviewed 2026-09-25.

<a id="nubit-bitcoin-thunderbolt"></a>
### Nubit / Bitcoin Thunderbolt

**Type:** infrastructure · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin transfer and programmability project now described around Thunderbolt.

- **Bitcoin mechanism:** Off-chain UTXO ownership changes with threshold-signing committees.
- **Review focus:** Committee assumptions, implementation maturity and enforceable exits.
- **Status evidence / qualification:** Older descriptions focused only on data availability are incomplete.
- **Project/resource:** [Nubit / Bitcoin Thunderbolt](https://docs.nubit.org/overview)
- **Source 1:** [Primary source](https://docs.nubit.org/bitcoin-thunderbolt/the-blueprint-for-bitcoins-next-era/how-it-works) — primary; reviewed 2026-09-25.

<a id="rebar-labs"></a>
### Rebar Labs

**Type:** infrastructure · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin APIs, metaprotocol data and transaction-submission tools with MEV-focused features.

- **Bitcoin mechanism:** Bitcoin indexing and transaction-flow infrastructure.
- **Review focus:** Data accuracy, transaction visibility and service dependence.
- **Status evidence / qualification:** Earn, Shield and data products need separate evaluation; no yield claim is inferred from API access.
- **Project/resource:** [Rebar Labs](https://rebarlabs.io/)
- **Source 1:** [Primary source](https://rebarlabs.io/) — primary; reviewed 2026-09-25.

## Research, analytics and ecosystem maps

<a id="babylon-ecosystem"></a>
### Babylon ecosystem

**Type:** ecosystem-directory · **Networks:** Bitcoin, Babylon · **Status:** `documented` · **Reviewed:** 2026-09-25

Official discovery map for staking providers and connected infrastructure.

- **Bitcoin mechanism:** Ecosystem self-reporting.
- **Review focus:** Distinguish direct staking, liquid wrappers and infrastructure providers.
- **Status evidence / qualification:** Partner inclusion is not an audit or endorsement by this list.
- **Project/resource:** [Babylon ecosystem](https://babylonlabs.io/ecosystem)
- **Source 1:** [Primary source](https://babylonlabs.io/ecosystem?aecfdcd8_page=3) — primary; reviewed 2026-09-25.

<a id="bitcoin-layers"></a>
### Bitcoin Layers

**Type:** research-resource · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Independent directory analyzing Bitcoin layers, BTC representations and trust assumptions.

- **Bitcoin mechanism:** Research rather than custody or execution infrastructure.
- **Review focus:** Methodology, assessment date and scope of each project review.
- **Status evidence / qualification:** A useful counterweight to project marketing; classifications can evolve.
- **Project/resource:** [Bitcoin Layers](https://www.bitcoinlayers.org/)
- **Source 1:** [Primary source](https://www.bitcoinlayers.org/) — primary; reviewed 2026-09-25.

<a id="bitcoin-layers-methodology"></a>
### Bitcoin Layers methodology

**Type:** research-resource · **Networks:** Bitcoin, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

Framework covering data availability, operators, settlement and bridge custody.

- **Bitcoin mechanism:** Structured risk analysis.
- **Review focus:** Apply dimensions separately; avoid turning a label into a universal safety score.
- **Status evidence / qualification:** Used as a research lens, not reproduced as a rating system.
- **Project/resource:** [Bitcoin Layers methodology](https://bitcoin-layers.gitbook.io/bitcoin-layers/approach-to-analyzing-risk)
- **Source 1:** [Primary source](https://bitcoin-layers.gitbook.io/bitcoin-layers/approach-to-analyzing-risk) — primary; reviewed 2026-09-25.

<a id="defillama-bitcoin-dashboard"></a>
### DefiLlama Bitcoin dashboard

**Type:** analytics · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Protocol discovery and metrics for projects classified under Bitcoin.

- **Bitcoin mechanism:** Aggregator adapters and category definitions.
- **Review focus:** Double counting, classifications, adapter coverage and TVL versus deposited BTC.
- **Status evidence / qualification:** Bitcoin-linked assets on other chains require additional dashboards; no static TVL ranking is copied here.
- **Project/resource:** [DefiLlama Bitcoin dashboard](https://defillama.com/chain/bitcoin)
- **Source 1:** [Primary source](https://defillama.com/chain/bitcoin?currency=USD) — primary; reviewed 2026-09-25.

<a id="sok-bitcoin-layer-two"></a>
### SoK: Bitcoin Layer Two

**Type:** research-paper · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Research paper surveying Bitcoin layer-two constructions and tradeoffs.

- **Bitcoin mechanism:** Academic systematization.
- **Review focus:** Paper version and gap between design and deployed implementation.
- **Status evidence / qualification:** Complements current project documentation; not a live product directory.
- **Project/resource:** [SoK: Bitcoin Layer Two](https://arxiv.org/abs/2409.02650)
- **Source 1:** [Primary source](https://arxiv.org/abs/2409.02650) — primary; reviewed 2026-09-25.

<a id="stacks-ecosystem"></a>
### Stacks ecosystem

**Type:** ecosystem-directory · **Networks:** Stacks · **Status:** `documented` · **Reviewed:** 2026-09-25

Official application, wallet and developer-tool discovery map.

- **Bitcoin mechanism:** Ecosystem self-reporting.
- **Review focus:** A listing is not a security review or current service guarantee.
- **Status evidence / qualification:** Used for discovery and cross-checking relevance.
- **Project/resource:** [Stacks ecosystem](https://www.stacks.co/explore/ecosystem)
- **Source 1:** [Primary source](https://www.stacks.co/explore/ecosystem) — primary; reviewed 2026-09-25.

## Centralized and institutional finance

<a id="bima"></a>
### Bima

**Type:** platform · **Networks:** Bitcoin, Multichain · **Status:** `changed` · **Reviewed:** 2026-09-25

Structured financing against digital assets with an agreed upside-sharing component.

- **Bitcoin mechanism:** Accountable vault infrastructure and FalconX-held collateral in the documented arrangement.
- **Review focus:** Counterparty and derivative terms, downside exposure and foregone upside.
- **Status evidence / qualification:** Current docs describe institutional structured financing; do not assume the older stablecoin framing still applies.
- **Project/resource:** [Bima](https://docs.bima.money/)
- **Source 1:** [Primary source](https://docs.bima.money/) — primary; reviewed 2026-09-25.

<a id="bouncebit"></a>
### BounceBit

**Type:** platform · **Networks:** Bitcoin, BounceBit, Multichain · **Status:** `documented` · **Reviewed:** 2026-09-25

CeDeFi platform combining custodied assets, managed strategies and an EVM settlement chain.

- **Bitcoin mechanism:** BB-tokens backed through external custody and investment arrangements.
- **Review focus:** Custodian and exchange exposure, manager risk and withdrawal terms.
- **Status evidence / qualification:** Listed as hybrid/centralized finance rather than Bitcoin-native non-custodial staking.
- **Project/resource:** [BounceBit](https://www.bouncebit.io/)
- **Source 1:** [Primary source](https://www.bouncebit.io/) — primary; reviewed 2026-09-25.

<a id="exsat"></a>
### exSat

**Type:** platform · **Networks:** Bitcoin, exSat · **Status:** `changed` · **Reviewed:** 2026-09-25

Digital-asset banking platform offering qualified-access custody, payments and strategy products.

- **Bitcoin mechanism:** Custody and managed strategies alongside Bitcoin-related infrastructure.
- **Review focus:** Eligibility, legal counterparties, strategy leverage and redemption windows.
- **Status evidence / qualification:** Current homepage emphasizes digital banking rather than only a Bitcoin scaling layer.
- **Project/resource:** [exSat](https://exsat.network/)
- **Source 1:** [Primary source](https://exsat.network/) — primary; reviewed 2026-09-25.

<a id="ledn"></a>
### Ledn

**Type:** platform · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Centralized Bitcoin-backed loans and related credit products.

- **Bitcoin mechanism:** Contractual loans with collateral held through custody arrangements.
- **Review focus:** Custody, lender solvency, loan terms, liquidation and jurisdiction.
- **Status evidence / qualification:** CeFi comparison entry; no claim that collateral is controlled solely by the borrower.
- **Project/resource:** [Ledn](https://www.ledn.io/)
- **Source 1:** [Primary source](https://ledn.io/) — primary; reviewed 2026-09-25.

<a id="unchained"></a>
### Unchained

**Type:** platform · **Networks:** Bitcoin · **Status:** `documented` · **Reviewed:** 2026-09-25

Bitcoin financial services built around collaborative custody.

- **Bitcoin mechanism:** Multisignature arrangements and product-specific financial contracts.
- **Review focus:** Key roles, service eligibility and the terms of each product.
- **Status evidence / qualification:** Custody services and borrowing products should be evaluated separately.
- **Project/resource:** [Unchained](https://www.unchained.com/)
- **Source 1:** [Primary source](https://unchained.com/) — primary; reviewed 2026-09-25.

## Discontinued, deprecated and changed projects

<a id="botanix"></a>
### Botanix

**Type:** network · **Networks:** Bitcoin, Botanix · **Status:** `discontinued` · **Reviewed:** 2026-09-25

Historical Bitcoin EVM ecosystem associated with the Spiderchain design.

- **Bitcoin mechanism:** Federated/sidechain execution and Bitcoin bridge arrangements.
- **Review focus:** Shutdown information and any remaining asset-recovery routes.
- **Status evidence / qualification:** Official site announces shutdown on July 1, 2026. Retained for historical context, not new deposits.
- **Project/resource:** [Botanix](https://botanixlabs.com/)
- **Source 1:** [Primary source](https://botanixlabs.com/) — primary; reviewed 2026-09-25.

<a id="pstake"></a>
### pSTAKE

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `deprecated` · **Reviewed:** 2026-09-25

Former Bitcoin/liquid-staking project whose current site presents a research collective.

- **Bitcoin mechanism:** Historical staking products with separate deprecation flows.
- **Review focus:** Legacy withdrawal instructions and product-specific closure status.
- **Status evidence / qualification:** Staking links now point to deprecation.pstake.finance; site focuses on Web3/AI research.
- **Project/resource:** [pSTAKE](https://www.pstake.finance/)
- **Source 1:** [Primary source](https://www.pstake.finance/) — primary; reviewed 2026-09-25.

<a id="tropykus"></a>
### Tropykus

**Type:** application · **Networks:** Rootstock · **Status:** `discontinued` · **Reviewed:** 2026-09-25

Historical Rootstock lending application.

- **Bitcoin mechanism:** Rootstock smart-contract lending pools.
- **Review focus:** Remaining contract interactions and recovery instructions.
- **Status evidence / qualification:** Official site says interface closed July 27 and support ended August 31, 2026; contracts may remain accessible.
- **Project/resource:** [Tropykus](https://tropykus.com/)
- **Source 1:** [Primary source](https://tropykus.com/) — primary; reviewed 2026-09-25.

<a id="yala"></a>
### Yala

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Status:** `changed` · **Reviewed:** 2026-09-25

Previously included in BTCfi stablecoin maps; current site presents prediction-market intelligence.

- **Bitcoin mechanism:** Legacy BTCfi products require separate redemption and backing review.
- **Review focus:** Legacy redemption availability, obligations and updated product scope.
- **Status evidence / qualification:** Homepage now describes an AI fair-value agent and retains a Redeem link; current YU minting was not established.
- **Project/resource:** [Yala](https://www.yala.org/)
- **Source 1:** [Primary source](https://www.yala.org/) — primary; reviewed 2026-09-25.
