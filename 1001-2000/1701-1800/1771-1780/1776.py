class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        ans = [-1] * len(cars)
        forward_slow_cars = []
        for i in range(len(cars)-1, -1, -1):
            pos, speed = cars[i]
            while len(forward_slow_cars) > 0:
                _pos, _speed, collide_time = forward_slow_cars[-1]
                if speed <= _speed:
                    forward_slow_cars.pop(-1)
                    continue
                if len(forward_slow_cars) > 1 and (_pos - pos) / (speed - _speed) > collide_time:
                    forward_slow_cars.pop(-1)
                    continue
                break

            if len(forward_slow_cars) > 0:
                _pos, _speed, _ = forward_slow_cars[-1]
                ans[i] = (_pos - pos) / (speed - _speed)
            forward_slow_cars.append((pos, speed, ans[i]))

        return ans
