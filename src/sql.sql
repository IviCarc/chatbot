USE AsistenciaTecnica;

DROP TABLE IF EXISTS Reuniones;
DROP TABLE IF EXISTS Clientes;
DROP TABLE IF EXISTS Anfitriones;


CREATE TABLE Clientes (
	ID INT UNIQUE NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR (255) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE Anfitriones (
	ID INT UNIQUE NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE Reuniones (
	ID INT UNIQUE NOT NULL AUTO_INCREMENT,
    chat VARCHAR(255) NOT NULL,
    fechaHora DATETIME NOT NULL,
    ID_cliente INT NOT NULL,
    ID_anfitrion INT NOT NULL,
    PRIMARY KEY (ID),
	FOREIGN KEY (ID_cliente) REFERENCES Clientes(ID),
    FOREIGN KEY (ID_anfitrion) REFERENCES Anfitriones(ID)
);

ALTER TABLE  `Reuniones` ADD UNIQUE (`fechaHora`, `ID_anfitrion`);
ALTER TABLE  `Reuniones` ADD UNIQUE (`fechaHora`, `ID_cliente`);

INSERT INTO Clientes (nombre, correo) VALUES ("Benito", "beni@gmail.com");
INSERT INTO Clientes (nombre, correo) VALUES ("Ivan", "ivan@gmail.com");

INSERT INTO Anfitriones (nombre, correo) VALUES ("Pelo", "pelo@gmail.com");
INSERT INTO Anfitriones (nombre, correo) VALUES ("Agus", "agus@gmail.com");

INSERT INTO Reuniones (chat, fechaHora, ID_cliente, ID_anfitrion) VALUES ("queonda", "2022-06-16 16:00:00", 1, 1);
INSERT INTO Reuniones (chat, fechaHora, ID_cliente, ID_anfitrion) VALUES ("queonda", "2022-06-16 16:30:00", 2, 1);