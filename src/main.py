from cadCAD.configuration import Configuration
from .initial_conditions import initial_conditions
from .partial_state_update_blocks import partial_state_update_blocks
from .simulation_parameters import simulation_parameters
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor


config = Configuration(initial_state=initial_conditions,
                       partial_state_update_blocks=partial_state_update_blocks,
                       sim_config=simulation_parameters
                       )

exec_mode = ExecutionMode()
exec_context = ExecutionContext(exec_mode.single_proc)
executor = Executor(exec_context, [config])
raw_result, tensor = executor.execute()

raw_result = [d for d in raw_result if d['substep'] == len(partial_state_update_blocks)]
