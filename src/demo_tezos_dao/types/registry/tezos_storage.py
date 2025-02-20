# generated by DipDup 8.1.1

from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict


class Key(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    owner: str
    delegate: str


class Delegate(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    key: Key
    value: dict[str, Any]


class FreezeHistory(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    current_stage_num: str
    current_unstaked: str
    past_unstaked: str
    staked: str


class GovernanceToken(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    address: str
    token_id: str


class ProposalKeyListSortByLevelItem(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    nat: str
    bytes: str


class Key1(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    address: str
    bool: bool


class Voter(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    key: Key1
    value: str


class Proposals(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    downvotes: str
    metadata: str
    proposer: str
    proposer_frozen_token: str
    quorum_threshold: str
    start_level: str
    upvotes: str
    voters: list[Voter]
    voting_stage_num: str


class QuorumThresholdAtCycle(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    last_updated_cycle: str
    quorum_threshold: str
    staked: str


class RegistryStorage(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    admin: str
    delegates: list[Delegate]
    extra: dict[str, str]
    freeze_history: dict[str, FreezeHistory]
    frozen_token_id: str
    frozen_total_supply: str
    governance_token: GovernanceToken
    guardian: str
    metadata: dict[str, str]
    pending_owner: str
    permits_counter: str
    proposal_key_list_sort_by_level: list[ProposalKeyListSortByLevelItem]
    proposals: dict[str, Proposals]
    quorum_threshold_at_cycle: QuorumThresholdAtCycle
    start_level: str
    custom_entrypoints: dict[str, str]
    decision_lambda: str
    fixed_proposal_fee_in_token: str
    governance_total_supply: str
    max_proposals: str
    max_quorum_change: str
    max_quorum_threshold: str
    max_voters: str
    min_quorum_threshold: str
    period: str
    proposal_check: str
    proposal_expired_level: str
    proposal_flush_level: str
    quorum_change: str
    rejected_proposal_slash_value: str
