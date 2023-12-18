import time
from src.fibonacci import fibonacci
from argparse import ArgumentParser
from unittest import TestLoader, TextTestRunner
from src.utils.argparse_custom_types import range_type

def main(n: int, a: str) -> None:
    start = time.perf_counter_ns()
    res = fibonacci(n, a)
    finish = time.perf_counter_ns()
    print(f"F_{n} = {res}")
    print(f"time: {finish - start} ns")


if __name__ == "__main__":
    parser = ArgumentParser(usage="fib.py [-h] -n N -a A | --test")
    group_arguments = parser.add_argument_group("arguments")
    group_tests = parser.add_argument_group("tests")
    group_arguments.add_argument("-n", type=range_type(min_val=0, max_val=500), help="№ of the required number 0..500 of the Fibonacci sequence")
    group_arguments.add_argument("-a", type=str, choices=("N", "LogN"), help="Algorithm (N or logN)")
    group_tests.add_argument("--test", action="store_true", help="Run tests")

    args = parser.parse_args()

    if args.test and (args.n or args.a):
        parser.error("Can't run with both --test and -n or -a")

    if args.test:
        loader = TestLoader()
        tests = loader.discover("tests")
        runner = TextTestRunner()
        result = runner.run(tests)
    else:
        if args.a is None:
            parser.error(f"-a is required")
        if args.n is None:
            parser.error(f"-n is required")

        main(args.n, args.a)