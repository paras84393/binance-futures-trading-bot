import logging
from .client import get_client

client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logging.info(
            f"Order Request: {symbol} {side} {order_type} qty={quantity} price={price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:

        logging.error(f"Order Failed: {str(e)}")
        raise