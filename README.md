

# DailyBlog - A Django Blog Website

**DailyBlog** is a blog website built using Django, where users can sign up, create, read, update, and delete their blog posts. The website features object-level permissions using `django-guardian`, allowing users to manage their own blog posts and allowing admins to ban users. Additionally, users can search blog posts by keyword, filter by tags and categories, and sort by view count or date.

## Features

- **User Signup & Authentication**: Users can sign up, log in, and manage their account.
- **CRUD Operations on Blogs**: Users can create, read, update, and delete their own blog posts.
- **Object-Level Permissions**: `django-guardian` is used to provide object-level permissions for blog posts, ensuring that only the author can edit or delete their posts.
- **Admin Features**: Admins can ban users, preventing them from accessing the website.
- **Search**: Users can search for blog posts using keywords.
- **Filtering**: Blog posts can be filtered by tags and categories.
- **Sorting**: Blog posts can be sorted by view count or date.

## Prerequisites

Before setting up **DailyBlog**, ensure you have the following installed:

- **Python 3.x** (required to run Django)
- **pip** (Python's package installer)

### 1. Install Python

If you don’t already have Python installed, follow these steps:

- Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python 3.x for your operating system.
- Follow the installation instructions for your operating system. Ensure that the option to **Add Python to PATH** is checked during installation.
- After installing Python, you can verify the installation by opening a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS/Linux) and typing:

  ```bash
  python --version
  ```

  You should see something like this:

  ```bash
  Python 3.x.x
  ```

- Install `pip`, Python's package installer, by running:

  ```bash
  python -m ensurepip --upgrade
  ```

  You can verify `pip` is installed by running:

  ```bash
  pip --version
  ```

---

### 2. Install Django

Now that you have Python and `pip` installed, you can install Django, which is the web framework used for this project.

1. **Create a virtual environment** to isolate the dependencies for this project:

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   After activation, you’ll see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

3. **Install Django**:

   ```bash
   pip install django
   ```

4. **Verify Django installation**:

   ```bash
   django-admin --version
   ```

   You should see the installed version of Django, like `4.x.x`.

---

### 3. Install `django-guardian` Manually

`django-guardian` provides object-level permissions, and we need to install it manually.

1. **Install `django-guardian`**:

   In your activated virtual environment, run:

   ```bash
   pip install django-guardian
   ```

2. **Add `guardian` to `INSTALLED_APPS` in `settings.py`**:

   Open your `settings.py` file and add `'guardian'` to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       ...
       'guardian',
       ...
   ]
   ```

3. **Add `Guardian` to the `AUTHENTICATION_BACKENDS`**:

   In the same `settings.py` file, add `guardian.backends.ObjectPermissionBackend` to `AUTHENTICATION_BACKENDS` to enable object-level permissions:

   ```python
   AUTHENTICATION_BACKENDS = (
       'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
       'guardian.backends.ObjectPermissionBackend',  # Object-level permission backend
   )
   ```

4. **Migrate the database**:

   `django-guardian` requires additional database tables for permissions. Run the following command to apply the migrations:

   ```bash
   python manage.py migrate guardian
   ```

---

## Setup DailyBlog Project

### 1. Clone the Repository

If you haven't cloned the repository yet, you can do so by running:

```bash
git clone https://github.com/d7vya/Blogging-Platform---DailyBlog.git
cd DailyBlog
```

### 2. Set Up the Database

1. **Apply migrations** to set up the database schema:

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser** to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   You'll be prompted to enter a username, email, and password for the admin user.

---

### 3. Run the Development Server

Once the database is set up and the superuser is created, start the development server:

```bash
python manage.py runserver
```

Now, open your web browser and navigate to `http://127.0.0.1:8000/` to access the **DailyBlog** application.

---

## Features in Detail

### User Authentication & Authorization

- Users can register, log in, and manage their account via the Django authentication system.
- Each user can only edit or delete their own blog posts.
- Admins have special privileges, including banning users.

### CRUD Operations

- **Create**: Users can create a new blog post with a title, content, tags, and category.
- **Read**: Users can view all blog posts. Each blog post includes details such as the author, title, content, tags, and category.
- **Update**: Users can edit their own blog posts. Admins can also edit any blog post.
- **Delete**: Users can delete their own blog posts. Admins can delete any blog post.

### Object-Level Permissions

- **`django-guardian`** is used for object-level permissions, ensuring that users can only edit or delete their own blog posts.
- Admins have additional permissions to ban users.

### Search, Filtering, and Sorting

- **Search**: Users can search blog posts by entering keywords in the search bar. The search queries will match the content of blog posts.
- **Filtering**: Users can filter blog posts based on tags and categories to narrow down their search results.
- **Sorting**: Blog posts can be sorted by either view count (most viewed) or by date (newest or oldest first).

### Admin Features

- Admin users have the ability to ban other users. Banned users will be unable to log in or access the site.
  
### Model Overview

- **User**: Custom user model (Django's `User` model or extended).
- **Blog**: Model for storing blog posts. Fields include:
  - `title`
  - `content`
  - `author` (ForeignKey to User)
  - `tags` (ManyToManyField to Tag model)
  - `category` (ForeignKey to Category model)
  - `view_count`
  - `created_at`
  - `updated_at`
  
- **Tag**: Model to store tags that can be associated with blog posts.
- **Category**: Model to store categories for filtering blog posts.

## Dependencies

- Django: `4.x`
- django-guardian: `2.x` for object-level permissions





## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. All contributions are welcome!

---

Feel free to make any modifications or updates according to the specific implementation of your project. Happy coding!
```

