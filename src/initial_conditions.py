initial_conditions = {
    # INITIAL CONDITIONS TO PLAY WITH
    'bat_lim': 25, # max kWh able to be stored in battery
    'price_per_kwh': {'price': price_per_kwh, 'max_price': max_price_per_kwh, 'min_price': 0.0}, # EUR cents
    'maintenance_rate': maintenance_rate, # days between each maintenance call
    # INITIAL CONDITIONS TO LET BE, but no hard rules on that :)
    # initial ownership breakdown
    'ownership': {'solartainer': 1., 'operator': 0., 'priority': 0., 'business': 0., 'leisure': 0., 'maintenance': 0., 'crowdfunders': 0.},
    # total tracking of max values
    'energy_prod': {'available': 0., 'remaining': 0.}, # total energy produced by the system per timestep
    'energy_appetite': {'priority': 0., 'business': 0., 'leisure': 0.}, # amount of energy appetite
    # total tracking of actual usage
    'energy_cons': {'tot': 0, 'prod': 0., 'bat_use': 0., 'priority': 0., 'business': 0., 'leisure': 0., 'bybat': 0}, # total energy consumed
    'energy_revenue': {'tot': 0, 'prod': 0., 'bat_use': 0., 'priority': 0., 'business': 0., 'leisure': 0., 'bybat': 0}, # total energy consumed
    # time tracking
    'hour': 0,
    # track when maintenance occurs (binary)
    'maintenance_cost': {'maintenance_cost': 0, 'maintenance_occured': 0, 'maintenance_cost_per': maintenance_cost_per},
    'op_cost': {'operations': op_cost_per_hour, 'op_cost_per_kwh': op_cost_per_kwh}, # 4 EUR cents per kwh of operations, 10 EUR cents per hour of operations
    # track time-based variances
    'annual_var': {'prod': 0., 'priority': 0., 'business': 0., 'leisure': 0.},
    'daily_mult': {'prod': .8, 'priority': .8, 'business': .8, 'leisure': .8},
    # limited mechanics tracking
    'bat_level': 0, # amount of energy currently stored in the battery
    'production_efficiency': {'value': 1., 'decay': production_decay_rate} # % of production and battery storage usable, decay=0.9999 to start
}