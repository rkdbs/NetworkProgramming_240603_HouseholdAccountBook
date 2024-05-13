# helloidol2
---

1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2
   3. File > Settings... > Language & Frameworkds > Django
        [v] Enable Django Support
   4. Run > Edit Configurations... > + > Django Server > Name: runserver
   5. VCS > Enable Version Control Intergration... > git > ok
2. startapp 브레드이발소
   1. python manage.py startapp 브레드이발소
   2. '브레드이발소', in INSTALLED_APPS in settings.py
3. 브레드이발소/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
      2. python manage.py makemigrations 브레드이발소
      3. python manage.py migrate 브레드이발소