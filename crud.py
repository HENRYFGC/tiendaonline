import connect
import psycopg2


conn = connect.connect()


if conn is not None:
     
    cur = conn.cursor() 
    consulta = input("Ingrese id a consultar: ")

    try:
        cur.execute("SELECT * FROM usuarios WHERE id = %s", (consulta,))
        resultados = cur.fetchall()
        print(resultados)

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # cerrar el cursor y la conexión
    cur.close()
    conn.close()
else:
    print("No se pudo establecer la conexión con la base de datos.")


#Digitar para una sola busqueda según lista desplegable tkinter

#filtroUsuariosid = input("Ingrese el id del usuario a consultar")
#filtroUsuarios = input("Ingrese el nombre de usuario a consultar")

#filtroProducto = input("Ingrese el id del producto a consultar")
#filtroProducto = input("Ingrese el nombre del producto a consultar")