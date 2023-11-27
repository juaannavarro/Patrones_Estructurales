

#quiero crear una clase usuario que tenga un nombre, un apellido, un email y un telefono
#quiero que el usuario pueda ser creado con un builder
#quiero que el builder tenga un metodo para crear el usuario
#quiero que el builder tenga un metodo para crear el nombre
#quiero que el builder tenga un metodo para crear el apellido
#quiero que el builder tenga un metodo para crear el email
#quiero que el builder tenga un metodo para crear el telefono

class Usuario:
    def __init__(self, nombre, apellido, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Telefono: {self.telefono}"

class UsuarioBuilder:
    
    def __init__(self):
        self.usuario = None
        
    def crear_usuario(self):
        self.usuario = Usuario("","","","")
        
    def crear_nombre(self, nombre):
        self.usuario.nombre = nombre
        
    def crear_apellido(self, apellido):
        self.usuario.apellido = apellido
        
    def crear_email(self, email):
        self.usuario.email = email
        
    def crear_telefono(self, telefono):
        self.usuario.telefono = telefono
        
    def get_usuario(self):
        return self.usuario
    
class UsuarioDirector:

    def __init__(self, builder):
        self.builder = builder
        
    def crear_usuario(self, nombre, apellido, email, telefono):
        self.builder.crear_usuario()
        self.builder.crear_nombre(nombre)
        self.builder.crear_apellido(apellido)
        self.builder.crear_email(email)
        self.builder.crear_telefono(telefono)
        
    def get_usuario(self):
        return self.builder.get_usuario()
    
    






    