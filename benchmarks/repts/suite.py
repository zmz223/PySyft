import pyperf
from .bench_constructor import create_bench_constructor
from .bench_serialization import create_bench_rept_serialize
from .bench_deserialization import create_bench_rept_deserialize


def run_rept_suite(runner: pyperf.Runner, rept_dimension: int, rows: int, cols: int, upper_bound: int, lower_bound: int) -> None:
    create_bench_constructor(runner, rept_dimension, rows, cols, upper_bound, lower_bound)
    create_bench_rept_serialize(runner, rept_dimension, rows, cols, upper_bound, lower_bound)
    create_bench_rept_deserialize(runner, rept_dimension, rows, cols, upper_bound, lower_bound)