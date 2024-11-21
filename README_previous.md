<img src="assets/images/readme_images/LQ2050_logo6.png" alt="Loqta2050 logo" width="400"/>

 
# Loqta2050 News Site

## Welcome 

Welcome to **Loqta2050**, a dynamic and interactive news platform built using Django. Loqta2050 is designed to provide users with the ability to post, read, and comment on news articles, offering a community-driven space for discussion and engagement. Whether you want to stay up-to-date with the latest news, engage in discussions, or share your opinions, **Loqta2050** provides a user-friendly platform for a seamless experience.

[Here is the live version of the project](https://loqta2050-89fbbef45245.herokuapp.com/admin)

[Here is our E-commerce Website](https://loqta2050.com/)

![devices](assets/images/readme_images/devices.png)

## Purpose of the project

The goal of **Loqta2050** is to create a modern, Reddit-style news platform where users can share and discuss stories from around the world. By leveraging Django and PostgreSQL, this project aims to foster a community of contributors and readers, with features designed to enhance interaction, such as upvoting, commenting, and categorizing content by topics.

Whether you're a casual reader, an active participant, or a site admin, **Loqta2050** provides tools to create, manage, and engage with content in a meaningful way.



## User Stories:

### As a User:

1. I want to view news stories and comments on different topics so I can stay informed and engaged.
2. I want to register and log in to the platform so I can contribute by posting news stories and leaving comments.
3. I want to upvote or downvote posts so I can show my opinion on the content.
4. I want to filter posts by categories so I can quickly find stories that interest me.
5. I want to view the time and date of each post so I can know when the story was published.

### As an Admin:

1. I want to manage user posts and comments so I can moderate inappropriate content.
2. I want to manage categories so I can keep the content organized.
3. I want to view all user activities and ensure compliance with community guidelines.

## Features:

### Existing Features:

The **Loqta2050 News Site** offers several features to enhance user experience:

1. **User Registration and Authentication**: 
   Users can create accounts, log in, and log out securely. Once logged in, users can create and comment on posts.

2. **Post Creation and Voting**: 
   - Users can submit news stories on different topics.
   - Other users can upvote or downvote these posts based on their preferences.

   ![Create Post](assets/images/readme_images/create_post.png)


    ![alt text](assets/images/readme_images/Django_administration.png)

3. **Commenting System**: 
   Users can comment on posts, fostering discussions on different news stories.
   
   ![Commenting](assets/images/readme_images/commenting.png)

4. **Categorization**: 
   Posts are categorized by topics such as Politics, Technology, Entertainment, etc., allowing users to filter stories easily.

   ![Categories](assets/images/readme_images/categories.png)

5. **Time and Date of Posting**: 
   Each post displays the date and time it was published to provide context to the news stories.
   
   ![Date and Time](assets/images/readme_images/date_time.png)

6. **User-friendly Interface**: 
   Loqta2050 provides a simple and intuitive interface for users to navigate posts, leave comments, and upvote/downvote stories.

7. **Admin Moderation Tools**: 
   Admin users have access to moderation tools, allowing them to approve, delete, or edit user content when necessary.

![alt text](assets/images/readme_images/add_user.png)

8. **Pagination for Posts**: 
   Users can browse through a paginated list of posts, making it easier to explore older news stories.

   ![Pagination](assets/images/readme_images/pagination.png)


### Future Features:

1. **Private Messaging**: 
   Users will be able to send private messages to one another for more direct engagement.
   
2. **Multimedia Support**: 
   The ability for users to include images or videos in their posts to enhance the richness of shared content.
   
3. **Push Notifications**: 
   Users will receive notifications for upvotes, comments, and replies on their posts.
   
4. **Tagging System**: 
   Implement a tagging system for posts to enable better organization and searching across topics.

## Data Model:

This project uses Django’s Object-Relational Mapping (ORM) to handle data interactions between the application and PostgreSQL. The key models are as follows:

- **User**: Handles authentication and user profile information.
- **Post**: Represents a news article or story, including its title, content, author, category, and timestamp.
- **Comment**: Represents user comments on a post.
- **Category**: Represents a grouping or category of posts (e.g., Politics, Technology).
- **Vote**: Handles upvoting and downvoting of posts and comments.

The relational model ensures each post has associated comments, votes, and categories.



## Testing:

### Manual Testing:
We conducted manual testing by simulating common user behaviors to ensure the system works as expected. The scenarios tested include:

- **Creating posts and comments**: We verified that logged-in users can successfully create, edit, and delete posts and comments, ensuring that these actions were handled correctly by the system.
- **Upvoting and downvoting posts**: We tested the voting functionality to confirm that users could only vote once per post and that votes were correctly recorded and displayed.
- **Filtering posts by category**: We checked the category filter functionality to ensure users could easily browse posts based on specific categories.
- **Handling valid and invalid inputs**: We tested the system's ability to handle both valid and invalid inputs, ensuring appropriate error messages were displayed when users submitted empty forms, invalid post data, or attempted duplicate votes.

### Automated Unit Testing:
We also wrote and ran unit tests using Django’s `unittest` framework to verify the core functionalities of the website. Below is a summary of the unit tests we implemented:

1. **Post Creation and Retrieval:**
   - We wrote tests to verify that logged-in users can create new posts and that required fields are validated.
   - We ensured that posts were correctly displayed on both the homepage and individual post pages.
   - We tested the pagination feature to confirm that posts were properly divided into pages.

2. **Comment Submission:**
   - We confirmed that logged-in users could submit comments on posts and that these comments were correctly linked to the relevant posts and displayed in the right order.
   - We ensured non-logged-in users were restricted from submitting comments.

3. **User Authentication:**
   - We created unit tests to verify that users could successfully register, log in, and log out.
   - We tested that only authenticated users could create, edit, or delete posts and comments.
   - We ensured that password reset and account management features functioned as expected.

4. **Post Voting System:**
   - We wrote tests to confirm that the upvoting and downvoting functionality worked correctly, ensuring users could only vote once per post.
   - We ensured that vote counts were updated in real-time and accurately reflected user inputs.

5. **Category Filtering:**
   - We tested the category filtering functionality to confirm that posts were correctly filtered and displayed based on the category selected.
   - We ensured users could navigate between categories without any errors.

6. **Error Handling:**
   - We validated that the system properly handled invalid inputs, such as attempts to create posts or comments with missing data or invalid forms.
   - We checked that the system displayed helpful error messages when users performed invalid actions.

### Running Tests:
To run the unit tests we created, you can use the following command in the project directory:

```bash
python manage.py test
```

This command will execute all the tests we implemented, allowing you to confirm that each core functionality works as intended. Running these tests ensures that the site remains robust and stable throughout development.
## Bugs:

- http://127.0.0.1:8000/admin/posts/post/

![alt text](assets/images/readme_images/post_add.png)


- http://127.0.0.1:8000/admin/posts/post/add/

![alt text](assets/images/readme_images/post_show.png)


### Solved Bugs:
- Pagination initially displayed incorrectly on smaller devices. This was fixed by adjusting the CSS for responsive behavior.
- An issue with user authentication when attempting to comment was resolved by properly linking the user session to the comment submission form.

### Remaining Bugs:
- Currently, no known bugs remain.

## Validator Testing:

All Python code has been validated using `flake8`, and the HTML has been tested using [W3C Markup Validator](https://validator.w3.org/). No major issues were found.


## Getting Started:

To set up **Loqta2050** locally for development or testing purposes, follow these steps:

1. Clone this repository to your local machine.
2. Create a virtual environment and install the dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database and configure environment variables in `.env` (use `.env.example` for reference).
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Start the Django development server:
   ```
   python manage.py runserver
   ```
7. Access the site locally at [http://localhost:8000](http://localhost:8000).

## Deployment:

This project can be deployed on platforms such as **Heroku** using the following steps:

1. Create a Heroku app and set the buildpacks to:
   1. `heroku/python`
   2. `heroku/nodejs` (if using front-end dependencies)
   
2. Set the required environment variables:
   - `DATABASE_URL`
   - `SECRET_KEY`
   - `DEBUG` (set to `False` in production)
   
3. Push your project to Heroku:
   ```
   git push heroku main
   ```
## Credits:

- Django documentation for providing in-depth guidance on using the framework.
- [Unsplash](https://unsplash.com/) for free images used in the project.
- [Pexels](https://www.pexels.com/) for additional media resources.
- Icons from [FontAwesome](https://fontawesome.com/).
- Other Django, Python Websites