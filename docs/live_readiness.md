# Live readiness

- **Project:** Agent Bazaar Hooks
- **Track:** Slice
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:19+00:00`

## Trust boundaries

- **Slice** — `rest_json` — Drive checkout hooks and storefront policy changes.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.
- **Virtuals** — `rest_json` — Sync agent personas and commerce-facing identity metadata.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Celo** — `contract_call` — Settle stablecoin-native transfers on Celo rails.

## Offline-ready partner paths

- **ENS** — prepared_contract_call
- **Lido** — prepared_contract_call
- **ERC-8004 Receipts** — prepared_contract_call
- **Celo** — prepared_contract_call

## Live-only partner blockers

- **Slice**: SLICE_API_KEY, SLICE_HOOK_URL — https://docs.slice.so/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Virtuals**: VIRTUALS_API_URL — https://www.virtuals.io/

## Highest-sensitivity actions

- `slice_checkout_hook` — Slice — Use Slice for a bounded action in this repo.
- `paywithlocus_subaccount_pay` — PayWithLocus — Use PayWithLocus for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for SliceHookController.
- Run python3 scripts/run_agent.py to produce a dry run for slice_bazaar.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
