from cadCAD.configuration import Configuration
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from agents import Central
from parameters import Parameters
from simulation_parameters import simulation_parameters


def main():
    c = Central(500, 30)
    params = Parameters(c)
    config = Configuration(initial_state=params.initial_state(),
                           partial_state_update_blocks=params.partial_state_update_blocks,
                           sim_config=simulation_parameters
                           )

    exec_mode = ExecutionMode()
    exec_context = ExecutionContext(exec_mode.single_proc)
    executor = Executor(exec_context, [config])
    executor.execute()

    #raw_result = [d for d in raw_result if d['substep'] == len(partial_state_update_blocks)]


if __name__ == "__main__":
    main()
