import os
import sys
import click
from dotenv import load_dotenv
from typing import Optional
from bot.logging_config import configure_logging
from bot.client import FuturesClient
from bot.orders import OrderManager

load_dotenv()


@click.command()
@click.option('--symbol', required=True, help='Trading symbol, e.g. BTCUSDT')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL'], case_sensitive=False), help='BUY or SELL')
@click.option('--order-type', 'order_type', required=True, type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False), help='Order type')
@click.option('--quantity', required=True, type=float, help='Order quantity (contract size)')
@click.option('--price', required=False, type=float, help='Price for LIMIT orders')
@click.option('--testnet/--no-testnet', default=True, help='Use Binance Futures Testnet')
def main(symbol: str, side: str, order_type: str, quantity: float, price: Optional[float], testnet: bool):
	"""Simple Binance Futures Testnet trading CLI.

	Example:
	  python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
	"""

	configure_logging()

	# Create client and order manager
	try:
		client = FuturesClient(testnet=testnet)
	except Exception as e:
		click.echo(f'Failed to create Binance client: {e}', err=True)
		sys.exit(2)

	manager = OrderManager(client)

	try:
		resp = manager.place_order(symbol=symbol.upper(), side=side.upper(), order_type=order_type.upper(), quantity=quantity, price=price)
		click.echo('Order response:')
		click.echo(resp)
	except Exception as e:
		click.echo(f'Error placing order: {e}', err=True)
		sys.exit(1)


if __name__ == '__main__':
	main()

