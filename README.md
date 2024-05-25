<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />

<!-- ABOUT THE PROJECT -->

## About The Project

This project provides a backend service for managing cats through a RESTful API. You can perform various operations like fetching all cats, creating a new cat, deleting a cat, and updating cat information. You can check here the API testing project: <h2>https://github.com/Bogii02/python-cat-api-test</h2>


### Built With

The following technologies were used during the project:

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Postgresql][Postgres]][Postgres-url]
* [![Docker][Docker]][Docker-url]
* [![Postman][Postman]][Postman-url]

<h3>If you want to try out the endpoints of this project, I recommend using Postman.</h3>
**If you want to send, delete, or update a cat, you'll need to use a JSON structure with fields like name, age, and color.**

<h3><code>
   {
   <span style="color:#D009F6">"name":</span> <span style="color:#2FF609">"Example"</span>,
   <span style="color:#D009F6">"age":</span> <span style="color:#2FF609">10</span>,
   <span style="color:#D009F6">"color":</span> <span style="color:#2FF609">"example"</span>
   }
</code><h3>


<!-- GETTING STARTED -->

## Getting Started

### Installation

To get started with the Cat API backend, follow these steps:

1. Clone the repository.
   ```sh
   git clone git@github.com:Bogii02/python-cat-api.git
   ```
2. Change directory to python-cat-api
   ```sh
   cd python-cat-api
   ```
3. Change .env.sample file name to .env.
   ```sh
   mv .env.sample .env
   ```
4. Fill out .env file with necessary data. Port number can be the default postgres port (***5432***).

5. Start the project.
   ```sh
   docker compose up --build
   ```

<!-- FEATURES -->

## API Endpoints

- **GET /api/cats**: Retrieve all cats.

- **GET /api/cats/{cat_id}**: Get a cat by its ID.

- **POST /api/cats**: Create a new cat.

- **DELETE /api/cats/{cat_id}**: Delete a cat by its ID.

- **PUT /api/cats/{cat_id}**: Update information of a cat by its ID.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Boglárka Bakos - [@Boglárka Bakos_LinkedIn](https://linkedin.com/in/boglarka-bakos)

Project Link: [https://github.com/Bogii02/python-cat-api](https://github.com/Bogii02/python-cat-api)


[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org

[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com

[Postman]: https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white
[Postman-url]: https://www.postman.com