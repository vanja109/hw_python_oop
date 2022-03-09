class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0.65
        M_IN_KM = 1000
        return self.action * LEN_STEP / M_IN_KM 
        #pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        result = get_distance() / duration
        return result
        #pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        #print(f'{тип тренировки}. За {duration} Вы преодолели {get_distance()}
        #со ср. скоростью {get_mean_speed()}. Сожжено {get_spent_calories} кал)
        pass


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        (coeff_calorie_1 * get_mean_speed() - coeff_calorie_2) 
        * weight / M_IN_KM * duration
        pass
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        (coeff_calorie_1 * weight + (get_mean_speed**2 // height) 
        * coeff_calorie_2 * weight) * duration
        pass
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
        pass
    
    #super().get_distance   LEN_STEP = 1.38
    #передать в родительский класс длину гребка

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        lenght_pool * count_pool / M_IN_KM / duration
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        (get_mean_speed + coeff_calorie_1) * coeff_calorie_2 * weight
        pass
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
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

