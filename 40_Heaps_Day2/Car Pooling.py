"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where
trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and
the locations to pick them up and drop them off are fromi and toi respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return the number of total passengers picked up and dropped off
"""

T = [
    [2,1,4],
    [3,2,6],
    [4,3,5],
    [2,5,8],
    [3,6,9],
    [9,7,10],
    [4,8,11]
]
capacity = 10

from heapq import heappush, heappop


def car_pooling(trips, capacity):
    heap = []
    total_passengers = 0
    available_space = capacity

    for passengers, pickup, drop in trips:
        while heap and heap[0][0] <= pickup:
            _,passenger_count = heappop(heap)
            available_space += passenger_count

        if passengers <= available_space:
            heappush(heap, (drop, passengers))
            available_space -= passengers
            total_passengers += passengers
        else:
            heappush(heap, (drop , available_space))
            total_passengers += available_space
            available_space = 0

    return total_passengers

print("total passenger count : ", car_pooling(T, 10))




