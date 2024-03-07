from geopy.distance import geodesic
from deliveries.courier import Courier
from deliveries.order import Order
import argparse

def add_courier(couriers, courier_id, point):
    """
    Добавляем нового курьера в список курьеров.

    Args:
        couriers (list): Список курьеров.
        courier_id (int): Идентификатор курьера.
        point (tuple): Координаты текущего местоположения курьера.
    """
    courier = Courier(courier_id, point)
    couriers.append(courier)
    print(f"Courier {courier_id} added successfully.")
    print(f"Current couriers: {couriers}")

def add_order(orders, point_A, point_B, price):
    """
    Добавление нового заказа в список заказов.

    Args:
        orders (list): Список заказов.
        point_A (tuple): Координаты точки А (откуда).
        point_B (tuple): Координаты точки Б (куда).
        price (float): Цена заказа.

    """
    order = Order(point_A, point_B, price)
    orders.append(order)
    print("Order added successfully.")

def assign_order(couriers, orders):
    """
    Назначение заказа курьеру с наименьшим расстоянием до точки А заказа.

    Args:
        couriers (list): Список курьеров.
        orders (list): Список заказов.
    """
    for order in orders:
        if not couriers:
            print("No available couriers to assign the order.")
            return

        distances = []  # Создаем список для хранения расстояний от каждого курьера до точки А заказа
        for courier in couriers:
            # Вычисляем расстояние от текущего курьера до точки А заказа и добавляем его в список distances
            distance = geodesic(courier.location, order.point_A).miles
            distances.append(distance)

        # Находим минимальное расстояние из списка distances
        min_distance = min(distances)

        # Находим индекс курьера с минимальным расстоянием
        closest_courier_index = distances.index(min_distance)

        # Получаем самого ближайшего курьера по индексу
        closest_courier = couriers[closest_courier_index]

        # Выводим информацию о назначенном курьере и расстоянии до точки А заказа
        print(f"Order assigned to courier {closest_courier.id}, distance: {min_distance} kilometers")
        print(f"Order location: {order.point_A}")

        # Удаляем назначенного курьера из списка, чтобы он больше не участвовал в назначении заказов
        del couriers[closest_courier_index]

def main():
    couriers = []
    orders = []

    parser = argparse.ArgumentParser(description="Courier assignment application")
    parser.add_argument("--couriers", nargs="+", metavar=('courier_id', 'point'), help="Add new couriers")
    parser.add_argument("--order", nargs=5, metavar=('point_A_lat', 'point_A_lon', 'point_B_lat', 'point_B_lon', 'price'), help="Add a new order")

    args = parser.parse_args()
    # Добавляем новых курьеров, если они указаны в аргументах
    if args.couriers:
        for i in range(0, len(args.couriers), 2):
            courier_id = int(args.couriers[i])
            point = tuple(map(float, args.couriers[i+1].split()))
            add_courier(couriers, courier_id, point)

    # Добавляем новый заказ, если он указан в аргументах
    if args.order:
        point_A_lat, point_A_lon, point_B_lat, point_B_lon, price = map(float, args.order)
        add_order(orders, (point_A_lat, point_A_lon), (point_B_lat, point_B_lon), price)

    # Назначаем заказы курьерам
    assign_order(couriers, orders)

if __name__ == "__main__":
    main()
