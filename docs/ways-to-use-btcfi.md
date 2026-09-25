# Ways to use BTCfi

[Back to Awesome BTCfi](../README.md) · Snapshot: September 25, 2026

BTCfi is an umbrella term, not a single architecture. A product can use BTC economically while executing on another chain, entrusting BTC to a custodian, or exposing the holder to a strategy. This map groups **activities**, while the [directory](directory.md) groups **projects and infrastructure**.

These are descriptions of mechanisms, not recommended allocations. Examples identify relevant projects; they do not imply that a particular market is open, available in your jurisdiction, or appropriate for you.

## Activity map

| Approach | What you do / hold | Where the economic benefit comes from | Examples | Main tradeoffs |
| --- | --- | --- | --- | --- |
| Pay with native BTC off-chain | Use a Lightning channel, Ark implementation or statechain-style system | Faster or cheaper payments; no automatic yield | [Lightning](directory.md#lightning-network), [Second](directory.md#second), [Spark](directory.md#spark) | Recovery, operator assumptions, liquidity and Bitcoin exit fees differ |
| Route Lightning payments | Run a node and commit BTC to channels | Routing fees paid by users | [Lightning](directory.md#lightning-network), [LDK](directory.md#lightning-dev-kit) | Uptime, channel balance, rebalancing costs; revenue can be below costs |
| Lease channel liquidity | Allocate channel capacity for a term | Fees from buyers of liquidity | [Lightning Pool](directory.md#lightning-pool) | Demand, lease commitments and node operations |
| Swap across networks | Exchange BTC for a destination-chain asset | Access to another asset or market, rather than yield itself | [Atomiq](directory.md#atomiq), [Garden](directory.md#garden), [Boltz](directory.md#boltz) | Refund paths, timeouts and every additional route component |
| Make markets for native cross-chain swaps | Supply capital to cross-chain liquidity systems | Swap or execution fees | [THORChain](directory.md#thorchain), [Chainflip](directory.md#chainflip) | Network vault custody, price exposure and pool mechanics |
| Borrow against Bitcoin in multisig | Lock BTC collateral and receive fiat or stablecoins | Liquidity without an immediate spot sale; borrowing has costs | [Lendasat](directory.md#lendasat), [Firefish](directory.md#firefish), [Debifi](directory.md#debifi) | Shared-key control, contracts, disputes and liquidation |
| Lend fiat or stablecoins against BTC | Fund another party's collateralized loan | Borrower interest | [Hodl Hodl](directory.md#lend-at-hodl-hodl), [Firefish](directory.md#firefish) | Loan is often denominated in dollars, not BTC; default and execution risk |
| Supply a BTC representation to a money market | Deposit a wrapper such as WBTC or BTCB | Interest paid by borrowers, sometimes incentives | [Aave](directory.md#aave), [Venus](directory.md#venus), [Zest](directory.md#zest-protocol) | Wrapper, contract, oracle and withdrawal-liquidity risk |
| Borrow against wrapped BTC | Post a BTC representation as collateral | Access to stablecoins or other assets | [Morpho](directory.md#morpho), [Granite](directory.md#granite) | Liquidation, changing interest, wrapper depeg and chain risk |
| Mint a collateral-backed dollar | Open a collateralized debt position or use a shared collateral system | Dollar liquidity and a different price exposure | [Mezo](directory.md#mezo), [Money On Chain](directory.md#money-on-chain), [Ducat](directory.md#ducat-unit) | Different peg designs, collateral controls, redemptions and liquidation rules |
| Provide stablecoin liquidation liquidity | Supply funds to a stability mechanism | Compensation associated with liquidations and sometimes rewards | [Sovryn Zero](directory.md#sovryn-zero), [Arkadiko](directory.md#arkadiko) | Can receive declining collateral during stressed markets |
| Provide liquidity between BTC representations | Supply assets such as two different BTC wrappers | Trading fees and optional incentives | [Curve](directory.md#curve) | A broken peg can leave the pool holding the weaker asset |
| Provide BTC/stablecoin or BTC/other-asset liquidity | Hold a changing basket through an AMM position | Trading fees | [Bitflow](directory.md#bitflow), [Uniswap](directory.md#uniswap), [SideSwap](directory.md#sideswap) | Impermanent loss, price ranges, liquidity and underlying asset trust |
| Lock native BTC for external-network security | Create a BTC staking or delegation position | External network rewards | [Babylon](directory.md#babylon-bitcoin-staking), [Core](directory.md#core) | Designs differ: slashing, timelocks, exit windows and reward currencies are not interchangeable |
| Stake a BTC wrapper on another chain | Stake supported tokenized BTC | Rewards from that network | [Starknet Bitcoin staking](directory.md#starknet-bitcoin-staking) | Adds wrapper/bridge and chain dependencies; rewards are STRK |
| Hold a liquid staking receipt | Exchange a supported asset for a transferable staking claim | Underlying staking rewards, potentially compounded | [Stacking DAO](directory.md#stacking-dao), [Endur](directory.md#endur) | Receipt-token depeg, redemption conditions and stacked dependencies |
| Restake Bitcoin-linked collateral | Allocate an eligible representation to shared security | Payments or incentives from secured services | [Pell](directory.md#pell-network), [SatLayer](directory.md#satlayer) | Additional enforcement/slashing rights; terms differ by service and vault |
| Trade principal and future yield separately | Buy principal tokens or yield tokens | A maturity claim or the underlying asset's future income | [Pendle](directory.md#pendle), [Spectra](directory.md#spectra) | Underlying loss risk persists; yield tokens can lose their entire purchase value |
| Use leveraged liquidity strategies | Deposit into a strategy managing liquidity and debt | Trading fees net of funding and rebalancing costs | [YieldBasis](directory.md#yieldbasis) | Reducing one form of loss can introduce leverage and borrowing risks |
| Use covered-call or structured BTC strategies | Hold a managed receipt or enter a financing contract | Option premiums or exchanged future upside | [Lombard LBTC](directory.md#lombard-lbtc), [Bima](directory.md#bima) | Payoff differs from holding BTC; losses, counterparties and exit terms matter |
| Use basis or other managed strategies | Allocate to a manager combining spot and derivatives or other markets | Funding, spreads or investment returns | [Bedrock](directory.md#bedrock), [BounceBit](directory.md#bouncebit), [exSat](directory.md#exsat) | “Delta-neutral” does not remove leverage, venue or liquidity risk |
| Borrow or trade through a centralized provider | Sign a loan agreement or fund an account | Credit access or trading exposure | [Ledn](directory.md#ledn), [LN Markets](directory.md#ln-markets) | Counterparties and contractual claims remain even with Bitcoin or Lightning funding |
| Lend BTC against collectibles | Fund BTC loans secured by supported Ordinals or Runes | Borrower interest | [Liquidium](directory.md#liquidium) | Default can leave the lender holding illiquid collateral worth less than the loan |
| Issue or trade Bitcoin-related assets | Create or use tokens and contracts | Application utility; issuer-dependent economics | [RGB](directory.md#rgb), [Taproot Assets](directory.md#taproot-assets), [Runes](directory.md#runes), [Liquid](directory.md#liquid-network) | Issued tokens are not native BTC; asset rights and redemption can depend on an issuer |
| Use private ecash | Hold bearer claims against a mint or federation | Private, efficient payments; not inherent yield | [Cashu](directory.md#cashu), [Fedimint](directory.md#fedimint) | Mint/federation solvency and availability |

## Follow the asset, not the brand

Consider three different paths:

1. **Native collateral loan:** BTC → Bitcoin collateral escrow → a fiat/stablecoin loan. The key questions are who can release collateral, what triggers liquidation, and who resolves disputes.
2. **Wrapped BTC loan:** BTC → issuer or bridge → BTC representation → a lending contract → borrowed stablecoin. Review each step; a strong lending contract cannot repair failed wrapper backing.
3. **Composed yield position:** BTC → representation or staking receipt → yield token or vault → another collateralized position. Every added contract, manager and liquidation condition changes the total exposure.

Tokenized yield also needs a unit of account. More units of a reward token do not necessarily mean more BTC. A dollar yield can be positive while underperforming BTC; a BTC-denominated strategy can lose Bitcoin principal. A points program is not realized cash income.

## What “Bitcoin staking” does and does not mean

Bitcoin itself uses proof of work. BTCfi staking typically uses BTC or a BTC representation to participate in **another system's security or incentive design**. [Babylon's documentation](https://babylonlabs.io/institutional-staking), [Core's explanation](https://coredao.org/) and [Starknet's guide](https://www.starknet.io/staking/) describe materially different arrangements.

Also separate **staking STX and earning BTC** from **staking BTC**. [Stacking DAO](https://www.stackingdao.com/) now describes products for both, with different input assets and receipts. Never infer the deposited asset or security model from the currency in which rewards are advertised.

## Areas this map intentionally does not turn into a shopping list

Leveraged looping, leveraged derivatives and recursive receipt-token strategies are possible compositions, not new sources of risk-free return. Mining operations, every centralized exchange, individual collectible collections and all Bitcoin ETFs would turn a BTCfi directory into a general Bitcoin industry catalog. They are outside the core scope, although custody, tokenization and institutional credit are included where they directly explain a BTCfi pathway.
