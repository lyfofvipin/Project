# Projects
## I keep all my projects in this repository which I code in any language.

### [My Bloger](https://github.com/vipin3699/Projects/tree/master/MyBloger)

This Project is my first test project i have completed with learning Django, I create database models, link and routes, Forms, use class based views, learn about Admin page and about jinja2.

This app is similar to WordPress or any blogger here user can create posts and modify them if needed and delete if nessesury each user have an account for creating posts and modifying them, 
user can change there Passwords, Profile Picture and username if they want.

##### [Requirements](https://github.com/vipin3699/Projects/blob/master/MyBloger/requirements.txt)

```Available routs for the users :-

    1.  'admin/'
        This route is for Admin of the website.
    2. '/'  [name='Home']
        This is the home route here user can see the latest post of another users  and can got to other routes when needed.
    3. 'post/<int:pk>' [name='post-detail']
        This route will provide an brief detail of an specific post of any user.
    4. 'new-post' [name='post-create']
        This route will take user to a page that allow you to create a new Post.
    5. 'post/<int:pk>/update' [name='post-update']
        This page will allow user to update there post if they want to modify that.
    6. 'user/<str:username>' [name='user-post-detail']
        This route will display all the post a particular user.
    7. 'post/<int:pk>/delete/' [name='post-delete']
        This route will allow users to delete there own post.
    8. 'register' [name='Registration']
        This route is for registering a new user so they can create posts.
    9. 'login' [name='Login']
        After creating an account everyone has to login to create or modify there posts so this route help in logging in the user.
    10. 'logout' [name='Logout']
        This route will help user in logging out in any browser so anyone else can't misbehave there posts.
    11. 'profile' [name='Profile']
        This route provide all information of the logged in user and allow him to modify there details like username, email and profile picture.
    12. 'password-reset/' [name='password_reset']
        This route come in use when a user forgot his password and want to reset them.
    13. 'password-reset/done/' [name='password_reset_done']
        This route confirms that an password reset link is been sanded to the user mail address.
    14. 'password-reset-confirm/<uidb64>/<token>/' [name='password_reset_confirm']
        This route come in use when user click on the password reset link on there mail.
    15. 'password-reset-complete/' [name='password_reset_complete']
        This route will confirm that your password has been change.```
