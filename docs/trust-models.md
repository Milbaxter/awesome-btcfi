# Trust models and due diligence

[Back to Awesome BTCfi](../README.md)

This directory does not assign numerical safety scores. A single score hides the fact that custody, settlement, liquidity and economic exposure can fail independently. The [Bitcoin Layers methodology](https://bitcoin-layers.gitbook.io/bitcoin-layers/approach-to-analyzing-risk) provides a useful starting point for separating network operators, settlement, data availability and bridge custody.

## Compare the mechanism

| Mechanism | What controls the Bitcoin or claim? | Questions that distinguish implementations |
| --- | --- | --- |
| Bitcoin payment channel | Bitcoin transaction and script rules, with participant monitoring | Can I recover without the provider? What backups and online monitoring are required? |
| Native collateral escrow / DLC | Contract participants, scripts and possibly oracle signatures | Which key combinations can move BTC? What happens after a missed oracle event or borrower default? |
| Ark / statechain-like design | Off-chain ownership machinery, transaction trees and service participation | Which transfers need operator honesty? When must I refresh? What does unilateral recovery cost? |
| Federation / threshold peg | A signer quorum or federation holding BTC | Can signers collude or censor? How are members changed? Who can redeem? |
| Institutional wrapper | A custodian and the token's legal/technical issuer | Who owns reserves? What are redemption rights, eligibility rules and freeze powers? |
| ICP chain-key representation | Canisters, subnet signing and network governance | Who can upgrade the minter? What transaction screening applies? How does BTC redemption fail? |
| Optimistic / BitVM-related bridge | Protocol-specific proofs, challengers, operators and liquidity | Who can challenge, within what time, using which data? Who funds withdrawals and disputes? |
| Client-validated asset | Proofs and state held or retrieved by users | Does the seed restore asset history? Can I independently validate issuance and transfers? |
| Bitcoin metaprotocol | Additional interpretation/execution of data in Bitcoin transactions | Can independent indexers agree? Which rules are enforced by Bitcoin itself versus external software? |
| Liquid staking / yield receipt | Underlying collateral mechanism plus receipt-token contracts | What exactly backs the receipt? Is the exchange rate fixed or variable? Can I redeem during stress? |
| Ecash | A mint or federation owing redemption | What proves solvency? What happens if the mint is unavailable or refuses redemption? |
| Managed strategy | Custodians, managers, counterparties and financial positions | Can a manager trade, withdraw or rehypothecate? Are exposures and exit terms visible? |

These are review categories, not endorsements. “Native,” “trustless,” “decentralized,” “ZK” and “Bitcoin L2” are insufficient descriptions on their own.

## A practical review sequence

1. **Identify the exact asset and network.** A ticker is not an identifier. WBTC, cbBTC, BTCB, BTC.b, sBTC, cBTC and ckBTC are different systems. The same ticker on two networks can have additional bridge layers.
2. **Draw the custody path.** Record where BTC goes, who can sign, who holds keys, and whether you retain unilateral spending authority. A wallet being self-custodial says nothing about a subsequent protocol deposit.
3. **Test the exit model on paper.** Separate normal redemption, an operator outage, a chain halt, a challenge and an emergency exit. List delays, required data, liquidity and transaction costs.
4. **Inspect current deployment and controls.** Read the actual deployed contracts and privileged roles. A whitepaper may describe the destination architecture rather than the system in use today. Ask which components are upgradeable, pausable or permissioned.
5. **Trace the return.** Identify borrower interest, fees, network rewards, token subsidies, options premiums, funding, or off-chain investments. Record the payout currency and who ultimately pays.
6. **Inspect collateral and leverage.** Read loan-to-value rules, oracle fallback behavior, liquidation penalties and whether a wrapper depeg can trigger liquidation before BTC itself moves.
7. **Read security evidence with scope.** An audit must match the code version and deployment. Check incident postmortems, fixes, privileged roles and bounty scope. An audit badge is not an insurance policy.
8. **Check economic and legal claims separately.** Proof of reserves may not establish total liabilities, ownership, segregation or enforceable redemption. A licensing statement does not prove a strategy is safe or accessible to every user.

## Three common accounting mistakes

- **Double-counting BTC.** A deposited coin, its wrapper, a staking receipt and a vault receipt can appear in several TVL totals. Adding them does not create more underlying Bitcoin.
- **Mixing reward units.** “BTC staking APY” may be paid in CORE, STRK or another token. A promotional rate can include incentives with different liquidity and price exposure.
- **Confusing leverage with yield.** Repeated borrowing and redepositing increases exposure to the same position. It does not create an independent source of return.

The per-entry **review focus** in the [catalog](directory.md) highlights the questions most relevant to that listing. It is not a claim that this repository has answered all of them.
