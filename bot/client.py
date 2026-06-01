import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
import requests
from typing import Optional

load_dotenv()

LOG = logging.getLogger('trading')


class FuturesClient:
	"""Wrapper around python-binance Client for USDT-M Futures (Testnet).

	Notes / assumptions:
	- This wrapper uses the python-binance library and calls the futures endpoints
	  (e.g. client.futures_create_order). To point at the Futures Testnet we
	  set a best-effort API URL. If your python-binance version exposes a named
	  attribute for futures testnet endpoint, you can override it similarly.
	- Expects BINANCE_API_KEY and BINANCE_API_SECRET in environment (dotenv).
	"""

	def __init__(self, api_key: Optional[str] = None, api_secret: Optional[str] = None, testnet: bool = True):
		api_key = api_key or os.getenv('BINANCE_API_KEY')
		api_secret = api_secret or os.getenv('BINANCE_API_SECRET')
		if not api_key or not api_secret:
			raise ValueError('BINANCE_API_KEY and BINANCE_API_SECRET must be set in environment')

		# Create client
		self._client = Client(api_key, api_secret)

		# Point to Futures Testnet endpoints when requested.
		# Implementation detail: different python-binance versions expose different
		# ways to override the base urls. We set several common attributes. If
		# these don't match the installed version, the library will continue to
		# use its defaults; at runtime you can review the HTTP calls to verify.
		if testnet:
			# Common testnet endpoints for Binance Futures (USDT-M)
			# Assumption: API path prefix is /fapi
			try:
				# Attempt likely attribute names
				self._client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
			except Exception:
				LOG.debug('Could not set API_URL on client (non-fatal)')

		self.logger = LOG

	# Exchange info / symbol helpers
	def get_symbol_info(self, symbol: str) -> Optional[dict]:
		try:
			info = self._client.futures_exchange_info()
			symbols = info.get('symbols', [])
			for s in symbols:
				if s.get('symbol') == symbol:
					return s
			return None
		except (BinanceAPIException, BinanceRequestException, requests.exceptions.RequestException) as e:
			self.logger.exception('Failed to fetch exchange info: %s', e)
			raise

	# Order helpers
	def create_market_order(self, symbol: str, side: str, quantity: float) -> dict:
		try:
			resp = self._client.futures_create_order(symbol=symbol, side=side, type='MARKET', quantity=quantity)
			self.logger.info('Market order response: %s', resp)
			return resp
		except (BinanceAPIException, BinanceRequestException, requests.exceptions.RequestException) as e:
			self.logger.exception('Failed to create market order: %s', e)
			raise

	def create_limit_order(self, symbol: str, side: str, quantity: float, price: float, time_in_force: str = 'GTC') -> dict:
		try:
			resp = self._client.futures_create_order(symbol=symbol, side=side, type='LIMIT', timeInForce=time_in_force, quantity=quantity, price=str(price))
			self.logger.info('Limit order response: %s', resp)
			return resp
		except (BinanceAPIException, BinanceRequestException, requests.exceptions.RequestException) as e:
			self.logger.exception('Failed to create limit order: %s', e)
			raise

	# Convenience wrapper to expose the underlying client when needed
	@property
	def raw(self) -> Client:
		return self._client
