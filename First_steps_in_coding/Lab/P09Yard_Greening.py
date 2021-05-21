yard_kv = float(input())
price_for_yard = yard_kv * 7.61
price_discount = price_for_yard * 0.18
total_final_price = price_for_yard - price_discount
print(f'The final price is: {total_final_price} lv.\nThe discount is: {price_discount} lv.')