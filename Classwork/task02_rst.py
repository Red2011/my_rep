from multiprocessing import Pool
import time, struct, random, hashlib


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def codeer():
    if __name__ == '__main__':
        with Pool(processes=50) as pool:
            print(sum(pool.imap(slow_calculate, range(501))))
            # print(sum(pool.map(slow_calculate, range(501))))


first_time = time.time()
codeer()
print(time.time() - first_time)
