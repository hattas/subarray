# Max Subarray Stock Analysis
Analyzing historical stock market data using the divide and conquer maximum subarray algorithm from chapter 4 of [Introduction to Algorithms](https://en.wikipedia.org/wiki/Introduction_to_Algorithms)

Project for COEN 4650 Introduction to Algorithms, Spring 2019

### Contributors
* [Kevin Brosam](https://github.com/KevinBrosam)
* [John Hattas](https://github.com/hattas)
* [Nathan Lang](https://github.com/Nathanlang14)

### Data
The [alpha_vantage](https://pypi.org/project/alpha_vantage/) Python package is used for getting historical stock data.<br>
You must have an Alpha Vantage API key in key.txt. Get one [here](https://www.alphavantage.co/support/#api-key).

### Files
use `from <file> import *` to use functions inside the files

**[algs.py](algs.py)**: Functions to compute max subarray<br>
**[data.py](data.py)**: Functions for getting and processing stock data<br>
**[download_data.py](download_data.py)** Script to download full stock history of S&P 500 companies.  Only needs to be run once.

### Deliverables
Item | Due
-- | --
Proposal | Feb 11, 2019 11:59 PM
Prototype Report | Mar 28, 2019 11:59 PM
Poster | May 1, 2019 11:59 PM

## Proposal

### Proposal Timeline
Task | Date | Done
-- | -- | --
get stock data | 2/15 | :white_check_mark:
implement max sub alg | 2/22 | :white_check_mark:
use alg with stock data | 3/1 | :white_check_mark:
add date ranges and max subarray length | 3/8 | :white_check_mark:
implement multiple buys and sells | 3/22 | :white_check_mark:
graphing (highlight hold period) | 3/29 | :white_check_mark:
performance metrics | 4/12 | :white_check_mark:
analysis on stock market history/fun facts | 4/19 | :white_check_mark:
Compile results and prepare project poster | 5/3 | :white_check_mark:

