# Basic indicators
This is an example application on how to create and use an indicator.

## Approach
The approach was simple. Look for the documentation in the internet and learn :)

Well, first I needed a sample, so the first thing was to connect to an exchange server (Binance sounded good). After having some data with hardcoded parameters, started to sketch the RSI calculation, using pandas.

After having that roughly working, went though the service configuration to make it more flexible. Also added the capability to connect to different servers (just for fun).

When all seemed to work, I began testing the RSI function. To do so, I found the pandas_ta library, which helped a lot in the testing and refactoring (along with some good information with data I found online).

In the end, testing the parameterization of the service and code clean up, adding the plot functionality seemed a nice idea.


## About the configuration
The approach to that configuration style it's because it's really easy to use in python. Other configuration styles would increase slightly the difficulty in that part.

## Additions
- Plot
- Multiple server support

## Other ideas
- Generate artifacts that signal position entries and exits
- Mark the position entries and exits with the Closed P&L result
- Detect divergencies between the price and the rsi movement
- Make test suite
- Remove 'spec' dependency from config.py
