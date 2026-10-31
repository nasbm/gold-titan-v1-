# GOLD TITAN AI V1.00

TEAMNASBM Gold live scalping research prototype. Node.js web app with authenticated FxPro MT5 Python bridge. Technical-only signals; fundamental and sentiment are explicitly **not connected**. No automatic orders.

## Run
Node.js 20+: `npm start` and open `http://localhost:3000`. Set `BRIDGE_TOKEN` to a long random secret in your host environment.

## Connect FxPro MT5
On Windows with logged-in MT5: `pip install MetaTrader5 requests`. Set `WEBAPP_URL` (HTTPS backend URL), `BRIDGE_TOKEN` (same as server), `MT5_SYMBOL` (broker symbol), then run `python bridge/mt5_bridge.py`.

## Deploy
Use Render Node web service with `render.yaml`; configure `BRIDGE_TOKEN` manually. GitHub Pages cannot run this backend. Free hosts may sleep. This is not yet validated for live trading. No broker credentials in GitHub.
