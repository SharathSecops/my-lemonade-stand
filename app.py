# INSECURE LEMONADE STAND CODE 
password = "sweetlemon123"  # OH NO! Hardcoded password!
lemonade_price = 5

def sell_lemonade(cups):
    total = cups * lemonade_price
    print(f"Sold {cups} cups! Total: ${total}")
    return total

sell_lemonade(10)
