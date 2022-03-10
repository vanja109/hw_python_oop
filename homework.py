class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> str:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; Длительность: '
                f'{round(self.duration, 3)} ч.; Дистанция: '
                f'{round(self.distance, 3)} км; Ср. скорость: '
                f'{round(self.speed, 3)} км/ч; Потрачено ккал: '
                f'{round(self.calories, 3)}.')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration * 60       #convert hours to minutes
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0.65
        M_IN_KM = 1000
        result = self.action * LEN_STEP / M_IN_KM
        return result

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        result = self.get_distance() / self.duration
        return result

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        pass


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        result = (
            (coeff_calorie_1 * self.get_mean_speed() - coeff_calorie_2)
            * self.weight / self.M_IN_KM * self.duration)
        return result


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        result = (
            (coeff_calorie_1 * self.weight + (self.get_mean_speed()**2
             // self.height) * coeff_calorie_2 * self.weight) * self.duration)
        return result
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        super().get_distance(self)
        self.LEN_STEP = 1.38

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        result = (
            self.lenght_pool * self.count_pool / self.M_IN_KM / self.duration)
        return result

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        result = (
            (self.get_mean_speed + coeff_calorie_1)
            * coeff_calorie_2 * self.weight)
        return result
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    #dic = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    """
        SWM : [720, 1, 80, 25, 40]
        if ключ словаря == SWM:
            swim = SWM (720, 1, 80, 25, 40)

	    Функция должна определить тип тренировки и создать объект
        соответствующего класса, передав ему на вход параметры,
        полученные во втором аргументе. Этот объект функция должна вернуть."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    """При выполнении функции main()для этого экземпляра должен быть вызван
        метод show_training_info(); результатом выполнения метода должен быть
        объект класса InfoMessage, его нужно сохранить в переменную info.
		Для объекта InfoMessage, сохранённого в переменной info, должен
        быть вызван метод, который вернет строку сообщения с данными о
        тренировке; эту строку нужно передать в функцию print()."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)