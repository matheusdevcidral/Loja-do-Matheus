## About the Projet
This project simulates a basic management system for small businesses, operated entirely through the terminal. The user can register customers with their respective services and prices, log sales, and track accumulated revenue — all stored in .txt files.

## Features

- List of registered customers
- Register new customers with name, service, and price
- Log billing entries (sales and services)
- View total revenue
- Input validation with error messages
- Colorful terminal interface using the Rich library

## Technologies Used

- Python 3
- Rich and Time libraries — the first to improve the visual experience and the second for better UX in the terminal
- .txt files — simple data persistence

## How to Run

1. Clone the repository
   git clone https://github.com/matheusdevcidral/Loja-do-Matheus.git

2. Install the dependency
   pip install rich

3. Run
   python system.py

## What I Learned

- File handling with open() (reading and writing)
- Robust user input validation
- String formatting with alignment (:<, :^, :>)
- Using the Rich library for terminal UI
- Code organization with well-defined functions
