# easycredit


 **Antes de comenzar**


URL : https://easy-credit.herokuapp.com/


GitHub: https://github.com/Marckhz/easycredit
Para la instalacion de todos los modulos del proyecto clonar el reposotorio de github. 
El proyecto se trabajo en Python con el microframework Flask. 



La instalacion de los paquetes se realiza mediante pip. Si tienes instalada una version de python2>=2.7 o python3>=3.4
no tendras problemas para la instalacion. 

El proyecto se puede correr de manera en general en sistema operativo pero, por preferencia personal me gusta crear ambientes virtuales ya que, de esa manera si tengo algun otro paquete instalado en mi sistema operativo que mi proyecto no necesite puedese llegar a causar conflicto. Al momento de desarrollarse localmente esto no puede ser de mucho problema, sin embargo, al llevar a produccion es probable que surgan conflictos.

Dentro del repositorio existe un archivo llamado requirements.txt  Este archivo contiene todos lo necesario
para continuar con el desarrollo del proyecto y de la misma manera para ejecutarse localmente.
Las instrucciones para instalar --> pip -r requirements.txt
Todas los paquetes que se hablaran a continuacion seran instalados mediante requirements.txt  asi que no hay que preocuparse por que falte alguno.

Despues de este comando se instalaran todas las dependencias para ejecutar el proyecto. 
El proyecto esta bajo Gunicorn que es un Python WSGI HTTP server para UNIX

Hay tres maneras de ejecutarse el servidor localmente, la primera mediante Heroku, la aplicacion esta alojada en Heroku, asi que es bueno ejecutar la aplicacion de esta manera pues nos da el historial de los errores que pueden llegar a pasar al darse el deploy. La segunda manera es ejecutar mediante Gunicorn, gunicorn es un tipo servidor HTTP este es simplemente mas robusto que el que contiene Flask por defecto. 
