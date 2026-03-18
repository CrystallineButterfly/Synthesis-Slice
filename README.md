# Agent Bazaar Hooks

- **Repo:** `Synthesis-Slice`
- **Primary track:** Slice
- **Category:** commerce
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

An agent storefront that models dynamic pricing, checkout policy, and identity-aware access for ENS and Locus-powered commerce.

## Selected concept

An agent storefront models dynamic pricing, checkout policy, and identity-aware access. The contract stores pricing rule hashes and merchant policy state, while Python scripts assemble hook configurations and buyer flows.

## Idea shortlist

1. ENS + Locus Commerce Store
2. Dynamic Agent Pricing Hooks
3. ERC-8128 Web Auth Checkout

## Partners covered

Slice, PayWithLocus, ENS, Lido, Virtuals, ERC-8004 Receipts, Celo

## Architecture

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[SliceHookController policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> slice[Slice]
    Contract --> paywithlocus[PayWithLocus]
    Contract --> ens[ENS]
    Contract --> lido[Lido]
    Contract --> virtuals[Virtuals]
    Contract --> erc_8004_receipts[ERC-8004 Receipts]
```

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `slice_checkout_hook` | Slice | Use Slice for a bounded action in this repo. | $35 | medium |
| `paywithlocus_subaccount_pay` | PayWithLocus | Use PayWithLocus for a bounded action in this repo. | $120 | medium |
| `ens_ens_publish` | ENS | Use ENS for a bounded action in this repo. | $5 | low |
| `lido_yield_route` | Lido | Use Lido for a bounded action in this repo. | $200 | medium |
| `virtuals_identity_sync` | Virtuals | Use Virtuals for a bounded action in this repo. | $5 | medium |
| `erc_8004_receipts_receipt_anchor` | ERC-8004 Receipts | Use ERC-8004 Receipts for a bounded action in this repo. | $1 | medium |
| `celo_payment_settle` | Celo | Use Celo for a bounded action in this repo. | $150 | low |

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| Slice | SLICE_API_KEY, SLICE_HOOK_URL | https://docs.slice.so/ |
| PayWithLocus | LOCUS_API_KEY, LOCUS_PAYMENT_URL | https://docs.locus.finance/ |
| ENS | ENS_NAME | https://docs.ens.domains/ |
| Lido | RPC_URL | https://docs.lido.fi/ |
| Virtuals | VIRTUALS_API_URL | https://www.virtuals.io/ |
| ERC-8004 Receipts | RPC_URL | https://eips.ethereum.org/EIPS/eip-8004 |
| Celo | CELO_RPC_URL | https://docs.celo.org/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for SliceHookController.
3. Run python3 scripts/run_agent.py to produce a dry run for slice_bazaar.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
