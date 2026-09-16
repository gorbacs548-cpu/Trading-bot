class Portfolio():
    def __init__(self,balance):
        self.balance = balance
        self.btc = 0
        self.trades = []
        
    def buy(self,price , amount):
        if price * amount <= self.balance:
            self.balance-=price*amount
            self.btc+=amount
            print("Bought" ,amount, "BTC for $",(price*amount))
            self.trades.append({
                "type": "BUY",
                "price": price,
                "amount": amount
})
        else: print("BUY FAILED: insufficient balance")
            
    def sell(self,price , amount):
        if amount<=self.btc:
            self.balance+=price*amount
            self.btc-=amount
            print("Sold" ,amount, "BTC for $",(price*amount))
            self.trades.append({
                "type": "SELL",
                "price": price,
                "amount": amount
})
        else: print("SELL FAILED: insufficient BTC")

    def show_trades(self):
        for trade in self.trades:print(
        trade["type"],
        trade["amount"],
        "BTC at $",
        trade["price"]
)
    def total_value(self, price):
        return self.balance+(self.btc*price)
        
            
portfolio = Portfolio(1000)

portfolio.buy(100, 3)
portfolio.sell(120, 1)
portfolio.sell(120, 1)
portfolio.buy(100, 3)
portfolio.buy(100, 3)


print(portfolio.balance)
print(portfolio.btc)
portfolio.show_trades()
print(portfolio.total_value(150))
