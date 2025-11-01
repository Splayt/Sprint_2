class PointsForPlace:
    def get_points_for_place(self, place):
        self.points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            self.points = 101 - place
        return self.points
class PointsForMeters:
    def get_points_for_meters(self, meters):
        self.points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            self.points = meters * 0.5
        return self.points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        points_place = self.get_points_for_place(place)
        points_meters = self.get_points_for_meters(meters)
        self.total = points_place + points_meters
        return self.total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))