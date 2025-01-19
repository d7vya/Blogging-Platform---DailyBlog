Blog Website - "DailyBlog"
"Daily Project" is a Django-powered blogging platform designed to provide users with a rich and secure blogging experience. The platform features group-based permissions, tagging, and a ban system to ensure flexible and controlled interactions among users.

Features
Core Functionalities
1)User Authentication
User Registration, Login, Logout, and Password Reset.

2)Blog Management
Users can create, update, delete, and view their blogs.
Each blog includes fields such as title, description, body, slug, category, and tags.
>Tags:
Choose from predefined tags or request new ones (admin approval required).
Blog views are tracked directly in the Blog model.

3)Group-Based Permissions
>Staff Group:
Can add, update, delete, and view their own blogs.
Can comment on blogs, including admin posts.

>User Group:
Can add, update, delete, and view their own blogs.
Can view and comment on posts by others, including admin posts.

>Banned User Group:
Can view all blogs but cannot add, update, delete, or comment.

4)Ban System
Admins can assign users to the "Banned User" group.
Banned users can view blogs but are restricted from creating new ones or commenting.

5)Search and Filtering
Search blogs by keywords (case-insensitive).
filter blogs by tags, categories, or sort them by views and dates.

6)Comments
Users can add, view, and manage comments on blogs, based on their group permissions.
