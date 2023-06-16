Herramienta Digital: Recordatorio de Eventos y Mensajes de WhatsApp 

Esta herramienta digital utiliza la API de Google Calendar para obtener los próximos eventos de tu calendario y enviar mensajes de WhatsApp a los contactos asociados a esos eventos. 
Guía de Usuario 

    Asegúrate de tener instaladas las siguientes librerías: 
        google-auth
        google-auth-oauthlib
        google-auth-httplib2
        google-api-python-client
        pyautogui
        keyboard
        tkinter

    Obten tu archivo JSON de credenciales de la API de Google Calendar y guárdalo en el mismo directorio que este script. Asegúrate de que el nombre del archivo sea  googleusercontent.com.json. (Puedes obtener el archivo JSON de las  credenciales de la API de Google Calendar ). 

    Ejecuta el script. Se abrirá una ventana emergente para autenticarte en tu cuenta de Google. 

    Una vez autenticado, la herramienta buscará los próximos eventos en tu calendario y mostrará el primero en la ventana emergente. 

    Si el evento es para el día actual, se enviará un mensaje de WhatsApp al contacto asociado al evento. Asegúrate de tener WhatsApp Web abierto en tu navegador antes de ejecutar la herramienta. 

Guía de Instalación 

    Clona o descarga el repositorio en tu máquina local. 

    Asegúrate de tener Python 3 instalado en tu sistema. 

    Instala las siguientes dependencias utilizando pip: 

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pyautogui keyboard tkinter

Obtén tu archivo JSON de credenciales de la API de Google Calendar y guárdalo en la misma carpeta que el script. Asegúrate de que el nombre del archivo sea  googleusercontent.com.json. 

Ejecuta el script utilizando el siguiente comando: 

    python script.py

Dependencias

    google-auth: librería para autenticación con Google.
    google-auth-oauthlib: librería para autenticación con OAuth2 para Google APIs. 
    google-auth-httplib2: librería para autenticación HTTP con Google para Google APIs. 
    google-api-python-client: cliente de Python para Google APIs. 
    pyautogui: librería para automatización de la interfaz de usuario. 
    keyboard: librería para el manejo de eventos del teclado. 
    tkinter: librería para la creación de interfaces gráficas. 

Cómo Contribuir 

Si deseas contribuir a este proyecto, puedes seguir estos pasos: 

    Haz un fork del repositorio. 

    Realiza tus modificaciones en tu propio repositorio. 

    Envía una solicitud de extracción ("pull request") para que podamos revisar tus cambios. 

    Agradecemos cualquier contribución que hagas para mejorar esta herramienta. 

Autor/es 

    yggDev 

Información Adicional 

    Si deseas obtener más información sobre la API de Google Calendar, visita la  documentación oficial . 

Licencia 

Este proyecto se encuentra bajo la licencia  MIT License . Consulta el archivo LICENSE.md para más detalles.

Expresiones de Gratitud 🎁 

    Comenta a otros sobre este proyecto 📢 


