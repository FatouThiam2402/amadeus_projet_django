
DROP DATABASE IF EXISTS amadeus;

create DATABASE amadeus;

use amadeus;


DROP TABLE IF EXISTS Client;

CREATE TABLE Client (
	id integer   PRIMARY KEY auto_increment,
	nomComplet varchar(200), 
	telephone varchar(200), 
	email varchar(200), 
	adresse varchar(200), 
    date_naissance date,
	dernierTicketAchete date 
    );


DROP TABLE IF EXISTS  Personne;
CREATE TABLE Personne (
	id integer   PRIMARY KEY auto_increment, 
	nomPersonne varchar(200)  , 
	telephone varchar(200)  , 
	email varchar(200)  , 
	genre varchar(50)  , 
	typePersonne varchar(200)  , 
	numeroCarte varchar(200)  , 
	Pointage integer, 
	estblackliste  boolean,

    );
    



DROP TABLE IF EXISTS TypeOffre;
CREATE TABLE TypeOffre(
	id integer   PRIMARY KEY auto_increment, 
	typeofr varchar(200)
    );




DROP TABLE IF EXISTS Reservation;
CREATE TABLE Reservation (
	id integer   PRIMARY KEY auto_increment, 
	dateReservation date, 
	dateAnnulationReservation date,
	prixReservation integer, 
	devise varchar(200), 
	montantTotal integer, 
	bagageInclus  bool, 
	Personne_id integer,
    Client_id integer,
    Service_id integer,
    Foreign key (Personne_id) references Personne(id),
    Foreign key (Client_id) references Client(id),
    Foreign key (Service_id) references TypeOffre(id)
    
    );




DROP TABLE IF EXISTS compagnie;

CREATE TABLE compagnie (
	id integer   PRIMARY KEY auto_increment, 
	nomCompagnie varchar(200),
    Service_id integer,
    Foreign key (Service_id) references TypeOffre(id)
    );



DROP TABLE IF EXISTS Adresse;

CREATE TABLE Adresse (
	id integer PRIMARY KEY auto_increment, 
	nomVille varchar(200), 
	pays varchar(200),
    latitude real,
    longitude real
    );



DROP TABLE IF EXISTS Hotel;
       
        create table Hotel(
            idHotel varchar(255) primary key,
            nom varchar(255),
            Adresse_id integer,
            Foreign key (Adresse_id) references Adresse(id),
            Service_id integer,
            Foreign key (Service_id) references TypeOffre(id)
            
        );


DROP TABLE IF EXISTS Chambre;

        create table Chambre(
            num_chambre int   primary key auto_increment,
            nom_chambre varchar(255),
            description varchar(255),
            prix_chambre int,
            image varchar(255),
            idHotel varchar(255),
            Foreign key (idHotel) references Hotel(idHotel)

        );


DROP TABLE IF EXISTS Voiture;

CREATE TABLE Voiture (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marque VARCHAR(100), 
    modele VARCHAR(60),
    nombre_places INT(100), 
    boite_vitesse VARCHAR(100), 
    carburant VARCHAR(100),
    climatisation VARCHAR(100),  
    couleur VARCHAR(100), 
    annee_production INT,
    matricule VARCHAR(100),
    prix real,
    id_Service int,
    Foreign key (id_Service) references TypeOffre(id)
    
);        
        




DROP TABLE IF EXISTS Vol;

CREATE TABLE Vol (
	id integer   PRIMARY KEY auto_increment, 
	achatInstantane  bool  , 
	allerSimple  bool  , 
	dernierAchat date  , 
	nombreSiegeReserve integer  , 
	dateDepart date  , 
	dateArrivee date  , 
	Service_id integer  ,
    Foreign key (Service_id) references TypeOffre(id)

);




DROP TABLE IF EXISTS Aeroport;
CREATE TABLE Aeroport (
	id integer   PRIMARY KEY auto_increment, 
	nomAeroport varchar(200)  
);



DROP TABLE IF EXISTS Volgenerique;
CREATE TABLE Volgenerique (
	id integer PRIMARY KEY auto_increment, 
	compagnie varchar(200), 
	heureDepart date, 
	heureArrivee date, 
	capacite integer, 
	aeroportDepart varchar(200)  , 
	aeroportArrivee varchar(200) ,
    Vol_id integer,
    Foreign key (Vol_id) references Vol(id),
    aeroport_id integer,
    Foreign key (aeroport_id) references Aeroport(id)

);

