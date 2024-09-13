OBJECTIFS :

- Comprendre plusieurs concepts et compétences fondamentales en gestion de bases de données et en SQL
- Maîtriser des compétences et des connaissances essentielles dans le développement du web en Python.

CONSIGNE : 

Dans la suite des notions abordées en cours, où nous avons créé des routes pour répondre à des requêtes clients, ce projet  s’inscrit dans la continuité de ce travail.

Les liens suivants sont les routes de votre serveur web qui permettent de récupérer les informations de la base de données. 

Vous devez créer la base de données pour accueillir les données dans un fichier que vous trouverez sur ce lien

 
Créer les routes pour les actions suivantes :

 

    GET /api/departements : Récupérer tous les départements.
    GET /api/departements/<int:departement_id> : Récupérer un département spécifique par son ID.
    GET /api/departements/code/<string:departement_code> : Récupérer un département par son code.
    GET /api/villes/nom/<string:ville_nom> : Récupérer les villes par nom.
    GET /api/villes/code_postal/<string:code_postal> : Récupérer les villes par code postal.
    GET /api/villes/population/<int:annee>/<int:population> : Récupérer les villes avec une population supérieure ou égale à une valeur spécifiée pour l'année spécifiée.
    GET /api/villes : Récupérer une liste limitée de villes (les 10 premières).
    GET /api/villes/<int:ville_id> : Récupérer une ville spécifique par son ID.
    GET /api/villes/departement/<string:departement_code> : Récupérer toutes les villes appartenant à un département spécifique par son code.

 

Cette API REST en Flask permet de récupérer des données des tables departement et villes sous forme de JSON.

Vous créez un service MySQL avec :

Le conteneur nommé mysql_db.
Un utilisateur MySQL sophie avec le mot de passe root.
Une base de données nommée france.
Les données MySQL sont persistées dans un volume Docker (db_data).
Vous configurez également un conteneur phpMyAdmin avec le mot de passe root MySQL défini.

Pour démarrer le tout, exécutez :

bash
Copier le code
docker-compose up -d
Ensuite, accédez à phpMyAdmin via : http://localhost:8080.

Vous pouvez vous connecter avec l'utilisateur sophie et le mot de passe root.


REQUETES BASE DE DONNEES :

CREATE TABLE `villes_france_free` (
  `ville_id` INT NOT NULL AUTO_INCREMENT,
  `ville_departement` VARCHAR(10) NOT NULL,
  `ville_slug` VARCHAR(100) NOT NULL,
  `ville_nom` VARCHAR(100) NOT NULL,
  `ville_nom_simple` VARCHAR(100) NOT NULL,
  `ville_nom_reel` VARCHAR(100) NOT NULL,
  `ville_nom_soundex` VARCHAR(100),
  `ville_nom_metaphone` VARCHAR(100),
  `ville_code_postal` VARCHAR(10) NOT NULL,
  `ville_commune` VARCHAR(10) NOT NULL,
  `ville_code_commune` VARCHAR(10) NOT NULL,
  `ville_arrondissement` INT,
  `ville_canton` VARCHAR(10),
  `ville_amdi` INT,
  `ville_population_2010` INT,
  `ville_population_1999` INT,
  `ville_population_2012` INT,
  `ville_densite_2010` INT,
  `ville_surface` FLOAT,
  `ville_longitude_deg` FLOAT,
  `ville_latitude_deg` FLOAT,
  `ville_longitude_grd` VARCHAR(10),
  `ville_latitude_grd` VARCHAR(10),
  `ville_longitude_dms` VARCHAR(10),
  `ville_latitude_dms` VARCHAR(10),
  `ville_zmin` INT,
  `ville_zmax` INT,
  PRIMARY KEY (`ville_id`)
);


CREATE TABLE `departement` (
  `departement_id` INT NOT NULL AUTO_INCREMENT,
  `departement_code` VARCHAR(10) NOT NULL,
  `departement_nom` VARCHAR(100) NOT NULL,
  `departement_nom_uppercase` VARCHAR(100) NOT NULL,
  `departement_slug` VARCHAR(100) NOT NULL,
  `departement_nom_soundex` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`departement_id`)
);



ALTER TABLE `departement` ADD UNIQUE (`departement_code`);


ALTER TABLE `villes_france_free`
ADD CONSTRAINT fk_ville_departement
FOREIGN KEY (`ville_departement`) REFERENCES `departement`(`departement_code`)
ON DELETE CASCADE
ON UPDATE CASCADE;
