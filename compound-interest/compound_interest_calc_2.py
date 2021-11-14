#!/usr/bin/env python3

##################################################
# Replicate https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator
# > & "C:/Program Files/Python39/python.exe" c:/scripts/compound_interest_calc_2.py
# Total after 10 years is $15,256.36
##################################################

def future_val(fv, pv, pmt, nper, rate, when):
    val = fv + pv*(1+rate)**nper + pmt*(1 + rate*when)/rate*((1 + rate)**nper - 1)
    return val

def main():
    
    initial_investment = 100
    monthly_contribution = 100
    number_years = 10
    annual_interest = 5
    compounds = "annually" # only assumes monthly if not annually

    if compounds == "annually":
        annual_interest = annual_interest / 100
        rate = annual_interest
        nper = number_years
        pmt = 12 * monthly_contribution
        pv = initial_investment
        when = 0
        fv = 0
        # per numpy fv formula https://numpy.org/doc/1.17/reference/generated/numpy.fv.html
        return_val = future_val(fv, pv, pmt, nper, rate, when)
        currency_string = "${:,.2f}".format(round(return_val, 2))
        print(f"Total after {round(nper)} years is {currency_string}")
    else:
        annual_interest = annual_interest / 100
        rate = annual_interest/12
        nper = 12 * number_years
        pmt = monthly_contribution
        pv = initial_investment
        when = 0
        fv = 0
        # per numpy fv formula https://numpy.org/doc/1.17/reference/generated/numpy.fv.html
        return_val = future_val(fv, pv, pmt, nper, rate, when)
        currency_string = "${:,.2f}".format(round(return_val, 2))
        print(f"Total after {round(nper/12)} years is {currency_string}")

if __name__ == '__main__':
    main()