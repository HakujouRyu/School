income = int(input("Please enter your income: "))
tier1 = int(0)
tier2 = int(0)
tier3 = int(0)
tier4 = int(0)
tier5 = int(0)
tax1 = float(0.05)
tax2 = float(0.1)
tax3 = float(0.15)
tax4 = float(0.25)
tax5 = float(0.35)
if income >= 900000:
    tier1 = 50000
    tier2 = 200000
    tier3 = 400000
    tier4 = 900000
    tier5 = (income - tier4)
    taxBracket = "Tier 5"
elif income < 900000:
    if income >= 400000:
        tier1 = 50000
        tier2 = 200000
        tier3 = 400000
        tier4 = (income - tier3)
        taxBracket = "Tier 4"
    elif income < 400000:
        if income >= 200000:
            tier1 = 50000
            tier2 = 200000
            tier3 = (income - tier2)
            taxBracket = "Tier 3"
        elif income < 200000:
            if income >= 50000:
                tier1 = 50000
                tier2 = (income - tier1)
                taxBracket = "Tier 2"
            elif income < 50000:
                taxBracket = "Tier 1"
                tier1 = income
totalTax = ((tier1 * tax1) + (tier2 * tax2) + (tier3 + tax3) + (tier4 * tax4) + (tier5 * tax5))
print(taxBracket)
print(totalTax)