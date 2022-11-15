from decimal import Decimal
from decimal import InvalidOperation

from demo_tzbtc_transfers.handlers.on_balance_update import on_balance_update
from dipdup.context import HandlerContext
from dipdup.models import TokenTransferData


async def on_token_transfer(
    ctx: HandlerContext,
    token_transfer: TokenTransferData,
) -> None:
    from_, to = token_transfer.from_address, token_transfer.to_address
    if not from_ or not to or from_ == to:
        return
    try:
        amount = Decimal(token_transfer.amount or 0) / (10**8)
    except InvalidOperation:
        return
    if not amount:
        return

    await on_balance_update(from_, -amount, token_transfer.timestamp)
    await on_balance_update(to, amount, token_transfer.timestamp)
