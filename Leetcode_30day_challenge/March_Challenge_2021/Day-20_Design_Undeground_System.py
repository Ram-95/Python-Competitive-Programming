class UndergroundSystem:

    def __init__(self):
        # Stores the Station_name and checkin time of a passenger
        # {id: (stationname, time)}
        self.check_in = {}
        # Stores the {(startStation, endStation): [duration_time, total_journeys]}. Used in calculating the average
        self.time = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in:
            # Start Station
            A = self.check_in[id][0]
			# Board Time
            board_time = self.check_in[id][1]
			# If the pair of stations is already present then add the current duration to prev duration and also
			# prev_count + 1
            if (A, stationName) not in self.time:
                self.time[(A, stationName)] = [t - board_time, 1]
            else:
                self.time[(A, stationName)][0] += t - board_time
                self.time[(A, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(self.time[(startStation, endStation)][0]/self.time[(startStation, endStation)][1])
