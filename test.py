import random
import string
import datetime

from timeit import timeit, default_timer as timer


NUMBER = 1000

start = timer()
print(f'start perf experiment at {datetime.datetime.now().strftime("%c")}')
print('=' * 20)

# Generating 1M elemenets list
gen_list_time = timeit(
    lambda: [random.randint(1000000, 100000000) for _ in range(1000000)],
    number=NUMBER
)
print(f'generate 1M elements list: {gen_list_time}')


# Generating 1M elemenets tuple
gen_tuple_time = timeit(
    lambda: tuple(random.randint(1000000, 100000000) for _ in range(1000000)),
    number=NUMBER
)
print(f'generate 1M elements tuple: {gen_tuple_time}')


# Generating strings
gen_str_time = timeit(
    lambda: ''.join(random.choice(string.ascii_letters) for _ in range(10)),
    number=NUMBER
)
print(f'generate 10 latters string: {gen_str_time}')
str_ = ''.join(random.choice(string.ascii_letters) for _ in range(10))

gen_str_a_time = timeit(
    lambda: ''.join(random.choice(string.ascii_letters) for _ in range(100)),
    number=NUMBER
)
print(f'generate 100 latters string: {gen_str_a_time}')
str_a = ''.join(random.choice(string.ascii_letters) for _ in range(100))

gen_str_b_time = timeit(
    lambda: ''.join(random.choice(string.ascii_letters) for _ in range(1000)),
    number=NUMBER
)
print(f'generate 1k latters string: {gen_str_b_time}')
str_b = ''.join(random.choice(string.ascii_letters) for _ in range(1000))

gen_str_c_time = timeit(
    lambda: ''.join(random.choice(string.ascii_letters) for _ in range(1000000)),
    number=NUMBER
)
print(f'generate 1M latters string: {gen_str_c_time}')
str_c = ''.join(random.choice(string.ascii_letters) for _ in range(1000000))

# Concat strings
super_str_time = timeit(
    lambda: str_a + str_b + str_c,
    number=NUMBER
)
print(f'concat super string: {super_str_time}')

format_super_str_time = timeit(
    lambda: f'{str_a}{str_b}{str_c}',
    number=NUMBER
)
print(f'concat super string using format: {format_super_str_time}')

print('=' * 20)
print(
    f'finished perf test at {datetime.datetime.now().strftime("%c")}, '
    f'took {timer() - start}'
)
