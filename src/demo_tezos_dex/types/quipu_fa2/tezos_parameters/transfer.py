# generated by DipDup 8.1.1

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import RootModel


class Tx(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    to_: str
    token_id: str
    amount: str


class TransferParameterItem(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    from_: str
    txs: list[Tx]


class TransferParameter(RootModel[list[TransferParameterItem]]):
    root: list[TransferParameterItem]
