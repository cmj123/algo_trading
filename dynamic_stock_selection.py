from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage

def initialize(context):
    # Create and attach an empty Pipeline.
    pipe = Pipeline()
    pipe = attach_pipeline(pipe, name='my_pipeline')

    # Construct Factor
    sma_10 = SimpleMovingAverage(inputs=[USEquityPricing.close],window_length=10)
    sma_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

    # Construct a Filter
    price_under_5 = (sma_10 < 5)

    # Register outputs
    pipe.add(sma_10, 'sma_10')
    pipe.add(sma_30, 'sma_30')

    # Remove rows for which the Filter returns False
    pipe.set_screen(price_under_5)

def before_trading_start(context, data):
    # Access result using the name passed to 'attach_pipeline'
    results = pipeline_output('my_pipeline')
    print results.head(5)
    # Store pipeline results for use by the rest of the algorithms
    context.pipeline_results = results
