import csv
import os


class CarBase:
    car_type = None

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = "car"
    passenger_seats_count = 2

    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying,):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    car_type = "truck"

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl.count("x") == 2:
            body_lst = body_whl.split(sep="x")
            try:
                body_lst = list(map(float, body_lst))
            except ValueError:
                self.body_length = self.body_width = self.body_height = 0
            else:
                self.body_length = body_lst[0]
                self.body_width = body_lst[1]
                self.body_height = body_lst[2]
        else:
            self.body_length = self.body_width = self.body_height = 0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = "spec_machine"
    extra = ""

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            for elem in row:
                elems = elem.split(";")
            if elems[0] == "car":
                tmp_obj = Car(elems[1], elems[2], elems[3], elems[5])
                car_list.append(tmp_obj)

        return car_list


if __name__ == "__main__":
    result = get_car_list("test.csv")
    for elem in result:
        print(elem.car_type)
        print(elem.brand)
        print(elem.passenger_seats_count)
        print(elem.photo_file_name)
        print(elem.carrying)
        print("------------------------")
