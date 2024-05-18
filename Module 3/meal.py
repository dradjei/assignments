def calculateTip(charge):
    tipPercentage = 0.18
    return tipPercentage * charge
def calculateSalesTax(charge):
    salesTaxPercentage = 0.07
    return salesTaxPercentage * charge


if __name__ == "__main__":
    charge = float(input("Enter the charge of the meal purchased $"))
    tax = calculateSalesTax(charge)
    tip = calculateTip(charge)
    print("Tax(7%) of meal purchased: ${:.2f}".format(tax))
    print("Tip(18%) of meal purchased: ${:.2f}".format(tip))
    total_price = charge + tax + tip
    print("Total Amount: ${:.2f}".format(total_price))