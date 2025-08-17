def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_amount = price * (discount_percent / 100)
        result = price - discounted_amount
        return result
    else:
        return price
    
def main():
    original_price=input("Enter the original price of the item")
    discount = input("Enter the discount percentage without percent sign")
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Your final price is -> {final_price}")
    else:
        print(f"No discount was given. The price to pay is -> {original_price}")