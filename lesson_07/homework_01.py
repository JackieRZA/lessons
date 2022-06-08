"""Используя условие первой задачи из урока, проверить то же самое только для коней."""

def is_figures_beat_each_other(x1, y1, x2, y2):
    if abs(x1-x2) == 1 and abs(y1-y2) == 2 or abs(x1-x2) == 2 and abs(y1-y2) == 1:
        return True
    return False

def main():
    x1 = int(input("Enter x1"))
    y1 = int(input("Enter y1"))
    x2 = int(input("Enter x2"))
    y2 = int(input("Enter y2"))

    if is_figures_beat_each_other (x1, y1, x2, y2):
        print ("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()