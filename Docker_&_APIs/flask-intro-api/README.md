# Intro API with Flask

## Ressources

* Flask documentation: https://flask.palletsprojects.com/en/2.0.x/

* Conda cheatsheet: https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf

## Dependencies

* Anaconda or Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

## Setup

1. Create a new conda env named md4-api (if you haven't already) for the project in the Conda application or in the terminal:
```
conda create --name md4-api python=3.7 
```

2. Activate the conda env (you can check your availables env with: conda env list):
```
conda activate md4-api
```

3. Install the project python dependencies :
```
pip install -r requirements.txt
```

4. Install flask in your terminal to be able to launch it:
```
conda install -c conda-forge flask
```

5. Launch the API :
```
flask run --port=3000
```

## Project structure

-- resources : this folder will contains all the resources of the API
    
----- xxx.py : "xxx" will be replaced by the resource name

-- app.py : the main API file that will list all the available endpoints

-- config.py : this file will contain the configuration of the api

-- requirements.txt : this files will list the dependencies of the project

