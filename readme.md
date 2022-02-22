django-admin для старта
# Linux
sudo apt-get install python3-venv # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate  или .venv\Scripts\Activate.ps1
2. python -m pip install --upgrade pip
3. python -m pip install django

python manage.py           <command> [options]

python manage.py migrate # Создайте пустую базу данных разработки
python manage.py runserver   
[contenttypes]
    remove_stale_contenttypes

# [django] comand
{   check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
}
