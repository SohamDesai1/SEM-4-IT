from functools import lru_cache
import time

@lru_cache(maxsize=2)
def work(n):
    time.sleep(n)
    print(n)

if __name__ == '__main__':
    print("Starting")
    work(3)
    print("calling again")
    work(3)
    print("called again")
    