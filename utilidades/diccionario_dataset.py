
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

        for i in atajo:
            print(i)


atajos("ver")