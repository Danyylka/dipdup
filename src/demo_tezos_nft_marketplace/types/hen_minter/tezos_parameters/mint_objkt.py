# generated by DipDup 8.1.1

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class MintOBJKTParameter(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    address: str
    amount: str
    metadata: str
    royalties: str
