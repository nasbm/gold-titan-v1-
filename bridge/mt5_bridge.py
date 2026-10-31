import os,time,requests
import MetaTrader5 as mt5
URL=os.environ.get('WEBAPP_URL','http://localhost:3000').rstrip('/')+'/api/bridge'
TOKEN=os.environ['BRIDGE_TOKEN']
SYMBOL=os.environ.get('MT5_SYMBOL','XAUUSD')
if not mt5.initialize(): raise RuntimeError('MT5 initialize failed')
if not mt5.symbol_select(SYMBOL,True): raise RuntimeError('Symbol not available: '+SYMBOL)
while True:
 try:
  tick=mt5.symbol_info_tick(SYMBOL)
  bars=mt5.copy_rates_from_pos(SYMBOL,mt5.TIMEFRAME_M1,0,70)
  if tick is None or bars is None or len(bars)<55: print('Waiting for valid MT5 data')
  else:
   candles=[{'time':int(b['time']),'open':float(b['open']),'high':float(b['high']),'low':float(b['low']),'close':float(b['close'])} for b in bars]
   r=requests.post(URL,json={'symbol':SYMBOL,'bid':float(tick.bid),'ask':float(tick.ask),'candles':candles},headers={'Authorization':'Bearer '+TOKEN},timeout=10)
   print('Bridge:',r.status_code,r.text[:100])
 except Exception as e: print('Bridge error:',str(e))
 time.sleep(10)
