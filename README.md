<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />

<!-- ABOUT THE PROJECT -->

## About The Project

# This API is available here: [https://python-cat-api.onrender.com](https://python-cat-api.onrender.com)
<h3>This project provides a backend service for managing cats through a RESTful API. You can perform various operations like fetching all cats, creating a new cat, deleting a cat, and updating cat information.</h3>
<h3>Check here for the API testing project: https://github.com/Bogii02/python-cat-api-test</h3>


### Built With

The following technologies were used during the project:

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Postgresql][Postgres]][Postgres-url]
* [![Docker][Docker]][Docker-url]
* [![Postman][Postman]][Postman-url]

<!-- GETTING STARTED -->

## Getting Started

<h3>If you want to try out the endpoints of this project, I recommend using Postman.</h3>
<h3>If you want to send, delete, or update a cat, you'll need to use a JSON structure with fields like name, age, and color.</h3>

<h3><code>{
   <span style="color:#D009F6">"name":</span> <span style="color:#2FF609">"Example"</span>,
   <span style="color:#D009F6">"age":</span> <span style="color:#2FF609">10</span>,
   <span style="color:#D009F6">"color":</span> <span style="color:#2FF609">"example"</span>
}
</code><h3>

<!-- FEATURES -->

## API Endpoints

- **GET /api/cats**: Retrieve all cats.

- **GET /api/cats/{cat_id}**: Get a cat by its ID.

- **POST /api/cats**: Create a new cat.

- **DELETE /api/cats/{cat_id}**: Delete a cat by its ID.

- **PUT /api/cats/{cat_id}**: Update information of a cat by its ID.


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
