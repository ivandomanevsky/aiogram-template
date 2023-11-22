from aiogram import F, Router, Bot
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

from src.configuration import conf

router = Router()

@router.message(F.text == '/payment')
async def payment(msg: Message) -> None:
    token = conf.payment.token
    prices = [LabeledPrice(label="Test", amount=10000)]
    await msg.answer_invoice("Name test", "Description test",
                             "Invoice test", token, "RUB", prices,
                             need_name=True, need_email=True, send_email_to_provider=True)


@router.pre_checkout_query()
async def pre_checkout_query(pcq: PreCheckoutQuery) -> None:
    await pcq.answer(ok=True)


@router.message(F.successful_payment.invoice_payload.in == 'Invoice test')
async def successful_payment(message: Message) -> None:
    await message.answer('Successful payment')
