def rectangle_area(width, length):
    return width * length

def circle_area(radius):
    return 3.14 * radius * radius

def rectangle_volume(width, length, height):
    return width * length * height

def sphere_volume(radius):
    return (4/3) * 3.14 * radius ** 3

while True:
    print("************************************************")
    print("AREA & CUBE")
    print("1. พื้นที่สี่เหลี่ยม 2. พื้นที่วงกลม 3. ปริมาตรทรงสี่เหลี่ยม 4. ปริมาตรทรงกลม 0. ออกจากการทำงาน")
    print("************************************************")

    choice = int(input("เลือกเมนู : "))
    try:
        if choice == 0:
            print("ออกจากการทำงาน")
            break
        elif choice in [1, 2, 3, 4]:
            if choice == 1:
                width = float(input("ป้อนความกว้าง: "))
                length = float(input("ป้อนความยาว: "))
                result = rectangle_area(width, length)
                print(f"พื้นที่สี่เหลี่ยม: {result:.2f}")
            elif choice == 2:
                radius = float(input("ป้อนรัศมี: "))
                result = circle_area(radius)
                print(f"พื้นที่วงกลม: {result:.2f}")
            elif choice == 3:
                width = float(input("ป้อนความกว้าง: "))
                length = float(input("ป้อนความยาว: "))
                height = float(input("ป้อนความสูง: "))
                result = rectangle_volume(width, length, height)
                print(f"ปริมาตรทรงสี่เหลี่ยม: {result:.2f}")
            elif choice == 4:
                radius = float(input("ป้อนรัศมี: "))
                result = sphere_volume(radius)
                print(f"ปริมาตรทรงกลม: {result:.2f}")
        else:
            print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
    except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น")