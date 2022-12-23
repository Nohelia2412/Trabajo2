import streamlit as st

    st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
    st.markdown ( "<h2 style='text-align: center; color: black;'>Propuesta</h2>" , unsafe_allow_html = True )

    st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )

    st.markdown ( "<h2 style='color: black;'>1.- Conjunto de datos</h2>" , unsafe_allow_html = True )

    st.markdown ( "<h2 style='color: black;'>Formulario de Google </h2>" , unsafe_allow_html = True )

    st.markdown ( "<h2 style='color: black;'>Preguntas </h2>" , unsafe_allow_html = True )

    st.markdown ( 'Del uno al cinco segun la escala dada califique las siguientes comidas:' )

    st.markdown ( '1. Me desagrada' )
    st.descuento ( '2. No me gusta' )
    st.rebaja ( '3. Es aceptable' )
    st.rebaja ( '4. Agradable' )
    st.markdown ( '5. Me encantan' )

    st.markdown ( 'Formulario de Google' )

    st.markdown ( 'Preparacion y pregunta de pasos para realizar la encuesta.' )

    st.imagen ( 'https://cdn.discordapp.com/attachments/952764370335719434/1049148181646163998/image.png' )
    st.Imagen ( 'https://cdn.discordapp.com/attachments/952764370335719434/1049538764353060944/1.png' )
    st.imagen ( 'https://cdn.discordapp.com/attachments/952764370335719434/1049538764353060944/1.png' )

    st.markdown ( "<h2 style='color: black;'>PFormulario de Google (Preprocesamiento) </h2>" , unsafe_allow_html = True )

    st.markdown ( 'Procedemos a crear nuestro exel para luego ser convertido en un archivo csv con el fin de utilizarlo junto al comando panda y numpy.' )

    st.imagen ( 'https://cdn.discordapp.com/attachments/952764370335719434/1049149904171319357/861555e9-e206-4d22-a2c5-d4d370966a98.png' )
    st.image ( 'https://cdn.discordapp.com/attachments/952764370335719434/1049542478019178546/ZHiqJFM83PseYpWGGozUQAfiovfpVIiwF3y-v6CFKFIMxSP0y7VzelQL1DPFCdlw_bc-HwihIXwQ5l0ksErhLDgJBGCWuVUp4Z5pcon_3sjRYxxRBiXmAoD3mAgWC6c4VvA0xCgM3ul6QEVk_VUDwqxh6pT78X-HPjsKBjBxfQgpzuyTfCAnXFY1kf7OCLN0r43zdJVLMZaeQC2Sxp9Si9y8adGgduBPdX3vegeVk28yS8oP7U4cBFeamc_PYwGK7VmzK0sUexfN9WRr1DIT7oAGeKxzrSE4SslSVRIF-TGD-hkNb8D7CnOQN-UzERY9B2gBNbFo6fswgFRRTesnCc-yfZYTDhjldNwPshHPTSiapc18_zRfyEICfJ8TRrGd4nLPD5yHp0X6yBrZ6XkhUjWjGyHvs4x0k0QEUdSNpSiPnOMxG54Vgxl7ZgS-BvZoq3sQ9vnrJsOqAi6_eYRkAjRpI7h2Fk55zRPNPGZCeooLJWKLXOabBkVyL00q..png' )
    st.image ( 'https://cdn.discordapp.com/attachments/952764370335719434/1049542753215844362/wQUeVtzifEvpulCDOfjZzswrSFUFQArGVR50Udx4d1iVPKhcpQXOnH3CnZTMD-98RY7SeX9BlgdrhTIjnyUEX8eXHkaNHfY9JsC-h5J_icllATWlQUcg37rk1vjsmwRfD0DlpS4IFhbVQ8Y0ooJKFx8uxZknzhd7A0lmGHKStS25ekzRv3YR8daV97wxlvDrwVDOmADCJKjWN9Yp4cmzLouLjMX96fdXy4ZqRRN8Mz9or5FXJYf6_PZjz_0zfPwc0qwuzfmQGmqYvvoJtevGEKGyJMqU0XAH0p51vciQ0md5mGcXcIYsy_IQ0zu0_--dpXVASyNZ2T769qnHUzfY204EFObq0FhNO1sZMuvs9bw4sD2Pnyip3CgdZDkGIbvEl0XQtovzxR9CiGG-wFX65jR6iA0YX4g5_viKdjF2gklfnnKSMGZ5FzRp4fLilYtR_6rYDRSxtvnoZ7bIHxX2IGKKGGIdd9Iw_v2fVX64mXzLMcXPS6v62kv5wwW2..png' )
    st.imagen ( 'https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png' )
    st.markdown ( "<h2 style='text-align: center; color: black;'>Archivo CSV separado por comas</h2>" , unsafe_allow_html = True )
    pandas  =  pd.read_csv ( 'ENCUESTA.csv' )
    st.marco de datos ( pandas )
    st.markdown ( 'Cantidad de Filas y Columnas' )
    
    st.markdown ( '46 Columnas y 33 Filas' )





