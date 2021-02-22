# Casting Agency

Site live at : [https://mario-agency.herokuapp.com/](https://mario-agency.herokuapp.com/)

### Endpoints

#### GET /movies

- Returns all the movies.
- Roles: Casting Assistant,Casting Director,Executive Producer.

```json
{
  "movies": [
    {
      "id": 1,
      "release_date": "2022-08-04",
      "title": "Movie 1"
    },
    {
      "id": 2,
      "release_date": "2022-08-05",
      "title": "Movie 2"
    }
  ],
  "success": true
}
```

#### GET /movies/\<int:id\>

- Returns all the movies.
- Roles: Casting Assistant,Casting Director,Executive Producer.

```json
{
  "movie": {
    "id": 1,
    "release_date": "2022-08-04",
    "title": "Movie 1"
  },
  "success": true
}
```

#### POST /movies

- Creates a new movie based on a payload.
- Roles authorized : Executive Producer.

```json
{
  "movie": {
    "id": 3,
    "release_date": "2022-08-06",
    "title": "Movie 3"
  },
  "success": true
}
```

#### PATCH /movies/\<int:id\>

- Patches a movie based on a payload.
- Roles authorized : Casting Director, Executive Producer.

```json
{
  "movie": {
    "id": 3,
    "release_date": "2022-08-06",
    "title": "Movie 3 + patch"
  },
  "success": true
}
```

#### DELETE /movies/<int:id\>

- Deletes a movies by id form the url parameter.
- Roles authorized : Executive Producer.

```json
{
  "message": "movie id 3, titled Movie 3 + patch was deleted",
  "success": true
}
```

#### GET /actors

- Returns all the actors.
- Roles authorized : Casting Assistant,Casting Director,Executive Producer.

```json
{
  "actors": [
    {
      "age": 2,
      "gender": "female",
      "id": 1,
      "name": "Janice"
    },
    {
      "age": 3,
      "gender": "male",
      "id": 2,
      "name": "Windsor"
    }
  ],
  "success": true
}
```

#### GET /actors/\<int:id\>

- Route for getting a specific actor.
- Roles authorized : Casting Assistant,Casting Director,Executive Producer.

```json
    {
      "age": 2,
      "gender": "female",
      "id": 1,
      "name": "Janice"
    },
  "success": true
}
```

#### POST /actors

- Creates a new actor based on a payload.
- Roles authorized : Casting Director,Executive Producer.

```json
{
  "actor": {
    "age": 24,
    "gender": "female",
    "id": 3,
    "name": "Ryan"
  },
  "success": true
}
```

#### PATCH /actors/\<int:id\>

- Patches an actor based on a payload.
- Roles authorized : Casting Director, Executive Producer.

```json
{
  "actor": {
    "age": 23,
    "gender": "female",
    "id": 3,
    "name": "Gin"
  },
  "success": true
}
```

#### DELETE /actors/<int:id\>

- Patches an actor based on a payload.
- Roles authorized : Casting Director, Executive Producer.

```json
{
  "message": "actor id 3, named Gin was deleted",
  "success": true
}
```

## Project dependencies

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

Follow instructions to set up virtual environment in the [python packaging docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Installing Dependencies

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup

The project uses Postgresql as its database, you would need to create one locally and reflect it in setup.sh.
To update the database and seed run the following :

```bash
python manage.py db upgrade
python manage.py seed
```

- you may need to change the database url in setup.sh after which you can run

```bash
source setup.sh
```

- Start server by running

```bash
flask run
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)

- [SQLAlchemy](https://www.sqlalchemy.org/)

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#)

## Testing

Replace the jwt tokens in test_app.py with a new one.

For testing locally, we need to reset database.
To reset database, run

```
python manage.py db downgrade
python manage.py db upgrade
python manage.py seed
```

### Error Handling

- 400 – bad request
- 401 – unauthorized
- 404 – resource not found
- 422 – unprocessable
- 500 – internal server error
