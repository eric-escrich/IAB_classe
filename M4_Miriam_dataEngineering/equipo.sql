DROP DATABASE IF EXISTS equipo;
CREATE DATABASE IF NOT EXISTS equipo;
USE equipo;

CREATE TABLE persona (
    DNI VARCHAR(8) PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Edad INT
);

CREATE TABLE estadio (
    Id INT PRIMARY KEY,
    Direccion VARCHAR(100),
    Nombre_estadio VARCHAR(50)
);

CREATE TABLE jugador (
    DNI VARCHAR(8) PRIMARY KEY,
    Numero_camiseta VARCHAR(5),
    sueldo INT,
    FOREIGN KEY (DNI) REFERENCES persona(DNI)
);

CREATE TABLE entrenamiento (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    DNI_jugador VARCHAR(8),
    Fecha_entreno DATE,
    DNI_persona VARCHAR(8),
    FOREIGN KEY (DNI_jugador) REFERENCES jugador(DNI),
    FOREIGN KEY (DNI_persona) REFERENCES persona(DNI)
);

CREATE TABLE contacto_jugador (
    DNI VARCHAR(8),
    Telefono VARCHAR(14),
    Notas VARCHAR(255),
    PRIMARY KEY (DNI, Telefono),  -- Clave primaria compuesta
    FOREIGN KEY (DNI) REFERENCES jugador(DNI)
);

CREATE TABLE posicion (
    Tipo INT PRIMARY KEY AUTO_INCREMENT,
    Descripcion VARCHAR(25)
);

CREATE TABLE partido (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    DNI_jugador VARCHAR(8),
    ID_estadio INT,
    Fecha_partido DATE,
    Tipo INT,
    FOREIGN KEY (DNI_jugador) REFERENCES jugador(DNI),
    FOREIGN KEY (ID_estadio) REFERENCES estadio(Id),
    FOREIGN KEY (Tipo) REFERENCES posicion(Tipo)
);

-- Inserts para la tabla persona
INSERT INTO persona (DNI, Nombre, Apellido, Edad) VALUES
('00100000', 'Juan', 'Rodriguez Huerta', NULL),
('11100000', 'De la Cruz', 'Meneguer Domingo', 33),
('21100000', 'Miguel', 'De la Cruz', 12),
('30010000', 'Mickey', 'Mouse', 41),
('04000000', 'Elsa', 'Frozen', 36);

-- Inserts para la tabla estadio
INSERT INTO estadio (Id, Direccion, Nombre_estadio) VALUES
(1, 'C/ de los malditos 3', 'Estadio Buenavista'),
(2, 'Avenida de las manzanas', 'Pabellón Manzanares'),
(3, 'Carretera sin número', 'Campo no encontrado'),
(4, 'C/ de los pinos', 'Campo la pineda');

-- Inserts para la tabla jugador
INSERT INTO jugador (DNI, Numero_camiseta, sueldo) VALUES
('00100000', '02', 10000),
('21100000', '28', 22000),
('04000000', '45', 400000);

-- Inserts para la tabla entrenamiento
INSERT INTO entrenamiento (DNI_jugador, Fecha_entreno, DNI_persona) VALUES
('00100000', '2010-10-02', '11100000'),
('21100000', '2020-03-13', '30010000'),
('04000000', '2022-09-25', '30010000');

-- Inserts para la tabla contacto_jugador
INSERT INTO contacto_jugador (DNI, Telefono, Notas) VALUES
('00100000', '01000100', 'Teléfono de casa'),
('00100000', '01110100', 'Teléfono de mi madre'),
('21100000', '22202020', 'Teléfono de la suegra'),
('21100000', '20020200', 'Teléfono del trabajo'),
('04000000', '04440404', 'Teléfono privado. No llamar si no es urgente');

-- Inserts para la tabla posicion
INSERT INTO posicion (Tipo, Descripcion) VALUES
(1, 'Delantero'),
(2, 'Trasero'),
(3, 'Portero'),
(4, 'Banquillo');

-- Inserts para la tabla partido
INSERT INTO partido (DNI_jugador, ID_estadio, Fecha_partido, Tipo) VALUES
('00100000', 1, '2012-11-21', 1),
('21100000', 2, '2016-01-22', 1),
('00100000', 2, '2012-11-22', 4),
('04000000', 1, '2016-01-21', 3),
('21100000', 1, '2016-01-21', 3),
('04000000', 3, '2020-07-23', 2);
