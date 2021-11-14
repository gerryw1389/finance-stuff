#!/usr/bin/env python3

##################################################
# Replicate https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator
# Example:
# > & "C:/Program Files/Python39/python.exe" c:/scripts/compound_interest_calc.py
# Is it compounded monthly or yearly?y
# Total after 10 years is $15,256.36
##################################################

def main():
    
    initial_investment = 100
    monthly_contribution = 100
    number_years = 10
    annual_interest = 5

    annual_interest = annual_interest / 100
    
    monthly_or_yearly = input("Is it compounded monthly or yearly?")
    if monthly_or_yearly == 'm':
        rate = annual_interest/12
    else:
        rate = annual_interest
    
    if monthly_or_yearly == 'm':
        nper = 12 * number_years
    else:
        nper = number_years
    
    if monthly_or_yearly == 'm':
        pmt = monthly_contribution
    else:
        pmt = 12 * monthly_contribution

    pv = initial_investment
    when = 0
    fv = 0
    
    # per numpy fv formula https://numpy.org/doc/1.17/reference/generated/numpy.fv.html
    val = fv + pv*(1+rate)**nper + pmt*(1 + rate*when)/rate*((1 + rate)**nper - 1)
    currency_string = "${:,.2f}".format(round(val, 2))
    
    if monthly_or_yearly == 'm':
        print(f"Total after {nper/12} years is {currency_string}")
    else:
        print(f"Total after {nper} years is {currency_string}")
    

if __name__ == '__main__':
    main()