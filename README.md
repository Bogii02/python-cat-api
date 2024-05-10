<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">MERN APP</h3> 
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>        
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contact">Contact</a></li>    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project provides a backend service for managing cats through a RESTful API. You can perform various operations like fetching all cats, creating a new cat, deleting a cat, and updating cat information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

The following technologies were used during the project:

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![Postgresql][Postgres]][Postgres-url]
* [![Docker][Docker]][Docker-url]



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Installation

To get started with the Cat API backend, follow these steps:

1. Clone the repository.
   ```sh
   git clone git@github.com:Bogii02/python-cat-api.git
   ```
2. Change .env.sample file name to .env.
   ```sh
   mv .env.sample .env
   ```
3. Fill out .env file with necessary data.


4. Start the project
   ```sh
   docker compose up --build
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org

[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com