heroku login

heroku addons:create heroku-postgresql:hobby-dev

heroku pg:wait

python deploy/csv2db.py

heroku create

git push heroku master

heroku ps:scale web=1

heroku open

