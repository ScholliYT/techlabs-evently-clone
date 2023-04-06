 ## TODO for the Techies
Please **fill out the following information below**, as soon as possible. It is **required** to have this file completely filled out and up to date at the end of the project phase.
You can of course use this file to manage your project, e.g. as a place to keep your todos and to plan your features. Also, feel free to edit this readme in any kind of way you like, but the required base layout and information should be consistent throughout all techie projects.

**Hint:** The following file is written in `markdown` which is a language to format text with simple characters. If you are unsure on how to use markdown then have a look at [this guide](https://www.markdownguide.org/basic-syntax/)

By the end you should have filled out the following:
1. **Project Title:** The title of the project, including a description which states the motivation/problem of the project and the developed solution.
2. **How to Setup and Run:** The respective commands to install and run the project
3. **Examples:** A brief overview on how to use the main functionalities of your project (does not have to be code)
4. **Roadmap:** The general outline of what you want to do in what order. Please keep this up to date, so that we can follow what you are and will be doing.
5. **Authors:** Please add all of you and link your respective GitHub profile and other information if you want to. This part if completely up to you.
6. If you are done filling out the information below, please **delete this TODO Section** to keep your project readme clean for other people to get to know more about your project.

# Evently - Find events, sign up, meet new people!

There are a ton of things to do in the Dortmund area… and a lot of people to do them with! Evently offers users an online platform on which to meet other users with shared interests and bond in real life by attending fun events in the Dortmund area. The website therefore facilitates finding and participating in social activities - something some people struggle with, because they are new in town or because prolongued Covid-quarantines have impaired their social skills.


## How to Setup and Run

In order to setup and run the project, please proceed as follows:

```
python3 -m venv venv && source venv/bin/activate

pip3 install -r requirements.txt

start python application

either via VSCode (Run & Debug) or via `python3 main.py`

Open http://127.0.0.1:8000
and open http://127.0.0.1:8000/api/docs

```

## Examples

You can see a brief overview of how to use the main functionality below

```
Backend:

def load_csv_data() in app/main.py:
- loads data from csv file into database

via http://127.0.0.1:8000/api/docs
GET event (reading all events)
POST event (manually adding events to database)
GET event by id
PUT event (update event information)
DELETE event

Frontend:

- filtering events (skipping to categories)
- being transferred to website when clicking on event
- creating own events

```

  
## Roadmap and future goals

What we did so far:
- searching data
- manipulating and cleaning data file
- building RestAPI
- GET/POST/PUT/DELETE functions
- building frontend
- connecting backend and frontend
- working create event button 
- frontend finetuning
- including pictures in databank

What we would do next:
- adding comment and chat function
- adding user profiles
- options for people to connect (friend requests)
- seperate page for every location including upcoming events/meetings
- including other cities
- ...

  
## Authors

- [@laurastaedtler](https://github.com/laurastaedtler)
- [@Leonardo-Bia](https://github.com/Leonardo-Bia)
- [@maxlearnscode](https://github.com/maxlearnscode)
- [@Jannik-V](https://github.com/Jannik-V)
- [@GitHubMagnus](https://github.com/GitHubMagnus)
- [@DerEmmanuel2004](https://github.com/DerEmmanuel2004)

  

