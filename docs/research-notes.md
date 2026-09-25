# Material changes and terminology traps

[Back to Awesome BTCFi](../README.md) · Reviewed September 25, 2026

This is a selective research log, not a complete incident database. It records changes that materially affected how entries were classified.

| Finding | Directory treatment | Evidence |
| --- | --- | --- |
| Botanix's website announces a July 1, 2026 shutdown | `discontinued`; historical section | [Official website](https://botanixlabs.com/) |
| Tropykus says its interface closed July 27 and support ended August 31, 2026 | `discontinued`; note that remaining contracts and recovery guidance may still exist | [Official notice](https://tropykus.com/) |
| pSTAKE's current site focuses on Web3/AI research and routes staking links to a deprecation domain | `deprecated`; avoid presenting old staking descriptions as current availability | [Official website](https://www.pstake.finance/) |
| Yala's site now presents a prediction-market intelligence product and retains a redemption link | `changed`; historical BTCFi inclusion, current YU minting unconfirmed | [Official website](https://www.yala.org/) |
| Lombard says LBTC moved from Babylon staking to an institutional covered-call strategy in August 2026 | `changed`; classify under managed yield instead of simply calling it a Babylon LST | [Current asset documentation](https://docs.lombard.finance/learn/products/assets) |
| Lombard published September 2026 chain-support changes, including deprecated mint/redemption routes | Do not copy old supported-chain lists into LBTC or BTC.b entries | [Bridge documentation and migration pointers](https://docs.lombard.finance/use/bridging) |
| Bima's current documentation describes structured financing with named counterparties and upside sharing | `changed`; institutional-finance category | [Current documentation](https://docs.bima.money/) |
| exSat's current site emphasizes qualified-access banking, custody and managed strategies | `changed`; institutional-finance category | [Official website](https://exsat.network/) |
| Bedrock describes a wider yield-vault suite beyond its earlier staking framing | `changed`; product-specific yield and custody review | [Official website](https://www.bedrock.technology/) |
| Alpen's docs explicitly identify Bitcoin signet testnet and future mainnet support | `testnet`; no inferred launch from marketing | [Technical documentation](https://docs.alpen.org/) |
| Babylon's new vault page links to a testnet app while staking is a separate product | Separate Bitcoin Staking and Trustless Bitcoin Vault entries | [Official website](https://babylonlabs.io/) |
| Zest describes both Stacks markets and a different Bitcoin collateral-vault architecture | Preserve the distinction; no blanket deployment assertion | [Official website](https://www.zestprotocol.com/) |

## Names that can mislead

- **BTCFi / BitcoinFi:** broad industry labels; also used in specific product brands, including [BTCFi (Bifrost)](directory.md#btcfi-bifrost).
- **LBTC:** the Lombard product in this list. A matching ticker elsewhere is not sufficient identity verification.
- **BTC.b versus BTCB:** separate systems; the dot is meaningful.
- **sBTC:** the Stacks bridge asset here, not every other historical use of this ticker.
- **stBTC:** multiple issuers use similar symbols. Stacking DAO and Lorenzo must be identified by issuer, network and contract.
- **Spark:** Bitcoin payment infrastructure at `spark.money` in this directory; not the similarly named Ethereum DeFi protocol.
- **USDA, USDa, USDh, MUSD, UNIT and ctUSD:** different assets, collateral models, issuers and redemption rules. Some are BTC-linked, one is described as STX-collateralized, and ctUSD is described as fiat-reserve-backed.
- **STX stacking and BTC staking:** neither the deposited asset nor the security mechanism can be inferred from the reward ticker.

## Interpreting a current homepage

A homepage update establishes a change in public description, not proof that legacy liabilities were settled or that a new strategy has reached full deployment. For example, a target allocation or advertised yield is not a verified current position. This is why the list records **what changed** without declaring the replacement product safe, fully deployed or available to everyone.

Historical entries remain visible to make old ecosystem maps easier to interpret. No deposit instructions are provided for closed or deprecated projects.
