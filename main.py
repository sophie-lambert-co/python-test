from flask import Flask
from mysql.connector import connect


app = Flask(__name__)

# dictionary containing the database configuration
db_config = { 
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "france"
}

# route to the home page
@app.route("/")
def index():
    return"<h1>Hello, World!</h1>"


#GET /api/departements : Récupérer tous les départements.
@app.route("/api/departements")
def get_departements():
    # connect to the database
    # **db_config sert à mettre les valeurs de db_config dans les paramètres de connect c"est à dire host, user, password, database.
    connection = connect(**db_config)

    # le cursor permet de faire des requêtes, en gros c"est un objet qui permet de faire des requêtes
    cursor = connection.cursor(dictionary=True)


    # execute the query
    cursor.execute("SELECT * FROM departement")

    # fetch the results, c"est à dire récupérer les résultats, fetch en français signifie récupérer
    departements = cursor.fetchall()

    # close the connection
    cursor.close()
    connection.close()


    # return the departments as a JSON object
    return departements 


# GET /api/departements/{id} : Récupérer un département par son ID.
@app.route("/api/departements/<int:departement_id>")
def get_departement(departement_id):
    connection = connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departement WHERE departement_id = %s", (departement_id,))
    departement = cursor.fetchone()
    cursor.close()
    connection.close()
    if departement:
        return {"departement": departement}
    else:
        return {"error": "Département non trouvé"}, 404

# GET /api/departements/code/{code} : Récupérer un département par son code.
@app.route("/api/departements/code/<string:departement_code>")
def get_departement_by_code(departement_code):
    connection = connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departement WHERE departement_code = %s", (departement_code,))
    departement = cursor.fetchone()
    cursor.close()
    connection.close()
    if departement:
        return {"departement": departement}
    else:
        return {"error": "Département non trouvé"}, 404

# GET /api/departements/nom/{nom} : Récupérer un département par son nom.
@app.route("/api/departements/nom/<string:departement_nom>")
def get_departement_by_nom(departement_nom):
    connection = connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM departement WHERE departement_nom  = %s", (departement_nom,))
    departement = cursor.fetchone()
    cursor.close()
    connection.close()
    if departement:
        return {"departement": departement}
    else:
        return {"error": "Département non trouvé"}, 404

# GET /api/villes/nom/{nom} : Récupérer toutes les villes par nom.
@app.route("/api/villes/nom/<string:ville_nom>")
def get_villes_by_nom(ville_nom):
    db = None
    cursor = None
    try:
        db = connect(**db_config)
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM villes_france_free WHERE ville_nom = %s", [ville_nom])
        resultat = cursor.fetchall()
        return resultat
    except:
        return f"Une erreur sauvage est apparue"
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
    

    
# GET /api/villes/code_postal/{code_postal} : Récupérer toutes les villes par code postal.
# @app.route("/api/villes/code_postal/<string:code_postal>")
# def get_villes_by_code_postal(code_postal):
#     connection = connect(**db_config)
#     cursor = connection.cursor(dictionary=True)
#     #cursor.execute("SELECT * FROM villes_france_free WHERE ville_code_postal = %s", (code_postal,))
#     #ou
#     #cursor.execute("SELECT * FROM villes_france_free WHERE ville_code_postal LIKE %s", (code_postal,))
#     villes = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return str(villes)


# Récupérer les villes par code postal.
@app.route("/api/villes/code_postal/<string:code_postal>")
def get_villes_by_code_postal(code_postal):
    db = connect(**db_config)
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM villes_france_free WHERE ville_code_postal LIKE %s", [code_postal+"%"])
    resultat = cursor.fetchall()
    cursor.close()
    db.close()
    return resultat



# GET /api/villes/population/{annee}/{population} : Récupérer toutes les villes par population.
# @app.route("/api/villes/population/<int:annee>/<int:population>")
# def get_villes_by_population(annee, population):
#     column_name = f"ville_population_{annee}"
#     query = f"SELECT * FROM villes_france_free WHERE {column_name} >= %s"
#     connection = connect(**db_config)
#     cursor = connection.cursor(dictionary=True)
#     cursor.execute(query, (population,))
#     villes = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return str(villes)



# Récupérer les villes avec une population supérieure ou égale à une valeur spécifiée pour l'année spécifiée.
@app.route("/api/villes/population/<int:annee>/<int:population>")
def get_villes_by_population_for_year(annee, population):
    if annee not in [1999, 2010, 2012]:
        return "Nous n'avons que les données pour les années : 1999, 2010 et 2012"
    db = connect(**db_config)
    cursor = db.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM villes_france_free WHERE ville_population_%s >= %s", [annee, population])
    resultat = cursor.fetchall()
    cursor.close()
    db.close()
    return resultat



# GET /api/villes : Récupérer les 10 premières villes.
@app.route("/api/villes")
def get_villes():
    try :
        connection = connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM villes_france_free LIMIT 10")
        villes = cursor.fetchall()
        return str(villes)
    except Exception as e:
        return f"Erreur : {e}"
    finally:
        cursor.close()
        connection.close()  



# GET /api/villes/{id} : Récupérer une ville par son ID.
@app.route("/api/villes/<int:ville_id>")
def get_ville_by_id(ville_id):
    connection = connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM villes_france_free WHERE ville_id = %s", (ville_id,))
    ville = cursor.fetchone()
    cursor.close()
    connection.close()
    if ville:
        return str(ville)
    else:
        return "Ville non trouvée", 404

# GET /api/villes/departement/{code} : Récupérer toutes les villes par département.
@app.route("/api/villes/departement/<string:departement_code>")
def get_villes_by_departement_code(departement_code):
    connection = connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM villes_france_free WHERE ville_departement = %s", (departement_code,))
    villes = cursor.fetchall()
    cursor.close()
    connection.close()
    return str(villes)




#http://127.0.0.1:5000/
#flask --app server run : pour lancer le serveur avec flask
# commande pour activer l"environnement virtuel : source ./bin/activate  
# commande pour désactiver l"environnement virtuel : deactivate
# commande pour installer flask : pip install flask

