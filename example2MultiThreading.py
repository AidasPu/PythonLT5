import threading
import time

def process_toll_booth(car):
    print(f"processign {car}")
    time.sleep(2)
    print(f"finished processing {car}")

def do_threading():
    cars = ['toyota', 'kamaz', 'audi', 'toyota', 'kamaz', 'audi', 'toyota', 'kamaz', 'audi', 'toyota', 'kamaz', 'audi',
            'toyota', 'kamaz', 'audi', 'toyota', 'kamaz', 'audi']
    threads = []

    start_time = time.time()
    for car in cars:
        new_thread = threading.Thread(target=process_toll_booth, args=[car])
        threads.append(new_thread)
        new_thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time() - start_time
    print(f"it took {end_time} to process all cars")


do_threading()

cars = ['toyota', 'kamaz', 'audi']
for car in cars:
    tuple_example = [car]
    print(tuple_example)


# def example(kintamasis1, kintamasis2):
#     print(kintamasis1 + kintamasis2)
#
# def exampleargs(*args):
#     print(args[0] + args[1])
#     print(args[3])
#
# def examplekwargs(**kwargs):
#     print(kwargs['pirmas_kintamasis'] + kwargs['antras_kintamasis'])
#
# example(5,5)
# exampleargs(5,5)
# examplekwargs(pirmas_kintamasis=5, antras_kintamasis=5)
