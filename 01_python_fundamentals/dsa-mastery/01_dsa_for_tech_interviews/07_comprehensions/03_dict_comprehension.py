tea_prices_inr={
    "Masala Chai":40,
    "Black Tea":23.99,
    "Lemon Tea":45.99
}

tea_prices_usd={tea:price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)