import logging
from typing import Optional
from .client import FuturesClient

LOG = logging.getLogger('trading')


def validate_symbol(client: FuturesClient, symbol: str) -> None:
	if not symbol or not isinstance(symbol, str):
		raise ValueError('Symbol must be a non-empty string')
	info = client.get_symbol_info(symbol)
	if not info:
		raise ValueError(f'Symbol not found on exchange: {symbol}')


def validate_side(side: str) -> None:
	if not isinstance(side, str):
		raise ValueError('Side must be a string')
	if side.upper() not in ('BUY', 'SELL'):
		raise ValueError('Side must be BUY or SELL')


def validate_order_type(order_type: str) -> None:
	if not isinstance(order_type, str):
		raise ValueError('Order type must be a string')
	if order_type.upper() not in ('MARKET', 'LIMIT'):
		raise ValueError('Order type must be MARKET or LIMIT')


def validate_quantity_price(order_type: str, quantity: float, price: Optional[float]) -> None:
	try:
		q = float(quantity)
	except Exception:
		raise ValueError('Quantity must be numeric')
	if q <= 0:
		raise ValueError('Quantity must be greater than zero')

	if order_type.upper() == 'LIMIT':
		if price is None:
			raise ValueError('Price is required for LIMIT orders')
		try:
			p = float(price)
		except Exception:
			raise ValueError('Price must be numeric')
		if p <= 0:
			raise ValueError('Price must be greater than zero')

