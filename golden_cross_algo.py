# Intialise the function
def initialize(context):

    # Trading Telsa
    context.tsla = sid(39840)

    # Set the schedule function
    schedule_function(rebalance,
                      date_rule = date_rules.every_day(),
                      time_rule = time_rules.market_open(hours=1)
                      )
 
# Defining the rebalance function
def rebalance(context, data):

    history_50 = data.history(
        context.tsla,
        fields='price',
        bar_count=50,
        frequency='1d'

        )

    history_200 = data.history(
        context.tsla,
        fields='price',
        bar_count=200,
        frequency='1d'
        )

    sma_50 = history_50.mean()
    sma_200 = history_200.mean()

    if data.can_trade(context.tsla):
        if sma_50 > sma_200:
            order_target_percent(context.tsla,1)

        elif sma_50 < sma_200:
            order_target_percent(context.tsla,0)


    if sma_50 > sma_200:
        print "Buying"
    elif sma_50 < sma_200:
        print "Selling-Hold"

    record(Fifty_Day_Moving=sma_50, Two_Hundred_Day_Moving=sma_200)
    
