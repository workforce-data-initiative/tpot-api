etp-api
=======

**etp-api** is a framework for a web service that provides an API for aggregated ETP outcomes. The default setting for the server is Heroku with Heroku Postgres database. The goal is for every institution to have an easy deployment for their ETP outcomes that could be used in more sophisticated tools, analyses and downstream applications by developers.

Quick Deployment
------------

One-click deploy

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


Quick Start for Developers
-----------

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
pip install requirements.txt
```

### 5. Run and deploy

Run the `deploy.sh` and enter the right information for Heroku username and password. The **etp-api** server will be deployed on Heroku.

```bash
./deploy.sh
```

### 6. Automating deployment using habitat

[Habitat](https://www.habitat.sh/) helps package an app or service into containers that can be run in any infrastructure, without committing to a specific container format or platform.

#### Installing habitat
To install habitat, simply download the binary.
* Unzip `hab` into `/usr/local/bin`
* Run `sudo chmod a+x hab` to make it executable.
* You'll also need docker installed if on Mac. Find docker [here](https://store.docker.com/editions/community/docker-ce-desktop-mac)
* To confirm if habitat is installed, re-open your terminal and type `hab` then press enter. You should see a list menu with all the habitat options available. Moving on swiftly!


#### Setup a habitat origin
* Run `hab setup` and set the origin name to **`brighthive`**.
* Go to Settings on your github account and create a Personal Access Token under Developer Settings. Here's a link to get you [there](https://github.com/settings/tokens/new).

The GitHub personal access token needs information provided from the `user:email` and `read:org` OAuth scopes. Habitat uses the information provided through these scopes for authentication and to determine features based on team membership.

This is how it should look like when running the setup:
<img width="636" alt="screenshot 2017-07-28 18 18 26" src="https://user-images.githubusercontent.com/15085180/28724015-5ac259ca-73c1-11e7-9eda-94e1fe74b3f2.png">


#### Running etp-api using habitat
* Cd into the repo's directory
```bash
cd etp-api
```

* Enter the habitat studio
```bash
hab studio enter
```
This is an awesome isolated environment for building great things so that when building, it doesn't affect anything on your computer.
Let's go ahead and build the etp-api!

* Inside the studio, run the `build` command to execute the etp-api plan
```bash
[5][default:/src:0]# build
```

License
-------
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
