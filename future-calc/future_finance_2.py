#!/usr/bin/env python3

##################################################
# Requires tabulate module:
# https://pypi.org/project/tabulate/
# pip install tabulate

# Example:
# > & "C:/Program Files/Python39/python.exe" c:/scripts/future_finance_2.py
# Total after 10 years is $15,256.36

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


# +------+------------+------------+------------+------------+-------------+-------------------------+
# | Date |  Savings   | Retirement | Brokerage  |   Crypto   |    Total    |          Notes          |
# +------+------------+------------+------------+------------+-------------+-------------------------+
# | 2021 | $1,000.00  | $1,520.00  | $1,000.00  |  $240.00   |  $3,760.00  |                         |
# | 2022 | $2,200.00  | $2,801.60  | $1,648.00  |  $865.20   |  $7,514.80  |                         |
# | 2023 | $3,400.00  | $4,121.65  | $2,315.44  | $1,509.16  | $11,346.24  |                         |
# | 2024 | $4,600.00  | $5,481.30  | $3,002.90  | $2,172.43  | $15,256.63  |                         |
# | 2025 | $5,800.00  | $6,881.74  | $3,710.99  | $2,855.60  | $19,248.33  |                         |
# | 2026 | $7,000.00  | $8,324.19  | $4,440.32  | $3,559.27  | $23,323.78  |                         |
# | 2027 | $8,200.00  | $9,809.91  | $5,191.53  | $4,284.05  | $27,485.49  |                         |
# | 2028 | $9,400.00  | $11,340.21 | $5,965.28  | $5,030.57  | $31,736.06  |                         |
# | 2029 | $10,600.00 | $12,916.42 | $6,762.23  | $5,799.49  | $36,078.14  |                         |
# | 2030 | $11,800.00 | $14,539.91 | $7,583.10  | $6,591.47  | $40,514.48  |                         |
# | 2031 | $13,000.00 | $16,212.11 | $8,428.59  | $7,407.22  | $45,047.92  |                         |
# | 2032 | $14,200.00 | $17,934.47 | $9,299.45  | $8,247.43  | $49,681.36  |                         |
# | 2033 | $15,400.00 | $19,708.51 | $10,196.44 | $9,112.86  | $54,417.80  |                         |
# | 2034 | $16,600.00 | $21,535.76 | $11,120.33 | $10,004.24 | $59,260.33  |                         |
# | 2035 | $17,800.00 | $23,417.83 | $12,071.94 | $10,922.37 | $64,212.14  |                         |
# | 2036 | $19,000.00 | $25,356.37 | $13,052.10 | $11,868.04 | $69,276.51  |                         |
# | 2037 | $20,200.00 | $27,353.06 | $14,061.66 | $12,842.08 | $74,456.80  | Savings requirement met |
# | 2038 | $21,400.00 | $29,409.65 | $15,101.51 | $13,845.34 | $79,756.50  | Savings requirement met |
# | 2039 | $22,600.00 | $31,527.94 | $16,172.55 | $14,878.70 | $85,179.20  | Savings requirement met |
# | 2040 | $23,800.00 | $33,709.78 | $17,275.73 | $15,943.07 | $90,728.58  | Savings requirement met |
# | 2041 | $25,000.00 | $35,957.07 | $18,412.00 | $17,039.36 | $96,408.43  | Savings requirement met |
# | 2042 | $26,200.00 | $38,271.78 | $19,582.36 | $18,168.54 | $102,222.69 | Savings requirement met |
# | 2043 | $27,400.00 | $40,655.94 | $20,787.83 | $19,331.60 | $108,175.37 | Savings requirement met |
# | 2044 | $28,600.00 | $43,111.62 | $22,029.47 | $20,529.54 | $114,270.63 | Savings requirement met |
# | 2045 | $29,800.00 | $45,640.96 | $23,308.35 | $21,763.43 | $120,512.75 | Savings requirement met |
# | 2046 | $31,000.00 | $48,246.19 | $24,625.60 | $23,034.33 | $126,906.13 | Savings requirement met |
# | 2047 | $32,200.00 | $50,929.58 | $25,982.37 | $24,343.36 | $133,455.31 | Savings requirement met |
# | 2048 | $33,400.00 | $53,693.47 | $27,379.84 | $25,691.66 | $140,164.97 | Savings requirement met |
# | 2049 | $34,600.00 | $56,540.27 | $28,819.24 | $27,080.41 | $147,039.92 | Savings requirement met |
# | 2050 | $35,800.00 | $59,472.48 | $30,301.81 | $28,510.83 | $154,085.12 | Savings requirement met |
# | 2051 | $37,000.00 | $62,492.65 | $31,828.87 | $29,984.15 | $161,305.67 | Savings requirement met |
# | 2052 | $38,200.00 | $65,603.43 | $33,401.74 | $31,501.67 | $168,706.84 | Savings requirement met |
# | 2053 | $39,400.00 | $68,807.54 | $35,021.79 | $33,064.72 | $176,294.05 | Savings requirement met |
# | 2054 | $40,600.00 | $72,107.76 | $36,690.44 | $34,674.67 | $184,072.87 | Savings requirement met |
# | 2055 | $41,800.00 | $75,506.99 | $38,409.15 | $36,332.91 | $192,049.05 | Savings requirement met |
# | 2056 | $43,000.00 | $79,008.20 | $40,179.43 | $38,040.89 | $200,228.53 | Savings requirement met |
# | 2057 | $44,200.00 | $82,614.45 | $42,002.81 | $39,800.12 | $208,617.38 | Savings requirement met |
# | 2058 | $45,400.00 | $86,328.88 | $43,880.90 | $41,612.12 | $217,221.90 | Savings requirement met |
# | 2059 | $46,600.00 | $90,154.75 | $45,815.32 | $43,478.49 | $226,048.56 | Savings requirement met |
# +------+------------+------------+------------+------------+-------------+-------------------------+

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

savings_target = 20000
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

for r in range(2022, 2060):
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
