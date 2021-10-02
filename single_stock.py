import quantstats as qs

qs.extend_pandas()

stock = qs.utils.download_returns('FB')

sharpe_ratio = qs.stats.sharpe(stock)
print(sharpe_ratio)

print(stock)
print(stock.cagr())
print(stock.monthly_returns())
print(stock.max_drawdown())
print([f for f in dir(stock) if f[0] != '_'])

stock.plot_earnings(savefig='output/fb_earnings.png', start_balance=100000)

stock.plot_monthly_heatmap(savefig='output/fb_monthly_heatmap.png')