
def atajos(accion):
    #función que retorna los shortcuts para acceder a la definición de la nomenclatura

    atajo = [
        "tipo_divorcio",
        "ent_regis", 
        "mun_regist",
        "loc_regis",
        "tloc_regis",
        "ent_mat",
        "mun_mat",
        "local_mat",
        "tloc_mat",
        "dia_mat",
        
        "mes_mat",
        "anio_mat",
        "dia_reg",
        "mes_reg",
        "anio_reg",
        "dia_sen",
        "mes_sen",
        "anio_sen",
        "dia_eje",  
        "mes_eje",

        "anio_eje",
        "ini_juic",
        "favor",
        "caus",
        "hijos",
        "hijos_men",
        "custodia",
        "cus_hij",
        "pat_pot",
        "pat_hij",

        "pension",
        "pen_hij",
        "naci_div1",
        "edad_div1",
        "nacim_div1",
        "eciv_adiv1",
        "ent_rhdiv1",
        "mun_rhdiv1",
        "loc_rhdiv1",
        "tloc_div1",
        
        "escol_div1",
        "con_acdiv1",
        "dedic_div1",
        "postr_div1",
        "sexo_div1",
        "naci_div2",
        "edad_div2",
        "nacim_div2",
        "eciv_adiv2",
        "ent_rhdiv2",
        
        "mun_rhdiv2",
        "loc_rhdiv2",
        "tloc_div2",
        "escol_div2",
        "con_acdiv2",
        "dedic_div2",
        "postr_div2",
        "sexo_div2",
        "dura_soc",
        "dura_leg",

        "edad_mdiv1",
        "edad_mdiv2",
        "t_dvante",
        "dis_reoax"
        ]

    descripcion = [
        "Tipo de divorcios comtemplados en México",
        "Entidad donde se inicio el tramite de divorcio"
        "Municipio o alacaldía de registro",
        "Localidad de registro",
        "Tamaño de localidad de registro",
        "Entidad de registro del matrimonio",
        "Municipio o alcaldía de registro del matrimonio",
        "Localidad de registro del matrimonio",
        "Tamaño de localidad de registro del matrimonio",
        "Día de registro del matrimonio",

        "Mes de registro del matrimonio",
        "Año de registro del matrimonio",
        "Día de registro de la demanda",
        "Mes de registro de la demanda",
        "Año de registro de la demanda",
        "Día de la sentencia",
        "Mes de la sentencia",
        "Año de la sentencia",
        "Día de ejecutoria del divorcio",
        "Mes de ejecutoria del divorcio",


        "Año de ejecutoria del divorcio",
        "Persona que inicio el juicio",
        "A favor de quien se resolvió el juicio",
        "Causas de divorcio",
        "Número de hijos en el matrimonio",
        "Número de hijos menores de edad",
        "Persona a quien se otorga la custodia",
        "Número de hijos en custodia",
        "Persona a quien se le asigna la patria potestad",
        "Número de hijos en patria potestad",
        
        "Personas a quien se le asigna la pensión alimenticia",
        "Número de hijos a quienes se les asigna la pensión alimenticia",
        "Nacionalidad del primer divorciante",
        "Edad al divorcio del primer divorciante",
        "Año de nacimiento del primer divorciante",
        "Estado conyugal (civil) anterior del primer divorciante",
        "Entidad de residencia habitual del primer divorciante",
        "Municipio o alcaldía de residencia habitual del primer divorciante",
        "Localidad de residencia habitual del primer divorciante",
        "Tamaño de localidad de residencia habitual del primer divorciante",
        
        "Nivel de escolaridad del primer divorciante (escolaridad)",
        "Condición de actividad económica del primer divorciante",
        "A qué se dedica el primer divorciante",
        "Posición en el trabajo del primer divorciante",
        "Sexo del primer divorciante",
        "Nacionalidad del segundo divorciante",
        "Edad al divorcio del segundo divorciante",
        "Año de nacimiento del segundo divorciante",
        "Estado conyugal (civil) anterior del segundo divorciante",
        "Entidad de residencia habitual del segundo divorciante",

        "Municipio o alcaldía de residencia habitual del segundo divorciante",
        "Localidad de residencia habitual del segundo divorciante",
        "Tamaño de localidad de residencia habitual del segundo divorciante",
        "Nivel de escolaridad del segundo divorciante (escolaridad)",
        "Condición de actividad económica del segundo divorciante",
        "A qué se dedica el segundo divorciante",
        "Posición en el trabajo del segundo divorciante",
        "Sexo del segundo divorciante",
        "Duración social del matrimonio",
        "Duración legal del matrimonio",


        "Edad al matrimonio del primer divorciante",
        "Edad al matrimonio del segundo divorciante",
        "Tipo de divorciante",
        "Distritos de registro de Oaxaca"
    ]

    if accion == "ver":
        print("Estos son los terminos usandos en el data set")

        resultado = [f'"{a}" ---> "{d}"' for a, d in zip(atajo, descripcion)]

        for r in resultado:
            print(r)
    
    atajos("ver")


#atajos("ver")


def info_features(a):

    atajo = {

        'tipo_divorcio' : "Guarda el tipo de tramite del cuál se recoge información en el conjunto de datos.\n Se designa la **clave '1'** para divorcio Judicial y la **clave '2'** para divorcio Administrativo.\n Recibe valores de **tipo N**, es decir numéricos.",

        'ent_regis' : "Guarda la entidad donde se realiza el tramite de divorcio.\n Se designan claves del '01' al '32' para identificar las entidades federativas (Estados),\n la clave '33' para aquellos divorcios (de matrimonios realizados en territorio mexicano)\n realizados en los Estados Unidos de América,\n la calve '34' para aquellos divorcios (de matrimonios realizados \n en territorio mexicano) realizados en los otros paises de Latiniamérica,\n la clave '35' para aquellos divorcios (de matrimonios realizados en territorio mexicano) \n realizados en cualquier otro país que no forme parte de las anteriores consideraciones.\n Recibe valores de **tipo C**, es decir categóricos",

        "mun_regist" : "Guarda la entidad donde se realiza el tramite de divorcio. \n \n Se designan claves del '01' al '32' para identificar las entidades federativas (Estados),\n la clave '33' para aquellos divorcios (de matrimonios realizados en territorio mexicano)\n realizados en los Estados Unidos de América,\n la calve '34' para aquellos divorcios (de matrimonios realizados en \n territorio mexicano) realizados en los otros paises de Latiniamérica,\n la clave '35' para aquellos divorcios (de matrimonios realizados en territorio mexicano) \n realizados en cualquier otro país que no forme parte de las anteriores consideraciones. \n Recibe valores de **tipo C**, es decir categóricos",

        "loc_regis" : "Guarda la localidad donde se realiza el tramite. \n \n Se designan claves del '0000' al '3395' para identificar las localidades del territorio mexicano, \n mientras que la clave designa '7777' 'Cifra confidencial. Establecido en la Ley del SNIEG.',\n la clave '9998' y '9999' indica 'localidad no especificada'\n \n Recibe valores de tipo C, es decir categóricos",

        "tloc_regis" : "Guarda el rango poblacional de la  donde se realizó l tramite de divorcio, \n designando claves que van del 1 al 17 para los rangos de población, la clave '98' para no aplica y '99' para 'No especificada' \n \n clave, descripción  \n \n1,  De 1 a 999 habitantes\n 2,  De 1 000 a 1 999 habitantes\n 3,  De 2 000 a 2 499 habitantes\n 4,  De 2 500 a 4 999 habitantes\n 5,  De 5 000 a 9 999 habitantes\n 6,  De 10 000 a 14 999 habitantes\n 7,  De 15 000 a 19 999 habitantes\n 8,  De 20 000 a 29 999 habitantes\n 9,  De 30 000 a 39 999 habitantes\n 10, De 40 000 a 49 999 habitantes\n 11, De 50 000 a 74 999 habitantes\n 12, De 75 000 a 99 999 habitantes\n 13, De 100 000 a 249 999 habitantes\n 14, De 250 000 a 499 999 habitantes\n15, De 500 000 a 999 999 habitantes\n 16, De 1 000 000 a 1 499 999 habitantes\n 17, De 1 500 000 y más habitantes\n 98, No aplica\n 99, No especificado",

        "ent_mat" : "Guarda la entidad donde se realizó el regirto del metrimonio. \n \n Se designan claves del '01' al '32' para identificar las entidades federativas (Estados),\n la clave '33' para aquellos divorcios (de matrimonios realizados en territorio mexicano)\n realizados en los Estados Unidos de América, \n la calve '34' para aquellos divorcios (de matrimonios realizados en territorio mexicano)\n realizados en los otros paises de Latiniamérica, la clave '35' para aquellos divorcios \n (de matrimonios realizados en territorio mexicano) realizados en cualquier \n otro país que no forme parte de las anteriores consideraciones.\n \n Recibe valores de **tipo C**, es decir categóricos",

        "mun_mat" : "Guarda la municipalidad donde se realizó el registro de matrimonio. \n \n Se designan claves del '000' al '930' para identificar las municipalidades del territorio mexicano, \n  mientras que la clave '998' indica la categoría 'no aplica y la clave '999'\n  indica 'municipio no indicado' \n \n Recibe valores de tipo C, es decir categóricos",

        "local_mat" : "Guarda la localidad donde se realizó el registro del metrimonio. \n \n Se designan claves del '0000' al '3395' para identificar las localidades del territorio mexicano,\n  mientras que la clave designa '7777' 'Cifra confidencial. Establecido en la Ley del SNIEG.' \n, la clave '9998' y '9999' indica 'localidad no especificada' \n\nRecibe valores de tipo C, es decir categóricos",

        "tloc_mat" : "Guarda el rango poblacional de la localidad donde se realizó el regirtro del matrimonio, \n designando claves que van del 1 al 17 para los rangos de población, la clave '98' para no aplica y '99' para 'No especificada' \n\n clave, descripción \n \n 1,  De 1 a 999 habitantes \n 2,  De 1 000 a 1 999 habitantes \n 3,  De 2 000 a 2 499 habitantes \n 4,  De 2 500 a 4 999 habitantes \n 5,  De 5 000 a 9 999 habitantes \n 6,  De 10 000 a 14 999 habitantes \n 7,  De 15 000 a 19 999 habitantes \n 8,  De 20 000 a 29 999 habitantes\n 9,  De 30 000 a 39 999 habitantes \n 10, De 40 000 a 49 999 habitantes \n 11, De 50 000 a 74 999 habitantes \n 12, De 75 000 a 99 999 habitantes \n 13, De 100 000 a 249 999 habitantes \n 14, De 250 000 a 499 999 habitantes \n 15, De 500 000 a 999 999 habitantes \n 16, De 1 000 000 a 1 499 999 habitantes \n 17, De 1 500 000 y más habitantes \n 98, No aplica",

        "dia_mat" : "Guarda el día del mes en el que se ralizó el registro del matrimonio. \n \n Se asignan valores del 1 al 31 para los días y el valor 99 para describir un valor no especificado.",

        "mes_mat" : "Guarda el mes en el cual se realiza el registro del matrimonio de la siguiente manera: \n \n clave,   descripción \n \n 1,       Enero \n 2,       Febrero \n 3,       Marzo\n 4,       Abril \n 5,       Mayo \n 6,       Junio \n 7,       Julio \n 8,       Agosto \n 9,       Septiembre \n 10,      Octubre \n 11,      Noviembre \n 12,      Diciembre \n 99,      No especificado",

        "anio_mat" : "Registra el año que se realizó el matrimonio con valores desde **1950** hasta el año de recolección de cada conjunto de datos",

        "dia_reg" : "Guarda el día del mes en el que se ralizó el registro de la demanda de divorcio. \n \n Se asignan valores del 1 al 31 para los días y el valor 99 para describir un valor no especificado.",

        "mes_reg" : "Guarda el mes en el cual se realiza el registro de la demanda de la siguiente manera: \n \n clave,   descripción \n 1,       Enero \n 2,       Febrero \n 3,       Marzo \n 4,       Abril \n 5,       Mayo \n 6,       Junio \n 7,       Julio \n 8,       Agosto \n 9,       Septiembre \n 10,      Octubre \n 11,      Noviembre \n 12,      Diciembre \n 99,      No especificado",

        "anio_reg" : "Registra el año que se registro la demanda de divorcio con valores desde **1950** hasta el año de recolección de cada conjunto de datos",

        "dia_sen" : "Guarda el día del mes en el que se emitio la sentencia de la demanda de divorcio.\n\n Se asignan valores del 1 al 31 para los días y el valor 99 para describir un valor no especificado.",

        "mes_sen" : "Guarda el mes en el cual se emitió la sentencia de la demanda de divorcio de la siguiente manera: \n \nclave, descripción 1, Enero 2, Febrero 3, Marzo 4, Abril 5, Mayo 6, Junio 7, Julio 8, Agosto 9, Septiembre 10, Octubre 11, Noviembre 12, Diciembre 99, No especificado",

        "anio_sen" : "Contiene el año en el cuál se emitió la sentencia de la demanda de divorcio. Se asignan valores desde **1950** hasta el año de recolección de cada conjunto de datos.",

        "dia_eje" : "Contiene el día del mes en el que se realiza la ejecutoria de divorcio. \n \n Se asignan valores del 1 al 31 para los días y el valor 99 para describir un valor no especificado.",

        "mes_eje" : "Contiene el mes en el cual se efectua la ejecutoria de la demanda de divorcio de la siguiente manera:clave, descripción 1, Enero 2, Febrero 3, Marzo 4, Abril 5, Mayo 6, Junio 7, Julio 8, Agosto 9, Septiembre 10, Octubre 11, Noviembre 12, Diciembre 99, No especificado",

        "anio_eje" : "Contiene el año en el cuál se realizó la ejecutoria de divorcio. Se asignan valores desde 1950 hasta el año de recolección de cada conjunto de datos.",

        "ini_juic" : "Indica cuál de los conyuges inicia el proceso de divorcio. clave,   descripcion 1,       Divorciante 1 2,       Divorciante 2 3,       Ambos 9,       No especificado",

        "favor" : "Indica a favor de quién se resolvio la demanda: clave, descripcion 1, Divorciante 1 2, Divorciante 2 3, Ambos 9, No especificado",

        "caus" : "Contiene las causales presentadas para iniciar la demanda de divorcio, de la siguiente forma: clave,descripcion 1,Mutuo consentimiento 2,Adulterio o infidelidad sexual 3,Alumbramiento ilegítimo 4,Propuesta de prostitución 5,Incitación a la violencia 6,Corrupcion y/o maltrato a los hijos 7,'Enfermedad crónica o incurable, la impotencia o esterilidad incurable' 8,Enajenación mental incurable o el estado de interdicción declarado por sentencia 9,'Separación del hogar conyugal por más de 1 año, con o sin causa justificada' 10,'Abandono de hogar por más de 3 o 6 meses, sin causa justificada' 11,Declaración de ausencia o presunción de muerte 12,'Sevicia, amenazas o injurias o la violencia intrafamiliar' 13,Negativa a contribuir voluntariamente o por sentencia del juez familiar al sostenimiento del hogar 14,Acusación calumniosa 15,Haber cometido delito doloso o infamante 16,'Hábitos de juego, embriaguez o drogas' 17,Cometer acto delictivo contra el cónyuge 18,Incompatibilidad de caracteres 19,La separación por 2 años o más independientemente del motivo 20,La bigamia 21,'No acompañar la mujer a su marido, cuando cambie de residencia dentro o fuera del país' 22,'Si un cónyuge solicitó el divorcio por causa injustificada, el demandado puede divorciarse 3 meses después de la última sentencia' 23,Fecundación asistida sin consentimiento del cónyuge 24,Impedir uno de los cónyuges a otro desempeñar una actividad lícita 25,Reconocer la mujer a un hijo nacido antes del matrimonio sin consentimiento del marido 26,Uso de métodos de esterilización permanente sin consentimiento del cónyuge 27,'Bisexualidad manifestada, o intención o cambio de sexo por tratamiento médico o quirúrgico' 28,Voluntario unilateral 99,No especificada",

        "hijos" :  "Contiene el numero de hijos existententes en el matrimonio desde 0 hasta 25 y se designan las claves 98 para no aplica y la clave 99 para no especificado",
        ####
        "hijos_men" : "Contiene el número de hijos existentes en el matrimonio que son menores de edad, se cuenta desde 0 hasta 25 y se designa la clave 98 para 'No aplica' y la clave '99' para 'No especificado'",

        "custodia" : "Contiene la asignación de custodia de los menores de edad dentro del matrimonio, de las siguente forma:clave,descripción 0,No se otorga 1,Divorciante 1 2,Divorciante 2 3,Ambos 4,Otro 98,No aplica 99,No especificado",

        "cus_hij" : "Contiene los datos sobre el número de hijos en custodia dentro del matrimonio, se cuenta desde 0 hasta 25 y se asigna la clave 98 para 'No aplica' y la clave 99 para 'No especificado'",

        "pat_pot" : "Contiene los datos sobre el otorgamiento de la patri potestad de los hijos de la siguiente forma: clave,descripción 0,No se otorga 1,Divorciante 1 2,Divorciante 2 3,Ambos 4,Otro 98,No aplica 99,No especificado",

        "pat_hij" : "Contiene el número de hijos que se encuentran bajo patria potestad se cuenta desde 0 hasta 25 y se asigna la clave 98 para 'No aplica' y la clave 99 para 'No especificado'",

        "pension" : "Contiene el dato sobre a que persona se le asigna la pensión alimenticia. clave,descripción 1,Hijos 2,Divorciante 1 3,Divorciante 2 4,Ninguno 12,Hijos y Divorciante 1 13,Hijos y Divorciante 2 98,No aplica 99,No especificado",

        "pen_hij" : "Contiene información sobre el numero de hijos a los que se les asigna pensión se cuenta desde 0 hasta 25 y se asigna la clave 98 para 'No aplica' y la clave 99 para 'No especificado'",

        "naci_div1" : "Contiene el dato sobre la necionalidad del primer divorciante de la siguiente forma: clave,descripción 1,Mexicana 2,Extranjera",

        "edad_div1" : "Contiene la edad del divorciante 1 al moemnto del divorcio. Se asignan valores numéricos del 0 al 95 para designar la edad y se asigna el valor 999 para 'No especificado'",

        "nacim_div1" : "Contiene el año de nacimiento del primer divorciante.Asigna valores desde 1920 hasta 2005 para los años de nacimientos y el valor 999 para 'No especificado'",

        "eciv_adiv1" : "Contiene el estado conyugal o civil del primer divorciante antes del matrimonio actual. clave,descripción 1,Soltero 2,Unión libre 3,Divorciado 4,Separado 5,Viudo 9,No especificado",

        "ent_rhdiv1" : "Entidad de residanecia habitual del primer divorciante Se designan claves del '01' al '32' para identificar las entidades federativas (Estados), la clave '33' para aquellos divorcios (de matrimonios realizados en territorio mexicano) realizados en los Estados Unidos de América, la calve '34' para aquellos divorcios (de matrimonios realizados en territorio mexicano) realizados en los otros paises de Latiniamérica, la clave '35' para aquellos divorcios (de matrimonios realizados en territorio mexicano) realizados en cualquier otro país que no forme parte de las anteriores consideraciones. Recibe valores de **tipo C**, es decir categóricos",

        "mun_rhdiv1" : "Contiene el municipo o alcaldía de residencia habitual del primer divorciante. Se designan claves del '000' al '930' para identificar las municipalidades del territorio mexicano, mientras que la clave '998' indica la categoría 'no aplica y la clave '999' indica 'municipio no indicado' Recibe valores de tipo C, es decir categóricos",

        "loc_rhdiv1" : "Contiene la localidad de residencia habitual del primer divorciante. Se designan claves del '0000' al '3395' para identificar las localidades del territorio mexicano, mientras que la clave designa '7777' 'Cifra confidencial. Establecido en la Ley del SNIEG.', la clave '9998' y '9999' indica 'localidad no especificada' Recibe valores de tipo C, es decir categóricos",

        "tloc_div1" : "Contiene el tamaño de localidad donde habitualmente reside el primer divorciante. Se designan claves que van del 1 al 17 para los rangos de población, la clave '98' para no aplica y '99' para 'No especificada' clave, descripción 1, De 1 a 999 habitantes 2, De 1 000 a 1 999 habitantes 3, De 2 000 a 2 499 habitantes 4, De 2 500 a 4 999 habitantes 5, De 5 000 a 9 999 habitantes 6, De 10 000 a 14 999 habitantes 7, De 15 000 a 19 999 habitantes 8, De 20 000 a 29 999 habitantes 9, De 30 000 a 39 999 habitantes 10, De 40 000 a 49 999 habitantes 11, De 50 000 a 74 999 habitantes 12, De 75 000 a 99 999 habitantes 13, De 100 000 a 249 999 habitantes 14, De 250 000 a 499 999 habitantes 15, De 500 000 a 999 999 habitantes 16, De 1 000 000 a 1 499 999 habitantes 17, De 1 500 000 y más habitantes 98, No aplica 99, No especificado",

        "escol_div1" : "Contiene el nivel de escolaridad del primer divorciante. clave,  descripción 0,  Sin escolaridad 1,  1 a 3 años de primaria 2,  4 a 5 años de primaria 3,  Primaria completa 4,  Secundaria o equivalente 5,  Preparatoria o equivalente 6,  Superior 7,  Carrera técnica 8,  Otra 9,  No especificada",

        "con_acdiv1" : "Contiene la condición de actividad económica del primer divorciante. Asignando el valor de 1 para 'Trabaja', el valor de 2 para 'No trabaja' y el valor de 9 para 'No especificado'.",

        "dedic_div1" : "Contiene ocupación del primer divorciante en esta estructura: clave,descripción 1,Trabaja 2,Al hogar  3,Estudiante 4,Pensionado o jubilado 5,Rentista 6,Incapacitado permanentemente para trabajar 7,Busca trabajo 8,Otra (no trabaja) 9,No especificada",

        "postr_div1" : "Posición en el trbajo del primer divorciante. clave,descripción 1,Empleado 2,Obrero 3,Jornalero o peón agrícola 4,Patrón o empresario 5,Miembro de cooperativa 6,Trabajador no remunerado 7,Trabajador por cuenta propia 8,Otra 9,No especificada",

        "sexo_div1" : "Sexo del primer divorciante. clave,descripción 1,Hombre 2,Mujer",

        "naci_div2" : "Nacionalidad del segundo divorciante clave,descripción  1,Mexicana 2,Extranjera",

        "edad_div2" : "Edad del segundo divorciante al momento del divorcio. Se asignan valores numéricos del 0 al 95 para designar la edad y se asigna el valor 999 para 'No especificado'",

        "nacim_div2" : "Año de nacimiento del segundo divorciante. Contiene el año de nacimiento del primer divorciante.Asigna valores desde 1920 hasta 2005 para los años de nacimientos y el valor 999 para 'No especificado'",

        "eciv_adiv2" : "Estado conyugal (civil) anterior del segundo divorciante. clave,descripción 1,Soltero 2,Unión libre 3,Divorciado 4,Separado 5,Viudo 9,No especificado",

        "ent_rhdiv2" : "Entidad de residencia habitual del segundo divorciante. Se designan claves del '01' al '32' para identificar las entidades federativas (Estados), la clave '33' para aquellos divorcios (de matrimonios realizados en territorio mexicano) realizados en los Estados Unidos de América, la calve '34' para aquellos divorcios (de matrimonios realizados en territorio mexicano) realizados en los otros paises de Latiniamérica, la clave '35' para aquellos divorcios (de matrimonios realizados en territorio mexicano) realizados en cualquier otro país que no forme parte de las anteriores consideraciones. Recibe valores de **tipo C**, es decir categóricos",

        "mun_rhdiv" : "Municipio o alcaldía de residencia habitual del segundo divorciante. Se designan claves del '000' al '930' para identificar las municipalidades del territorio mexicano, mientras que la clave '998' indica la categoría 'no aplica y la clave '999' indica 'municipio no indicado' Recibe valores de tipo C, es decir categóricos",

        "loc_rhdiv2" : "Localidad de residencia habitual del segundo divorciante.Se designan claves del '0000' al '3395' para identificar las localidades del territorio mexicano, mientras que la clave designa '7777' 'Cifra confidencial. Establecido en la Ley del SNIEG.', la clave '9998' y '9999' indica 'localidad no especificada' Recibe valores de tipo C, es decir categóricos",

        "tloc_div2" : "Tamaño de la localidad de residencia habitual del segundo divorciante. Se designan claves que van del 1 al 17 para los rangos de población, la clave '98' para no aplica y '99' para 'No especificada' clave, descripción 1, De 1 a 999 habitantes 2, De 1 000 a 1 999 habitantes 3, De 2 000 a 2 499 habitantes 4, De 2 500 a 4 999 habitantes 5, De 5 000 a 9 999 habitantes 6, De 10 000 a 14 999 habitantes 7, De 15 000 a 19 999 habitantes 8, De 20 000 a 29 999 habitantes 9, De 30 000 a 39 999 habitantes 10, De 40 000 a 49 999 habitantes 11, De 50 000 a 74 999 habitantes 12, De 75 000 a 99 999 habitantes 13, De 100 000 a 249 999 habitantes 14, De 250 000 a 499 999 habitantes 15, De 500 000 a 999 999 habitantes 16, De 1 000 000 a 1 499 999 habitantes 17, De 1 500 000 y más habitantes 98, No aplica 99, No especificado",

        "escol_div2" : "Nivel de escolaridad del segundo divorciante. clave, descripción 0, Sin escolaridad 1, 1 a 3 años de primaria 2, 4 a 5 años de primaria 3, Primaria completa 4, Secundaria o equivalente 5, Preparatoria o equivalente 6, Superior 7, Carrera técnica 8, Otra 9, No especificada",

        "con_acdiv2" : "Contiene la condición de actividad económica del segundo divorciante. Asignando el valor de 1 para 'Trabaja', el valor de 2 para 'No trabaja' y el valor de 9 para 'No especificado'.",

        "dedic_div2" : "Contiene ocupación del segundo divorciante en esta estructura: clave,descripción 1,Trabaja 2,Al hogar 3,Estudiante 4,Pensionado o jubilado 5,Rentista 6,Incapacitado permanentemente para trabajar 7,Busca trabajo 8,Otra (no trabaja) 9,No especificada",

        "postr_div2" : "Posición en el trbajo del segundo divorciante. clave,descripción 1,Empleado 2,Obrero 3,Jornalero o peón agrícola 4,Patrón o empresario 5,Miembro de cooperativa 6,Trabajador no remunerado 7,Trabajador por cuenta propia 8,Otra 9,No especificada",

        "sexo_div2" : "Sexo del segundo divorciante. clave,descripción 1,Hombre 2,Mujer",

        "dura_soc" : "Duración social del matrimonio Se asigna valores de 1 a 91 para los años de duración del matrimonio. 92 se asigna a aquellos matrimonios que hayan durado 92 o más años, 93 para los matrimonios con duración de menos de un mes, 94 para aquellos con una duración de 1 a 2 meses,95 para aquellos con duración de 3 meses, 96 para aquellos con duración de 4 a 5 meses, 97 para aquellos con duración de 6 meses, 98 para los que tienen una duración de entre  7 a 11 meses y 99 para duración No especificada.",

        "dura_leg" : "Duración legal del matrimonio Se asigna valores de 1 a 91 para los años de duración del matrimonio. 92 se asigna a aquellos matrimonios que hayan durado 92 o más años, 93 para los matrimonios con duración de menos de un mes, 94 para aquellos con una duración de 1 a 2 meses,95 para aquellos con duración de 3 meses, 96 para aquellos con duración de 4 a 5 meses, 97 para aquellos con duración de 6 meses, 98 para los que tienen una duración de entre  7 a 11 meses y 99 para duración No especificada.",

        "edad_mdiv1" : "Edad al matrimonio del primer divorciante. Se asignan valores numéricos del 0 al 95 para designar la edad y se asigna el valor 999 para 'No especificado'",

        "edad_mdiv2" : "Edad al matrimonio del segundo divorciante. Se asignan valores numéricos del 0 al 95 para designar la edad y se asigna el valor 999 para 'No especificado'",

        "t_dvante" : "Tipo de divorciante. clave,descripción 1,Divorciantes hombre - mujer 2,Divorciantes del mismo sexo hombres 3,Divorciantes del mismo sexo mujeres",

        "dis_reoax" : "Distrito de registro de Oaxaca"

    }

    if a in atajo:
           print("")
           return(atajo[a])
    else:
        print(f"La clave '{a}' no se encuentra registrada")

    
    info_features()

