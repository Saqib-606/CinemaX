Cinema Ticket Booking System (Python – OOP Based)
A console-based Cinema Ticket Booking System developed using Python and Object-Oriented Programming (OOP) concepts.
This project simulates a real-life cinema environment where users can select movies, choose shows, book seats (Standard or VIP), and receive a printed ticket.
The system is designed to focus on clean OOP architecture, logical flow, and real-world booking behavior.

Project Overview
In real cinemas, users do not create cinemas or halls — they simply select movies, shows, and seats.
This project follows the same idea and provides a step-by-step booking flow, just like an actual cinema ticket counter.

The system allows users to:
Choose a movie
Select an available show
Pick a seat from a seat matrix
Book VIP or Standard seats
Generate a ticket with full details

Key Features
Fully built using Object-Oriented Programming
Multiple movies support
Multiple shows per movie (date, time, hall-wise)
Seat matrix visualization (Available / Booked)
VIP & Standard seat handling
Separate pricing for VIP and Standard seats
Auto-generated ticket with unique Ticket ID
Multiple bookings in one session
Interactive console-based system
Core Components (Classes)

1) Cinema
Acts as the root / foundation class.
Responsibilities:
Store cinema name
Manage movies
Manage shows
Display available movies

2) Movie
Stores movie-related information:
Movie title
Duration (in minutes)
Each movie can have multiple shows.

3) Show
Represents a specific show of a movie.
Stores:
Movie reference
Show date
Show time
Hall number
Standard seat price
VIP seat price
Seat matrix

4) SeatMatrix
Manages seating arrangement for a show.
Features:
2D seat layout (rows × columns)
Available / Booked seat tracking
Housefull detection
Seat display in console

5) VIPSeat (Inheritance)
Extends SeatMatrix to support VIP seat rules.
Responsibilities:
Identify VIP rows
Restrict VIP seats to VIP bookings only
Override seat booking behavior

6) Ticket
Generates a printable cinema ticket.
Includes:
Unique Ticket ID
Movie name
Date & time
Hall number
Seat number
Seat type (VIP / Standard)
Final price

7) BookingSystem
Handles the complete booking flow:
Movie selection
Show selection
Seat selection
Price calculation
Ticket generation
Acts as the controller of the system.

How to Run the Project
.) Requirements
Python 3.x

.) Steps

Clone the repository or download the project files
Open terminal / command prompt
Run the program:
CinemaX.py
