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
    - plaid key 1
    - plaid key 2
    - TBD
- `$ tbd.sh`
- `$ open http://0.0.0.0`

<a name="todo"></a>
## TODO
List of things to do (ordered):

- <strike>Fork [SaaS Boilerplate](https://github.com/saasitive/django-react-boilerplate) and get it working</strike>
- Get backend hot reloads to work in docker containers
- Get frontend hot reloads to work in docker containers
- Remove all secret things from the code base and use environment variables (lingo?)
- Write a script hosting everything locally
- Setup PostgreSQL DB on AWS
- Switch from SQLite to PostgreSQL
- Write a script to deploy everything to production
- Write a github action/workflow (lingo?) to automatically roll out to production
- Build connect plaid account screen
- Build manage/remove plaid account screen
- Build caching layer for Plaid data
- Clean up venv, gitignore, pipfile, requirements.txt, package.json, yaml, pipenv, iml

