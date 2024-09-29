

# Vispr - A Simple Social Media App

**Vispr** is a minimalist social media application where users can share their thoughts, similar to a basic version of Twitter. This app allows users to create, edit, and delete their own "tweets" while having the ability to log in, register, and log out. Each user’s activity is isolated, meaning one user cannot interact with another user’s content.

## Features

- **User Authentication**: 
  - Users can register, log in, and log out.
  
- **Create, Edit, and Delete Posts**: 
  - Users can create, modify, and delete their own posts "tweets".
  
- **User Isolation**: 
  - Users can only interact with their own data, and cannot view or modify other users' content.

## Technologies Used

- **Django**: A Python-based web framework for rapid development.
- **SQLite**: A lightweight relational database for local development and storage.
- **Pillow**: A Python imaging library used for handling image-related features.

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ishant9805/vispr.git
    cd vispr
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate    # For Linux/macOS
    venv\Scripts\activate       # For Windows
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Change to main app directory**:
    ```bash
    cd vispr
    ```

5. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (to access the admin panel, if needed):
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the app**:
   Open your browser and go to `http://127.0.0.1:8000/` to start using **Vispr**.

## Usage

Once the server is running, you can:

- **Register** for a new account.
- **Log in** with an existing account.
- **Create new posts**, edit your own, or delete them.
- **Log out** of your account.

Each user’s actions are restricted to their own content, with no interaction between users.

## Folder Structure

```
vispr/
│
├── vispr/vispr/               # Project settings
├── vispr/tweet/            # Main app for the posts (tweets)
├── vispr/db.sqlite3           # SQLite database
├── vispr/manage.py            # Django management script
├── vispr/static/              # Static files (CSS, JS)
├── vispr/media/               # To store media files (images, gifs etc.)
├── vispr/templates/           # HTML templates
└── requirements.txt     # List of Python dependencies
```

## Future Enhancements

Some potential future features for **Vispr**, I might add:

- Allowing users to view and interact with other users' posts (e.g., liking, commenting).
- Adding media support (images, videos) for posts.
- Pagination of posts for better user experience.
- User profiles with the ability to follow others.


---

Feel free to tweak it or add any further details! If you need any additional sections or modifications, let me know!