# E-Commerce-WebApp

# Auction Web Application

This is a web application built using Django and PostgreSQL that allows users to participate in auctions by bidding on active listings. Users can create accounts, log in, and register for auctions. The application includes several key features such as adding products to a watchlist, filtering products by category, and sending alerts to the highest bidder.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Authentication and Authorization](#authentication-and-authorization)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/auction-web-app.git
   cd auction-web-app
   ```

2. Set up a virtual environment:

   ```shell
   python -m venv env
   source env/bin/activate  # for Linux/Mac
   env\Scripts\activate  # for Windows
   ```

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Install and set up PostgreSQL if you haven't already.
   - Create a new PostgreSQL database.
   - Update the `DATABASES` configuration in the `settings.py` file with your database credentials.

5. Run database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Create a new account or log in with your existing credentials.
2. Browse the active auctions listed on the homepage.
3. Click on an auction to view more details about the product and current bids.
4. Place a bid by entering your bid amount and clicking the "Bid" button.
5. You can add a product to your watchlist by clicking the "Add to Watchlist" button.
6. Use the category filter to narrow down the displayed auctions.
7. Receive alerts if you are the highest bidder on an auction.
8. Manage your account settings, including updating your profile information and password.

## Features

- User registration and authentication system.
- Create, update, and delete auctions.
- Place bids on active auctions.
- Add products to the watchlist for easy access.
- Filter auctions by category.
- Receive alerts when you are the highest bidder.
- User-friendly interface for easy navigation.
- Secure user access and data protection.

## Authentication and Authorization

Authentication and authorization are implemented to ensure secure user access to the application. Users are required to create an account and log in before they can participate in auctions. Passwords are securely stored using encryption techniques to protect user information. Authorization controls are in place to restrict access to certain features and actions based on user roles and permissions.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the established coding conventions and provide clear commit messages when contributing.
