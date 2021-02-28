import time


def process_toll_booth(car):
    print(f"processign {car}")
    time.sleep(2)
    print(f"finished processing {car}")


if __name__ == "__main__":
    cars = ['toyota', 'kamaz', 'audi', 'toyota', 'kamaz', 'audi']
    start_time = time.time()
    print(start_time)
    for car in cars:
        process_toll_booth(car)
    end_time = time.time() - start_time

    print(end_time)
    print(f"it took {end_time} to process all cars")
