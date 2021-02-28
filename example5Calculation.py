import time


def count(_from, _to):
    while _from >= _to:
        _from -= 1


def wo_threading_func():
    count(400000, 0)


def with_threading_func():
    import threading

    t1 = threading.Thread(target=count, args=(400000, 200000))
    t2 = threading.Thread(target=count, args=(200000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def calculation_timing():
    start_time_wo_threading = time.time()
    wo_threading_func()
    end_time = time.time() - start_time_wo_threading
    print(end_time)

    start_time_with_threading = time.time()
    with_threading_func()
    end_time = time.time() - start_time_with_threading
    print(end_time)