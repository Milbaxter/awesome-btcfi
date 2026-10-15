# Detailed BTCFi directory

Snapshot: **2026-10-15**. [Method and status definitions](methodology.md) · [Awesome list](../README.md)

Descriptions summarize publisher documentation. Review focuses are editorial questions, not completed security assessments. Network tags describe relevance, not a certified list of live deployments.

## Bitcoin contracts and asset protocols

<a id="alkanes"></a>
### Alkanes

**Type:** protocol · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `code-only` · **Lifecycle:** `unverified`

WASM-based metaprotocol supporting programmable assets and DeFi logic.

- **Bitcoin mechanism:** Bitcoin witness data interpreted by a metaprotocol runtime and indexer.
- **Review focus:** Runtime correctness, indexer agreement and upgrade rules.
- **Evidence and availability qualification:** Contract execution is not Bitcoin Core executing a general-purpose VM.
- **Project/resource:** [Alkanes](https://github.com/kungfuflex/alkanes-rs)
- **Source 1:** [Primary source](https://github.com/kungfuflex/alkanes-rs) — primary; reviewed 2026-09-25.

<a id="ark"></a>
### Ark

**Type:** protocol · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Shared-UTXO payment design with virtual UTXOs and a coordinating server.

- **Bitcoin mechanism:** Prearranged Bitcoin transaction trees and off-chain transfers.
- **Review focus:** Server availability, refresh deadlines, transfer assumptions and unilateral exit costs.
- **Evidence and availability qualification:** Implementations differ; see Arkade and Second.
- **Project/resource:** [Ark](https://ark-protocol.org/)
- **Source 1:** [Primary source](https://ark-protocol.org/) — primary; reviewed 2026-09-25.

<a id="bitvm"></a>
### BitVM

**Type:** research · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `research`

Off-chain computation with Bitcoin-enforced dispute mechanisms, used in bridge and rollup designs.

- **Bitcoin mechanism:** Fraud-proof constructions using existing Bitcoin scripting capabilities.
- **Review focus:** Version-specific challengers, setup, liquidity and dispute assumptions.
- **Evidence and availability qualification:** BitVM is a construction family; its existence does not prove a particular bridge is deployed or safe.
- **Project/resource:** [BitVM](https://bitvm.org/)
- **Source 1:** [Primary source](https://bitvm.org/) — primary; reviewed 2026-09-25.

<a id="brc-20"></a>
### BRC-20

**Type:** standard · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Inscription-based token experiment with off-chain balance interpretation.

- **Bitcoin mechanism:** Deploy, mint and transfer inscriptions interpreted by indexers.
- **Review focus:** Indexer agreement, evolving protocol rules and token liquidity.
- **Evidence and availability qualification:** Original specification is historical; it points to Layer 1 Foundation for evolving documentation.
- **Project/resource:** [BRC-20](https://domo-2.gitbook.io/brc-20-experiment)
- **Source 1:** [Primary source](https://domo-2.gitbook.io/brc-20-experiment) — primary; reviewed 2026-09-25.

<a id="discreet-log-contracts-dlcs"></a>
### Discreet Log Contracts (DLCs)

**Type:** standard · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Oracle-attested Bitcoin contracts for contingent payments, derivatives and collateral arrangements.

- **Bitcoin mechanism:** Bitcoin transactions with outcomes selected using oracle signatures.
- **Review focus:** Oracle accuracy and availability, contract construction and refund paths.
- **Evidence and availability qualification:** A contract family, not a single lending platform.
- **Project/resource:** [Discreet Log Contracts (DLCs)](https://dlc.wiki/)
- **Source 1:** [Primary source](https://dlc.wiki/) — primary; reviewed 2026-09-25.
- **Source 2:** [DLC specifications](https://github.com/discreetlogcontracts/dlcspecs) — primary; reviewed 2026-09-25.

<a id="lightning-network"></a>
### Lightning Network

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Payment channels that route BTC off-chain and can settle to Bitcoin.

- **Bitcoin mechanism:** Bitcoin channel transactions and timelocked settlement.
- **Review focus:** Channel backups, online monitoring, liquidity and on-chain exit fees.
- **Evidence and availability qualification:** Protocol overview reviewed; individual wallet custody varies.
- **Project/resource:** [Lightning Network](https://lightning.network/)
- **Source 1:** [Primary source](https://lightning.network/) — primary; reviewed 2026-09-25.

<a id="op-net"></a>
### OP_NET

**Type:** protocol · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Smart-contract execution system that embeds contract data in Bitcoin transactions.

- **Bitcoin mechanism:** Additional execution and verification rules applied to Bitcoin witness data.
- **Review focus:** Execution consensus, indexing, contract security and network-specific deployment stage.
- **Evidence and availability qualification:** Documentation reviewed; this entry does not certify mainnet deployment or inherit marketing security claims.
- **Project/resource:** [OP_NET](https://docs.opnet.org/)
- **Source 1:** [Primary source](https://docs.opnet.org/getting-started/introduction-to-op-net/bitcoin-smart-contracts-explained) — primary; reviewed 2026-09-25.

<a id="ordinals"></a>
### Ordinals

**Type:** standard · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Satoshi indexing and inscriptions underlying collectible markets and collateral use cases.

- **Bitcoin mechanism:** Bitcoin transactions interpreted by ordinal-aware software.
- **Review focus:** Indexer conventions, UTXO handling, fees and collectible liquidity.
- **Evidence and availability qualification:** Adjacent infrastructure, not an intrinsic BTC yield mechanism.
- **Project/resource:** [Ordinals](https://docs.ordinals.com/)
- **Source 1:** [Primary source](https://docs.ordinals.com/) — primary; reviewed 2026-09-25.

<a id="rgb"></a>
### RGB

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Client-validated contracts and asset issuance anchored to Bitcoin outputs.

- **Bitcoin mechanism:** Off-chain contract state and proofs associated with Bitcoin ownership.
- **Review focus:** Proof backups, wallet interoperability and issuer terms.
- **Evidence and availability qualification:** Issued assets are distinct from native BTC.
- **Project/resource:** [RGB](https://rgb.tech/)
- **Source 1:** [Primary source](https://rgb.tech/) — primary; reviewed 2026-09-25.

<a id="rgb-plus-plus"></a>
### RGB++

**Type:** protocol · **Networks:** Bitcoin, Nervos CKB · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Asset protocol connecting Bitcoin UTXOs and CKB cells through isomorphic bindings.

- **Bitcoin mechanism:** Asset ownership bindings across Bitcoin and CKB.
- **Review focus:** CKB dependencies and the separate custody model of any BTC wrapper.
- **Evidence and availability qualification:** Distinct from RGB; token movement does not by itself make native BTC bridge-free.
- **Project/resource:** [RGB++](https://github.com/utxostack/rgbpp-sdk)
- **Source 1:** [Primary source](https://talk.nervos.org/t/rgb-protocol-light-paper-translation/7790) — primary; reviewed 2026-09-25.

<a id="runes"></a>
### Runes

**Type:** standard · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Fungible-token metaprotocol with balances assigned to Bitcoin outputs.

- **Bitcoin mechanism:** Runestones encoded in Bitcoin transactions.
- **Review focus:** Indexer correctness, token economics, market liquidity and fee costs.
- **Evidence and availability qualification:** Rune tokens are separate assets, not bitcoin.
- **Project/resource:** [Runes](https://docs.ordinals.com/runes.html)
- **Source 1:** [Primary source](https://docs.ordinals.com/runes.html) — primary; reviewed 2026-09-25.

<a id="taproot-assets"></a>
### Taproot Assets

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Asset issuance and transfers using Taproot, including Lightning-based transfers.

- **Bitcoin mechanism:** Bitcoin commitments, client-side asset proofs and Lightning channels.
- **Review focus:** Issuer backing, proof availability, wallet compatibility and channel liquidity.
- **Evidence and availability qualification:** An issuance protocol; a dollar token adds its own issuer risk.
- **Project/resource:** [Taproot Assets](https://docs.lightning.engineering/the-lightning-network/taproot-assets)
- **Source 1:** [Primary source](https://docs.lightning.engineering/the-lightning-network/taproot-assets) — primary; reviewed 2026-09-25.

## Execution networks and Bitcoin layers

<a id="alpen"></a>
### Alpen

**Type:** network · **Networks:** Bitcoin, Alpen · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `testnet`

EVM-compatible validity-rollup project for programmable Bitcoin applications.

- **Bitcoin mechanism:** Validity proofs with Bitcoin consensus and data availability in the documented design.
- **Review focus:** Testnet limitations, bridge construction and eventual mainnet controls.
- **Evidence and availability qualification:** Docs explicitly describe a work-in-progress rollup on Bitcoin signet; mainnet is a future release.
- **Project/resource:** [Alpen](https://www.alpen.org/)
- **Source 1:** [Primary source](https://docs.alpen.org/) — primary; reviewed 2026-09-25.

<a id="arch-network"></a>
### Arch Network

**Type:** network · **Networks:** Bitcoin, Arch · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Financial application infrastructure designed around native Bitcoin settlement.

- **Bitcoin mechanism:** External execution and signing infrastructure connected to Bitcoin transactions.
- **Review focus:** Validator or signer control, settlement guarantees and the current application design.
- **Evidence and availability qualification:** Native settlement language does not eliminate the need to review the execution and signing layer.
- **Project/resource:** [Arch Network](https://www.arch.network/)
- **Source 1:** [Primary source](https://www.arch.network/) — primary; reviewed 2026-09-25.

<a id="b2-network"></a>
### B2 Network

**Type:** network · **Networks:** Bitcoin, B2 · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin extension ecosystem with rollup infrastructure, bridges and application products.

- **Bitcoin mechanism:** B2 Hub, execution network and separate asset bridges.
- **Review focus:** Bridge control, data availability, proof verification and current product scope.
- **Evidence and availability qualification:** Official product navigation includes B2 Hub, Rollup and BTC Bridge.
- **Project/resource:** [B2 Network](https://www.bsquared.network/)
- **Source 1:** [Primary source](https://www.bsquared.network/) — primary; reviewed 2026-09-25.

<a id="bitcoinos"></a>
### BitcoinOS

**Type:** infrastructure · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

BitSNARK and Grail-related infrastructure for Bitcoin proofs, bridges and interoperable applications.

- **Bitcoin mechanism:** Proof and bridge constructions intended to connect external computation to Bitcoin.
- **Review focus:** Implementation maturity, custody, proof challenge assumptions and each integration's deployment.
- **Evidence and availability qualification:** Infrastructure claims reviewed; no blanket mainnet or trustlessness assertion.
- **Project/resource:** [BitcoinOS](https://www.bitcoinos.build/)
- **Source 1:** [Primary source](https://www.bitcoinos.build/) — primary; reviewed 2026-09-25.

<a id="bitlayer"></a>
### Bitlayer

**Type:** network · **Networks:** Bitcoin, Bitlayer · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin execution ecosystem associated with BitVM infrastructure and the YBTC product family.

- **Bitcoin mechanism:** Separate execution and product-specific Bitcoin bridge arrangements.
- **Review focus:** Current deployment versus whitepaper design, custody and withdrawal conditions.
- **Evidence and availability qualification:** Homepage now emphasizes YBTC; distinguish the network from individual products.
- **Project/resource:** [Bitlayer](https://www.bitlayer.org/)
- **Source 1:** [Primary source](https://static.bitlayer.org/Bitlayer-Technical-Whitepaper.pdf) — primary; reviewed 2026-09-25.
- **Source 2:** [Current Bitlayer products](https://www.bitlayer.org/) — primary; reviewed 2026-09-25.

<a id="bob"></a>
### BOB

**Type:** network · **Networks:** Bitcoin, Ethereum, BOB · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Hybrid-chain ecosystem with Bitcoin intents, DeFi access and Bitcoin vault development.

- **Bitcoin mechanism:** EVM execution plus route-dependent bridging, intents and BitVM-related infrastructure.
- **Review focus:** Current chain stage, privileged roles and the exact bridge or vault used.
- **Evidence and availability qualification:** Docs describe several products; do not assign one security model to all of them. BOB says wBTC.OFT holders must manually migrate to bridged wBTC before its LayerZero endpoint closes on Oct 31, 2026.
- **Project/resource:** [BOB](https://docs.gobob.xyz/)
- **Source 1:** [Primary source](https://docs.gobob.xyz/) — primary; reviewed 2026-09-25.
- **Source 2:** [wBTC.OFT migration notice (2026-09-29)](https://www.gobob.xyz/en/blog/wbtc-migration) — primary; reviewed 2026-10-15.

<a id="citrea"></a>
### Citrea

**Type:** network · **Networks:** Bitcoin, Citrea · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Bitcoin rollup project with EVM applications and the Clementine cBTC bridge.

- **Bitcoin mechanism:** Validity proofs and a BitVM-based bridge architecture.
- **Review focus:** Bridge challengers and operators, exit liquidity, sequencer and upgrade controls.
- **Evidence and availability qualification:** Official homepage states that mainnet is live; no transaction testing performed.
- **Project/resource:** [Citrea](https://citrea.xyz/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.
- **Source 2:** [Citrea architecture and getting started](https://docs.citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="fractal-bitcoin"></a>
### Fractal Bitcoin

**Type:** network · **Networks:** Bitcoin, Fractal · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-code-based scaling ecosystem supporting asset protocols and applications.

- **Bitcoin mechanism:** Separate SHA256d network with its own asset and consensus arrangements.
- **Review focus:** Separate-chain security and the custody of any asset bridged from Bitcoin.
- **Evidence and availability qualification:** FB is not BTC; compatibility with Bitcoin software does not imply identical security.
- **Project/resource:** [Fractal Bitcoin](https://docs.fractalbitcoin.io/)
- **Source 1:** [Primary source](https://docs.fractalbitcoin.io/getting-started/introduction) — primary; reviewed 2026-09-25.

<a id="goat-network"></a>
### GOAT Network

**Type:** network · **Networks:** Bitcoin, GOAT · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-oriented execution ecosystem advertising BTC fee income and programmable applications.

- **Bitcoin mechanism:** Separate execution network, bridge and operator arrangements.
- **Review focus:** BTC entry and exit path, operators, upgrades and fees versus token incentives.
- **Evidence and availability qualification:** BTC-denominated fees and GOATED rewards are distinct reward sources. GOAT announced Stargate support ends Oct 23, 2026 and default LayerZero DVN/Executor service ends Oct 30; bridged USDC.e, USDT and WETH need exiting via Stargate before then.
- **Project/resource:** [GOAT Network](https://www.goat.network/)
- **Source 1:** [Primary source](https://www.goat.network/) — primary; reviewed 2026-09-25.
- **Source 2:** [Stargate sunset and LayerZero V2 migration (2026-10-02)](https://www.goat.network/news/stargate-sunset-and-layerzero-v2-dvn-executor-migration) — primary; reviewed 2026-10-15.

<a id="hemi"></a>
### Hemi

**Type:** network · **Networks:** Bitcoin, Ethereum, Hemi · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin and Ethereum ecosystem offering programmable BTC-related finance and institutional access.

- **Bitcoin mechanism:** Hemi execution with product-specific Bitcoin access and custody paths.
- **Review focus:** Settlement architecture, bridge or custody route and strategy dependencies.
- **Evidence and availability qualification:** HEMI token staking is not the same thing as staking BTC.
- **Project/resource:** [Hemi](https://hemi.xyz/)
- **Source 1:** [Primary source](https://hemi.xyz/) — primary; reviewed 2026-09-25.

<a id="liquid-network"></a>
### Liquid Network

**Type:** network · **Networks:** Bitcoin, Liquid · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Federated Bitcoin sidechain for confidential transfers, asset issuance and capital markets; LBTC peg-outs paused since a September 2026 exploit.

- **Bitcoin mechanism:** BTC is represented as L-BTC on a federation-operated sidechain.
- **Review focus:** Federation control, peg-out access and issuer risk for non-BTC assets.
- **Evidence and availability qualification:** A Sept 6, 2026 Elements rangeproof-cache bug let an attacker mint unbacked LBTC and peg out about 4,000 BTC; about 3,400 BTC was returned. The official site still says peg-outs remain paused (checked 2026-10-15). Sidechain settlement has additional trust assumptions beyond Bitcoin.
- **Project/resource:** [Liquid Network](https://www.liquid.net/)
- **Source 1:** [Primary source](https://www.liquid.net/) — primary; reviewed 2026-10-15.
- **Source 2:** [Blockstream Liquid security incident assessment (2026-09-23)](https://blog.blockstream.com/liquid-network-security-incident-assessment/) — primary; reviewed 2026-10-15.

<a id="merlin-chain"></a>
### Merlin Chain

**Type:** network · **Networks:** Bitcoin, Merlin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

EVM-compatible ecosystem supporting Bitcoin-linked assets and applications.

- **Bitcoin mechanism:** A separate network with bridged Bitcoin assets and proof infrastructure.
- **Review focus:** Bridge custody, oracle and data availability assumptions, upgrades and exits.
- **Evidence and availability qualification:** Rollup branding is not treated as proof of Bitcoin-enforced withdrawals.
- **Project/resource:** [Merlin Chain](https://merlinchain.io/)
- **Source 1:** [Primary source](https://merlinchain.io/) — primary; reviewed 2026-09-25.

<a id="rootstock"></a>
### Rootstock

**Type:** network · **Networks:** Bitcoin, Rootstock · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-oriented EVM sidechain hosting lending, stablecoins and trading.

- **Bitcoin mechanism:** RBTC peg and a separate smart-contract execution network.
- **Review focus:** Powpeg custody, bridge delays, network consensus and application contracts.
- **Evidence and availability qualification:** The official site identifies Rootstock as a Bitcoin sidechain.
- **Project/resource:** [Rootstock](https://rootstock.io/)
- **Source 1:** [Primary source](https://rootstock.io/) — primary; reviewed 2026-09-25.

<a id="stacks"></a>
### Stacks

**Type:** network · **Networks:** Bitcoin, Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Smart-contract network for Bitcoin applications, including lending and exchanges using sBTC.

- **Bitcoin mechanism:** Separate execution with Bitcoin anchoring and an sBTC signer-based peg.
- **Review focus:** Signer custody, execution rules, upgrades and withdrawal mechanics.
- **Evidence and availability qualification:** Treat Stacks execution and sBTC custody as separate review questions.
- **Project/resource:** [Stacks](https://www.stacks.co/)
- **Source 1:** [Primary source](https://www.stacks.co/sbtc) — primary; reviewed 2026-09-25.

## Bitcoin representations and bridges

<a id="btc-b"></a>
### BTC.b

**Type:** asset · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `changed`

Non-yield BTC representation operated by Lombard, originally launched by Ava Labs.

- **Bitcoin mechanism:** BTC backing with Lombard consortium and chain-specific transfer infrastructure.
- **Review focus:** Consortium custody, supported-chain changes and redemption paths.
- **Evidence and availability qualification:** Lombard docs report acquisition in October 2025; September 2026 chain support changes require separate review.
- **Project/resource:** [BTC.b](https://docs.lombard.finance/learn/products/assets)
- **Source 1:** [Primary source](https://docs.lombard.finance/learn/products/assets) — primary; reviewed 2026-09-25.
- **Source 2:** [September 2026 chain support and bridging](https://docs.lombard.finance/use/bridging) — primary; reviewed 2026-09-25.

<a id="btcb"></a>
### BTCB

**Type:** asset · **Networks:** Bitcoin, BNB Chain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Binance-issued Bitcoin representation used in the BNB Chain ecosystem.

- **Bitcoin mechanism:** Custodial BTC backing and destination-chain tokens.
- **Review focus:** Binance custody, reserve verification, redemption and smart-contract permissions.
- **Evidence and availability qualification:** BTCB is distinct from native BTC and from unrelated similarly named tokens.
- **Project/resource:** [BTCB](https://www.bnbchain.org/en/blog/empowering-btcfi-on-bnb-chain-the-role-of-btcb-in-building-trust)
- **Source 1:** [Primary source](https://www.bnbchain.org/en/blog/empowering-btcfi-on-bnb-chain-the-role-of-btcb-in-building-trust) — primary; reviewed 2026-09-25.

<a id="cbbtc"></a>
### cbBTC

**Type:** asset · **Networks:** Bitcoin, Ethereum, Base, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Coinbase-backed BTC representation for on-chain collateral and trading.

- **Bitcoin mechanism:** BTC held by Coinbase with tokens issued on supported networks.
- **Review focus:** Custody, issuer controls, redemption eligibility and chain-specific bridge design.
- **Evidence and availability qualification:** Issuer documentation describes wrapping and redemption for eligible Coinbase accounts. The separate governance assessment concerns a destination-chain integration, not issuer evidence.
- **Project/resource:** [cbBTC](https://www.coinbase.com/cbbtc)
- **Source 1:** [Coinbase wrapped assets and eligibility](https://help.coinbase.com/en/coinbase/trading-and-funding/sending-or-receiving-cryptocurrency/coinbase-wrapped-btc) — primary; reviewed 2026-09-25.
- **Source 2:** [Aave governance assessment of cbBTC on Monad](https://governance.aave.com/t/coinbase-wrapped-btc-cbbtc-on-aave-monad-assessments/25257) — secondary; reviewed 2026-09-25.

<a id="ckbtc"></a>
### ckBTC

**Type:** asset · **Networks:** Bitcoin, Internet Computer · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Chain-key BTC representation managed by Internet Computer canisters.

- **Bitcoin mechanism:** Threshold signatures, ICP subnets and minter/ledger canisters.
- **Review focus:** ICP consensus and governance, canister upgrades, transaction screening and redemption.
- **Evidence and availability qualification:** No traditional single custodian does not mean no additional trust assumptions.
- **Project/resource:** [ckBTC](https://dashboard.internetcomputer.org/bitcoin)
- **Source 1:** [Primary source](https://docs.internetcomputer.org/concepts/chain-fusion/bitcoin/) — primary; reviewed 2026-09-25.

<a id="clementine-and-cbtc"></a>
### Clementine and cBTC

**Type:** bridge · **Networks:** Bitcoin, Citrea · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Citrea's bridge and BTC representation for its application environment.

- **Bitcoin mechanism:** BitVM-based optimistic verification in the documented bridge design.
- **Review focus:** Operator and challenger requirements, withdrawal liquidity and dispute windows.
- **Evidence and availability qualification:** The whitepaper specifies an honest watchtower assumption within a permissioned set; implementation and deployed configuration require separate review. Citrea's Oct 2026 cBTC Earn Vault is a separate curated carry strategy (cBTC collateral, ctUSD borrowing on Morpho) that adds curator, stablecoin and incentive dependencies.
- **Project/resource:** [Clementine and cBTC](https://citrea.xyz/)
- **Source 1:** [Clementine whitepaper](https://citrea.xyz/clementine_whitepaper.pdf) — primary; reviewed 2026-09-25.
- **Source 2:** [cBTC Earn Vault announcement (2026-10-01)](https://www.blog.citrea.xyz/announcing-cbtc-earn-vault-first-trust-minimized-btc-vault/) — primary; reviewed 2026-10-15.

<a id="fbtc"></a>
### FBTC

**Type:** asset · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin representation connecting custodial BTC reserves to destination-chain tokens.

- **Bitcoin mechanism:** On-chain contracts combined with off-chain custody operations.
- **Review focus:** Custody policy, pausing, upgrades and safety-committee emergency powers.
- **Evidence and availability qualification:** Distinct from the FBTC ticker used by a Bitcoin ETF.
- **Project/resource:** [FBTC](https://fbtc.com/)
- **Source 1:** [Primary source](https://docs.fbtc.com/security/risk-management/custody) — primary; reviewed 2026-09-25.

<a id="fiamma"></a>
### Fiamma Bridge / fiaBTC

**Type:** bridge · **Networks:** Bitcoin, Ethereum, Aptos, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

BitVM-related Bitcoin bridge and fiaBTC representation.

- **Bitcoin mechanism:** Deposits use pre-signed transactions with a bridge committee; operators front BTC for redemption.
- **Review focus:** Owner powers, operator liveness, challenger assumptions and whether the audited version matches deployed contracts.
- **Evidence and availability qualification:** The dedicated status page advertises mainnet modules, while overview/testnet pages retain earlier phases. The linked audit covers a specified 2025 code version, not every current deployment.
- **Project/resource:** [Fiamma Bridge / fiaBTC](https://docs.fiammalabs.io/)
- **Source 1:** [Fiamma bridge status](https://docs.fiammalabs.io/our-product-suite/pragmatically-trustless-bitvm-bitcoin-bridge/bridge-test) — primary; reviewed 2026-09-25.
- **Source 2:** [Fiamma user security assumptions](https://docs.fiammalabs.io/our-product-suite/pragmatically-trustless-bitvm-bitcoin-bridge/security-analysis/users) — primary; reviewed 2026-09-25.
- **Source 3:** [OpenZeppelin audit: scope, findings and privileged roles](https://www.openzeppelin.com/news/fiamma-bridge-audit) — primary; reviewed 2026-09-25.

<a id="ibtc-network"></a>
### iBTC Network / DLC.link

**Type:** asset · **Networks:** Bitcoin, Ethereum, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin representation using merchant vaults and an attestor network.

- **Bitcoin mechanism:** Documented two-party vault arrangements combine merchant participation with an attestor signing network.
- **Review focus:** Merchant eligibility, attestor quorum, redemption rights and deployed-contract controls.
- **Evidence and availability qualification:** Current iBTC documentation and DLC-link code identify the product. Source availability does not establish current minting capacity, liquidity or successful redemption.
- **Project/resource:** [iBTC Network / DLC.link](https://docs.ibtc.network/ibtc-documentation)
- **Source 1:** [iBTC architecture overview](https://docs.ibtc.network/ibtc-documentation) — primary; reviewed 2026-09-25.
- **Source 2:** [DLC.link contracts identifying the iBTC token](https://github.com/DLC-link/dlc-solidity) — primary; reviewed 2026-09-25.

<a id="l-btc"></a>
### L-BTC

**Type:** asset · **Networks:** Bitcoin, Liquid · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Liquid's Bitcoin-pegged settlement asset; peg-outs to BTC paused since a September 2026 exploit.

- **Bitcoin mechanism:** BTC locked under the Liquid federation's peg arrangements.
- **Review focus:** Federation behavior, peg-out access and network liveness.
- **Evidence and availability qualification:** Holding L-BTC is not identical to holding a Bitcoin L1 UTXO. After the Sept 2026 incident roughly 600 BTC of the drained reserve was reported unreturned; check current backing and peg-out status before relying on redemption.
- **Project/resource:** [L-BTC](https://www.liquid.net/)
- **Source 1:** [Primary source](https://www.liquid.net/) — primary; reviewed 2026-10-15.
- **Source 2:** [Blockstream Liquid security incident assessment (2026-09-23)](https://blog.blockstream.com/liquid-network-security-incident-assessment/) — primary; reviewed 2026-10-15.

<a id="sbtc"></a>
### sBTC

**Type:** asset · **Networks:** Bitcoin, Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

BTC-backed asset used by applications on Stacks.

- **Bitcoin mechanism:** Bitcoin deposits controlled through the sBTC signer system.
- **Review focus:** Signer threshold, withdrawals, upgrades and application-level risk.
- **Evidence and availability qualification:** Distinct from Synthetix's historical sBTC ticker.
- **Project/resource:** [sBTC](https://www.stacks.co/sbtc)
- **Source 1:** [Primary source](https://www.stacks.co/sbtc) — primary; reviewed 2026-09-25.

<a id="strkbtc"></a>
### strkBTC

**Type:** asset · **Networks:** Bitcoin, Starknet · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin representation on Starknet with optional shielded balances and staking integrations.

- **Bitcoin mechanism:** Bitcoin bridging plus Starknet token and privacy infrastructure.
- **Review focus:** Bridge backing, shielding controls, recovery and staking dependencies.
- **Evidence and availability qualification:** Privacy features do not remove the bridge's custody assumptions.
- **Project/resource:** [strkBTC](https://www.starknet.io/blog/strkbtc-user-guide/)
- **Source 1:** [Primary source](https://www.starknet.io/blog/strkbtc-user-guide/) — primary; reviewed 2026-09-25.

<a id="tbtc"></a>
### tBTC

**Type:** asset · **Networks:** Bitcoin, Ethereum, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Threshold Network's Bitcoin bridge asset for DeFi.

- **Bitcoin mechanism:** Threshold-signing custody rather than a single traditional custodian.
- **Review focus:** Signer thresholds, bridge governance, redemption and destination-chain contracts.
- **Evidence and availability qualification:** Review the current tBTC version, not assumptions from the earlier v1 system.
- **Project/resource:** [tBTC](https://www.threshold.network/)
- **Source 1:** [Primary source](https://docs.threshold.network/tbtc-v2) — primary; reviewed 2026-09-25.

<a id="wbtc"></a>
### WBTC

**Type:** asset · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Custodially backed Bitcoin representation used across DeFi markets.

- **Bitcoin mechanism:** BTC reserves, authorized merchants and token contracts on destination chains.
- **Review focus:** Custodian arrangements, mint and redemption access, freeze controls and additional bridge layers.
- **Evidence and availability qualification:** A BTC wrapper, not a yield product by itself. BOB reports that BitGo is moving WBTC cross-chain transfers from LayerZero OFT to Chainlink CCIP, which affects bridged WBTC contract identity per chain.
- **Project/resource:** [WBTC](https://www.wbtc.network/)
- **Source 1:** [Primary source](https://www.wbtc.network/) — primary; reviewed 2026-09-25.
- **Source 2:** [BOB wBTC.OFT migration notice (2026-09-29)](https://www.gobob.xyz/en/blog/wbtc-migration) — secondary; reviewed 2026-10-15.

## Staking and shared security

<a id="babylon-bitcoin-staking"></a>
### Babylon Bitcoin Staking

**Type:** protocol · **Networks:** Bitcoin, Babylon · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin collateral used to provide security to external proof-of-stake systems.

- **Bitcoin mechanism:** Bitcoin staking scripts and finality-provider delegation.
- **Review focus:** Slashing conditions, unbonding time, covenant rules and reward denomination.
- **Evidence and availability qualification:** This does not change Bitcoin consensus from proof of work to proof of stake.
- **Project/resource:** [Babylon Bitcoin Staking](https://babylonlabs.io/)
- **Source 1:** [Primary source](https://babylonlabs.io/institutional-staking) — primary; reviewed 2026-09-25.

<a id="core"></a>
### Core

**Type:** network · **Networks:** Bitcoin, Core · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

EVM network with BTC timelock-based delegation and CORE rewards.

- **Bitcoin mechanism:** Bitcoin CLTV timelocks help elect Core validators.
- **Review focus:** Lock duration, validator performance, CORE exposure and separate risks when using Core DeFi.
- **Evidence and availability qualification:** Official description distinguishes BTC timelocking from bridging; dual staking also requires CORE.
- **Project/resource:** [Core](https://coredao.org/)
- **Source 1:** [Primary source](https://coredao.org/) — primary; reviewed 2026-09-25.

<a id="endur"></a>
### Endur

**Type:** protocol · **Networks:** Starknet · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Liquid staking infrastructure for BTC representations and STRK on Starknet.

- **Bitcoin mechanism:** Receipt tokens backed by product-specific staking positions.
- **Review focus:** Underlying wrapper, staking contracts, token exchange rate and redemption.
- **Evidence and availability qualification:** Official site states Starknet mainnet availability; BTC and STRK products are distinct.
- **Project/resource:** [Endur](https://www.endur.fi/)
- **Source 1:** [Primary source](https://www.endur.fi/) — primary; reviewed 2026-09-25.

<a id="pell-network"></a>
### Pell Network

**Type:** protocol · **Networks:** Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Restaking platform using BTC representations and liquid staking derivatives for shared security.

- **Bitcoin mechanism:** Restaked collateral securing decentralized validated services.
- **Review focus:** Underlying wrapper custody, operators, service-specific slashing and reward tokens.
- **Evidence and availability qualification:** Terms depend on the particular asset and service selected.
- **Project/resource:** [Pell Network](https://pell.network/)
- **Source 1:** [Primary source](https://docs.pell.network/) — primary; reviewed 2026-09-25.

<a id="pumpbtc"></a>
### PumpBTC

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `code-only` · **Lifecycle:** `unverified`

Liquid Bitcoin staking contracts minting pumpBTC from supported BTC representations.

- **Bitcoin mechanism:** Operator-mediated conversion and Babylon staking in the published contract description.
- **Review focus:** Operator custody, wrapper backing, upgrade roles and unstaking terms.
- **Evidence and availability qualification:** Code reviewed; current user-facing service availability was not established.
- **Project/resource:** [PumpBTC](https://github.com/pumpbtc/pumpbtc-contract)
- **Source 1:** [Primary source](https://github.com/pumpbtc/pumpbtc-contract) — primary; reviewed 2026-09-25.

<a id="satlayer"></a>
### SatLayer

**Type:** protocol · **Networks:** Babylon, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Shared-security contracts on Babylon for Bitcoin Validated Services.

- **Bitcoin mechanism:** Wrapped BTC or BTC liquid staking tokens allocated to service security.
- **Review focus:** Underlying assets, operators, contracts and whether a given vault enables slashing.
- **Evidence and availability qualification:** Do not assume every displayed vault has the same slashing configuration.
- **Project/resource:** [SatLayer](https://docs.satlayer.xyz/)
- **Source 1:** [Primary source](https://docs.satlayer.xyz/) — primary; reviewed 2026-09-25.

<a id="stacking-dao"></a>
### Stacking DAO

**Type:** protocol · **Networks:** Stacks, Bitcoin · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Liquid staking products for BTC and STX, including stBTC, stSTX and stSTXbtc.

- **Bitcoin mechanism:** Stacks staking mechanisms and liquid receipt tokens.
- **Review focus:** Asset identity, signer or contract dependencies, redemption and yield source.
- **Evidence and availability qualification:** Current homepage offers BTC/sBTC deposits into stBTC; older STX-only descriptions are incomplete. Stacks says StackingDAO holds most of Bitcoin Staking Bond 2 capacity, issuing stBTC over sBTC; rewards come from PoX miner BTC with Endowment-set bootstrap targets, not a guaranteed rate.
- **Project/resource:** [Stacking DAO](https://www.stackingdao.com/)
- **Source 1:** [Primary source](https://www.stackingdao.com/) — primary; reviewed 2026-09-25.
- **Source 2:** [Stacks Bitcoin Staking Bond 2 (2026-10-05)](https://www.stacks.co/blog/bitcoin-staking-bond-2-liquid-staking) — primary; reviewed 2026-10-15.

<a id="starknet-bitcoin-staking"></a>
### Starknet Bitcoin staking

**Type:** protocol · **Networks:** Starknet · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Staking supported tokenized BTC on Starknet to receive STRK rewards.

- **Bitcoin mechanism:** BTC wrapper tokens locked in Starknet staking contracts.
- **Review focus:** Wrapper and bridge security, validator rules, unbonding and STRK price exposure.
- **Evidence and availability qualification:** Starknet is an Ethereum L2; this is not staking an unwrapped Bitcoin L1 UTXO.
- **Project/resource:** [Starknet Bitcoin staking](https://www.starknet.io/staking/)
- **Source 1:** [Primary source](https://www.starknet.io/staking/) — primary; reviewed 2026-09-25.

## Lending and Bitcoin collateral

<a id="aave"></a>
### Aave

**Type:** application · **Networks:** Ethereum, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Money markets supporting Bitcoin representations as collateral or supplied assets in selected markets.

- **Bitcoin mechanism:** Destination-chain contracts using tokens such as WBTC and cbBTC.
- **Review focus:** Market-specific collateral factors, oracles, liquidations and wrapper custody.
- **Evidence and availability qualification:** BTC exposure on Aave generally adds wrapper and chain dependencies; separate native-collateral pilots need separate review.
- **Project/resource:** [Aave](https://aave.com/)
- **Source 1:** [Primary source](https://aave.com/) — primary; reviewed 2026-09-25.

<a id="avalon-labs"></a>
### Avalon Labs

**Type:** application · **Networks:** Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-focused on-chain money markets, USDa borrowing and separate institutional credit products.

- **Bitcoin mechanism:** Product-specific smart contracts and, for CeDeFi loans, custodial collateral.
- **Review focus:** Identify on-chain versus institutional terms, custody, rates and liquidation controls.
- **Evidence and availability qualification:** The site's On-Chain and CeDeFi products are separate trust models.
- **Project/resource:** [Avalon Labs](https://www.avalonfinance.xyz/)
- **Source 1:** [Primary source](https://www.avalonfinance.xyz/) — primary; reviewed 2026-09-25.

<a id="babylon-trustless-bitcoin-vaults"></a>
### Babylon Trustless Bitcoin Vaults

**Type:** infrastructure · **Networks:** Bitcoin, Ethereum · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `testnet`

Native BTC collateral infrastructure targeting applications such as external-chain borrowing.

- **Bitcoin mechanism:** BTCVault construction with external recognition of Bitcoin collateral.
- **Review focus:** Actual testnet/mainnet stage, liquidation path, proof system and recovery conditions.
- **Evidence and availability qualification:** An Oct 7, 2026 post still describes TBV-backed borrowing as live on Aave v4 testnet; the access link points to a testnet app. No mainnet lending market is verified here.
- **Project/resource:** [Babylon Trustless Bitcoin Vaults](https://babylonlabs.io/)
- **Source 1:** [Primary source](https://babylonlabs.io/) — primary; reviewed 2026-09-25.
- **Source 2:** [HashKey Cloud TBV integration (2026-10-07)](https://babylonlabs.io/blog/hashkey-cloud-to-integrate-babylon-trustless-bitcoin-vaults) — primary; reviewed 2026-10-15.

<a id="debifi"></a>
### Debifi

**Type:** application · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Connects Bitcoin borrowers with institutional lenders for fiat and stablecoin loans.

- **Bitcoin mechanism:** Dedicated 3-of-4 Bitcoin multisignature collateral escrow.
- **Review focus:** Key-holder roles, lender terms, identity checks and liquidation processes.
- **Evidence and availability qualification:** Institutional lending marketplace; not an autonomous Bitcoin L1 money market.
- **Project/resource:** [Debifi](https://debifi.com/)
- **Source 1:** [Primary source](https://debifi.com/) — primary; reviewed 2026-09-25.

<a id="firefish"></a>
### Firefish

**Type:** application · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Marketplace for fiat or stablecoin loans secured by Bitcoin.

- **Bitcoin mechanism:** On-chain multisignature escrow with off-chain loan settlement.
- **Review focus:** Escrow roles, default procedures, liquidation execution and legal counterparties.
- **Evidence and availability qualification:** Combines Bitcoin collateral infrastructure with contractual lending relationships.
- **Project/resource:** [Firefish](https://firefish.io/)
- **Source 1:** [Primary source](https://docs.firefish.io/) — primary; reviewed 2026-09-25.

<a id="fluid"></a>
### Fluid

**Type:** application · **Networks:** Ethereum, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Liquidity and lending infrastructure with WBTC-related markets.

- **Bitcoin mechanism:** Smart-contract vaults and a shared liquidity architecture.
- **Review focus:** Liquidations, oracle behavior, contract architecture and BTC wrapper custody.
- **Evidence and availability qualification:** The cited proposal establishes WBTC market design; current live market parameters need app verification.
- **Project/resource:** [Fluid](https://fluid.io/)
- **Source 1:** [Primary source](https://gov.fluid.io/t/launch-wbtc-markets-on-fluid/787) — primary; reviewed 2026-09-25.

<a id="granite"></a>
### Granite

**Type:** application · **Networks:** Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-backed borrowing with isolated collateral and partial liquidations.

- **Bitcoin mechanism:** sBTC collateral in Stacks smart contracts.
- **Review focus:** sBTC peg, price oracles, liquidation execution and contract controls.
- **Evidence and availability qualification:** The protocol says posted collateral is not re-lent; that does not remove liquidation risk.
- **Project/resource:** [Granite](https://www.granite.world/)
- **Source 1:** [Primary source](https://www.granite.world/) — primary; reviewed 2026-09-25.

<a id="lava"></a>
### Lava

**Type:** application · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-collateralized dollar borrowing and related spending services.

- **Bitcoin mechanism:** BTC collateral arrangements linked to external loan and payment infrastructure.
- **Review focus:** Contract and key control, liquidation, funding counterparties and card eligibility.
- **Evidence and availability qualification:** Self-custody marketing is not used here as an independent security certification.
- **Project/resource:** [Lava](https://www.lava.xyz/)
- **Source 1:** [Primary source](https://www.lava.xyz/) — primary; reviewed 2026-09-25.

<a id="lend-at-hodl-hodl"></a>
### Lend at Hodl Hodl

**Type:** application · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Marketplace for crypto loans secured by Bitcoin multisignature escrow.

- **Bitcoin mechanism:** BTC collateral in a multisig contract; loan currency moves separately.
- **Review focus:** Counterparty performance, dispute resolution, LTV thresholds and contract recovery.
- **Evidence and availability qualification:** Lenders need to inspect the loan currency; BTC collateral does not mean BTC-denominated lending.
- **Project/resource:** [Lend at Hodl Hodl](https://lend.hodlhodl.com/)
- **Source 1:** [Primary source](https://lend.hodlhodl.com/) — primary; reviewed 2026-09-25.

<a id="lendasat"></a>
### Lendasat

**Type:** application · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Peer-to-peer loans with Bitcoin collateral and fiat or stablecoin settlement.

- **Bitcoin mechanism:** 2-of-3 multisignature collateral with a dispute-resolution participant.
- **Review focus:** Counterparty repayment, dispute process, liquidation and recovery tools.
- **Evidence and availability qualification:** Shared control is different from unilateral self-custody.
- **Project/resource:** [Lendasat](https://lendasat.com/docs)
- **Source 1:** [Primary source](https://lendasat.com/docs/p2p-loans/faq) — primary; reviewed 2026-09-25.

<a id="liquidium"></a>
### Liquidium

**Type:** application · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

BTC loans secured by supported Ordinals or Runes, with lenders exposed to the collateral on default.

- **Bitcoin mechanism:** Bitcoin-native collateral contracts for the Bitcoin product.
- **Review focus:** Repayment deadlines, collectible valuation, collateral transfer and illiquidity.
- **Evidence and availability qualification:** The site also has another-chain product; this listing covers Bitcoin loans.
- **Project/resource:** [Liquidium](https://liquidium.wtf/)
- **Source 1:** [Primary source](https://liquidium.wtf/) — primary; reviewed 2026-09-25.

<a id="morpho"></a>
### Morpho

**Type:** application · **Networks:** Ethereum, Base, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Isolated lending markets and curated vaults, including cbBTC collateral markets.

- **Bitcoin mechanism:** Token collateral in market-specific smart contracts.
- **Review focus:** Oracle selection, liquidation parameters, wrapper custody and vault-curator allocation.
- **Evidence and availability qualification:** A market can exist permissionlessly without being endorsed by Morpho or this list.
- **Project/resource:** [Morpho](https://morpho.org/)
- **Source 1:** [Primary source](https://morpho.org/blog/cbbtc-lending-markets-deployed-on-morpho) — primary; reviewed 2026-09-25.

<a id="sovryn"></a>
### Sovryn

**Type:** application · **Networks:** Rootstock · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Rootstock lending, collateralized borrowing and trading suite.

- **Bitcoin mechanism:** RBTC and other supported assets in smart contracts.
- **Review focus:** Rootstock peg, contract governance, oracles and liquidation rules.
- **Evidence and availability qualification:** Includes several subprotocols with different economics.
- **Project/resource:** [Sovryn](https://sovryn.app/)
- **Source 1:** [Primary source](https://sovryn.app/) — primary; reviewed 2026-09-25.

<a id="venus"></a>
### Venus

**Type:** application · **Networks:** BNB Chain, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Money-market protocol with BTCB and other Bitcoin-related collateral markets.

- **Bitcoin mechanism:** Wrapped assets in destination-chain lending contracts.
- **Review focus:** Wrapper backing, oracle configuration, liquidations and governance.
- **Evidence and availability qualification:** Supported assets differ by pool and chain; check current limits and pause flags.
- **Project/resource:** [Venus](https://venus.io/)
- **Source 1:** [Primary source](https://docs-v4.venus.io/risk) — primary; reviewed 2026-09-25.

<a id="vesu"></a>
### Vesu

**Type:** application · **Networks:** Starknet · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Starknet lending pools and curated vault infrastructure within the Bitcoin staking ecosystem.

- **Bitcoin mechanism:** Pool-specific collateral contracts on Starknet.
- **Review focus:** Accepted BTC representation, oracle, liquidation and curator configuration.
- **Evidence and availability qualification:** Endur lists Vesu as an integration; no individual BTC market or rate is certified here.
- **Project/resource:** [Vesu](https://vesu.xyz/)
- **Source 1:** [Primary source](https://docs.vesu.xyz/) — primary; reviewed 2026-09-25.

<a id="zest-protocol"></a>
### Zest Protocol

**Type:** application · **Networks:** Stacks, Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Stacks lending markets and a separately described Bitcoin Collateral Vault initiative.

- **Bitcoin mechanism:** sBTC-based lending; proposed/native-vault paths have different mechanics.
- **Review focus:** Liquidations, price oracles, sBTC signers and the deployment stage of each vault product.
- **Evidence and availability qualification:** Existing Stacks markets must not be conflated with new vault architecture.
- **Project/resource:** [Zest Protocol](https://www.zestprotocol.com/)
- **Source 1:** [Primary source](https://www.zestprotocol.com/) — primary; reviewed 2026-09-25.

## Stablecoins and synthetic dollars

<a id="arkadiko"></a>
### Arkadiko

**Type:** application · **Networks:** Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Stablecoin and DeFi system whose USDA vaults are described as STX-collateralized.

- **Bitcoin mechanism:** Stacks collateral contracts and oracle-dependent debt positions.
- **Review focus:** STX volatility, collateral ratios, liquidations and contract controls.
- **Evidence and availability qualification:** Bitcoin-ecosystem inclusion does not mean USDA is directly backed by BTC.
- **Project/resource:** [Arkadiko](https://arkadiko.finance/)
- **Source 1:** [Primary source](https://arkadiko.finance/) — primary; reviewed 2026-09-25.

<a id="btcfi-bifrost"></a>
### BTCFi (Bifrost)

**Type:** application · **Networks:** Bitcoin, Bifrost, Base · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-collateralized borrowing service and related BtcUSD ecosystem.

- **Bitcoin mechanism:** Product-specific collateral arrangements supporting native BTC and BTC representations.
- **Review focus:** Collateral custody, supported routes, liquidation rules and stablecoin redemption.
- **Evidence and availability qualification:** A specific product brand, distinct from the general term BTCFi; the source lists BTC, WBTC, BTCB and cbBTC collateral.
- **Project/resource:** [BTCFi (Bifrost)](https://www.btcfi.one/)
- **Source 1:** [Primary source](https://ecosystem.btcfi.one/) — primary; reviewed 2026-09-25.

<a id="ctusd"></a>
### ctUSD

**Type:** asset · **Networks:** Citrea · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Dollar stablecoin within the Citrea ecosystem described as backed by cash and short-term Treasury bills.

- **Bitcoin mechanism:** External fiat reserves and tokens on Citrea.
- **Review focus:** Issuer, reserves, redemption eligibility and chain risk.
- **Evidence and availability qualification:** Not BTC-collateralized despite use in Bitcoin capital markets.
- **Project/resource:** [ctUSD](https://citrea.xyz/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="ducat-unit"></a>
### Ducat / UNIT

**Type:** protocol · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

BTC-backed stablecoin design using collateral vaults and MPC-coordinated rules.

- **Bitcoin mechanism:** Native BTC collateral plus external guardians, oracles and protocol nodes.
- **Review focus:** Guardian/signing assumptions, liquidation path, oracle integrity and deployment stage.
- **Evidence and availability qualification:** BTC-native branding is not a claim that Bitcoin alone enforces every stablecoin rule.
- **Project/resource:** [Ducat / UNIT](https://docs.ducatprotocol.com/)
- **Source 1:** [Primary source](https://docs.ducatprotocol.com/how-ducat-works/vaults) — primary; reviewed 2026-09-25.

<a id="hermetica"></a>
### Hermetica

**Type:** application · **Networks:** Stacks, Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

USDh synthetic dollar and its staked receipt sUSDh, using BTC exposure and derivatives hedging.

- **Bitcoin mechanism:** Custodied BTC is hedged with short perpetual futures; approved participants mint and redeem using USDC or USDT.
- **Review focus:** Hedging and custody arrangements, counterparties, liquidity and product-specific redemption.
- **Evidence and availability qualification:** Direct USDh documentation reviewed. Minting and redemption require eligibility checks and can be paused; this entry does not establish the status of other Hermetica products.
- **Project/resource:** [Hermetica](https://docs.hermetica.fi/usdh/overview)
- **Source 1:** [USDh minting, custody and redemption](https://docs.hermetica.fi/usdh/how-it-works/mint) — primary; reviewed 2026-09-25.
- **Source 2:** [sUSDh funding-rate yield](https://docs.hermetica.fi/usdh/how-it-works/yield) — primary; reviewed 2026-09-25.

<a id="mezo"></a>
### Mezo

**Type:** application · **Networks:** Bitcoin, Mezo · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin finance platform with BTC-backed MUSD borrowing and yield-vault access.

- **Bitcoin mechanism:** Bitcoin-linked collateral on Mezo and application-specific debt/vault contracts.
- **Review focus:** Collateral bridge, liquidation and redemption rules; vaults add curator risk.
- **Evidence and availability qualification:** MUSD's dollar target is distinct from holding BTC; Upshift-powered vaults are a separate product. An Oct 5, 2026 veBTC VotingEscrow meta-transaction flaw let an attacker take about 5.52 BTC from 37 positions; Mezo says it was fixed Oct 6 and affected users will be repaid in BTC.
- **Project/resource:** [Mezo](https://mezo.org/)
- **Source 1:** [Primary source](https://mezo.org/) — primary; reviewed 2026-09-25.
- **Source 2:** [veBTC incident report (2026-10-07)](https://mezo.org/blog/incident-report-october-5-2026/) — primary; reviewed 2026-10-15.

<a id="money-on-chain"></a>
### Money On Chain

**Type:** application · **Networks:** Rootstock · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

DOC dollar exposure and BPRO Bitcoin exposure within a shared collateral system.

- **Bitcoin mechanism:** Bitcoin-linked collateral on Rootstock with risk allocated between token classes.
- **Review focus:** RBTC peg, collateral model, oracles and BPRO exposure.
- **Evidence and availability qualification:** BPRO is a risk-bearing product, not a plain BTC deposit.
- **Project/resource:** [Money On Chain](https://moneyonchain.com/)
- **Source 1:** [Primary source](https://moneyonchain.com/) — primary; reviewed 2026-09-25.

<a id="sovryn-zero"></a>
### Sovryn Zero

**Type:** application · **Networks:** Rootstock · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

BTC-backed stablecoin borrowing within the Sovryn ecosystem.

- **Bitcoin mechanism:** RBTC collateral, stablecoin debt and a liquidation stability pool.
- **Review focus:** Origination fees, redemptions, collateral ratio and liquidation.
- **Evidence and availability qualification:** The page includes DLLR and older ZUSD language; verify the current app and docs before interpreting terms.
- **Project/resource:** [Sovryn Zero](https://sovryn.com/zero)
- **Source 1:** [Primary source](https://sovryn.com/zero) — primary; reviewed 2026-09-25.

## Exchanges and trading

<a id="alex"></a>
### ALEX

**Type:** application · **Networks:** Stacks · **Reviewed:** 2026-09-25

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

Stacks DeFi suite with liquidity and exchange functionality.

- **Bitcoin mechanism:** Stacks contracts and associated ecosystem assets.
- **Review focus:** Incident history, paused functions, contract versions and current recovery information.
- **Evidence and availability qualification:** Ecosystem listing establishes identity, not present operational health.
- **Project/resource:** [ALEX](https://alexlab.co/)
- **Source 1:** [Primary source](https://www.stacks.co/explore/ecosystem) — primary; reviewed 2026-09-25.

<a id="bitflow"></a>
### Bitflow

**Type:** application · **Networks:** Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Exchange and liquidity infrastructure for Stacks assets including sBTC pairs.

- **Bitcoin mechanism:** Stacks smart-contract liquidity pools.
- **Review focus:** sBTC backing, pool design, price ranges, impermanent loss and contract risk.
- **Evidence and availability qualification:** Direct aggregator documentation describes routing across Stacks DEXs; this is not a verification of every pool or current quote.
- **Project/resource:** [Bitflow](https://www.bitflow.finance/)
- **Source 1:** [Primary source](https://www.stacks.co/blog/stacks-90-day-defi-incentive-program-announced-with-zest-and-bitflow) — primary; reviewed 2026-09-25.
- **Source 2:** [Bitflow DEX aggregator mechanics](https://docs.bitflow.finance/Bitflow-documentation/learn/what-is-the-dex-aggregator) — primary; reviewed 2026-09-25.

<a id="curve"></a>
### Curve

**Type:** application · **Networks:** Ethereum, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

Liquidity pools and related DeFi infrastructure used with tokenized Bitcoin.

- **Bitcoin mechanism:** Automated market makers on destination chains.
- **Review focus:** Pool composition, wrapper depegs, liquidity, impermanent loss and contracts.
- **Evidence and availability qualification:** WBTC's official site lists Curve among supported trading venues; verify the particular pool.
- **Project/resource:** [Curve](https://curve.finance/)
- **Source 1:** [Primary source](https://www.wbtc.network/) — primary; reviewed 2026-09-25.

<a id="flashnet"></a>
### Flashnet

**Type:** infrastructure · **Networks:** Bitcoin, Spark, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin trading and payment orchestration infrastructure with native-asset routing.

- **Bitcoin mechanism:** Route-dependent exchange, bridge and settlement integrations.
- **Review focus:** Route composition, provider trust, underlying payment layer and settlement recovery.
- **Evidence and availability qualification:** Spark identifies Flashnet as an ecosystem integration; route guarantees should be checked individually.
- **Project/resource:** [Flashnet](https://www.flashnet.xyz/)
- **Source 1:** [Primary source](https://www.flashnet.xyz/) — primary; reviewed 2026-09-25.

<a id="juiceswap"></a>
### JuiceSwap

**Type:** application · **Networks:** Citrea · **Reviewed:** 2026-09-25

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

Exchange listed among Citrea's Bitcoin applications.

- **Bitcoin mechanism:** Citrea application contracts and assets.
- **Review focus:** Pool deployment, liquidity, contract review and bridge dependencies.
- **Evidence and availability qualification:** Listed from the network's official directory; no execution testing performed.
- **Project/resource:** [JuiceSwap](https://bapp.juiceswap.com/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.

<a id="ln-markets"></a>
### LN Markets

**Type:** application · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin derivatives interface using Lightning and external exchange liquidity.

- **Bitcoin mechanism:** Lightning funding combined with platform-managed trading infrastructure.
- **Review focus:** Margin liquidation, platform custody, execution and exchange counterparties.
- **Evidence and availability qualification:** Lightning deposits do not turn a derivatives venue into a self-custodial protocol.
- **Project/resource:** [LN Markets](https://lnmarkets.com/)
- **Source 1:** [Primary source](https://lnmarkets.com/) — primary; reviewed 2026-09-25.

<a id="rujira"></a>
### Rujira

**Type:** application · **Networks:** Bitcoin, THORChain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

THORChain application suite covering trading, lending and collateralized borrowing.

- **Bitcoin mechanism:** BTC enters THORChain vault custody and is represented by secured-asset accounting for application use.
- **Review focus:** THORChain vault/signing assumptions, application contracts, liquidation rules and available withdrawal liquidity.
- **Evidence and availability qualification:** Product docs describe lending vaults and loans as live; no transaction was executed. Native BTC entry and exit do not mean BTC stays under the user's sole key control.
- **Project/resource:** [Rujira](https://rujira.network/)
- **Source 1:** [Rujira secured assets and custody path](https://rujira.network/secured-assets) — primary; reviewed 2026-09-25.
- **Source 2:** [RUJI money market mechanics and stated availability](https://docs.rujira.network/core-products/ruji-money-market) — primary; reviewed 2026-09-25.

<a id="satsuma"></a>
### Satsuma

**Type:** application · **Networks:** Citrea · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Citrea exchange with swaps, liquidity pools and token voting incentives.

- **Bitcoin mechanism:** Citrea application contracts and assets.
- **Review focus:** Pool deployment, liquidity, contract review and cBTC bridge dependencies.
- **Evidence and availability qualification:** The publisher interface describes cBTC swaps and liquidity/voting products. Source was readable through the web index; wallet operations and displayed metrics were not verified.
- **Project/resource:** [Satsuma](https://www.satsuma.exchange/)
- **Source 1:** [Primary source](https://citrea.xyz/) — primary; reviewed 2026-09-25.
- **Source 2:** [Satsuma exchange and liquidity products](https://www.satsuma.exchange/) — primary; reviewed 2026-09-25.

<a id="sideswap"></a>
### SideSwap

**Type:** application · **Networks:** Liquid · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Peer-to-peer swaps and settlement tools for Liquid assets.

- **Bitcoin mechanism:** Liquid asset transactions and L-BTC peg access.
- **Review focus:** Liquid federation, individual asset issuers and market liquidity.
- **Evidence and availability qualification:** Non-custodial trading does not remove the underlying Liquid peg assumptions.
- **Project/resource:** [SideSwap](https://sideswap.io/)
- **Source 1:** [Primary source](https://sideswap.io/) — primary; reviewed 2026-09-25.

<a id="unisat"></a>
### UniSat

**Type:** application · **Networks:** Bitcoin, Fractal · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Wallet, marketplace and data tools for Bitcoin asset protocols.

- **Bitcoin mechanism:** Ordinal, BRC-20, Rune and Alkane-aware transaction and indexing systems.
- **Review focus:** Asset-indexer correctness, signing, UTXO selection and marketplace liquidity.
- **Evidence and availability qualification:** Features on Fractal use a different network from Bitcoin mainnet.
- **Project/resource:** [UniSat](https://unisat.io/)
- **Source 1:** [Primary source](https://unisat.io/) — primary; reviewed 2026-09-25.

<a id="uniswap"></a>
### Uniswap

**Type:** application · **Networks:** Ethereum, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

General-purpose exchange infrastructure with tokenized BTC markets.

- **Bitcoin mechanism:** Version-specific automated market makers and, in v4, optional hooks.
- **Review focus:** Token authenticity, LP price ranges, wrapper risk and any pool-specific hook.
- **Evidence and availability qualification:** BTC trading uses a representation such as WBTC, not native Bitcoin settlement.
- **Project/resource:** [Uniswap](https://uniswap.org/)
- **Source 1:** [Primary source](https://www.wbtc.network/) — primary; reviewed 2026-09-25.

## Yield markets and managed strategies

<a id="bedrock"></a>
### Bedrock

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `changed`

uniBTC and brBTC alongside a broader Bitcoin yield-vault product suite.

- **Bitcoin mechanism:** BTC representations routed into product-specific strategies.
- **Review focus:** Custody, token backing, contracts and off-chain strategy dependencies.
- **Evidence and availability qualification:** Current site describes Bedrock 2.0, including lending, derivatives and RWA strategies beyond staking.
- **Project/resource:** [Bedrock](https://www.bedrock.technology/)
- **Source 1:** [Primary source](https://www.bedrock.technology/) — primary; reviewed 2026-09-25.

<a id="lombard-lbtc"></a>
### Lombard LBTC

**Type:** asset · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `changed`

Yield-bearing BTC asset now tied to a Bitwise-managed covered-call strategy.

- **Bitcoin mechanism:** Custodied BTC backing and non-rebasing tokens with an exchange rate.
- **Review focus:** Options losses, counterparties, custody and redemption delays.
- **Evidence and availability qualification:** Docs say Babylon backing ended in August 2026 and the new strategy started August 17; do not describe today's LBTC as simply a Babylon LST.
- **Project/resource:** [Lombard LBTC](https://docs.lombard.finance/use/lbtc)
- **Source 1:** [Primary source](https://docs.lombard.finance/learn/products/assets) — primary; reviewed 2026-09-25.
- **Source 2:** [Current LBTC yield mechanics](https://docs.lombard.finance/use/lbtc) — primary; reviewed 2026-09-25.

<a id="lorenzo-protocol"></a>
### Lorenzo Protocol

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin liquidity and asset-management infrastructure, including stBTC-related designs.

- **Bitcoin mechanism:** Tokenized BTC principal or yield exposure and strategy-specific backing.
- **Review focus:** Current product scope, custody, receipt-token rights and redemption availability.
- **Evidence and availability qualification:** Public Bitcoin-liquidity documentation exists; current front-end availability is not certified.
- **Project/resource:** [Lorenzo Protocol](https://www.lorenzo-protocol.xyz/)
- **Source 1:** [Primary source](https://lorenzo-protocol.gitbook.io/docs/bitcoin-liquidity-layer) — primary; reviewed 2026-09-25.

<a id="pendle"></a>
### Pendle

**Type:** application · **Networks:** Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Yield tokenization and trading usable with supported Bitcoin yield assets.

- **Bitcoin mechanism:** Principal and yield claims on an underlying yield-bearing token.
- **Review focus:** Underlying protocol and wrapper risk, maturity, liquidity and yield-token decay.
- **Evidence and availability qualification:** BTC market availability changes; inspect the specific underlying asset and expiry.
- **Project/resource:** [Pendle](https://www.pendle.finance/)
- **Source 1:** [Primary source](https://www.pendle.finance/pendle) — primary; reviewed 2026-09-25.

<a id="solv-protocol"></a>
### Solv Protocol

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

SolvBTC representation, xSolvBTC yield exposure and managed BTC strategies.

- **Bitcoin mechanism:** Product-specific custody, reserve and strategy arrangements.
- **Review focus:** Backing composition, manager permissions, counterparties and redemption terms.
- **Evidence and availability qualification:** SolvBTC, xSolvBTC and BTC+ should not be treated as identical products.
- **Project/resource:** [Solv Protocol](https://solv.finance/)
- **Source 1:** [Primary source](https://solv.finance/) — primary; reviewed 2026-09-25.

<a id="spectra"></a>
### Spectra

**Type:** application · **Networks:** Multichain, Hemi · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Permissionless yield markets and vault infrastructure, including Bitcoin-related ecosystem use.

- **Bitcoin mechanism:** Separate principal/yield claims and interest-rate markets.
- **Review focus:** Underlying backing, maturity, curator choices and secondary-market liquidity.
- **Evidence and availability qualification:** Hemi is among the networks shown; each BTC market needs independent verification.
- **Project/resource:** [Spectra](https://www.spectra.finance/)
- **Source 1:** [Primary source](https://www.spectra.finance/) — primary; reviewed 2026-09-25.

<a id="yieldbasis"></a>
### YieldBasis

**Type:** protocol · **Networks:** Ethereum · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Liquidity strategy designed to offset impermanent loss for tokenized BTC and ETH.

- **Bitcoin mechanism:** Leveraged liquidity positions rather than Bitcoin consensus rewards.
- **Review focus:** Leverage, borrowing costs, rebalancing, wrapper backing and pool losses.
- **Evidence and availability qualification:** The design's leverage is economically material; claims of eliminating IL do not eliminate all losses.
- **Project/resource:** [YieldBasis](https://yieldbasis.com/)
- **Source 1:** [Primary source](https://docs.yieldbasis.com/pdf/mica-whitepaper.pdf) — primary; reviewed 2026-09-25.

## Cross-chain and atomic swaps

<a id="atomiq"></a>
### Atomiq

**Type:** protocol · **Networks:** Bitcoin, Lightning, Solana, Starknet · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Atomic swaps between Bitcoin and supported smart-contract chains.

- **Bitcoin mechanism:** Escrow contracts, Bitcoin light-client verification and refund paths.
- **Review focus:** Light-client implementation, swap expiry, smart contracts and counterparty liquidity.
- **Evidence and availability qualification:** The site documents both on-chain Bitcoin and Lightning routes.
- **Project/resource:** [Atomiq](https://www.atomiq.exchange/)
- **Source 1:** [Primary source](https://www.atomiq.exchange/) — primary; reviewed 2026-09-25.

<a id="boltz"></a>
### Boltz

**Type:** application · **Networks:** Bitcoin, Lightning, Liquid, Rootstock, Arkade · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Submarine and chain swaps across Bitcoin payment layers, with additional stablecoin routes.

- **Bitcoin mechanism:** Atomic-swap contracts and route-specific execution legs.
- **Review focus:** Refund backups, timeouts, fees and any extra DEX or bridge used by a route.
- **Evidence and availability qualification:** Stablecoin routes can compose additional components beyond a basic BTC-to-Lightning swap.
- **Project/resource:** [Boltz](https://boltz.exchange/)
- **Source 1:** [Primary source](https://api.docs.boltz.exchange/lifecycle.html) — primary; reviewed 2026-09-25.

<a id="chainflip"></a>
### Chainflip

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Native-asset cross-chain swaps with liquidity, Boost and lending products.

- **Bitcoin mechanism:** Validator MPC custody and cross-chain execution.
- **Review focus:** Validator security, custody, confirmation risk and product-specific lending terms.
- **Evidence and availability qualification:** Swap, Boost and lending exposures have different risk profiles.
- **Project/resource:** [Chainflip](https://chainflip.io/)
- **Source 1:** [Primary source](https://chainflip.io/) — primary; reviewed 2026-09-25.

<a id="garden"></a>
### Garden

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Atomic-swap infrastructure and APIs connecting Bitcoin with other networks.

- **Bitcoin mechanism:** Chain-specific swap contracts and liquidity providers.
- **Review focus:** Timeouts, refund implementation, provider liquidity and destination-chain contracts.
- **Evidence and availability qualification:** Swap contracts and supported chain routes are documented separately.
- **Project/resource:** [Garden](https://garden.finance/docs/)
- **Source 1:** [Primary source](https://docs.garden.finance/) — primary; reviewed 2026-09-25.

<a id="lendaswap"></a>
### LendaSwap

**Type:** application · **Networks:** Bitcoin, Lightning, Arkade, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin-to-stablecoin swaps associated with Lendasat.

- **Bitcoin mechanism:** Route-specific swaps using Bitcoin payment layers.
- **Review focus:** Exact route, timeout/recovery behavior and stablecoin issuer.
- **Evidence and availability qualification:** Product directory describes Lightning and Arkade integration; distinct from Lendasat loans.
- **Project/resource:** [LendaSwap](https://lendasat.com/docs)
- **Source 1:** [Primary source](https://lendasat.com/docs) — primary; reviewed 2026-09-25.

<a id="thorchain"></a>
### THORChain

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Cross-chain exchange and liquidity infrastructure for native assets including BTC.

- **Bitcoin mechanism:** Threshold-controlled network vaults and pool-based exchange.
- **Review focus:** Validator economics, vault custody, pool exposure and network halts.
- **Evidence and availability qualification:** Native-asset swaps still have network custody assumptions; distinguish swap pools from historical lending products.
- **Project/resource:** [THORChain](https://thorchain.org/)
- **Source 1:** [Primary source](https://thorchain.org/) — primary; reviewed 2026-09-25.

## Payments, Lightning liquidity and ecash

<a id="amboss"></a>
### Amboss

**Type:** infrastructure · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin payment infrastructure and integration tooling.

- **Bitcoin mechanism:** Lightning-connected payment routes and receiving-wallet integrations.
- **Review focus:** Wallet custody choice, route support and service availability.
- **Evidence and availability qualification:** Current homepage emphasizes payment APIs; legacy product names need separate verification.
- **Project/resource:** [Amboss](https://amboss.tech/)
- **Source 1:** [Primary source](https://amboss.tech/) — primary; reviewed 2026-09-25.

<a id="arkade"></a>
### Arkade

**Type:** infrastructure · **Networks:** Bitcoin, Ark · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Ark-based toolkit for payments, programmable transaction flows and asset exchange.

- **Bitcoin mechanism:** Bitcoin transaction structures coordinated through Arkade.
- **Review focus:** Operator availability, committed recovery paths and implementation-specific assumptions.
- **Evidence and availability qualification:** Homepage labels Intents as developer preview; do not treat every feature as production-ready.
- **Project/resource:** [Arkade](https://arkadeos.com/)
- **Source 1:** [Primary source](https://arkadeos.com/) — primary; reviewed 2026-09-25.

<a id="cashu"></a>
### Cashu

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Open Chaumian ecash protocol with Bitcoin-linked mints and wallets.

- **Bitcoin mechanism:** Bearer claims issued by mints, commonly funded over Lightning.
- **Review focus:** Mint solvency, issuer trust and token loss or double spending.
- **Evidence and availability qualification:** Each mint is its own trust relationship.
- **Project/resource:** [Cashu](https://cashu.space/)
- **Source 1:** [Primary source](https://cashu.space/) — primary; reviewed 2026-09-25.

<a id="fedimint"></a>
### Fedimint

**Type:** protocol · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Federated ecash for Bitcoin payments and community custody.

- **Bitcoin mechanism:** Federation custody backing private ecash notes.
- **Review focus:** Guardian collusion, solvency, federation availability and exit liquidity.
- **Evidence and availability qualification:** Privacy and distributed custody do not make ecash self-custodial BTC.
- **Project/resource:** [Fedimint](https://fedimint.org/)
- **Source 1:** [Primary source](https://fedimint.org/) — primary; reviewed 2026-09-25.

<a id="lightning-loop"></a>
### Lightning Loop

**Type:** application · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Submarine swaps for moving value between Lightning and on-chain Bitcoin.

- **Bitcoin mechanism:** HTLC-based swaps and refund conditions.
- **Review focus:** Fees, timeout handling, liquidity and transaction monitoring.
- **Evidence and availability qualification:** Channel management service; not a passive yield product.
- **Project/resource:** [Lightning Loop](https://docs.lightning.engineering/lightning-network-tools/loop)
- **Source 1:** [Primary source](https://docs.lightning.engineering/lightning-network-tools/loop) — primary; reviewed 2026-09-25.

<a id="lightning-pool"></a>
### Lightning Pool

**Type:** application · **Networks:** Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Marketplace for leasing Lightning channel liquidity.

- **Bitcoin mechanism:** Bitcoin allocated to payment-channel capacity.
- **Review focus:** Channel demand, node uptime, lease terms, fees and operational costs.
- **Evidence and availability qualification:** Liquidity fees are a different source of return from lending or staking.
- **Project/resource:** [Lightning Pool](https://docs.lightning.engineering/lightning-network-tools/pool)
- **Source 1:** [Primary source](https://docs.lightning.engineering/lightning-network-tools/pool) — primary; reviewed 2026-09-25.

<a id="mercury-layer"></a>
### Mercury Layer

**Type:** infrastructure · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Statechain implementation using blinded co-signing and key updates.

- **Bitcoin mechanism:** UTXO ownership transfers supported by a key-share service.
- **Review focus:** Server key deletion/update assumptions, backup transactions and exit timelocks.
- **Evidence and availability qualification:** Implementation documentation reviewed; current service availability not transaction-tested.
- **Project/resource:** [Mercury Layer](https://mercurylayer.com/)
- **Source 1:** [Primary source](https://mercurylayer.com/) — primary; reviewed 2026-09-25.

<a id="second"></a>
### Second

**Type:** infrastructure · **Networks:** Bitcoin, Ark, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Ark implementation and SDKs connecting Ark, Lightning and on-chain payments.

- **Bitcoin mechanism:** Ark virtual UTXOs and implementation-specific transfer/recovery paths.
- **Review focus:** Server availability, VTXO expiry, backups and exit fees.
- **Evidence and availability qualification:** Official homepage announces mainnet; no payment testing performed.
- **Project/resource:** [Second](https://second.tech/)
- **Source 1:** [Primary source](https://second.tech/) — primary; reviewed 2026-09-25.

<a id="spark"></a>
### Spark

**Type:** infrastructure · **Networks:** Bitcoin, Spark, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin and asset payment infrastructure with Lightning connectivity.

- **Bitcoin mechanism:** Statechain-style transfers and an operator-assisted Bitcoin ownership system.
- **Review focus:** Operator and key-share assumptions, unilateral exit details and issued-asset backing.
- **Evidence and availability qualification:** Distinct from the Spark DeFi lending/savings brand on Ethereum.
- **Project/resource:** [Spark](https://www.spark.money/)
- **Source 1:** [Primary source](https://www.spark.money/) — primary; reviewed 2026-09-25.

## Wallets and access

<a id="bitlight-wallet"></a>
### Bitlight Wallet

**Type:** wallet · **Networks:** Bitcoin, RGB, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Wallet for Bitcoin and RGB assets, with asset issuance tooling.

- **Bitcoin mechanism:** Client-side RGB state and Bitcoin wallet functionality.
- **Review focus:** Asset proofs, issuer authenticity, backups and version compatibility.
- **Evidence and availability qualification:** RGB assets require more than a BTC-only recovery assumption.
- **Project/resource:** [Bitlight Wallet](https://bitlightlabs.com/wallet)
- **Source 1:** [Primary source](https://bitlightlabs.com/wallet) — primary; reviewed 2026-09-25.

<a id="leather"></a>
### Leather

**Type:** wallet · **Networks:** Bitcoin, Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Wallet for Bitcoin, Stacks assets and ecosystem applications.

- **Bitcoin mechanism:** Bitcoin and Stacks transaction signing.
- **Review focus:** Backups, hardware-wallet compatibility and application approvals.
- **Evidence and availability qualification:** Access layer rather than an independent source of yield.
- **Project/resource:** [Leather](https://leather.io/)
- **Source 1:** [Primary source](https://leather.io/) — primary; reviewed 2026-09-25.

<a id="xverse"></a>
### Xverse

**Type:** wallet · **Networks:** Bitcoin, Stacks, Spark, Starknet · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Wallet and application gateway for Bitcoin assets and connected financial services.

- **Bitcoin mechanism:** User signing plus integrations with distinct Bitcoin-related networks.
- **Review focus:** Recovery, signing permissions and the trust model of each connected service.
- **Evidence and availability qualification:** Wallet self-custody does not guarantee self-custody after depositing into an application.
- **Project/resource:** [Xverse](https://www.xverse.app/)
- **Source 1:** [Primary source](https://www.xverse.app/) — primary; reviewed 2026-09-25.

## Developer tools and infrastructure

<a id="bitcoin-dev-kit"></a>
### Bitcoin Dev Kit

**Type:** developer-tool · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Libraries for Bitcoin wallet and transaction applications.

- **Bitcoin mechanism:** Bitcoin descriptors, transaction construction and chain access.
- **Review focus:** Key handling, dependency versions and application security.
- **Evidence and availability qualification:** Developer infrastructure, not a financial service.
- **Project/resource:** [Bitcoin Dev Kit](https://bitcoindevkit.org/)
- **Source 1:** [Primary source](https://bitcoindevkit.org/) — primary; reviewed 2026-09-25.

<a id="bitcoin-s"></a>
### Bitcoin-S

**Type:** developer-tool · **Networks:** Bitcoin, Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Scala libraries and tooling for Bitcoin transaction applications.

- **Bitcoin mechanism:** Bitcoin and Lightning data structures and transaction APIs.
- **Review focus:** Application design, signing and maintained library versions.
- **Evidence and availability qualification:** Useful building block for Bitcoin financial software.
- **Project/resource:** [Bitcoin-S](https://bitcoin-s.org/)
- **Source 1:** [Primary source](https://bitcoin-s.org/) — primary; reviewed 2026-09-25.

<a id="breez-sdk"></a>
### Breez SDK

**Type:** developer-tool · **Networks:** Bitcoin, Lightning, Spark, Liquid · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

SDKs for embedding Bitcoin payments into applications.

- **Bitcoin mechanism:** Implementation-dependent Bitcoin payment-layer integrations.
- **Review focus:** Which SDK implementation is used, recovery, providers and payment liquidity.
- **Evidence and availability qualification:** Different SDK backends have different trust and availability properties.
- **Project/resource:** [Breez SDK](https://breez.technology/)
- **Source 1:** [Primary source](https://breez.technology/) — primary; reviewed 2026-09-25.

<a id="elements"></a>
### Elements

**Type:** developer-tool · **Networks:** Liquid, Sidechains · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Sidechain-capable software with confidential transactions and asset issuance.

- **Bitcoin mechanism:** Independent or pegged chains with configurable consensus.
- **Review focus:** Operator model, peg construction and issued-asset obligations.
- **Evidence and availability qualification:** Software capability does not certify any chain built from it. The rangeproof-cache flaw behind the Sept 2026 Liquid incident was fixed in Elements v23.3.4.
- **Project/resource:** [Elements](https://elementsproject.org/)
- **Source 1:** [Primary source](https://elementsproject.org/) — primary; reviewed 2026-09-25.
- **Source 2:** [Blockstream Liquid security incident assessment (2026-09-23)](https://blog.blockstream.com/liquid-network-security-incident-assessment/) — primary; reviewed 2026-10-15.

<a id="layeredge"></a>
### LayerEdge

**Type:** infrastructure · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Proof aggregation and anchoring infrastructure for external applications.

- **Bitcoin mechanism:** Aggregated proofs anchored to underlying networks.
- **Review focus:** Anchoring versus actual enforcement, verifier design and deployment stage.
- **Evidence and availability qualification:** Do not equate publishing a proof commitment with inheriting all Bitcoin security properties.
- **Project/resource:** [LayerEdge](https://www.layeredge.io/)
- **Source 1:** [Primary source](https://www.layeredge.io/) — primary; reviewed 2026-09-25.

<a id="lightning-dev-kit"></a>
### Lightning Dev Kit

**Type:** developer-tool · **Networks:** Lightning · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Modular Lightning implementation and SDK for applications.

- **Bitcoin mechanism:** Payment-channel logic integrated into the host application.
- **Review focus:** Persistence, channel monitoring and integration correctness.
- **Evidence and availability qualification:** Developers choose their own operational architecture.
- **Project/resource:** [Lightning Dev Kit](https://lightningdevkit.org/)
- **Source 1:** [Primary source](https://lightningdevkit.org/) — primary; reviewed 2026-09-25.

<a id="metashrew"></a>
### Metashrew

**Type:** developer-tool · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

WASM-powered indexing framework for Bitcoin metaprotocols.

- **Bitcoin mechanism:** Block processing and application-defined indexer logic.
- **Review focus:** Indexer implementation, reorg handling and state agreement.
- **Evidence and availability qualification:** Indexing a contract is different from Bitcoin consensus enforcing its full semantics.
- **Project/resource:** [Metashrew](https://github.com/kungfuflex/metashrew)
- **Source 1:** [Primary source](https://github.com/kungfuflex/metashrew) — primary; reviewed 2026-09-25.

<a id="nubit-bitcoin-thunderbolt"></a>
### Nubit / Bitcoin Thunderbolt

**Type:** infrastructure · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin transfer and programmability project now described around Thunderbolt.

- **Bitcoin mechanism:** Off-chain UTXO ownership changes with threshold-signing committees.
- **Review focus:** Committee assumptions, implementation maturity and enforceable exits.
- **Evidence and availability qualification:** Older descriptions focused only on data availability are incomplete.
- **Project/resource:** [Nubit / Bitcoin Thunderbolt](https://docs.nubit.org/overview)
- **Source 1:** [Primary source](https://docs.nubit.org/bitcoin-thunderbolt/the-blueprint-for-bitcoins-next-era/how-it-works) — primary; reviewed 2026-09-25.

<a id="rebar-labs"></a>
### Rebar Labs

**Type:** infrastructure · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin APIs, metaprotocol data and transaction-submission tools with MEV-focused features.

- **Bitcoin mechanism:** Bitcoin indexing and transaction-flow infrastructure.
- **Review focus:** Data accuracy, transaction visibility and service dependence.
- **Evidence and availability qualification:** Earn, Shield and data products need separate evaluation; no yield claim is inferred from API access.
- **Project/resource:** [Rebar Labs](https://rebarlabs.io/)
- **Source 1:** [Primary source](https://rebarlabs.io/) — primary; reviewed 2026-09-25.

## Research, analytics and ecosystem maps

<a id="babylon-ecosystem"></a>
### Babylon ecosystem

**Type:** ecosystem-directory · **Networks:** Bitcoin, Babylon · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Official discovery map for staking providers and connected infrastructure.

- **Bitcoin mechanism:** Ecosystem self-reporting.
- **Review focus:** Distinguish direct staking, liquid wrappers and infrastructure providers.
- **Evidence and availability qualification:** Partner inclusion is not an audit or endorsement by this list.
- **Project/resource:** [Babylon ecosystem](https://babylonlabs.io/ecosystem)
- **Source 1:** [Primary source](https://babylonlabs.io/ecosystem?aecfdcd8_page=3) — primary; reviewed 2026-09-25.

<a id="bitcoin-layers"></a>
### Bitcoin Layers

**Type:** research-resource · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Independent directory analyzing Bitcoin layers, BTC representations and trust assumptions.

- **Bitcoin mechanism:** Research rather than custody or execution infrastructure.
- **Review focus:** Methodology, assessment date and scope of each project review.
- **Evidence and availability qualification:** A useful counterweight to project marketing; classifications can evolve.
- **Project/resource:** [Bitcoin Layers](https://www.bitcoinlayers.org/)
- **Source 1:** [Primary source](https://www.bitcoinlayers.org/) — primary; reviewed 2026-09-25.

<a id="bitcoin-layers-methodology"></a>
### Bitcoin Layers methodology

**Type:** research-resource · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Framework covering data availability, operators, settlement and bridge custody.

- **Bitcoin mechanism:** Structured risk analysis.
- **Review focus:** Apply dimensions separately; avoid turning a label into a universal safety score.
- **Evidence and availability qualification:** Used as a research lens, not reproduced as a rating system.
- **Project/resource:** [Bitcoin Layers methodology](https://bitcoin-layers.gitbook.io/bitcoin-layers/approach-to-analyzing-risk)
- **Source 1:** [Primary source](https://bitcoin-layers.gitbook.io/bitcoin-layers/approach-to-analyzing-risk) — primary; reviewed 2026-09-25.

<a id="defillama-bitcoin-dashboard"></a>
### DefiLlama Bitcoin dashboard

**Type:** analytics · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Protocol discovery and metrics for projects classified under Bitcoin.

- **Bitcoin mechanism:** Aggregator adapters and category definitions.
- **Review focus:** Double counting, classifications, adapter coverage and TVL versus deposited BTC.
- **Evidence and availability qualification:** Bitcoin-linked assets on other chains require additional dashboards; no static TVL ranking is copied here.
- **Project/resource:** [DefiLlama Bitcoin dashboard](https://defillama.com/chain/bitcoin)
- **Source 1:** [Primary source](https://defillama.com/chain/bitcoin?currency=USD) — primary; reviewed 2026-09-25.

<a id="sok-bitcoin-layer-two"></a>
### SoK: Bitcoin Layer Two

**Type:** research-paper · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Research paper surveying Bitcoin layer-two constructions and tradeoffs.

- **Bitcoin mechanism:** Academic systematization.
- **Review focus:** Paper version and gap between design and deployed implementation.
- **Evidence and availability qualification:** Complements current project documentation; not a live product directory.
- **Project/resource:** [SoK: Bitcoin Layer Two](https://arxiv.org/abs/2409.02650)
- **Source 1:** [Primary source](https://arxiv.org/abs/2409.02650) — primary; reviewed 2026-09-25.

<a id="stacks-ecosystem"></a>
### Stacks ecosystem

**Type:** ecosystem-directory · **Networks:** Stacks · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Official application, wallet and developer-tool discovery map.

- **Bitcoin mechanism:** Ecosystem self-reporting.
- **Review focus:** A listing is not a security review or current service guarantee.
- **Evidence and availability qualification:** Used for discovery and cross-checking relevance.
- **Project/resource:** [Stacks ecosystem](https://www.stacks.co/explore/ecosystem)
- **Source 1:** [Primary source](https://www.stacks.co/explore/ecosystem) — primary; reviewed 2026-09-25.

## Centralized and institutional finance

<a id="bima"></a>
### Bima

**Type:** platform · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `changed`

Structured financing against digital assets with an agreed upside-sharing component.

- **Bitcoin mechanism:** Accountable vault infrastructure and FalconX-held collateral in the documented arrangement.
- **Review focus:** Counterparty and derivative terms, downside exposure and foregone upside.
- **Evidence and availability qualification:** Current docs describe institutional structured financing; do not assume the older stablecoin framing still applies.
- **Project/resource:** [Bima](https://docs.bima.money/)
- **Source 1:** [Primary source](https://docs.bima.money/) — primary; reviewed 2026-09-25.

<a id="bouncebit"></a>
### BounceBit

**Type:** platform · **Networks:** Bitcoin, BounceBit, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

CeDeFi platform combining custodied assets, managed strategies and an EVM settlement chain.

- **Bitcoin mechanism:** BB-tokens backed through external custody and investment arrangements.
- **Review focus:** Custodian and exchange exposure, manager risk and withdrawal terms.
- **Evidence and availability qualification:** Listed as hybrid/centralized finance rather than Bitcoin-native non-custodial staking.
- **Project/resource:** [BounceBit](https://www.bouncebit.io/)
- **Source 1:** [Primary source](https://www.bouncebit.io/) — primary; reviewed 2026-09-25.

<a id="exsat"></a>
### exSat

**Type:** platform · **Networks:** Bitcoin, exSat · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `changed`

Digital-asset banking platform offering qualified-access custody, payments and strategy products.

- **Bitcoin mechanism:** Custody and managed strategies alongside Bitcoin-related infrastructure.
- **Review focus:** Eligibility, legal counterparties, strategy leverage and redemption windows.
- **Evidence and availability qualification:** Current homepage emphasizes digital banking rather than only a Bitcoin scaling layer.
- **Project/resource:** [exSat](https://exsat.network/)
- **Source 1:** [Primary source](https://exsat.network/) — primary; reviewed 2026-09-25.

<a id="ledn"></a>
### Ledn

**Type:** platform · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Centralized Bitcoin-backed loans and related credit products.

- **Bitcoin mechanism:** Contractual loans with collateral held through custody arrangements.
- **Review focus:** Custody, lender solvency, loan terms, liquidation and jurisdiction.
- **Evidence and availability qualification:** CeFi comparison entry; no claim that collateral is controlled solely by the borrower.
- **Project/resource:** [Ledn](https://www.ledn.io/)
- **Source 1:** [Primary source](https://ledn.io/) — primary; reviewed 2026-09-25.

<a id="unchained"></a>
### Unchained

**Type:** platform · **Networks:** Bitcoin · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Bitcoin financial services built around collaborative custody.

- **Bitcoin mechanism:** Multisignature arrangements and product-specific financial contracts.
- **Review focus:** Key roles, service eligibility and the terms of each product.
- **Evidence and availability qualification:** Custody services and borrowing products should be evaluated separately.
- **Project/resource:** [Unchained](https://www.unchained.com/)
- **Source 1:** [Primary source](https://unchained.com/) — primary; reviewed 2026-09-25.

## Discontinued, deprecated and changed projects

<a id="botanix"></a>
### Botanix

**Type:** network · **Networks:** Bitcoin, Botanix · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `discontinued`

Historical Bitcoin EVM ecosystem associated with the Spiderchain design.

- **Bitcoin mechanism:** Federated/sidechain execution and Bitcoin bridge arrangements.
- **Review focus:** Shutdown information and any remaining asset-recovery routes.
- **Evidence and availability qualification:** Official site announces shutdown on July 1, 2026. Retained for historical context, not new deposits.
- **Project/resource:** [Botanix](https://botanixlabs.com/)
- **Source 1:** [Primary source](https://botanixlabs.com/) — primary; reviewed 2026-09-25.

<a id="pstake"></a>
### pSTAKE

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `deprecated`

Former Bitcoin/liquid-staking project whose current site presents a research collective.

- **Bitcoin mechanism:** Historical staking products with separate deprecation flows.
- **Review focus:** Legacy withdrawal instructions and product-specific closure status.
- **Evidence and availability qualification:** Staking links now point to deprecation.pstake.finance; site focuses on Web3/AI research.
- **Project/resource:** [pSTAKE](https://www.pstake.finance/)
- **Source 1:** [Primary source](https://www.pstake.finance/) — primary; reviewed 2026-09-25.

<a id="tropykus"></a>
### Tropykus

**Type:** application · **Networks:** Rootstock · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `discontinued`

Historical Rootstock lending application.

- **Bitcoin mechanism:** Rootstock smart-contract lending pools.
- **Review focus:** Remaining contract interactions and recovery instructions.
- **Evidence and availability qualification:** Official site says interface closed July 27 and support ended August 31, 2026; contracts may remain accessible.
- **Project/resource:** [Tropykus](https://tropykus.com/)
- **Source 1:** [Primary source](https://tropykus.com/) — primary; reviewed 2026-09-25.

<a id="yala"></a>
### Yala

**Type:** protocol · **Networks:** Bitcoin, Multichain · **Reviewed:** 2026-09-25

**Evidence:** `direct-source` · **Lifecycle:** `changed`

Previously included in BTCFi stablecoin maps; current site presents prediction-market intelligence.

- **Bitcoin mechanism:** Legacy BTCFi products require separate redemption and backing review.
- **Review focus:** Legacy redemption availability, obligations and updated product scope.
- **Evidence and availability qualification:** Homepage now describes an AI fair-value agent and retains a Redeem link; current YU minting was not established.
- **Project/resource:** [Yala](https://www.yala.org/)
- **Source 1:** [Primary source](https://www.yala.org/) — primary; reviewed 2026-09-25.
