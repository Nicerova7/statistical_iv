class BinningParameters:
    bin_column = 'Bin'
    event_column = 'Event'
    nonevent_column = 'Non-event'
    totals_column = 'Totals'
    one_bin_fail = '(-inf, inf)'
    max_table_one_bin_fail= 4

class OutPut:
    variable_column = 'variable'
    jhat_column = 'Ĵ-Estimate'
    stderror_column = 'Std-error'
    pvalue_column = 'p-value'

class Configuration:
    max_decimals = 6