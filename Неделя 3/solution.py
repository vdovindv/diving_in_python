import csv
from os.path import splitext

class CarBase:
    required = []

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate_input(brand)
        self.photo_file_name = self.validate_photo_filename(photo_file_name)
        self.carrying = float(self.validate_input(carrying))

    def validate_input(self, value):
        """метод валидации данных, возвращает значение, если передано не пустое значение,
        иначе выбрасывает исключение ValueError"""
        if value == '':
            raise ValueError
        return value

    def validate_photo_filename(self, filename):
        name, ext = splitext(filename)
        exten = ('.jpg', '.jpeg', '.png', '.gif')

        if name != '' and (ext in exten):
            return filename

        raise ValueError

    def get_photo_file_ext(self):
        _, ext = splitext(self.photo_file_name)
        return ext

    @classmethod
    def create_from_dict(cls, data):
        """создает экземпляр класса из словаря с параметрами"""

        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)


class Car(CarBase):
    required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(self.validate_input(passenger_seats_count))


class Truck(CarBase):
    required = ['brand', 'photo_file_name', 'carrying', 'body_whl']

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length = self.body_width = self.body_height = 0.0
        self.car_type = 'truck'

        try:
            whl = body_whl.split('x')
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])
            assert len(whl) == 3
        except (ValueError, AssertionError):
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    required = ['brand', 'photo_file_name', 'carrying', 'extra']

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = self.validate_input(extra)


def get_car_list(csv_filename):
    car_types = {'car': Car, 'spec_machine': SpecMachine, 'truck': Truck}
    csv.register_dialect('cars', delimiter=';')
    car_list = []

    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file, dialect='cars')
        for row in reader:
            try:
                car_class = car_types[row['car_type']]
                car_list.append(car_class.create_from_dict(row))
            except Exception:
                pass

    return car_list