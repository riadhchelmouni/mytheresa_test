
### **Backend Project Explanation**

I developed the backend of this project using **Django**, a powerful framework that facilitates rapid development. Django offers built-in features such as authentication, an admin panel, and form handling, making it ideal for this type of project.

I opted for **SQLite** as the database because it’s lightweight and requires minimal setup. Given that this project doesn't involve high transaction volumes or complex data structures, SQLite was a perfect fit. It integrates seamlessly with Django, allowing for quick and efficient development without the need for a more complex database setup.

Here’s a breakdown of the key decisions made during development:

1. **Product Model:**  
   I created a `Product` model to store product details such as SKU, name, category, and price. This model allows for easy product management.

2. **Price Calculation and Discounts:**  
   I implemented a custom method that calculates discounted prices based on product categories or SKUs. This ensures users receive the correct price, factoring in promotions or discounts.

3. **API Views:**  
   I used Django's `APIView` to build an endpoint for retrieving product data. The API supports filtering by category and price, and includes pagination to optimize performance when dealing with large datasets.

4. **Admin Interface:**  
   Django’s built-in admin interface simplifies product data management. I customized the interface to make it more intuitive and efficient for administrators to search and manage products.

5. **Testing:**  
   I wrote comprehensive tests to validate the functionality of the product creation process, discount application, filtering, and API behavior, ensuring the system works as expected.

6. **Cross-Origin Resource Sharing (CORS):**  
   I enabled CORS using `django-cors-headers` to allow the frontend to interact with the backend, even if they are hosted on different servers or ports.

By using Django, I was able to quickly develop a feature-rich backend, and with SQLite, I kept the database setup simple and lightweight, perfectly suiting the requirements of the project.


### **Frontend Explanation**

For the frontend, I developed a clean, user-friendly interface where users can view and filter products by category. The frontend dynamically fetches product data from the backend through API calls, which are powered by Django.

Using **JavaScript**, the frontend sends requests to the backend to retrieve product data, filtered by the chosen category. The product information is then displayed in a responsive grid layout, with each product card showing essential details such as the product name, category, and price (including any applicable discounts).

I also implemented filtering functionality, allowing users to easily narrow down their product search based on their preferences. This feature is particularly useful for creating an intuitive user experience.

To facilitate smooth communication between the frontend and backend, I configured **CORS** using `django-cors-headers`. This allows the frontend to interact with the backend even when they are hosted on different domains or ports.


### **Docker and Testing Explanation**

To meet the project’s requirements, I used **Docker** to containerize the application, ensuring that it can be easily run and tested on any machine with minimal setup. Docker provides an isolated environment, ensuring the application runs consistently regardless of the host machine.

I built the application image with the following command:

docker build . -t mytheresa


To run the project, use the following command, which will start the Django server:

docker run -p 8000:8000 -it mytheresa


The application will be accessible at `localhost:8000`.

For testing, I ensured that the application code is testable without the need for external networking or filesystem dependencies. To run the test suite, use the following command:

docker run -it mytheresa python manage.py test


This will execute all the tests for the Django application and ensure the functionality works as expected.

To access the application, use the following credentials:
- **Username:** riad
- **Password:** admin12345

By using Docker, I made the project portable and easy to set up. The tests ensure the application remains reliable and maintainable.


### **Access Links**

You can access the following resources in the application:

- **Admin Panel:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Product API Endpoint:** [http://localhost:8000/api/products/](http://localhost:8000/api/products/)
- **Static Frontend (index.html):** [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)


### **Version Control and GitHub**

In addition to the development and deployment of this project, I am proficient in using **Git** and **GitHub** for version control. I understand the importance of maintaining code integrity and collaboration, and I use GitHub to manage projects, track changes, and collaborate with others.

I am familiar with the following common Git commands used in managing repositories and workflows:

1. **Cloning a Repository:**  
   To clone an existing GitHub repository to my local machine:

   git clone <repository_url>
   

2. **Creating a New Branch:**  
   To create a new branch for feature development or bug fixes:

   git checkout -b <branch_name>


3. **Committing Changes:**  
   After making changes to the project, I commit them with a descriptive message:

   git add .
   git commit -m "Your commit message"


4. **Pushing Changes:**  
   To push local changes to a remote repository on GitHub:
   git push origin <branch_name>

5. **Pulling Latest Changes:**  
   To pull the latest changes from the remote repository:
   
   git pull origin <branch_name>
  

6. **Merging Branches:**  
   Once development is complete, I merge the feature branch into the main branch:
   
   git checkout main
   git merge <branch_name>
   

7. **Creating and Using Tags:**  
   I also use Git tags to mark release points in the project:
   
   git tag -a <tag_name> -m "Release description"
   git push origin <tag_name>
   

By using Git and GitHub, I ensure that my projects are well-managed, version-controlled, and easy to collaborate on with other developers. This experience is critical for maintaining code quality and for working in a team-based environment.
