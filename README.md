# Learning [FastAPI](https://fastapi.tiangolo.com/tutorial/#run-the-code)

<details open>
<summary>First Steps</summary>

## First Steps

1. Python version used `Python 3.13.2`
2. Create a virtual environment using the following command on your terminal.
   ```bash
   python3 -m venv <venv_name>
   ```
3. Activate the virtual_env.
4. Install all the required packages using the following command:
   ```bash
   pip3 install -r requirements.txt
   ```
5. Set up your `.env` files for the required projects with the required credentials.
6. Navigate to any of the fastapi applications.
7. Run the following command on your terminal.

   `If the project has a main.py file:`

   ```bash
   fastapi dev main.py
   ```

   <br>

   `If the project does not have a main.py file.`

   ```bash
   uvicorn <filename>:app --reload
   ```
</details>
<details>
<summary>Notes</summary>

Fastapi is the framework and uvicorn is the ASGI (Asynchronous Server Gateway Interface) server that runs our application.

</details>
<details>
<summary>HTTP Request Methods</summary>

## HTTP Request Methods
- GET -> READ DATA
- POST -> CREATE DATA
- PUT -> UPDATE DATA
- DELETE -> DELETE DATA
</details>

<details>
<summary>Setup for FastAPI Authentication</summary>

## Setup for FastAPI Authentication
1. Install the following packages:

   ```bash
   pip3 install "python-jose[cryptography]" "passlib[bcrypt]" "python-multipart"
   ```

      <br> 
      View their documentations here:

   - [`python-jose[cryptography]`](https://pypi.org/project/python-jose/)
   - [`passlib[bcrypt]`](https://passlib.readthedocs.io/en/stable/install.html)
   - [`python-multipart`](https://pypi.org/project/python-multipart/)
   </details>

<details>
<summary>Resources</summary>

## Resources
- [**YouTube Video Tutorial**](https://youtu.be/0sOvCWFmrtA?si=m0TAHkn3qo-n7Ok3)
- [**YouTube Playlist**](https://youtube.com/playlist?list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq_&si=Ql6SZHEsI8XSJgzS)
- [**Annotated from Typing**](<https://stackoverflow.com/questions/71898644/how-to-use-python-typing-annotated#:~:text=Annotated%20in%20python%20allows%20developers,additional%20information%20related%20to%20it.&text=This%20tells%20that%20name%20is,(metadata)%20to%20a%20reference.>)
- [**Website used to generate the SECRET_KEY**](https://jwtsecret.com/generate)
- [**Official JWT Website used to encode and decode JWT tokens**](https://jwt.io/)
- [**Website for all SQLAlchemy `Database URLS`**](https://docs.sqlalchemy.org/en/20/core/engines.html)

### Other Resouces:
- [**Telling the DB to calculate current time**](https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime)
- [**Websockets using Fastapi (Offical Doc)**](https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime)

</details>
