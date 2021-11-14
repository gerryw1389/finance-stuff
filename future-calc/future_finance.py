#!/usr/bin/env python3

##################################################
# Requires tabulate module:
# https://pypi.org/project/tabulate/
# pip install tabulate

# Example:
# > & "C:/Program Files/Python39/python.exe" c:/scripts/future_finance.py


# With these vars:

# yearly_savings = 1200
# yearly_retirement = 1200
# yearly_brokerage = 600
# yearly_crypto = 600

# current_year = 2021
# current_savings = 1000
# current_retirement = 1520
# current_crypto = 240
# current_brokerage = 1000


# retirement_interest = 0.03
# crypto_interest = 0.03
# brokerage_interest = 0.03

# ############################################

# Output will look like:


# +------+------------+------------+------------+------------+------------+-------+
# | Date |  Savings   | Retirement | Brokerage  |   Crypto   |   Total    | Notes |
# +------+------------+------------+------------+------------+------------+-------+
# | 2021 | $1,000.00  | $1,520.00  | $1,000.00  |  $240.00   | $3,760.00  |       |
# | 2022 | $2,200.00  | $2,801.60  | $1,648.00  |  $865.20   | $7,514.80  |       |
# | 2023 | $3,400.00  | $4,121.65  | $2,315.44  | $1,509.16  | $11,346.24 |       |
# | 2024 | $4,600.00  | $5,481.30  | $3,002.90  | $2,172.43  | $15,256.63 |       |
# | 2025 | $5,800.00  | $6,881.74  | $3,710.99  | $2,855.60  | $19,248.33 |       |
# | 2026 | $7,000.00  | $8,324.19  | $4,440.32  | $3,559.27  | $23,323.78 |       |
# | 2027 | $8,200.00  | $9,809.91  | $5,191.53  | $4,284.05  | $27,485.49 |       |
# | 2028 | $9,400.00  | $11,340.21 | $5,965.28  | $5,030.57  | $31,736.06 |       |
# | 2029 | $10,600.00 | $12,916.42 | $6,762.23  | $5,799.49  | $36,078.14 |       |
# | 2030 | $11,800.00 | $14,539.91 | $7,583.10  | $6,591.47  | $40,514.48 |       |
# | 2031 | $13,000.00 | $16,212.11 | $8,428.59  | $7,407.22  | $45,047.92 |       |
# | 2032 | $14,200.00 | $17,934.47 | $9,299.45  | $8,247.43  | $49,681.36 |       |
# | 2033 | $15,400.00 | $19,708.51 | $10,196.44 | $9,112.86  | $54,417.80 |       |
# | 2034 | $16,600.00 | $21,535.76 | $11,120.33 | $10,004.24 | $59,260.33 |       |
# | 2035 | $17,800.00 | $23,417.83 | $12,071.94 | $10,922.37 | $64,212.14 |       |
# | 2036 | $19,000.00 | $25,356.37 | $13,052.10 | $11,868.04 | $69,276.51 |       |
# | 2037 | $20,200.00 | $27,353.06 | $14,061.66 | $12,842.08 | $74,456.80 |       |
# | 2038 | $21,400.00 | $29,409.65 | $15,101.51 | $13,845.34 | $79,756.50 |       |
# | 2039 | $22,600.00 | $31,527.94 | $16,172.55 | $14,878.70 | $85,179.20 |       |
# +------+------------+------------+------------+------------+------------+-------+

##################################################



from tabulate import tabulate

# table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
# print(tabulate(table))

# -----  ------  -------------
# Sun    696000     1.9891e+09
# Earth    6371  5973.6
# Moon     1737    73.5
# Mars     3390   641.85
# -----  ------  -------------

# headers = ["Planet","R (km)", "mass (x 10^29 kg)"]
# print(tabulate(table, headers, tablefmt="pretty"))

# +--------+--------+-------------------+
# | Planet | R (km) | mass (x 10^29 kg) |
# +--------+--------+-------------------+
# |  Sun   | 696000 |    1989100000     |
# | Earth  |  6371  |      5973.6       |
# |  Moon  |  1737  |       73.5        |
# |  Mars  |  3390  |      641.85       |
# +--------+--------+-------------------+

yearly_savings = 1200
yearly_retirement = 1200
yearly_brokerage = 600
yearly_crypto = 600

current_year = 2021
current_savings = 1000
current_retirement = 1520
current_crypto = 240
current_brokerage = 1000
current_total = (
    current_savings + current_retirement + current_brokerage + current_crypto
)

####################################################
### Below is simple calculations with no interest:
####################################################
# table = [
#     [
#         current_year,
#         "${:,.2f}".format(round(current_savings, 2)),
#         "${:,.2f}".format(round(current_retirement, 2)),
#         "${:,.2f}".format(round(current_brokerage, 2)),
#         "${:,.2f}".format(round(current_crypto, 2)),
#         "${:,.2f}".format(round(current_total, 2)),
#     ],
# ]

# for r in range(2022, 2040):
#     current_year = r
#     current_savings = current_savings + yearly_savings
#     current_retirement = current_retirement + yearly_retirement
#     current_crypto = current_crypto + yearly_crypto
#     current_brokerage = current_brokerage + yearly_brokerage
#     current_total = (
#         current_savings + current_retirement + current_brokerage + current_crypto
#     )

#     table.append(
#         [
#             current_year,
#             "${:,.2f}".format(round(current_savings, 2)),
#             "${:,.2f}".format(round(current_retirement, 2)),
#             "${:,.2f}".format(round(current_brokerage, 2)),
#             "${:,.2f}".format(round(current_crypto, 2)),
#             "${:,.2f}".format(round(current_total, 2)),
#         ]
#     )

# headers = ["Date", "Savings", "Retirement", "Brokerage", "Crypto", "Total"]
# print(tabulate(table, headers, tablefmt="pretty"))

####################################################
## Below is a flat interest for each investment type
####################################################
# interest = .04

# table = [
#     [
#         current_year,
#         "${:,.2f}".format(round(current_savings, 2)),
#         "${:,.2f}".format(round(current_retirement, 2)),
#         "${:,.2f}".format(round(current_brokerage, 2)),
#         "${:,.2f}".format(round(current_crypto, 2)),
#         "${:,.2f}".format(round(current_total, 2)),
#     ],
# ]

# for r in range(2022, 2040):
#     current_year = r
#     current_savings = current_savings + yearly_savings
#     current_retirement = ((current_retirement + yearly_retirement)*interest)+current_retirement + yearly_retirement
#     current_crypto = ((current_crypto + yearly_crypto)*interest)+current_crypto + yearly_crypto
#     current_brokerage = ((current_brokerage + yearly_brokerage)*interest)+current_brokerage + yearly_brokerage
#     current_total = (
#         current_savings + current_retirement + current_brokerage + current_crypto
#     )

#     table.append(
#         [
#             current_year,
#             "${:,.2f}".format(round(current_savings, 2)),
#             "${:,.2f}".format(round(current_retirement, 2)),
#             "${:,.2f}".format(round(current_brokerage, 2)),
#             "${:,.2f}".format(round(current_crypto, 2)),
#             "${:,.2f}".format(round(current_total, 2)),
#         ]
#     )

# headers = ["Date", "Savings", "Retirement", "Brokerage", "Crypto", "Total"]
# print(tabulate(table, headers, tablefmt="pretty"))
####################################################

### Finally, interest for each investment type and add in some custom notes

retirement_interest = 0.03
crypto_interest = 0.03
brokerage_interest = 0.03

savings_target = 35000
millionair = 1000000

table = [
    [
        current_year,
        "${:,.2f}".format(round(current_savings, 2)),
        "${:,.2f}".format(round(current_retirement, 2)),
        "${:,.2f}".format(round(current_brokerage, 2)),
        "${:,.2f}".format(round(current_crypto, 2)),
        "${:,.2f}".format(round(current_total, 2)),
    ],
]

for r in range(2022, 2040):
    current_year = r
    current_savings = current_savings + yearly_savings
    current_retirement = (
        ((current_retirement + yearly_retirement) * retirement_interest)
        + current_retirement
        + yearly_retirement
    )
    current_crypto = (
        ((current_crypto + yearly_crypto) * crypto_interest)
        + current_crypto
        + yearly_crypto
    )
    current_brokerage = (
        ((current_brokerage + yearly_brokerage) * brokerage_interest)
        + current_brokerage
        + yearly_brokerage
    )
    current_total = (
        current_savings + current_retirement + current_brokerage + current_crypto
    )

    notes = ""
    if current_savings >= savings_target:
        notes = "Savings requirement met"

    if current_total >= millionair:
        if notes:
            notes = notes + "; Over one million saved!"
        else:
            notes = "Over one million saved!"

    table.append(
        [
            current_year,
            "${:,.2f}".format(round(current_savings, 2)),
            "${:,.2f}".format(round(current_retirement, 2)),
            "${:,.2f}".format(round(current_brokerage, 2)),
            "${:,.2f}".format(round(current_crypto, 2)),
            "${:,.2f}".format(round(current_total, 2)),
            notes,
        ],
    )

headers = ["Date", "Savings", "Retirement", "Brokerage", "Crypto", "Total", "Notes"]
print(tabulate(table, headers, tablefmt="pretty"))
