partial_state_update_blocks = [
    { # Maintenance if needed
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'maintenance': maintenance
        },
        'variables': { # The following state variables will be updated simultaneously
            'maintenance_cost': set_maintenance_cost,
        }
    },
    { # Get energy available to be used in this timestep
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'solartainer_produce': solartainer_produce
        },
        'variables': { # The following state variables will be updated simultaneously
            'energy_prod': set_energy_prod,
            'energy_appetite': set_energy_appetite,
            'energy_cons': set_energy_cons,
            'energy_prod': increment_energy_prod,
            'annual_var': update_annual_var,
            'daily_mult': update_daily_mult,
            'price_per_kwh': update_price_per_kwh,
            'energy_revenue': set_energy_revenue,
            'op_cost': set_op_cost
        }
    },
    { # Get priority users usage (Tier 1 users)
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'userGroup_priority': userGroup_priority
        },
        'variables': user_variables
    },
    { # Get business users usage (Tier 2 users)
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'userGroup_business': userGroup_business
        },
        'variables': user_variables
    },
    { # Get leisure users usage (Tier 3 users)
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'userGroup_leisure': userGroup_leisure
        },
        'variables': user_variables
    },
    { # Get battery usage (Tier 4)
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'battery_tracker': battery_tracker,
        },
        'variables': { # The following state variables will be updated simultaneously
            'energy_cons': increment_energy_cons,
            'op_cost': increment_op_cost,
            'bat_level': increment_bat_level,
            'hour': increment_hour
        }
    },
    { # Operate on ownership
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'ownership_dynamics': ownership_dynamics,
        },
        'variables': { # The following state variables will be updated simultaneously
            'ownership': update_ownership
        }
    }
]