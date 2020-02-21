# Couleur API
Scrapes instagram profiles for posts(images), generates color palettes for each post, returns hex values and image source 



## Install & run locally

Install:
```
git clone https://github.com/samg9/couleur.git  
cd couleur
```  
Create a virtualenv:  
```
python3 -m venv couleur   
```  
Activate it on Linux:
```
. couleur/bin/activate  
```  
Or on Windows cmd:  
```
couleur\Scripts\activate.bat  
```  
Install requirements:
```
pip install -r requirements.txt  
```  

export variables
```
export FLASK_APP=routes.py
```

Run app 
```
FLASK run
```

or via the Procfile with Gunicorn
```
gunicorn routes:app
```


View on [localhost:5000](http://127.0.0.1:5000)

