import csv
import os


class CarBase:
    car_type = None

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        try:
            self.carrying = float(carrying)
        except ValueError:
            self.carrying = 0.0

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = "car"
    passenger_seats_count = 0

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self.passenger_seats_count = 0


class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl.count("x") == 2:
            body_lst = body_whl.split(sep="x")
            try:
                body_lst = list(map(float, body_lst))
            except ValueError:
                self.body_length = self.body_width = self.body_height = 0.0
            else:
                self.body_length = body_lst[0]
                self.body_width = body_lst[1]
                self.body_height = body_lst[2]
        else:
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = "spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            elem = row[0].split(";")
            if len(elem) < 7:
                continue
            car_type = elem[0]
            brand = elem[1]
            passenger_seats_count = elem[2]
            photo_file_name = elem[3]
            body_whl = elem[4]
            print(f"body whl = {body_whl}, type {type(body_whl)}")
            carrying = elem[5]
            extra = elem[6]
            if (car_type not in ["car", "truck", "spec_machine"]) or (brand is "") or (carrying is "") or (
                    photo_file_name is ""):
                continue
            try:
                float(carrying)
            except ValueError:
                continue

            if os.path.splitext(photo_file_name)[1] not in ['.jpg', '.jpeg', '.png', '.gif']:
                continue

            if car_type == "car":
                if passenger_seats_count is "":
                    continue
                try:
                    passenger_seats_count = int(passenger_seats_count)
                except ValueError:
                    continue
                tmp_obj = Car(brand, photo_file_name, carrying, passenger_seats_count)
                car_list.append(tmp_obj)
            elif car_type == "truck":
                tmp_obj = Truck(brand, photo_file_name, carrying, body_whl)
                car_list.append(tmp_obj)
            elif car_type == "spec_machine":
                if extra is "":
                    continue
                tmp_obj = SpecMachine(brand, photo_file_name, carrying, extra)
                car_list.append(tmp_obj)
        return car_list


if __name__ == "__main__":
    result = get_car_list("test.csv")
    for elem in result:
        print(f"Car type: {elem.car_type}")
        print(f"Brand: {elem.brand}")
        print(f"Carrying: {elem.carrying}")
        if elem.car_type == "car":
            print(f"Passenger seat count: {elem.passenger_seats_count}")
        elif elem.car_type == "truck":
            print(f"Body whl: {elem.body_width} x {elem.body_height} x {elem.body_length}")
        elif elem.car_type == "spec_machine":
            print(f"Extra: {elem.extra}")
        print(f"Photo: {elem.photo_file_name}")
        print("------------------------")
    print(f"Total units: {len(result)}")
