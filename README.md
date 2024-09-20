# Shop Command-Line System

## Overview

This is a simple command-line-based (local) shop system that allows users to browse and purchase products. It includes user authentication (not secure), a shopping cart, and the ability to manage products and view purchase history. Additionally, the system provides admin functionality for managing users, products, sales, and cashing out earnings (without actual money transactions).

## Features

### _User Features_

-   **Login/Register**: Users can create an account or log in to access the system.
-   **View Products**: Browse the available products in the store.
-   **Add/Remove Products to/from Cart**: Users can add items to their cart for purchase or remove items before checking out.
-   **Purchase Items**: Finalize the purchase of items in the cart.
-   **View Purchase History**: After making a purchase, users can check their purchase history.

### _Admin Features_

-   **Manage Products**: Add, update, delete and edit stock of products in the store.
-   **Manage Users**: View and manage registered users.
-   **Check Sales**: View overall sales data and monitor the store’s performance.
-   **Cashout**: Admins can cash out the earnings (without using real money).

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/D4N1L0200/Shop.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Shop
    ```

3. **Run the application**: The system can be run from the command line using a simple Python command:
    ```bash
    python main.py
    ```

## Usage

### _**General Flow**_

1. **Start the system**.
2. **Login** with your username and password, or **register** if you're a new user.
3. Once logged in, **users** will be presented with a menu, type the desired number to access the wanted functionality.
4. **Admins** can access additional features, type the desired number to access the wanted functionality.

## Admin Access

To access the admin features, log in with the admin account (Username: admin, Password: admin). You will see menu options for managing products, users, and sales.

## License

This project is licensed under the [MIT License](LICENSE).
