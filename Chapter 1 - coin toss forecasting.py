# The 3% Signal by Jason Kelly
# Chapter 1 - page 16 - coin toss forecasting

import random
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import locale
locale.setlocale(locale.LC_ALL, '')

def money_format(amt, pos):
    return locale.currency(amt, symbol=True, grouping=True, international=False)

balance = 10000
balances = []             # Declare an empty list ...
balances.append(balance)  # ... and add the beginning balance to it

for i in range(1,51):
    result = random.choice(['H','t'])
    if result == 'H': # heads - Add 5% to balance
        balance = balance + balance * 0.05
        white_circle, = plt.plot(i, balance, 'wo', markersize=10) # plot a white circle to indicate 5% gain
    else:             # tails - Subtract 5% from balance
        balance = balance - balance * 0.05
        red_circle,   = plt.plot(i, balance, 'ro', markersize=10) # plot a red circle to indicate 5% loss
    balances.append(balance)

plt.plot(range(0,51), balances, 'k') # line plt, k=black line

plt.title('Change in $10,000 balance by coin toss.')
plt.xlabel('Coin Toss Number')
plt.ylabel('Balance $')
plt.legend([white_circle, red_circle], ['Heads +5%', 'Tails -5%'], numpoints=1)
plt.gca().axhline(balances[0], color='black') # Darken starting balance line to highlight it
plt.gca().xaxis.grid(True, linestyle='-', which='major', color='grey', alpha=0.5)
plt.gca().yaxis.grid(True, linestyle='-', which='major', color='grey', alpha=0.5)
plt.gca().yaxis.set_major_formatter(FuncFormatter(money_format))
plt.xlim(0, 51)
plt.ylim(min(balances)-1000, max(balances)+1000)

maxbal = max(balances[40:51]) # Display the annotation above the data plots
plt.annotate('Ending balance:%s' % money_format(balances[50],0), 
             xy=(50, balances[50]), 
             xytext=(40, maxbal+500),
             arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.show()