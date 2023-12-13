payment_methods = set()

with open('sales.txt') as file:
    for line in file:
        if line.startswith('PAYMENT:'):
            payment = line.split(':')[-1].strip()
            payment_methods.add(payment)

print("Unique Payment Methods:")
for method in payment_methods:
    print(method)

credit_card_variations = {
    'Credit Card',
    'Creditcard'
}

total_credit_card_sales = 0.0

with open('sales.txt') as file:
    for line in file:
        if line.startswith('PAYMENT:'):
            payment = line.split(':')[-1].strip()
            # Check if the payment method is a variation of Credit Card
            if payment in credit_card_variations:
                # Extract the price from the line
                price_line = file.readline()
                price = float(price_line.split(':')[-1].strip())
                total_credit_card_sales += price

# Print total Credit Card sales
print(f"Total Credit Card Sales: £{total_credit_card_sales:.2f}")
