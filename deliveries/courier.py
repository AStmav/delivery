class Courier:
    """Класс для представления курьера."""

    def __init__(self, courier_id, point):
        """
        Инициализация курьера.

        Args:
            courier_id (int): ID курьера.
            latitude (float): Широта текущего местоположения курьера.
            longitude (float): Долгота текущего местоположения курьера.
        """
        self.id = courier_id
        self.location = point
