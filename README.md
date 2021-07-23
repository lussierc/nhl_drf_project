# NHL Information DRF Project

The project & it's associated README are quite simple. The project uses Django and the Django REST Framework (DRF) to create a API containing hockey team information.

## Running the Project:
You can run the project using a virtual environment or locally, but ensure `python3`/`python` is on your system.

To use a virtual environment:
1. Create virtual env: `python3 -m venv ~/.virtualenvs/drf`
2. Enter virtual env shell: `source ~/.virtualenvs/drf/bin/activate`

Then, regardless of whether you are performing a local or virtual env run, run the following command to install the needed packages:
1. Install required packages using pip: `pip install requirements.txt`

Finally, you can run the project using the following commands:
1. Navigate to project source code directory: `cd src`
2. Run the Django App: `python3 manage.py runserver`
3. Open the outputted link in your web browser. You can then navigate to `/teams/` to view the API, `/teams/#/` where number is a corresponding team id to view a specific team, `/admin/` to view the Admin page, `/docs/` to view the Swagger Docs, or `/schema/` to get the API's associated schema.

Optional:
- Create a super-user: `python3 manage.py createsuperuser`
- Run tests using `python3 manage.py test`

## Features:
This project offers a variety of features:
- Admin Page
- User Authentication (accounts & tokens)
  - Users with authentication can perform POST, PUT, and similar tasks that non-authenticated users cannot perform
- Data serialization for defined models, with set attribute criteria
- Swagger Docs (with try-it-out examples, some of which require user authentication), auto-generated using `spectacular`
- View content from API by visiting endpoints
- etc...

## Potential Improvements:
Some potential improvements could be:
- Adding more models, such as a players model, that team models could reference.
- **More extensive testing** -- right now I am just testing model/serializer usage, but I should test things like authentication, usage of GET/POST/etc. commands, etc.
- Add a landing page or front-end that can interact with the create API.
- More extensive documentation for the Swagger Docs.
  - Could also fix the issue where some endpoints show they are locked when they are unlocked. This seems to be a spectacular library issue based on my research, so further investigation would be needed.
