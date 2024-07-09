import os


CHARACTERS = [*"qwertyuiopasdfghjklzxcvbnm"]
OUTPUT_DIR = "run"
OUTPUT_FILE = "run/test_2.csv"


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_FILE, "w", newline="") as f:
        f.write("name,num,text,text2\n")
        for (i, c) in enumerate(CHARACTERS):
            name = c
            num = i
            text = c * 3
            f.write(f"{name},{num},{text},{text}_suffix\n")


if __name__ == '__main__':
    main()
