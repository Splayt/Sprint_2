class PointsForPlace:
    
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        else:
            return 101 - place



class PointsForMeters:
    
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        else:
            return meters * 0.5



class TotalPoints(PointsForPlace, PointsForMeters):
    
    def get_total_points(self, meters, place):
        points_place = self.get_points_for_place(place)
        points_meters = self.get_points_for_meters(meters)
        self.total = points_place + points_meters
        return self.total



# Примеры использования
print(PointsForPlace.get_points_for_place(10))  # Вызов статического метода

print(PointsForMeters.get_points_for_meters(10))  # Вызов статического метода

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
