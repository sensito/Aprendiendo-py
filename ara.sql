CREATE DATABASE IF NOT EXISTS gim; #Crea la libreria si es que no exite
use gim; #uso de la libreria


CREATE IF NOT EXISTS customers (
  `customer` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name`  VARCHAR(60) NOT NULL,
  `mail` VARCHAR(60) NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `gender` ENUM('M','F','NP') NOT NULL,
  `address` VARCHAR(80) NOT NULL,
  `PHOTO` VARCHAR(100),
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `active` TINYINT(1) NOT NULL DEFAULT '1'
)CHARSET=utf8mb4;

CREATE IF NOT EXISTS clients(
  `client` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `customer` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `type_payment` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `start` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `finish` TIMESTAMP NOT NULL,
  `active` TINYINT(1) NOT NULL DEFAULT `1`
);

CREATE IF NOT EXISTS types of payments(
  `type_payment` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `cost` DOUBLE NOT NULL,
  `description` TEXT
);

CREATE  IF NOT EXISTS classes (
  `class` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `client` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  coach INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
  `date` DATE NOT NULL DEFAULT CURRENT_DATE,
  `finish` TIME NOT NULL
  `start` TIME NOT NULL,
)CHARSET=utf8mb4;
