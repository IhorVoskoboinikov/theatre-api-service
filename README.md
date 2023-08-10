# Documentation Theatre API Service

Theatre API Service (CRUD application) is an application that implements user interaction and the ability for the user to reserve tickets for a play.

## Entities:

1. User (Authenticated user with JWT authorization)
   - Used for user authentication and authorization.
   
2. TheatreHall
   - Represents a theater hall with a specified number of rows and seats per row.
   
3. Genre
   - Represents a genre that can be associated with a play.
   
4. Actor
   - Represents an actor who can be associated with a play.
   
5. Play
   - Represents a theatrical play with a title, description, associated genres, and actors.
   
6. Performance
   - Represents a specific performance of a play in a theatre hall at a certain time.
   
7. Reservation
   - Represents a reservation made by a user for one or more tickets to a specific performance.
   
8. Ticket
   - Represents a ticket reserved as part of a reservation for a specific performance.

## Setup:

### Option 1:

1. Clone the project:
   + `git clone https://github.com/IhorVoskoboinikov/theatre-api-service`
   
2. Create a virtual environment and activate it:
   + `python3 -m venv venv`
   + `source venv/bin/activate` (macOS and Linux)
   + `venv\Scripts\activate` (Windows)
   
3. Install dependencies:
   + `pip install -r requirements.txt`
   
4. Run migrations:
   + `python manage.py makemigrations`
   + `python manage.py migrate`
   
5. Create a superuser:
   + `python manage.py createsuperuser` (enter your username and password)
   
6. Run the development server:
   + `python manage.py runserver`

## Usage (local):

1. Go to the URL where the API was launched: [http://127.0.0.1:8000/api/doc/swagger/](http://127.0.0.1:8000/api/doc/swagger/), and use Swagger to test the API endpoints.

2. Since you are an administrator, you can also access the Django admin site: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/), where you can manage users, models, and access permissions.

![Website Interface](demo.PNG)

