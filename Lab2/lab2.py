import csv
from collections import defaultdict

class Booking:
    def __init__(self, t_id, t_name, source_station, dest_station, totalseats):
        self.t_id = t_id
        self.t_name = t_name
        self.source_station = source_station
        self.dest_station = dest_station
        self.totalseats = totalseats
        self.booked_seats = 0  

    def available_seats(self):
        return self.totalseats - self.booked_seats

    def book_seats(self, number):
        if self.available_seats() >= number:
            self.booked_seats += number
            return True
        return False

class Passenger:
    def __init__(self, name, train_id, num_tickets):
        self.name = name
        self.train_id = train_id
        self.num_tickets = num_tickets

def read_train_data(filename):
    bookings = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            t_id, t_name, source_station, dest_station, totalseats = row
            bookings[t_id] = Booking(t_id, t_name, source_station, dest_station, int(totalseats))
    return bookings

def read_passenger_data(filename):
    passengers = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            name, train_id, num_tickets = row
            passengers.append(Passenger(name, train_id, int(num_tickets)))
    return passengers

def process_bookings(bookings, passengers):
    revenue = defaultdict(int)
    fare_per_ticket = 100  
    for passenger in passengers:
        if passenger.train_id not in bookings:
            print(f"Error: Train ID {passenger.train_id} not found for passenger {passenger.name}.")
            continue
        
        train = bookings[passenger.train_id]
        if train.book_seats(passenger.num_tickets):
            total_fare = passenger.num_tickets * fare_per_ticket
            revenue[passenger.train_id] += total_fare
            print(f"Booking confirmed for {passenger.name} on {train.t_name}. Total fare: {total_fare}")
        else:
            print(f"Error: Not enough seats available for passenger {passenger.name} on train {train.t_name}.")

    return revenue

def generate_reports(bookings, revenue):
    print("\nTrain Details Report:")
    for train in bookings.values():
        print(f"Train: {train.t_name}, Source: {train.source_station}, Destination: {train.dest_station}, Available Seats: {train.available_seats()}")

    print("\nRevenue Report:")
    for train_id, total_revenue in revenue.items():
        print(f"Train ID: {train_id}, Total Revenue: {total_revenue}")

if __name__ == "__main__":
    bookings = read_train_data("trains.csv")
    passengers = read_passenger_data("passengers.csv")
    
    revenue = process_bookings(bookings, passengers)
    generate_reports(bookings, revenue)
