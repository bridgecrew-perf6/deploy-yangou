






pipenv shell

pipenv install django

django-admin startproject yengou .
python manage.py startapp jelou

python manage.py runserver




---------- 











**consola**

pip install gunicorn


**settings.py**

DEBUG = False
ALLOWED_HOSTS = ['*']


import os

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


**consola**

pip install whitenoise


**settings.py**

'whitenoise.middleware.WhiteNoiseMiddleware',


**consola**



**settings.py**
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


**urls.py**
from django.conf import settings



urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('website.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



**En Raíz**
crear carpeta `static`
crear dentro el archivo `.keep`






**consola**

python manage.py collectstatic --noinput


pip freeze > requirements.txt

**En Raíz**

crear archivo `Procfile` con:

web: gunicorn aqui_nombre_del_proyecto.wsgi --log-file -



**consola**

heroku login

git init
git add .
git commit -am "make it better"

heroku git:remote -a proyecto
git remote -v


git push heroku master



heroku local
http://0.0.0.0:5000/



git checkout -b main
git branch -D master
git push heroku main























