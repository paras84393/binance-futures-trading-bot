import argparse
from dotenv import load_dotenv
load_dotenv()
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("LIMIT orders require --price")

    print("\n====== ORDER SUMMARY ======")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)

    if args.price:
        print("Price:", args.price)

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n====== RESPONSE ======")
    print("OrderId:", response.get("orderId"))
    print("Status:", response.get("status"))
    print("ExecutedQty:", response.get("executedQty"))
    print("AvgPrice:", response.get("avgPrice"))

    print("\n✅ Order placed successfully")

except Exception as e:

    print("\n❌ Error:", str(e))