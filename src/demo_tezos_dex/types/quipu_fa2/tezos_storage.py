# generated by DipDup 8.1.1

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class Ledger(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    allowances: list[str]
    balance: str
    frozen_balance: str


class UserRewards(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    reward: str
    reward_paid: str


class Voters(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    candidate: str | None = None
    last_veto: str
    veto: str
    vote: str


class Storage(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    baker_validator: str
    current_candidate: str | None = None
    current_delegated: str | None = None
    last_update_time: str
    last_veto: str
    ledger: dict[str, Ledger]
    period_finish: str
    reward: str
    reward_paid: str
    reward_per_sec: str
    reward_per_share: str
    tez_pool: str
    token_address: str
    token_id: str
    token_pool: str
    total_reward: str
    total_supply: str
    total_votes: str
    user_rewards: dict[str, UserRewards]
    veto: str
    vetos: dict[str, str]
    voters: dict[str, Voters]
    votes: dict[str, str]


class QuipuFa2Storage(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dex_lambdas: dict[str, str]
    metadata: dict[str, str]
    storage: Storage
    token_lambdas: dict[str, str]
