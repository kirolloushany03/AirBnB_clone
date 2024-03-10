Certainly! Here's the README with emojis and the contributors Kirollous Hany and Ashraf Atef:

---

# AirBnB Clone Project

Welcome to the AirBnB Clone project! This project aims to create a simplified version of the AirBnB website, allowing users to manage rentals, bookings, and more. 🏠🔑

🚀 **Getting Started**
To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `console.py` file to start the command-line interface.

---

## Task 0: Set up your project

**Description:** Set up the project structure including directories for models, tests, and the console. Create a base model class `BaseModel` that will serve as the foundation for other classes. 🏗️

---

## Task 1: BaseModel Class

**Description:** Define the `BaseModel` class with common attributes like `id`, `created_at`, and `updated_at`. Implement methods like `save()` to update timestamps and `to_dict()` to convert the instance to a dictionary. 📝

---

## Task 2: Console I/O

**Description:** Implement basic I/O functionality for the console. Allow users to interact with the application through a command-line interface. Handle commands like `quit`, `help`, and `EOF`. 💬💻

---

## Task 3: User Class

**Description:** Create a `User` class with attributes like `email` and `password`. Implement methods for user authentication and profile management. 👤🔒

---

## Task 4: Storage Engine

**Description:** Set up a storage engine to manage serialization and deserialization of objects. Implement methods to save and load objects to/from JSON files. 💾

---

## Task 5: Place Class

**Description:** Define a `Place` class with attributes like `name`, `price`, and `city_id`. Implement methods to manage rental properties such as adding amenities and managing bookings. 🏡💼

---

## Task 6: Review Class

**Description:** Create a `Review` class with attributes like `place_id`, `user_id`, and `text`. Implement methods to manage user reviews for rental properties. 📝👥

---

## Task 7: File Storage

**Description:** Update the storage engine to use file storage. Implement methods to serialize objects to JSON format and save them to a file. 🗃️

---

## Task 8: Console Commands

**Description:** Extend the functionality of the console with commands like `create`, `show`, `destroy`, `update`, `all`, and `count` to manage instances of different classes. 🛠️

---

## Task 9: Amenity Class

**Description:** Define an `Amenity` class with attributes like `name` and `place_amenities`. Implement methods to manage amenities available at rental properties. ♨️

---

## Task 10: City Class

**Description:** Create a `City` class with attributes like `name` and `state_id`. Implement methods to manage cities where rental properties are located. 🌆🌎

---

## Task 11: State Class

**Description:** Define a `State` class with attributes like `name` and `cities`. Implement methods to manage states where rental properties are located. 🏞️🏙️

---

## Task 12: File Storage Reloaded

**Description:** Update the file storage engine to support reloading of objects from JSON files. Implement methods to load objects from JSON format and recreate instances. 🔄

---

## Task 13: User Management

**Description:** Enhance user management functionality with features like user registration, login, and profile management. Implement methods to handle user authentication and access control. 🎟️

---

## Task 14: More Console Commands

**Description:** Expand the console with additional commands to manage user profiles, bookings, and reviews. Implement commands for user registration, login, logout, and profile updates. 📑

---

## Task 15: Place Review

**Description:** Improve the review functionality for rental properties. Implement methods to allow users to submit reviews for places they have stayed. 🌟

---

## Task 16: Update Place

**Description:** Enhance the functionality to update rental property information. Implement methods to allow users to modify property details such as name, price, and amenities. 🔄💼

---

## Task 17: Advanced Features

**Description:** Implement advanced features such as search functionality, user ratings, and recommendation systems. Enhance the user experience with features that help users find and book rental properties more efficiently. 🔍🌟

---

## How to Use

1. Run `console.py` to start the command-line interface.
2. Use the available commands to manage instances of different classes.
3. Explore the functionality of each class and command to understand their usage.

---

## Contributors

- [Kirollous Hany](https://github.com/kirolloushany)
- [Ashraf Atef](https://github.com/ashrafatefdev)

---

🎉 **Congratulations!** You have successfully set up the AirBnB Clone project. Enjoy exploring its features and functionality! If you encounter any issues or have suggestions for improvements, feel free to contribute or reach out to the project contributors.
