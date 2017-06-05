etp-api
=======

**etp-api** is a framework for a web service that provides an API for aggregated ETP outcomes. The default setting for the server is Heroku with Heroku Postgres database. The goal is for every institution to have an easy deployment for their ETP outcomes that could be used in more sophisticated tools, analyses and downstream applications by developers.

[live demo](http://etp-api.dataatwork.org/api/v0)

Quick Deployment
------------

One-click deploy

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Quick Start for Developers

### 1. Prerequisites

- Have a [Heroku account](https://dashboard.heroku.com/).
- Have [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.
- Have a `data.csv` file in `/deploy` directory that matches the schema as `example_data.csv` in `/test` directory.



### 2. Clone repository

**etp-api** is available through cloning the repository and then working from the repository root.

```bash
git clone https://github.com/workforce-data-initiative/etp-api.git
cd etp-api
```


### 3. Virtualenv

**etp-api** depends on python3, so create a virtual environment using a python3 executable. Then activate the virtualenv.

```bash
virtualenv venv -p /usr/bin/python3
source venv/bin/activate
```
### 4. Python requirements

Install requirements.

```bash
pip install -r requirements.txt
```

### 5. Run and deploy

Run the `deploy.sh` and enter the right information for Heroku username and password. The **etp-api** server will be deployed on Heroku.

```bash
./deploy.sh
```

License
-------
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
