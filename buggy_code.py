def calculate_discount(price, discount_percent):
   
    final_price = price * (1 - discount_percent / 100)
    return final_price


def divide_prices(price1, price2):
    """
    Функция должна делить одну цену на другую.
    """
    return price1 / price2


def get_user_greeting(name):
    """
    Функция должна возвращать приветствие.
    """
    return f"Превет, {name}!"