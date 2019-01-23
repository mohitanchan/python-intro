"""List comprehensions provide a concise way to create lists."""

product_prices = [100, 200, 300, 400, 500]
prices_with_tax = []

print(f"Original Rates: {product_prices}")

# Add 10 to list items to list iems using for loop
for prod in product_prices:
    prices_with_tax.append(prod + 10)

print(f"With For loop : {prices_with_tax}")

# Add 10 to list items to list iems using 'List comprehension'
prices_with_tax_new = [(10 + a) for a in product_prices]
print(f"With List comprehension: {prices_with_tax_new}")
