def picker(prices):
    dates=[0,0]
    minIndex = None
    minBuy = float('inf')
    maxProfit = float('-inf')
    for i in range(1,len(prices)):
        if prices[i-1] < minBuy:
            minBuy = prices[i-1]
            minIndex = i - 1
        if prices[i] - minBuy > maxProfit:
            maxProfit = prices[i] - minBuy
            dates[1] = i
            dates[0] = minIndex
    return dates
