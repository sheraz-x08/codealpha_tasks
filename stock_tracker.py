prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330, "AMZN": 130}

portfolio = {}
print("Available stocks:", ", ".join(prices))

while True:
    name = input("Stock name (or 'done'): ").upper()
    if name == "DONE":
        break
    if name not in prices:
        print("Stock not found.")
        continue
    try:
        qty = int(input("Quantity: "))
    except ValueError:
        print("Enter a valid number.")
        continue
    portfolio[name] = portfolio.get(name, 0) + qty

total = 0
lines = []
for name, qty in portfolio.items():
    value = prices[name] * qty
    total += value
    lines.append(f"{name}: {qty} x ${prices[name]} = ${value}")

lines.append(f"Total Investment: ${total}")
result = "\n".join(lines)
print("\n" + result)

with open("portfolio.txt", "w") as f:
    f.write(result)
print("Saved to portfolio.txt")
