
def atajos(accion):
    #función que retorna los shortcuts para acceder a la definición de la nomenclatura

    atajo = ["tipo_divorcio", "ent_regis", "mun_regist","loc_regis","tloc_regis","ent_mat","mun_mat","local_mat","tloc_mat","dia_mat","mes_mat","anio_mat", "dia_reg", "mes_reg", "anio_reg","dia_sen","mes_sen", "anio_sen", "dia_eje","mes_eje","anio_eje", "ini_juic", "favor","caus","hijos", "hijos_men","custodia","cus_hij","pat_pot", "pat_hij","pension","pen_hij","naci_div1","edad_div1","nacim_div1","eciv_adiv1","ent_rhdiv1","mun_rhdiv1","loc_rhdiv1","tloc_div1","escol_div1","con_acdiv1","dedic_div1", "postr_div1","sexo_div1", "naci_div2","edad_div2","nacim_div2","eciv_adiv2","ent_rhdiv2","mun_rhdiv2","loc_rhdiv2","tloc_div2","escol_div2","con_acdiv2","dedic_div2","postr_div2","sexo_div2","dura_soc","dura_leg","edad_mdiv1","edad_mdiv2","t_dvante","dis_reoax"]

    if accion == "ver":
        print("Estos son los terminos usandos en el data set")

        for i in atajo:
            print(i)


atajos("ver")