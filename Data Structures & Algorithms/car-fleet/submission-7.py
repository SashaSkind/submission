class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr_of_cars = []
        if not position or not speed:
            return 0
        for i, car in enumerate(position):
            arr_of_cars.append((position[i], speed[i]))

        cars = sorted(arr_of_cars, reverse = True)
        stack = []
        for car in cars:
            time = (target - car[0]) / car[1]

            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)

        return len(stack)
