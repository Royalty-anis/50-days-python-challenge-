def my_discount():
    price = int(input("input price: "))
    discount_in = int(input("input discount: "))
    discount = price * (discount_in / 100)
    total = price - discount
    return total
