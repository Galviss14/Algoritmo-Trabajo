## MINI TIENDA URBAN STORE Rosmel Galvis- Diego Vera
class Producto:
    def __init__(self, tipo, modelo, precio, stock):
        self.tipo = tipo
        self.modelo = modelo
        self.__precio = precio
        self.__stock = stock

    def obtener_precio(self):
        return self.__precio

    def vender(self, cantidad):
      if cantidad <= self.__stock:
        self.__stock = self.__stock - cantidad
        return True
      else:
        return False

    def mostrar_producto (self):
        print(self.tipo, "-", self.modelo, "- Precio:", self.__precio, "- Stock:", self.__stock)


class Cliente:
    def __init__(self, nombre, cedula, telefono, direccion):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion

    def mostrar(self):
        print("Cliente:", self.nombre)
        print("Cédula:", self.cedula)
        print("Teléfono:", self.telefono)
        print("Dirección:", self.direccion)


class Carrito:
    def __init__(self, cliente):
      self.cliente = cliente
      self.total = 0
      self.lista = []

    def comprar(self, producto, cantidad):
      if producto.vender(cantidad):
        subtotal = producto.obtener_precio() * cantidad
        self.total = self.total + subtotal
        self.lista.append((producto.tipo, producto.modelo, cantidad, subtotal))
        print("Compra agregada")
      else:
        print("No hay stock")

    def ver_carrito(self):
      print("\n=== CARRITO ===")
      if len(self.lista) == 0:
        print("El carrito esta vacio")
      else:
        i = 1
        for item in self.lista:
          print(i, ".", item [0], "-", item[1], "x", item[2], "=", item[3])
          i = i + 1

    def eliminar_producto(self, posicion):
      if posicion >= 1 and posicion <= len(self.lista):
        item = self.lista.pop(posicion - 1)
        self.total = self.total - item[3]
        print("Producto eliminado")
      else:
        print("Producto no he encontrado")

    def pagar(self):
      if len(self.lista) == 0:
        print("No hay productos en el carrito")
        return
      print("\n=== PAGO CON TARJETA ===")
      numero = input("Número de tarjeta: ")
      nombre_tarjeta = input("nombre de la tarjeta: ")
      cvv = input("CVV: ")
      print(" ")
      print("Pago en proceso...")
      print(" ")
      print("Pago aprobado")
      print(" ")
      print("Gracias por su compra")

    def mostrar_factura(self):
      print("\n=== FACTURA ===")
      print("Cliente:", self.cliente.nombre)
      print("Cédula:", self.cliente.cedula)
      print("Teléfono:", self.cliente.telefono)
      print("Dirección:", self.cliente.direccion)
      print(" ")
      for item in self.lista:
        print(item[0], "-", item[1], "x", item[2], "=", item[3])
      print("Total a pagar:", self.total)
      print(" ")


## LISTA DE NUESTROS PRODUCTOS (INSTANCIA)
productos = [
    Producto("Gorra", "Gucci", 70000, 10),
    Producto("Gorra", "Nike", 50000, 8),
    Producto("Gorra", "Belica", 42000, 6),

    Producto("Reloj", "Patek", 110000, 8),
    Producto("Reloj", "Rolex", 150000, 5),
    Producto("Reloj", "G-shock", 70000, 6),

    Producto("Gafas", "Rayban", 40000, 10),
    Producto("Gafas", "Prada", 80000, 6),
    Producto("Gafas", "Dior", 50000, 8),

    Producto("Vaper", "Waka", 50000, 6),
    Producto("Vaper", "Voopoo", 60000, 8),
    Producto("Vaper", "Uwell", 70000, 10)
]

print("URBAN STORE")
print(" ")
print("REGISTRO DE CLIENTES")
print(" ")

nombre = input("Nombre: ")
cedula = input("Cédula: ")
telefono = input("Teléfono: ")
direccion = input("Dirección: ")
print(" ")
cliente = Cliente(nombre, cedula, telefono, direccion)

carrito = Carrito(cliente)

## MENU DE LA TIENDA

opcion = 0

while opcion != 9:
    print("1. Ver productos")
    print("2. Comprar gorra")
    print("3. Comprar reloj")
    print("4. Comprar gafas")
    print("5. Comprar vaper")
    print("6. Ver carrito")
    print("7. Eliminar producto")
    print("8. Pagar")
    print("9. Salir")

    print(" ")

    opcion = int(input("Elige: "))
    print(" ")

    if opcion == 1:
        i = 1
        for producto in productos:
            print(i, ".", producto.tipo, "-", producto.modelo, "- Precio:", producto.obtener_precio())
            i = i + 1
            print(" ")

    elif opcion == 2:
        print("Gorras disponibles:")
        print("1. Gucci")
        print("2. Nike")
        print("3. Belica")
        print(" ")


        eleccion = int(input("Elige modelo: "))
        cantidad = int(input("Cantidad: "))
        carrito.comprar(productos[eleccion - 1], cantidad)
        print(" ")

    elif opcion == 3:
        print("Relojes disponibles:")
        print("1. Patek")
        print("2. Rolex")
        print("3. G-shock")
        print(" ")

        eleccion = int(input("Elige modelo: "))
        cantidad = int(input("Cantidad: "))
        carrito.comprar(productos[eleccion + 2 ], cantidad)
        print(" ")

    elif opcion == 4:
        print("Gafas disponibles:")
        print("1. Rayban")
        print("2. Prada")
        print("3. Dior")
        print(" ")

        eleccion = int(input("Elige modelo: "))
        cantidad = int(input("Cantidad: "))
        carrito.comprar(productos[eleccion + 5], cantidad)
        print(" ")

    elif opcion == 5:
        print("Vapers disponibles:")
        print("1. Waka")
        print("2. Voopoo")
        print("3. Uwell")
        print(" ")

        eleccion = int(input("Elige modelo: "))
        cantidad = int(input("Cantidad: "))
        carrito.comprar(productos[eleccion + 8], cantidad)
        print(" ")

    elif opcion == 6:
        carrito.ver_carrito()
        print(" ")

    elif opcion == 7:
        carrito.ver_carrito()
        lugar = int(input("Elige la posicion del producto a eliminar: "))
        carrito.eliminar_producto(lugar)
        print(" ")

    elif opcion == 8:
        carrito.pagar()
        carrito.mostrar_factura()
        print(" ")

    elif opcion == 9:
        print(" ")
        print("Gracias por comprar")
