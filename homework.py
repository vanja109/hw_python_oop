from dataclasses import asdict, dataclass, field
from typing import Dict, List, Type

SWM_TYPE = "SWM"
RUN_TYPE = "RUN"
WLK_TYPE = "WLK"


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE: str = field(
        default=(
            "Тип тренировки: {training_type}; "
            "Длительность: {duration:.3f} ч.; "
            "Дистанция: {distance:.3f} км; "
            "Ср. скорость: {speed:.3f} км/ч; "
            "Потрачено ккал: {calories:.3f}."
        ), init=False
    )

    def get_message(self):
        return self.MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MIN_IN_H: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError()

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    COEFF_CALORIE_MULTIPLIER: int = 18
    COEFF_CALORIE_SUBTRACTER: int = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        return (
            (self.COEFF_CALORIE_MULTIPLIER * self.get_mean_speed()
             - self.COEFF_CALORIE_SUBTRACTER) * self.weight
            / self.M_IN_KM * self.duration * self.MIN_IN_H
        )


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEFF_CALORIE_SUMMAND: float = 0.035
    COEFF_CALORIE_MULTIPLIER: float = 0.029

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

        return (
            (self.COEFF_CALORIE_SUMMAND * self.weight + (self.get_mean_speed()
             ** 2 // self.height) * self.COEFF_CALORIE_MULTIPLIER
             * self.weight) * self.duration * self.MIN_IN_H
        )


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    COEFF_CALORIE_SUMMAND: float = 1.1
    COEFF_CALORIE_MULTIPLIER: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (
            (self.get_mean_speed() + self.COEFF_CALORIE_SUMMAND)
            * self.COEFF_CALORIE_MULTIPLIER * self.weight
        )


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""

    workout_types: Dict[str, Type[Training]] = {
        SWM_TYPE: Swimming,
        RUN_TYPE: Running,
        WLK_TYPE: SportsWalking
    }
    if workout_type not in workout_types.keys():
        raise ValueError("Неверный тип тренировки")
    return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == "__main__":

    packages: List[str, int] = [
        (SWM_TYPE, [720, 1, 80, 25, 40]),
        (RUN_TYPE, [15000, 1, 75]),
        (WLK_TYPE, [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
