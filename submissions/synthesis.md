# Agent Bazaar Hooks

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Slice
- **Primary track:** Slice
- **Overlap targets:** PayWithLocus, ENS, Lido stETH Treasury, Virtuals, ERC-8004 Receipts, Celo
- **Primary contract:** SliceHookController
- **Primary operator module:** slice_bazaar
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

An agent storefront that models dynamic pricing, checkout policy, and identity-aware access for ENS and Locus-powered commerce.

## Track evidence

- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`
- `artifacts/onchain_intents/celo_payment_settle.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Agent Bazaar Hooks",
  "track": "Slice",
  "plan_id": "0xc74765bbf4b587422f34c71cece659c301f5941db5c23e312ff20e8e76a14892",
  "simulation_hash": "0xfc70bc147f43b61a5be979f34da4dc86ad29f7c9ecff6508d609f47cf10f10ae",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/ens_ens_publish.json",
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json",
    "artifacts/onchain_intents/celo_payment_settle.json"
  ],
  "partner_statuses": {
    "Slice": "awaiting_credentials",
    "PayWithLocus": "awaiting_credentials",
    "ENS": "prepared_contract_call",
    "Lido": "prepared_contract_call",
    "Virtuals": "awaiting_credentials",
    "ERC-8004 Receipts": "prepared_contract_call",
    "Celo": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:19+00:00"
}
```
