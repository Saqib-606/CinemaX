cinema_name = "Nuplex"

class Cinema : # Foundation / Root Class 
    def __init__(self) :
        self.name = cinema_name
        print ("\n" + "="*70)
        print (f"        🎬 WELCOME TO {self.name.upper()} CINEMA 🎬")
        print ("="*70)
        self.movies = []  
        self.shows = []

    def add_movie (self, movie) : 
        self.movies.append (movie)

    def add_show (self, show) :
        self.shows.append (show)

    def show_movies (self) :
        print (f"\n🎥 NOW SHOWING AT {self.name.upper()} CINEMA")
        print ("-"*50)
        for movie in self.movies :
            movie.show_info ()

class Movie : # Independent Class
    def __init__(self, title, duration) :
        self.title = title
        self.duration = duration

    def show_info (self) :
        print (f"🎞️  {self.title}  ({self.duration} mins)")

class Show : 
    def __init__(self, movie, show_time, show_date, hall_number,standard_price, vip_price, rows, cols) :
        self.movie = movie  
        self.show_time = show_time
        self.show_date = show_date
        self.hall_number = hall_number
        self.standard_price = standard_price
        self.vip_price = vip_price

        self.seat_matrix = SeatMatrix (rows, cols)  
    
    def show_details (self) :
        print ("\n" + "-"*40)
        print ("🎟️  SHOW DETAILS")
        print ("-"*40)
        print ("\nShow Details:")
        print (f"Movie        : {self.movie.title}")
        print (f"Date         : {self.show_date}")
        print (f"Time         : {self.show_time}")
        print (f"Hall Number  : {self.hall_number}")
        print (f"Standard Fee : PKR {self.standard_price}")
        print (f"VIP Fee      : PKR {self.vip_price}")

class SeatMatrix : # Independent Class
    def __init__(self, rows, cols) :
        self.rows = rows  
        self.cols = cols  

        self.seats = []

        for r in range (rows) : 
            row = []
            for c in range (cols) : 
                row.append (0)  # 0 = empty
            self.seats.append (row)

    def display_seats (self) :
        print ("\n🪑 SEAT LAYOUT")
        print ("0 = Available | 1 = Booked")
        print ("-"*30)
        for row in self.seats :
            for seat in row :
                print (seat, end=" ")
            print ()  # New Line After One Row

    def is_seat_avaliable (self, row, col) :
        return self.seats [row] [col] == 0

    def book_seat (self, row, col) :
        if self.is_seat_avaliable (row, col) :
            self.seats [row] [col] = 1
            print ("✅ Seat booked successfully.")
        else :
            print ("❌ This seat is already booked. Please select another seat.")

    def is_housefull (self) :
        for row in self.seats :
            if 0 in row :
                return False 
        return True  

class VIPSeat (SeatMatrix) : # Inheritance
    def __init__(self, rows, cols, vip_rows=1):  # (default = front 1 row)
        super().__init__(rows, cols)  # Parent Class Constructor Call
        self.vip_rows = vip_rows

    def is_vip_seat (self, row) :   
        return row < self.vip_rows  
    
    def book_seat (self, row, col, is_vip_booking=False) : # Method (Override)
        if not self.is_seat_avaliable (row, col) :
            print ("⚠️  This is a VIP seat. VIP booking is required.")
            return
        
        if self.is_vip_seat (row) :
            if not is_vip_booking :
                print ("⚠️  This is a VIP seat. VIP booking is required.")
                return
            else :
                self.seats [row] [col] = 1
                print ("🌟 VIP seat booked successfully!")
        else : 
            self.seats [row] [col] = 1
            print ("Standard Seat Booked Successfylly!")

class Ticket : 
    ticket_counter = 1  # Class variable 

    def __init__(self, show, row, col, seat_type, price) :
        self.ticket_id = Ticket.ticket_counter # Generate Unique Ticket Id
        Ticket.ticket_counter += 1
        
        self.show = show   
        self.row = row    
        self.col = col    
        self.seat_type = seat_type  
        self.price = price  

    def show_ticket (self) :
        print ("\n" + "="*35)
        print ("🎫 CINEMA TICKET")
        print ("="*35)
        print (f"Ticket ID   : {self.ticket_id}")
        print (f"Movie       : {self.show.movie.title}")
        print (f"Date        : {self.show.show_date}")
        print (f"Time        : {self.show.show_time}")
        print (f"Hall        : {self.show.hall_number}")
        print (f"Seat        : Row {self.row + 1}, Col {self.col + 1}") # 1-based Indexing
        print (f"Seat Type   : {self.seat_type}")
        print (f"Price       : {self.price}")
        print ("="*35)
        print ("🙏 Thank you for choosing NUPLEX Cinema!")

class BookingSystem :
    def __init__(self, cinema) :
        self.cinema = cinema
        self.selected_movie = None
        self.selected_show = None
        self.selected_row = None
        self.selected_col = None
        self.seat_type = None
        self.price = None

    def select_movie (self) :
        print ("\nAvailable Movies:")
        for idx, movie in enumerate (self.cinema.movies, start=1) :
            print (f"{idx}. {movie.title}")

        choice = int (input ("\nSelect Movie: "))
        self.selected_movie = self.cinema.movies [choice - 1]
        return self.selected_movie

    def select_show (self) :
        print ("\nAvailable Shows:")
        available_shows = []

        for show in self.cinema.shows :
            if show.movie == self.selected_movie :
                available_shows.append (show)
        
        for idx, show in enumerate (available_shows, start=1):
            print (f"{idx}. Date: {show.show_date} | Time: {show.show_time} | Hall: {show.hall_number}")
        
        choice = int (input ("\nSelect Show: "))
        self.selected_show = available_shows [choice - 1]
        return self.selected_show

    def select_seat (self):
        seat_matrix = self.selected_show.seat_matrix

        while True:
            seat_matrix.display_seats ()
            self.selected_row = int (input("\nEnter Row: ")) - 1
            self.selected_col = int (input("Enter Column: ")) - 1

            if not seat_matrix.is_seat_avaliable (self.selected_row, self.selected_col) :
                print ("Seat Already Booked! Please choose another seat.")
                continue

            if isinstance (seat_matrix, VIPSeat) :
                vip_choice = input ("VIP Booking? (yes/no): ").lower ()
                if seat_matrix.is_vip_seat (self.selected_row) and vip_choice != "yes" :
                    print ("⚠️  This is a VIP seat. VIP booking is required.")
                    continue 
                self.seat_type = "VIP" if seat_matrix.is_vip_seat (self.selected_row) else "Standard"
                self.price = self.selected_show.vip_price if self.seat_type == "VIP" else self.selected_show.standard_price
                seat_matrix.book_seat (self.selected_row, self.selected_col, self.seat_type == "VIP")
            else:
                self.seat_type = "Standard"
                self.price = self.selected_show.standard_price
                seat_matrix.book_seat(self.selected_row, self.selected_col)

            break 

        return True

    def generate_ticket (self) :
        ticket = Ticket (self.selected_show, self.selected_row, self.selected_col, self.seat_type, self.price)
        ticket.show_ticket ()

    def start_booking (self) : 
        self.select_movie ()
        self.select_show ()
        if self.select_seat () :
            self.generate_ticket ()

cinema = Cinema ()

movies_data = [
    ("AVATAR FIRE AND ASH!", 195),
    ("ANACONDA!", 99),
    ("NOW YOU SEE ME: NOW YOU DON'T!", 112),
    ("THE HOME!", 95)
]

for title, duration in movies_data :
    cinema.add_movie (Movie (title, duration))

show_time = [  # Same movie in same index
    (0, "08:05 PM", "02-Jan-2026", 1, 1000, 1500),
    (0, "11:45 PM", "02-Jan-2026", 1, 1000, 1500),
    (0, "04:05 PM", "02-Jan-2026", 2, 1000, 1500),
    (1, "07:45 PM", "02-Jan-2026", 2, 1000, 1500),
    (1, "09:50 PM", "02-Jan-2026", 2, 1000, 1500),
    (1, "03:00 PM", "02-Jan-2026", 3, 1000, 1500),
    (1, "12:10 AM", "02-Jan-2026", 3, 1000, 1500),
    (2, "10:50 PM", "02-Jan-2026", 4, 1000, 1500),
    (3, "10:50 PM", "02-Jan-2026", 4, 1000, 1500)
]

for movie_index, time, date, hall, std_price, vip_price in show_time :
    show = Show (cinema.movies [movie_index], time, date, hall, std_price, vip_price, rows=5, cols=5)
    cinema.add_show (show)

while True :
    booking = BookingSystem (cinema)
    booking.start_booking ()

    another_booking = input ("\nWould you like to make another booking? (y/n): ").lower ()
    if another_booking != "y" :
        print ("🙏 Thank you for choosing NUPLEX Cinema!")
        print ("🍿 Enjoy your movie. Goodbye!")
        break