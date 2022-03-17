from django.shortcuts import render
from pycoingecko import CoinGeckoAPI

# Create your views here.
coingecko = CoinGeckoAPI()


def show_crypto_prices(request):
    bitcoin = coingecko.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
    btcdiff = (bitcoin * 0.02437757945262583) - 1000
    ethereum = coingecko.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
    ethdiff = (ethereum * 0.17805570294610965) - 500
    stellar = coingecko.get_price(ids='stellar', vs_currencies='usd')['stellar']['usd']
    xlmdiff = (stellar * 1591.1742866235281) - 300
    ripple = coingecko.get_price(ids='ripple', vs_currencies='usd')['ripple']['usd']
    ripplediff = (ripple * 565.7303201279304) - 450
    total = btcdiff + ethdiff + xlmdiff + ripplediff

    return render(request, "index.html", {
        'btc': bitcoin,
        'btc_at_buy': 40904,
        'btc_diff': round(btcdiff, 5),
        'eth': ethereum,
        'eth_at_buy': 2806,
        'eth_diff': round(ethdiff, 5),
        'xlm': stellar,
        'xlm_at_buy': 0.188577,
        'xlm_diff': round(xlmdiff, 5),
        'xrp': ripple,
        'xrp_at_buy': 0.795633,
        'xrp_diff': round(ripplediff, 5),
        'totalpl': round(total, 5)

    })
