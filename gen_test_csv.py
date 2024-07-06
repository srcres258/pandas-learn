import os


CHARACTERS = [*"qwertyuiopasdfghjklzxcvbnm"]
OUTPUT_DIR = "run"
OUTPUT_FILE = "run/test.csv"


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_FILE, "w", newline="") as f:
        f.write("name,num,text\n")
        for (i, c) in enumerate(CHARACTERS):
            name = c
            num = i
            text = c * 3
            f.write(f"{name},{num},{text}\n")


if __name__ == '__main__':
    main()
