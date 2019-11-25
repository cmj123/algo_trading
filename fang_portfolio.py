def initialize(context):
    context.fb = sid(42950)
    context.amzn = sid(16841)
    context.nflx = sid(23709)
    context.goog_l = sid(26578)

    context.fang = [sid(42950), sid(16841), sid(23709), sid(26578)]

    # schedule_function(function, date_rule, time_rule, calendar, half_days)
    schedule_function(rebalance,
                     date_rules.week_start(days_offset=2),
                     time_rules.market_open())

    # schedule function
    # schedule_function(trailing,
    #                   date_rules.week_start(days_offset=1),
    #                   time_rules.market_close(hours=0, minutes=30))

    schedule_function(end_rebalance,
                      date_rules.month_end(),
                      time_rules.market_close(hours=0, minutes=30))

def rebalance(context, data):
    order_target_percent(context.fb, 0.25)
    order_target_percent(context.amzn, 0.25)
    order_target_percent(context.nflx, 0.25)
    order_target_percent(context.goog_l, 0.25)

def trailing(context, data):

    # data.history(assets, field, bar_count, frequency)

    historical = data.history(context.fang,
                              fields="price",
                              bar_count=2,
                              frequency="1d")

    print(historical)

def end_rebalance(context, data):
    order_target_percent(context.fb, 0)
    order_target_percent(context.amzn, 0)
    order_target_percent(context.nflx, 0)
    order_target_percent(context.goog_l, 0)

# def handle_data(context, data): # Run minutely during trading day
#     # order_target - # of shares
#     # order_target_value - dollar amount

#     order_target_percent(context.fb, 0.25)
#     order_target_percent(context.amzn, 0.25)
#     order_target_percent(context.nflx, 0.25)
#     order_target_percent(context.goog_l, 0.25)
