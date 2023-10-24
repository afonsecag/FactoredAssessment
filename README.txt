In order to execute the project, you have to do the following steps:

Open a Command Prompt and get to the root of the project, the root is 
the most outside folder called Factored where you can find this readme,
the docker compose, the backend and the frontend.

Next, you have to get in the root by typing cd 'the path to Factored'
(in my case it was cd C:\Users\alanf\OneDrive\Documents\Web\Factored)

The next step is to execute the docker compose, this requires docker
is already downloaded in your computer, once in the root you are going
to type docker-compose build, this will build the image of the container,
once you do this, everything should work fine, it could take 1-3 minutes
to finish the execution.

Once it ends, you are going to type docker-compose up -d, this will 
deploy the container, to check everything is fine, you can type 
docker-compose ps, but this is optional. Then, you have to check if 
the database is already created or not, to do this, once you typed
docker-compose up -d you are going to type: 
docker-compose exec backend python init_db.py, if this shows an error
of "UNIQUE constraint failed: employees.email", everything is working
fine, if not it will not show the error, it will show a message of 
the correct addition of the user to the database.

Finally, to check the backend it will be deployed on http://localhost:8000,
it has 3 routes: employee/1, /login and /profile, the first one is 
where the data of the user is saved, the login is the route to receive
credentials and the profile is to show the information we want in the 
profile. The frontend, is deployed in http://localhost:3000, it has
2 routes: / that is the login and /profile where the information of the
user is shown.

When you are finished, to finish the execution of the container you are
going to write docker-compose down -v



