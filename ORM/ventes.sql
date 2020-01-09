DROP TABLE IF EXISTS vente;
DROP TABLE IF EXISTS produit;
DROP TABLE IF EXISTS client;

CREATE TABLE client(numero INT NOT NULL,
    nom VARCHAR(30),
    adresse VARCHAR(30),
    telephone VARCHAR(12),
    PRIMARY KEY(numero)) ;

CREATE TABLE produit(reference INT NOT NULL,
    nom VARCHAR(30),
    marque VARCHAR(30),
    prix REAL,
    PRIMARY KEY(reference)) ;

CREATE TABLE vente(numero INT NOT NULL,
             ref_produit INT,
             no_client INT NOT NULL,
             date DATE,
             PRIMARY KEY(numero),
             FOREIGN KEY(ref_produit) REFERENCES produit(reference)
             FOREIGN KEY(no_client) REFERENCES client(numero)
            ) ;

INSERT INTO client(numero,nom, adresse, telephone)
	VALUES('101', 'Durand', 'Nice', '034553324'),
    ('106', 'Fabre', 'Paris', NULL),
    ('110', 'Prosper', 'Paris', NULL),
    ('125', 'Anthonin', 'Marseille', '032234555');

INSERT INTO produit(reference, nom, marque, prix)
  VALUES('153', 'Rasoir', 'PWM', '8000'),
    ('589', 'Groupe électrogène', 'TransElect', '3465.75'),
    ('158', 'Saut en parachute', 'Yadus', '12045.20'),
    ('553', 'Vitamines', 'Citron', '7000');
INSERT INTO Vente(numero, ref_produit, no_client, date)
  VALUES('102', '153', '101', '2015-10-12'),
    ('845', '589', '106', '2016-03-15'),
    ('1003', '158', '106', '2017-11-03'),
    ('1058', '589', '125', '2018-07-23');