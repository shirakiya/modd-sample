import sys
import time

def get_message(count: int) -> str:
    return f'count: {count}'


def main():
    count = 0
    while True:
        print(get_message(count), file=sys.stderr)
        count += 1
        time.sleep(0.5)


if __name__ == '__main__':
    main()
