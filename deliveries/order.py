class Order:
    """
    Класс, представляющий заказ.

    Атрибуты:
        point_A (tuple): Координаты точки А (откуда).
        point_B (tuple): Координаты точки Б (куда).
    """
    def __init__(self, point_A, point_B, price):
        """
        Инициализация объекта заказа.

        Args:
            point_A (tuple): Координаты точки А (откуда).
            point_B (tuple): Координаты точки Б (куда).
        """
        self.point_A = point_A
        self.point_B = point_B
        self.price = price

