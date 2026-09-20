class Portfolio():
    def __init__(self,balance):
        self.balance = balance
        self.btc = 0
        self.trades = []
        
    def buy(self,price , amount):
        if price * amount <= self.balance:
            self.balance-=price*amount
            self.btc+=amount
            print("Bought" ,round(amount,2), "BTC for $",round(price*amount,2))
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
            print("Sold" ,round(amount,2), "BTC for $",round((price*amount),2))
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
    def total_value(self, price,):
        return self.balance+(self.btc*price)

    def sma(self,price,period):
        return sum(price[-period:])/period

    def signal(self,price):
        if self.sma(price,3)>self.sma(price,5):return "Buy"
        if self.sma(price,3)<self.sma(price,5):return "Sell"
        else: return "Hold"
        
    def trade(self, price):
        signal = self.signal(price)

        if signal == 'Buy' and self.btc == 0:
            amount = self.balance / price[-1]
            if amount > 0:
                self.buy(price[-1], amount)

        elif signal == 'Sell' and self.btc > 0:
            self.sell(price[-1], self.btc)
                
    def profit(self, begin_balance, price):
        final_value = self.balance + self.btc * price

        if final_value > begin_balance:
            print("Gain:",final_value - begin_balance, "$ /", ((final_value - begin_balance) / begin_balance) * 100,"%" )

        elif final_value < begin_balance:
            print( "Lose:",round(begin_balance - final_value,2),"$ /",round(((begin_balance - final_value) / begin_balance) * 100,2), "%" )
        else:
            print("No profit, no loss")

    def show_step(self, price):
        sma3 = self.sma(price, 3)
        sma5 = self.sma(price, 5)
        signal = self.signal(price)
        balance=self.balance
        btc=self.btc
        value=self.total_value(price[-1])

        print(
        "  Price:", price[-1],
        "| SMA3:", round(sma3, 2),
        "| SMA5:", round(sma5, 2),
        "| Signal:", signal,
        "| Balance:", round(balance, 2),
        "| BTC:", round(btc, 2),
        "| Value:", round(value, 2)
    )

            
portfolio = Portfolio(1000)
begin_balance=1000
history=[]
price = [100, 102, 98, 105, 110, 108, 115,100,112,134,156,89,90,234,120,112,122,156]

for current_price in price:
    history.append(current_price)
    if len(history)>=5:
        portfolio.show_step(history)
        portfolio.trade(history)
   
portfolio.profit(begin_balance,price[-1])

print(portfolio.balance)
print(portfolio.btc)

