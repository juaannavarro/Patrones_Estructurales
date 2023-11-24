# Patrones_Estructurale    gestor = GestorDocumental()

    # Crear documentos y carpetas
    documento_simple = Documento("Informe", "txt", 1024, "Contenido del informe")
    documento_secreto = ProxyDocumento(Documento("InformeSecreto", "pdf", 2048, "Contenido confidencial"))
    carpeta_personal = Carpeta("Personal")

    # Añadir documentos y carpetas al gestor
    gestor.añadir_componente(documento_simple)
    gestor.añadir_componente(documento_secreto, carpeta_personal)
    gestor.añadir_componente(carpeta_personal)

    # Mostrar la estructura del gestor documental
    print("Estructura del Gestor Documental:")
    gestor.mostrar_estructura()

    # Acceder a un documento a través del proxy
    print("\nAcceso al Documento Secreto a través del Proxy:")
    documento_secreto.request()
    #guardar todos los documentos en una carpetas