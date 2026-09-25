# Awesome BTCfi

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A researched awesome list of Bitcoin finance projects, protocols, tools and ways to use BTC.

Explore **Bitcoin-native contracts, payment layers, sidechains, BTC representations, staking, lending, stablecoins, trading and yield**, plus the infrastructure that makes them possible.

**Research snapshot: September 25, 2026.** This is a broad, curated directory, not an exhaustive census, ranking, audit or investment recommendation. “Awesome” names the list format; inclusion is not an endorsement. Open source refers to **this repository**; listed projects have their own licensing and custody models.

## Start here

- [Ways to use BTCfi](docs/ways-to-use-btcfi.md) — what each approach does, where returns come from, and what changes about your BTC.
- [Detailed directory](docs/directory.md) — mechanisms, review questions, status notes and dated sources for every entry.
- [Trust models and due diligence](docs/trust-models.md) — compare custody, exits, execution, collateral and reward sources.
- [Research method and scope](docs/methodology.md) — what was reviewed, what the labels mean, and the limits of this snapshot.
- [Material changes found](docs/research-notes.md) — shutdowns, migrations, changed products and terminology traps.
- [Machine-readable dataset](data/projects.json) — structured records for reuse.
- [HTTP link-check results](data/link-health.json) — reachability evidence, separate from project-status research.
- [Contribute an addition or correction](CONTRIBUTING.md).

**Read the labels:** `documented` means a relevant source was reviewed, **not** that deposits, withdrawals, solvency or audits were independently verified. `ecosystem-listed` is a lighter review based on an official ecosystem listing. `mainnet-announced` is the project's claim. `testnet`, `research`, `changed`, `status-unclear`, `deprecated` and `discontinued` keep uncertainty visible. See the [full definitions](docs/methodology.md#status-labels).

The [detailed directory](docs/directory.md) supplies a Bitcoin mechanism and review focus for each item. These short descriptions deliberately omit APY and TVL figures, which go stale and are frequently incomparable.

<!-- DIRECTORY:START -->

**128 entries · 15 categories · reviewed 2026-09-25**

## Contents

- [Bitcoin contracts and asset protocols](#bitcoin-primitives) (12)
- [Execution networks and Bitcoin layers](#networks) (14)
- [Bitcoin representations and bridges](#bitcoin-assets) (11)
- [Staking and shared security](#staking) (8)
- [Lending and Bitcoin collateral](#lending) (16)
- [Stablecoins and synthetic dollars](#stablecoins) (8)
- [Exchanges and trading](#trading) (10)
- [Yield markets and managed strategies](#yield) (7)
- [Cross-chain and atomic swaps](#swaps) (6)
- [Payments, Lightning liquidity and ecash](#payments) (9)
- [Wallets and access](#wallets) (3)
- [Developer tools and infrastructure](#builders) (9)
- [Research, analytics and ecosystem maps](#research) (6)
- [Centralized and institutional finance](#centralized) (5)
- [Discontinued, deprecated and changed projects](#historical) (4)

<a id="bitcoin-primitives"></a>
## Bitcoin contracts and asset protocols

- [Alkanes](https://github.com/kungfuflex/alkanes-rs) — WASM-based metaprotocol supporting programmable assets and DeFi logic. `documented` · [Details & sources](docs/directory.md#alkanes).
- [Ark](https://ark-protocol.org/) — Shared-UTXO payment design with virtual UTXOs and a coordinating server. `documented` · [Details & sources](docs/directory.md#ark).
- [BitVM](https://bitvm.org/) — Off-chain computation with Bitcoin-enforced dispute mechanisms, used in bridge and rollup designs. `research` · [Details & sources](docs/directory.md#bitvm).
- [BRC-20](https://domo-2.gitbook.io/brc-20-experiment) — Inscription-based token experiment with off-chain balance interpretation. `documented` · [Details & sources](docs/directory.md#brc-20).
- [Discreet Log Contracts (DLCs)](https://dlc.wiki/) — Oracle-attested Bitcoin contracts for contingent payments, derivatives and collateral arrangements. `documented` · [Details & sources](docs/directory.md#discreet-log-contracts-dlcs).
- [Lightning Network](https://lightning.network/) — Payment channels that route BTC off-chain and can settle to Bitcoin. `documented` · [Details & sources](docs/directory.md#lightning-network).
- [OP_NET](https://docs.opnet.org/) — Smart-contract execution system that embeds contract data in Bitcoin transactions. `documented` · [Details & sources](docs/directory.md#op-net).
- [Ordinals](https://docs.ordinals.com/) — Satoshi indexing and inscriptions underlying collectible markets and collateral use cases. `documented` · [Details & sources](docs/directory.md#ordinals).
- [RGB](https://rgb.tech/) — Client-validated contracts and asset issuance anchored to Bitcoin outputs. `documented` · [Details & sources](docs/directory.md#rgb).
- [RGB++](https://github.com/utxostack/rgbpp-sdk) — Asset protocol connecting Bitcoin UTXOs and CKB cells through isomorphic bindings. `documented` · [Details & sources](docs/directory.md#rgb-plus-plus).
- [Runes](https://docs.ordinals.com/runes.html) — Fungible-token metaprotocol with balances assigned to Bitcoin outputs. `documented` · [Details & sources](docs/directory.md#runes).
- [Taproot Assets](https://docs.lightning.engineering/the-lightning-network/taproot-assets) — Asset issuance and transfers using Taproot, including Lightning-based transfers. `documented` · [Details & sources](docs/directory.md#taproot-assets).

<a id="networks"></a>
## Execution networks and Bitcoin layers

- [Alpen](https://www.alpen.org/) — EVM-compatible validity-rollup project for programmable Bitcoin applications. `testnet` · [Details & sources](docs/directory.md#alpen).
- [Arch Network](https://www.arch.network/) — Financial application infrastructure designed around native Bitcoin settlement. `documented` · [Details & sources](docs/directory.md#arch-network).
- [B2 Network](https://www.bsquared.network/) — Bitcoin extension ecosystem with rollup infrastructure, bridges and application products. `documented` · [Details & sources](docs/directory.md#b2-network).
- [BitcoinOS](https://www.bitcoinos.build/) — BitSNARK and Grail-related infrastructure for Bitcoin proofs, bridges and interoperable applications. `documented` · [Details & sources](docs/directory.md#bitcoinos).
- [Bitlayer](https://www.bitlayer.org/) — Bitcoin execution ecosystem associated with BitVM infrastructure and the YBTC product family. `documented` · [Details & sources](docs/directory.md#bitlayer).
- [BOB](https://docs.gobob.xyz/) — Hybrid-chain ecosystem with Bitcoin intents, DeFi access and Bitcoin vault development. `documented` · [Details & sources](docs/directory.md#bob).
- [Citrea](https://citrea.xyz/) — Bitcoin rollup project with EVM applications and the Clementine cBTC bridge. `mainnet-announced` · [Details & sources](docs/directory.md#citrea).
- [Fractal Bitcoin](https://docs.fractalbitcoin.io/) — Bitcoin-code-based scaling ecosystem supporting asset protocols and applications. `documented` · [Details & sources](docs/directory.md#fractal-bitcoin).
- [GOAT Network](https://www.goat.network/) — Bitcoin-oriented execution ecosystem advertising BTC fee income and programmable applications. `documented` · [Details & sources](docs/directory.md#goat-network).
- [Hemi](https://hemi.xyz/) — Bitcoin and Ethereum ecosystem offering programmable BTC-related finance and institutional access. `documented` · [Details & sources](docs/directory.md#hemi).
- [Liquid Network](https://www.liquid.net/) — Federated Bitcoin sidechain for confidential transfers, asset issuance and capital markets. `documented` · [Details & sources](docs/directory.md#liquid-network).
- [Merlin Chain](https://merlinchain.io/) — EVM-compatible ecosystem supporting Bitcoin-linked assets and applications. `documented` · [Details & sources](docs/directory.md#merlin-chain).
- [Rootstock](https://rootstock.io/) — Bitcoin-oriented EVM sidechain hosting lending, stablecoins and trading. `documented` · [Details & sources](docs/directory.md#rootstock).
- [Stacks](https://www.stacks.co/) — Smart-contract network for Bitcoin applications, including lending and exchanges using sBTC. `documented` · [Details & sources](docs/directory.md#stacks).

<a id="bitcoin-assets"></a>
## Bitcoin representations and bridges

- [BTC.b](https://docs.lombard.finance/learn/products/assets) — Non-yield BTC representation operated by Lombard, originally launched by Ava Labs. `changed` · [Details & sources](docs/directory.md#btc-b).
- [BTCB](https://www.bnbchain.org/en/blog/empowering-btcfi-on-bnb-chain-the-role-of-btcb-in-building-trust) — Binance-issued Bitcoin representation used in the BNB Chain ecosystem. `documented` · [Details & sources](docs/directory.md#btcb).
- [cbBTC](https://www.coinbase.com/cbbtc) — Coinbase-backed BTC representation for on-chain collateral and trading. `documented` · [Details & sources](docs/directory.md#cbbtc).
- [ckBTC](https://dashboard.internetcomputer.org/bitcoin) — Chain-key BTC representation managed by Internet Computer canisters. `documented` · [Details & sources](docs/directory.md#ckbtc).
- [Clementine and cBTC](https://citrea.xyz/) — Citrea's bridge and BTC representation for its application environment. `documented` · [Details & sources](docs/directory.md#clementine-and-cbtc).
- [FBTC](https://fbtc.com/) — Bitcoin representation connecting custodial BTC reserves to destination-chain tokens. `documented` · [Details & sources](docs/directory.md#fbtc).
- [L-BTC](https://www.liquid.net/) — Liquid's Bitcoin-pegged settlement asset. `documented` · [Details & sources](docs/directory.md#l-btc).
- [sBTC](https://www.stacks.co/sbtc) — BTC-backed asset used by applications on Stacks. `documented` · [Details & sources](docs/directory.md#sbtc).
- [strkBTC](https://www.starknet.io/blog/strkbtc-user-guide/) — Bitcoin representation on Starknet with optional shielded balances and staking integrations. `documented` · [Details & sources](docs/directory.md#strkbtc).
- [tBTC](https://www.threshold.network/) — Threshold Network's Bitcoin bridge asset for DeFi. `documented` · [Details & sources](docs/directory.md#tbtc).
- [WBTC](https://www.wbtc.network/) — Custodially backed Bitcoin representation used across DeFi markets. `documented` · [Details & sources](docs/directory.md#wbtc).

<a id="staking"></a>
## Staking and shared security

- [Babylon Bitcoin Staking](https://babylonlabs.io/) — Bitcoin collateral used to provide security to external proof-of-stake systems. `documented` · [Details & sources](docs/directory.md#babylon-bitcoin-staking).
- [Core](https://coredao.org/) — EVM network with BTC timelock-based delegation and CORE rewards. `documented` · [Details & sources](docs/directory.md#core).
- [Endur](https://www.endur.fi/) — Liquid staking infrastructure for BTC representations and STRK on Starknet. `mainnet-announced` · [Details & sources](docs/directory.md#endur).
- [Pell Network](https://pell.network/) — Restaking platform using BTC representations and liquid staking derivatives for shared security. `documented` · [Details & sources](docs/directory.md#pell-network).
- [PumpBTC](https://github.com/pumpbtc/pumpbtc-contract) — Liquid Bitcoin staking contracts minting pumpBTC from supported BTC representations. `status-unclear` · [Details & sources](docs/directory.md#pumpbtc).
- [SatLayer](https://docs.satlayer.xyz/) — Shared-security contracts on Babylon for Bitcoin Validated Services. `documented` · [Details & sources](docs/directory.md#satlayer).
- [Stacking DAO](https://www.stackingdao.com/) — Liquid staking products for BTC and STX, including stBTC, stSTX and stSTXbtc. `documented` · [Details & sources](docs/directory.md#stacking-dao).
- [Starknet Bitcoin staking](https://www.starknet.io/staking/) — Staking supported tokenized BTC on Starknet to receive STRK rewards. `documented` · [Details & sources](docs/directory.md#starknet-bitcoin-staking).

<a id="lending"></a>
## Lending and Bitcoin collateral

- [Aave](https://aave.com/) — Money markets supporting Bitcoin representations as collateral or supplied assets in selected markets. `documented` · [Details & sources](docs/directory.md#aave).
- [Avalon Labs](https://www.avalonfinance.xyz/) — Bitcoin-focused on-chain money markets, USDa borrowing and separate institutional credit products. `documented` · [Details & sources](docs/directory.md#avalon-labs).
- [Babylon Trustless Bitcoin Vaults](https://babylonlabs.io/) — Native BTC collateral infrastructure targeting applications such as external-chain borrowing. `testnet` · [Details & sources](docs/directory.md#babylon-trustless-bitcoin-vaults).
- [Debifi](https://debifi.com/) — Connects Bitcoin borrowers with institutional lenders for fiat and stablecoin loans. `documented` · [Details & sources](docs/directory.md#debifi).
- [Firefish](https://firefish.io/) — Marketplace for fiat or stablecoin loans secured by Bitcoin. `documented` · [Details & sources](docs/directory.md#firefish).
- [Fluid](https://fluid.io/) — Liquidity and lending infrastructure with WBTC-related markets. `documented` · [Details & sources](docs/directory.md#fluid).
- [Granite](https://www.granite.world/) — Bitcoin-backed borrowing with isolated collateral and partial liquidations. `documented` · [Details & sources](docs/directory.md#granite).
- [Lava](https://www.lava.xyz/) — Bitcoin-collateralized dollar borrowing and related spending services. `documented` · [Details & sources](docs/directory.md#lava).
- [Lend at Hodl Hodl](https://lend.hodlhodl.com/) — Marketplace for crypto loans secured by Bitcoin multisignature escrow. `documented` · [Details & sources](docs/directory.md#lend-at-hodl-hodl).
- [Lendasat](https://lendasat.com/docs) — Peer-to-peer loans with Bitcoin collateral and fiat or stablecoin settlement. `documented` · [Details & sources](docs/directory.md#lendasat).
- [Liquidium](https://liquidium.wtf/) — BTC loans secured by supported Ordinals or Runes, with lenders exposed to the collateral on default. `documented` · [Details & sources](docs/directory.md#liquidium).
- [Morpho](https://morpho.org/) — Isolated lending markets and curated vaults, including cbBTC collateral markets. `documented` · [Details & sources](docs/directory.md#morpho).
- [Sovryn](https://sovryn.app/) — Rootstock lending, collateralized borrowing and trading suite. `documented` · [Details & sources](docs/directory.md#sovryn).
- [Venus](https://venus.io/) — Money-market protocol with BTCB and other Bitcoin-related collateral markets. `documented` · [Details & sources](docs/directory.md#venus).
- [Vesu](https://vesu.xyz/) — Starknet lending pools and curated vault infrastructure within the Bitcoin staking ecosystem. `documented` · [Details & sources](docs/directory.md#vesu).
- [Zest Protocol](https://www.zestprotocol.com/) — Stacks lending markets and a separately described Bitcoin Collateral Vault initiative. `documented` · [Details & sources](docs/directory.md#zest-protocol).

<a id="stablecoins"></a>
## Stablecoins and synthetic dollars

- [Arkadiko](https://arkadiko.finance/) — Stablecoin and DeFi system whose USDA vaults are described as STX-collateralized. `documented` · [Details & sources](docs/directory.md#arkadiko).
- [BTCFi (Bifrost)](https://www.btcfi.one/) — Bitcoin-collateralized borrowing service and related BtcUSD ecosystem. `documented` · [Details & sources](docs/directory.md#btcfi-bifrost).
- [ctUSD](https://citrea.xyz/) — Dollar stablecoin within the Citrea ecosystem described as backed by cash and short-term Treasury bills. `documented` · [Details & sources](docs/directory.md#ctusd).
- [Ducat / UNIT](https://docs.ducatprotocol.com/) — BTC-backed stablecoin design using collateral vaults and MPC-coordinated rules. `documented` · [Details & sources](docs/directory.md#ducat-unit).
- [Hermetica](https://www.stacks.co/bitcoin-native-finance) — USDh synthetic-dollar product and hBTC Bitcoin yield strategies. `ecosystem-listed` · [Details & sources](docs/directory.md#hermetica).
- [Mezo](https://mezo.org/) — Bitcoin finance platform with BTC-backed MUSD borrowing and yield-vault access. `documented` · [Details & sources](docs/directory.md#mezo).
- [Money On Chain](https://moneyonchain.com/) — DOC dollar exposure and BPRO Bitcoin exposure within a shared collateral system. `documented` · [Details & sources](docs/directory.md#money-on-chain).
- [Sovryn Zero](https://sovryn.com/zero) — BTC-backed stablecoin borrowing within the Sovryn ecosystem. `documented` · [Details & sources](docs/directory.md#sovryn-zero).

<a id="trading"></a>
## Exchanges and trading

- [ALEX](https://alexlab.co/) — Stacks DeFi suite with liquidity and exchange functionality. `ecosystem-listed` · [Details & sources](docs/directory.md#alex).
- [Bitflow](https://www.bitflow.finance/) — Exchange and liquidity infrastructure for Stacks assets including sBTC pairs. `ecosystem-listed` · [Details & sources](docs/directory.md#bitflow).
- [Curve](https://curve.finance/) — Liquidity pools and related DeFi infrastructure used with tokenized Bitcoin. `ecosystem-listed` · [Details & sources](docs/directory.md#curve).
- [Flashnet](https://www.flashnet.xyz/) — Bitcoin trading and payment orchestration infrastructure with native-asset routing. `documented` · [Details & sources](docs/directory.md#flashnet).
- [JuiceSwap](https://bapp.juiceswap.com/) — Exchange listed among Citrea's Bitcoin applications. `ecosystem-listed` · [Details & sources](docs/directory.md#juiceswap).
- [LN Markets](https://lnmarkets.com/) — Bitcoin derivatives interface using Lightning and external exchange liquidity. `documented` · [Details & sources](docs/directory.md#ln-markets).
- [Satsuma](https://www.satsuma.exchange/) — Exchange listed in Citrea's application ecosystem. `ecosystem-listed` · [Details & sources](docs/directory.md#satsuma).
- [SideSwap](https://sideswap.io/) — Peer-to-peer swaps and settlement tools for Liquid assets. `documented` · [Details & sources](docs/directory.md#sideswap).
- [UniSat](https://unisat.io/) — Wallet, marketplace and data tools for Bitcoin asset protocols. `documented` · [Details & sources](docs/directory.md#unisat).
- [Uniswap](https://uniswap.org/) — General-purpose exchange infrastructure with tokenized BTC markets. `ecosystem-listed` · [Details & sources](docs/directory.md#uniswap).

<a id="yield"></a>
## Yield markets and managed strategies

- [Bedrock](https://www.bedrock.technology/) — uniBTC and brBTC alongside a broader Bitcoin yield-vault product suite. `changed` · [Details & sources](docs/directory.md#bedrock).
- [Lombard LBTC](https://docs.lombard.finance/use/lbtc) — Yield-bearing BTC asset now tied to a Bitwise-managed covered-call strategy. `changed` · [Details & sources](docs/directory.md#lombard-lbtc).
- [Lorenzo Protocol](https://www.lorenzo-protocol.xyz/) — Bitcoin liquidity and asset-management infrastructure, including stBTC-related designs. `documented` · [Details & sources](docs/directory.md#lorenzo-protocol).
- [Pendle](https://www.pendle.finance/) — Yield tokenization and trading usable with supported Bitcoin yield assets. `documented` · [Details & sources](docs/directory.md#pendle).
- [Solv Protocol](https://solv.finance/) — SolvBTC representation, xSolvBTC yield exposure and managed BTC strategies. `documented` · [Details & sources](docs/directory.md#solv-protocol).
- [Spectra](https://www.spectra.finance/) — Permissionless yield markets and vault infrastructure, including Bitcoin-related ecosystem use. `documented` · [Details & sources](docs/directory.md#spectra).
- [YieldBasis](https://yieldbasis.com/) — Liquidity strategy designed to offset impermanent loss for tokenized BTC and ETH. `documented` · [Details & sources](docs/directory.md#yieldbasis).

<a id="swaps"></a>
## Cross-chain and atomic swaps

- [Atomiq](https://www.atomiq.exchange/) — Atomic swaps between Bitcoin and supported smart-contract chains. `documented` · [Details & sources](docs/directory.md#atomiq).
- [Boltz](https://boltz.exchange/) — Submarine and chain swaps across Bitcoin payment layers, with additional stablecoin routes. `documented` · [Details & sources](docs/directory.md#boltz).
- [Chainflip](https://chainflip.io/) — Native-asset cross-chain swaps with liquidity, Boost and lending products. `documented` · [Details & sources](docs/directory.md#chainflip).
- [Garden](https://garden.finance/docs/) — Atomic-swap infrastructure and APIs connecting Bitcoin with other networks. `documented` · [Details & sources](docs/directory.md#garden).
- [LendaSwap](https://lendasat.com/docs) — Bitcoin-to-stablecoin swaps associated with Lendasat. `documented` · [Details & sources](docs/directory.md#lendaswap).
- [THORChain](https://thorchain.org/) — Cross-chain exchange and liquidity infrastructure for native assets including BTC. `documented` · [Details & sources](docs/directory.md#thorchain).

<a id="payments"></a>
## Payments, Lightning liquidity and ecash

- [Amboss](https://amboss.tech/) — Bitcoin payment infrastructure and integration tooling. `documented` · [Details & sources](docs/directory.md#amboss).
- [Arkade](https://arkadeos.com/) — Ark-based toolkit for payments, programmable transaction flows and asset exchange. `documented` · [Details & sources](docs/directory.md#arkade).
- [Cashu](https://cashu.space/) — Open Chaumian ecash protocol with Bitcoin-linked mints and wallets. `documented` · [Details & sources](docs/directory.md#cashu).
- [Fedimint](https://fedimint.org/) — Federated ecash for Bitcoin payments and community custody. `documented` · [Details & sources](docs/directory.md#fedimint).
- [Lightning Loop](https://docs.lightning.engineering/lightning-network-tools/loop) — Submarine swaps for moving value between Lightning and on-chain Bitcoin. `documented` · [Details & sources](docs/directory.md#lightning-loop).
- [Lightning Pool](https://docs.lightning.engineering/lightning-network-tools/pool) — Marketplace for leasing Lightning channel liquidity. `documented` · [Details & sources](docs/directory.md#lightning-pool).
- [Mercury Layer](https://mercurylayer.com/) — Statechain implementation using blinded co-signing and key updates. `documented` · [Details & sources](docs/directory.md#mercury-layer).
- [Second](https://second.tech/) — Ark implementation and SDKs connecting Ark, Lightning and on-chain payments. `mainnet-announced` · [Details & sources](docs/directory.md#second).
- [Spark](https://www.spark.money/) — Bitcoin and asset payment infrastructure with Lightning connectivity. `documented` · [Details & sources](docs/directory.md#spark).

<a id="wallets"></a>
## Wallets and access

- [Bitlight Wallet](https://bitlightlabs.com/wallet) — Wallet for Bitcoin and RGB assets, with asset issuance tooling. `documented` · [Details & sources](docs/directory.md#bitlight-wallet).
- [Leather](https://leather.io/) — Wallet for Bitcoin, Stacks assets and ecosystem applications. `documented` · [Details & sources](docs/directory.md#leather).
- [Xverse](https://www.xverse.app/) — Wallet and application gateway for Bitcoin assets and connected financial services. `documented` · [Details & sources](docs/directory.md#xverse).

<a id="builders"></a>
## Developer tools and infrastructure

- [Bitcoin Dev Kit](https://bitcoindevkit.org/) — Libraries for Bitcoin wallet and transaction applications. `documented` · [Details & sources](docs/directory.md#bitcoin-dev-kit).
- [Bitcoin-S](https://bitcoin-s.org/) — Scala libraries and tooling for Bitcoin transaction applications. `documented` · [Details & sources](docs/directory.md#bitcoin-s).
- [Breez SDK](https://breez.technology/) — SDKs for embedding Bitcoin payments into applications. `documented` · [Details & sources](docs/directory.md#breez-sdk).
- [Elements](https://elementsproject.org/) — Sidechain-capable software with confidential transactions and asset issuance. `documented` · [Details & sources](docs/directory.md#elements).
- [LayerEdge](https://www.layeredge.io/) — Proof aggregation and anchoring infrastructure for external applications. `documented` · [Details & sources](docs/directory.md#layeredge).
- [Lightning Dev Kit](https://lightningdevkit.org/) — Modular Lightning implementation and SDK for applications. `documented` · [Details & sources](docs/directory.md#lightning-dev-kit).
- [Metashrew](https://github.com/kungfuflex/metashrew) — WASM-powered indexing framework for Bitcoin metaprotocols. `documented` · [Details & sources](docs/directory.md#metashrew).
- [Nubit / Bitcoin Thunderbolt](https://docs.nubit.org/overview) — Bitcoin transfer and programmability project now described around Thunderbolt. `documented` · [Details & sources](docs/directory.md#nubit-bitcoin-thunderbolt).
- [Rebar Labs](https://rebarlabs.io/) — Bitcoin APIs, metaprotocol data and transaction-submission tools with MEV-focused features. `documented` · [Details & sources](docs/directory.md#rebar-labs).

<a id="research"></a>
## Research, analytics and ecosystem maps

- [Babylon ecosystem](https://babylonlabs.io/ecosystem) — Official discovery map for staking providers and connected infrastructure. `documented` · [Details & sources](docs/directory.md#babylon-ecosystem).
- [Bitcoin Layers](https://www.bitcoinlayers.org/) — Independent directory analyzing Bitcoin layers, BTC representations and trust assumptions. `documented` · [Details & sources](docs/directory.md#bitcoin-layers).
- [Bitcoin Layers methodology](https://bitcoin-layers.gitbook.io/bitcoin-layers/approach-to-analyzing-risk) — Framework covering data availability, operators, settlement and bridge custody. `documented` · [Details & sources](docs/directory.md#bitcoin-layers-methodology).
- [DefiLlama Bitcoin dashboard](https://defillama.com/chain/bitcoin) — Protocol discovery and metrics for projects classified under Bitcoin. `documented` · [Details & sources](docs/directory.md#defillama-bitcoin-dashboard).
- [SoK: Bitcoin Layer Two](https://arxiv.org/abs/2409.02650) — Research paper surveying Bitcoin layer-two constructions and tradeoffs. `documented` · [Details & sources](docs/directory.md#sok-bitcoin-layer-two).
- [Stacks ecosystem](https://www.stacks.co/explore/ecosystem) — Official application, wallet and developer-tool discovery map. `documented` · [Details & sources](docs/directory.md#stacks-ecosystem).

<a id="centralized"></a>
## Centralized and institutional finance

- [Bima](https://docs.bima.money/) — Structured financing against digital assets with an agreed upside-sharing component. `changed` · [Details & sources](docs/directory.md#bima).
- [BounceBit](https://www.bouncebit.io/) — CeDeFi platform combining custodied assets, managed strategies and an EVM settlement chain. `documented` · [Details & sources](docs/directory.md#bouncebit).
- [exSat](https://exsat.network/) — Digital-asset banking platform offering qualified-access custody, payments and strategy products. `changed` · [Details & sources](docs/directory.md#exsat).
- [Ledn](https://www.ledn.io/) — Centralized Bitcoin-backed loans and related credit products. `documented` · [Details & sources](docs/directory.md#ledn).
- [Unchained](https://www.unchained.com/) — Bitcoin financial services built around collaborative custody. `documented` · [Details & sources](docs/directory.md#unchained).

<a id="historical"></a>
## Discontinued, deprecated and changed projects

- [Botanix](https://botanixlabs.com/) — Historical Bitcoin EVM ecosystem associated with the Spiderchain design. `discontinued` · [Details & sources](docs/directory.md#botanix).
- [pSTAKE](https://www.pstake.finance/) — Former Bitcoin/liquid-staking project whose current site presents a research collective. `deprecated` · [Details & sources](docs/directory.md#pstake).
- [Tropykus](https://tropykus.com/) — Historical Rootstock lending application. `discontinued` · [Details & sources](docs/directory.md#tropykus).
- [Yala](https://www.yala.org/) — Previously included in BTCfi stablecoin maps; current site presents prediction-market intelligence. `changed` · [Details & sources](docs/directory.md#yala).

<!-- DIRECTORY:END -->

## Search and reuse

Browse this README, use GitHub search, or search the dataset locally with Python 3.10+:

```sh
python3 scripts/search.py bitcoin
python3 scripts/search.py --category lending
python3 scripts/search.py --network Stacks
python3 scripts/search.py --status discontinued
python3 scripts/search.py --category staking --json
```

No package installation, API key or wallet connection is required.

## Maintain the list

Edit `data/projects.json`, then regenerate and validate:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

To perform a fresh public HTTP check, separately:

```sh
python3 scripts/check_links.py
```

The link checker makes ordinary public GET requests. It does not connect wallets or interact with financial contracts. HTTP failures remain visible for manual review; they do not automatically delete an entry or label a project dead.

## License

[MIT](LICENSE). You can copy, adapt and redistribute this directory and its tooling with the license notice. External project code, trademarks, papers and websites retain their own terms.
