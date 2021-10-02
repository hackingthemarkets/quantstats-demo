import quantstats as qs

qs.extend_pandas()

stock = qs.utils.download_returns('GLD', period="10y")

qs.reports.html(stock, title='PTL Investments', output='output/gld.html')

qs.reports.html(stock, "SPY", title="GLD vs. SPY", output='output/gld_vs_spy.html')

stock = qs.utils.download_returns('QQQ', period="10y")

qs.reports.html(stock, "SPY", title="QQQ vs. SPY", output='output/qqq_ovs_spy.html')

stock = qs.utils.download_returns('TQQQ', period="10y")

qs.reports.html(stock, "QQQ", title="TQQQ vs. QQQ", output='output/tqqq_vs_qqq.html')

tickers = {
    'FB': 0.2,
    'AAPL': 0.2, 
    'AMZN': 0.2,
    'MSFT': 0.2,
    'GOOG': 0.2 
}

fmaga = portfolio = qs.utils.make_index(tickers)

qs.reports.html(fmaga, "qqq", output="output/fmaga_vs_qqq.html")
