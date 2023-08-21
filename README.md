# Documentation Theatre API Service

Theatre API Service (CRUD application) is an application that implements user interaction and the ability for the user
to reserve tickets for a play.

## DB Structure:

![Website Interface](DB Structure.PNG)

1. User (Authenticated user with JWT authorization)
2. CRUD operations with actor, genre, play, performance, theatre hall, reservation
3. Checking reservations for rows and seats per play.


## Setup:

### Option with Docker:

1. Install Docker ( [Link](https://www.docker.com/products/docker-desktop/) ) if you don't have it installed
2. Clone the project:
    + `git clone https://github.com/IhorVoskoboinikov/theatre-api-service`
2. Add file .env (look for example in .env.sample):
3. Create Docker images:
    + `docker-compose build`
4. Run app:
    + `docker-compose up`

## Usage (local):

1. Go to the URL where the API was
   launched: [http://127.0.0.1:8000/api/doc/swagger/](http://127.0.0.1:8000/api/doc/swagger/), and use Swagger to test
   the API endpoints.

![Website Interface](demo.PNG)

