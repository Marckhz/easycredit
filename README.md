# easycredit


 **Antes de comenzar**




**-------------------------------------------------------------------------------------------------------------------------**

URL : https://easy-credit.herokuapp.com/

**-------------------------------------------------------------------------------------------------------------------------**

GitHub: https://github.com/Marckhz/easycredit

**-------------------------------------------------------------------------------------------------------------------------**

Para la instalacion de todos los modulos del proyecto clonar el reposotorio de github. 
El proyecto se trabajo en Python con el microframework **Flask**. 

La instalacion de los paquetes se realiza mediante pip. Si tienes instalada una version de **python2>=2.7 o python3>=3.4**
no tendras problemas para la instalacion. 

El proyecto se puede correr de manera en general en sistema operativo pero, por preferencia personal me gusta crear ambientes virtuales ya que, de esa manera si tengo algun otro paquete instalado en mi sistema operativo que mi proyecto no necesite puedese llegar a causar conflicto. Al momento de desarrollarse localmente esto no puede ser de mucho problema, sin embargo, al llevar a produccion es probable que surgan conflictos.

**-------------------------------------------------------------------------------------------------------------------------**

crear ambiente virtual --->  **pip install virtualenv**   ---- > **virtualenv myfolder**

**-------------------------------------------------------------------------------------------------------------------------**

Dentro del repositorio existe un archivo llamado requirements.txt  Este archivo contiene todos lo necesario
para continuar con el desarrollo del proyecto y de la misma manera para ejecutarse localmente.
**Instruccion para instalar --> pip -r requirements.txt **
Todas los paquetes que se hablaran a continuacion seran instalados mediante requirements.txt  asi que no hay que preocuparse por que falte alguno.

El proyecto instalable se encuentra en la carpeta **dist** este es un archivo de tipo whl. Se instala mediante pip
**-------------------------------------------------------------------------------------------------------------------------**
**pip install "el archivo**
**-------------------------------------------------------------------------------------------------------------------------**

Instalara todo el proyecto de la manera en la que fue desarrollado. 

Despues de este comando se instalaran todas las dependencias para ejecutar el proyecto. 
El proyecto esta bajo Gunicorn que es un Python WSGI HTTP server para UNIX

Para ejecutar el servidor  primero es necesario ejecutar estos dos comandos. 


**export FLASK_APP=flaskr**
**export FLASK_ENV=env**


El proyecto se comporta como paquete es por esto la razon de este estilo de ejecucion.

Se utilizo SQLite3, Para inicializar la base datos ---> **flask init-db**

Ejecutar servidor ---> **flask run**
Es todo lo que se necesita para ejecutar el proyecto. 

