from rectangle import Rectangle

def main():
    rect = Rectangle(3, 2)
    print(rect)

    circumference = rect.calculate_circumference()
    print(f"Circumference : {circumference} cm")

    area = rect.calculate_area()
    print(f"Area          : {area} cm²")

if __name__ == "__main__":
    main()