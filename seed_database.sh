rm db.sqlite3
rm -rf ./ezlifenubapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations ezlifenubapi
python3 manage.py migrate ezlifenubapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata genres
python3 manage.py loaddata games
python3 manage.py loaddata game_genres
python3 manage.py loaddata game_issue_tickets
