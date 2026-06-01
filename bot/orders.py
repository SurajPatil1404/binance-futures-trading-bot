from typing import Any, Dict, Optional
import logging
from typing import Any, Dict
from .client import FuturesClient
from .validators import validate_symbol, validate_side, validate_order_type, validate_quantity_price
from binance.exceptions import BinanceAPIException

LOG = logging.getLogger('trading')


class OrderManager:
	def __init__(self, client: FuturesClient):
		self.client = client
		self.logger = LOG

	def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: Optional[float] = None) -> Dict[str, Any]:
		# Validate inputs
		validate_symbol(self.client, symbol)
		validate_side(side)
		validate_order_type(order_type)
		validate_quantity_price(order_type, quantity, price)

		try:
			if order_type.upper() == 'MARKET':
				self.logger.info('Placing MARKET %s %s qty=%s', side, symbol, quantity)
				resp = self.client.create_market_order(symbol=symbol, side=side.upper(), quantity=quantity)
			else:
				assert price is not None
				self.logger.info('Placing LIMIT %s %s qty=%s price=%s', side, symbol, quantity, price)
				resp = self.client.create_limit_order(symbol=symbol, side=side.upper(), quantity=quantity, price=price)

			self.logger.info('Order placed successfully: %s', resp)
			return resp
		except BinanceAPIException as e:
			self.logger.exception('Binance API error while placing order: %s', e)
			raise
		except Exception as e:
			self.logger.exception('Unexpected error while placing order: %s', e)
			raise

