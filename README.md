# Django_Custom_user

# Step 1
Clone the project
```
git clone git@github.com:amirhosseindehghan1/Django_Custom_user.git
```

# Step 2
Create Virtual Environment or Run this project with Docker

# Step 3
Run this command
```
python manage.py migrate
```
or
```
docker exec -it container_name_or_id sh -c 'python manage.py migrate'
```

# Step 4
Create SuperUser

```
python manage.py createsuperuser
```
or
```
docker exec -it container_name_or_id sh -c 'python manage.py createsuperuser'
```

Finaly run the project