import time
from src.fib_logN import fib_logN
from src.fib_N import fib_N
from argparse import ArgumentParser, ArgumentTypeError

def main(n: int, a: str):
    if a == "N":
        start = time.perf_counter_ns()
        res = fib_N(n)
        finish = time.perf_counter_ns()
        print(f"F_{n} = {res}")
        print(f"time: {finish - start} ns")
        return res
    elif a == "logN":
        start = time.perf_counter_ns()
        res = fib_logN(n)
        finish = time.perf_counter_ns()
        print(f"F_{n} = {res}")
        print(f"time: {finish - start} ns")
        return res

def range_type(astr, min=0, max=500):
    value = int(astr)
    if min <= value <= max:
        return value
    else:
        raise ArgumentTypeError(f"n is not in range 0..500")

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-n", type=range_type, help="№ of the required number 0..500")
    parser.add_argument("-a", type=str, choices=("N", "logN"), help="Algorithm")
    parser.add_argument('--test', action='store_true', help='Run tests')

    args = parser.parse_args()

    if args.test and (args.n or args.a):
        parser.error("can't run with both --test and -n or -a")

    if args.test:
        print("TESTS")
    else:
        if args.a is None:
            parser.error(f"-a is required")
        if args.n is None:
            parser.error(f"-n is required")

        if args.a == "N":
            start = time.perf_counter_ns()
            res = fib_N(args.n)
            finish = time.perf_counter_ns()
            print(f"F_{args.n} = {res}")
            print(f"time: {finish - start} ns")
        elif args.a == "logN":
            start = time.perf_counter_ns()
            res = fib_logN(args.n)
            finish = time.perf_counter_ns()
            print(f"F_{args.n} = {res}")
            print(f"time: {finish - start} ns")