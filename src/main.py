from cadCAD.configuration import Configuration
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from agents import Central
from parameters import Parameters
from simulation_parameters import simulation_parameters
from plot_results import plot_results


def main():
    c = Central(300)
    params = Parameters(c)
    config = Configuration(initial_state=params.initial_state(),
                           partial_state_update_blocks=params.partial_state_update_blocks,
                           sim_config=simulation_parameters
                           )

    exec_mode = ExecutionMode()
    exec_context = ExecutionContext(exec_mode.single_proc)
    executor = Executor(exec_context, [config])
    raw_result, tensor = executor.execute()
    raw_result = [d for d in raw_result]
    plot_results(raw_result)


if __name__ == "__main__":
    main()
