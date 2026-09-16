# Return the rounded rate to 4 decimal places
def round_rate(rate):
    rate = round(rate,4)
    return rate    

# Return the inverse rate rounded to 4 decimal places
def reverse_rate(rate):
    if rate == 0:
        return 0
    else:
        rate = round(1/rate, 4)
        return rate    

# Return the formatted output with the conversion rate, converted amount and inverse rate
def format_output(date, from_currency, to_currency, rate, amount):
    converted_amount = round(amount * rate, 2)
    inverse_rate = reverse_rate(rate)
    output = f"The conversion rate on {date} from {from_currency} to {to_currency} was:\n {rate}\n"
    output += f"So {amount} in {from_currency} correspond to: \n {converted_amount} {to_currency}\n"
    output += f"The inverse rate was:\n {inverse_rate}\n"
    return output