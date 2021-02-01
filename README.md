# Finance App

End-to-end fin-tech app built using AWS, Docker, PostgreSQL, Django, ReactJs and Plaid.

## Table of Contents

- [Motivation](#motivation)
- [About](#about)
- [Setup](#setup)
- [TODO](#todo)

<a name="motivation"></a>
## Motivation

#### One day, I hope to use technology to lift everyone in the world out of poverty.

I'm currently pretty far from achieving that goal, prior to this project, I have very little
experience working with any the technologies listed in this tech stack. So hopefully working on this
project gets me a few steps closer to changing the world.

Also, I just love to build/ship/hack, so this project really feels perfect for me.

<a name="About"></a>
## About

<i>&lt;&lt;insert a fancy visual diagram here&gt;&gt;</i>

Key tech things:

- AWS
    - Rationale: 
      - Cloud everything is a mystery to me
      - All the cool kids are using AWS
      - The learning curve between AWS and GCP is probably pretty low
- Docker
    - Rationale: Easy to deploy, develop and onboard
    - Dockerfile for Django backend
    - Dockerfile for ReactJs frontend
    - Docker compose file orchestration (lingo? I don't understand)
- PostgreSQL DB hosted on AWS
    - Rationale: because it's what all the cool kids are doing?
    - TBD: PostgreSQL DB will be hosted by AWS (lingo?)
- Django
    - Rationale:
        - Python is easy to write (I have an unjustified dislike of Javascript)
        - Django is easy to set up
        - Framework focuses on modularization, which is important to me :)
        - ORM features are pretty cool
    - TBD: Fill out more details around backend architecture
- ReactJs
    - Rationale:
        - Angular is better, but the learning curve is too high
        - Flutter or other PWA frameworks aren't what I'm looking for (yet)
    - TBD: Fill out more details around frontend architecture
- Plaid
    - Rationale: They are the defacto leaders in banking APIs and personal banking data
    - Used to fetch user's personal banking data, currently only operating in sandbox mode

<a name="setup"></a>
## Setup

A shorthand guide on how to reuse this code and get your own fintech app up and running:

- Install and setup Docker
- Clone the repo and setup your IDE (I use IntelliJ, cool kids use VS Code).
- Create a Plaid account
- Set the following environment variables:
    - RDS_PASSWORD
    - RDS_HOSTNAME
    - SECRET_KEY
    - DJANGO_DEBUG
- `$ cd /path/to/project/awsick && docker-compose -f docker-compose-dev.yml up --build`
- `$ open http://localhost`

You can restart a specific image using:
`$ docker-compose -f docker-compose-dev.yml up --build <image-name>`

<a name="todo"></a>
## TODO
List of things to do (ordered):

### Core Dev Tasks
- <strike>Fork [SaaS Boilerplate](https://github.com/saasitive/django-react-boilerplate) and get it working</strike>
- <strike>Get backend hot reloads to work in docker containers</strike>
- <strike>Get frontend hot reloads to work in docker containers</strike>
- <strike>Remove all secret things from the code base and use .env variables</strike>
- <strike>Setup PostgreSQL DB on AWS</strike>
- <strike>Switch from SQLite to PostgreSQL</strike>
- Build connect plaid account screen
- Build manage/remove plaid account screen
- Build caching layer for Plaid data

### Productionization Tasks
- Setup LetsEncrypt
- Setup hosting/web domain
- Setup docker-compose-prod.yml

### Polish Tasks
- Setup [YAPF](https://github.com/google/yapf) [pre-commit](https://github.com/pre-commit/pre-commit) hook.
- Update README with setup/getting started steps
- Write a script hosting everything locally
- Write a script to deploy everything to production
- Write a github action/workflow (lingo?) to automatically roll out to production
- Clean up gitignore, yaml, iml
- <strike>Clean up venv, pipfile, requirements.txt, package.json, pipenv</strike>
