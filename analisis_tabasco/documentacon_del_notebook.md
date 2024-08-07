# DOCUMENTACIÓN

Aquí encontrarás las definiciones e información sobre el uso de funciones, modúlo u otras herramientas creadas para faciltar el trabajo de análisis en el proyecto.

**diccionario_dataset**

Es un módulo creado dentro del área global del repositorio con la finalidad de guardar funciones que pueden ser usadas en los notebooks para consultar información de soporte.

*diccionario_dataset.atajos("ver")*

Esta sentencia imprime la abreviación que se usa en los datasets 'datos...'  y muestra el nombre completo de las columnas al que hacen referencia las abreviaturas de las columnas de los datasets.

Se recomeinda usarla cuando se necesite conocer cuál es el significado de las cabeceras de las columnas. 

*print(diccionario_dataset.info_features("  "))*

Esta sentencia imprime la información necesaria para enteder cada feature de los datset 'datos...' desde a que hace referencia, como a los valores asignados por el INEGI y su significado.

Esta sentencia usa como parametro los nombres de las columnas del dataset. Para que la sentencia llame la información asociada a cada nombre de columna o feature se debe ingresar el nombre de dicha columna en los parentesis 'internos' y entre comillas simples o dobles.

Se envuelve la sentencia en la función "print()" para facilitar la visualizzación de la información y que esta sea presentada en formato parrafo. La sentencia funciona aún si esta no se envuelve en la función 'print'.

**diccionario_variables**

Es una utilidad creada para proporcionar información de las variables creadas en el notebook.

*print(diccionario_variables(" "))*

Esta sentencia imprime la información necesaria sobre las variables usadas en el notebook

La sentencia usa como parametros los nombres de las variables que se registran en la función 'diccionario_variables' y que corresponden a las usadas en el notebook. Para que la sentencia llame la información asociada a cada variable del notebook la variable debe existir en el diccionario de la función y se debe ingresar el nombre de dicha variable en los parentesis 'internos' de la sentencia y entre comillas simples o dobles.

Se envuelve la sentencia en la función "print()" para facilitar la visualizzación de la información y que esta sea presentada en formato parrafo. La sentencia funciona aún si esta no se envuelve en la función 'print', por ejemplo:

print(diccionario_variables("ruta_data"))