import multiprocessing

# Implementuoti skaiciavimus su 4 repeticijom
# formule 8*8*8*8*8


def formule(skaicius):
    for _ in range(10000000):
        result = skaicius * skaicius * skaicius * skaicius * skaicius * skaicius * skaicius
    print(result)


if __name__ == '__main__':
    skaicius = 200
    processes = []
    for _ in range(4):
        processes.append(multiprocessing.Process(target=formule, args=(skaicius,)))
    print(processes)

    for p in processes:
        p.start()

    for p in processes:
        p.join()




