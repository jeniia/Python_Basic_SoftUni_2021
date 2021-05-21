month = str(input())
nights_count = int(input())
if month == "May" or month == "October":
    studio = 50.0
    apartment = 65.0
    if nights_count > 14:
        studio *= 0.70
        apartment *= 0.90
    elif nights_count > 7:
        studio *= 0.95
    price_studio = nights_count * studio
    price_apartment = nights_count * apartment
    print(f"Apartment: {price_apartment:.2f} lv.")
    print(f"Studio: {price_studio:.2f} lv.")
if month == "June" or month == "September":
    studio_js = 75.20
    apartment_js = 68.70
    if nights_count > 14:
        studio_js *= 0.80
        apartment_js *= 0.90
    price_studio_js = nights_count * studio_js
    price_apartment_js = nights_count * apartment_js
    print(f"Apartment: {price_apartment_js:.2f} lv.")
    print(f"Studio: {price_studio_js:.2f} lv.")
if month == "July" or month == "August":
    studio_ja = 76.0
    apartment_ja = 77.0
    if nights_count > 14:
        apartment_ja *= 0.90
    price_studio_ja = nights_count * studio_ja
    price_apartment_ja = nights_count * apartment_ja
    print(f"Apartment: {price_apartment_ja:.2f} lv.")
    print(f"Studio: {price_studio_ja:.2f} lv.")