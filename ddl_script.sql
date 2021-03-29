-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mydatabase
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydatabase
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydatabase` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mydatabase` ;

-- -----------------------------------------------------
-- Table `mydatabase`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydatabase`.`customers` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(64) NULL DEFAULT NULL,
  `last_name` VARCHAR(64) NULL DEFAULT NULL,
  `title` VARCHAR(32) NULL DEFAULT NULL,
  `email` VARCHAR(128) NULL DEFAULT NULL,
  `phone` VARCHAR(16) NULL DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE INDEX `customer_id_UNIQUE` (`customer_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydatabase`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydatabase`.`orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `fk_customer_id` INT NOT NULL,
  `order_date` VARCHAR(32) NULL DEFAULT NULL,
  `order_status` VARCHAR(256) NULL DEFAULT NULL,
  `shipping_method` VARCHAR(256) NULL DEFAULT NULL,
  `shipping_amount` DECIMAL(12,2) UNSIGNED NULL DEFAULT NULL,
  `price_amount` DECIMAL(12,2) UNSIGNED NULL DEFAULT NULL,
  `subtotal_currency` VARCHAR(256) NULL DEFAULT NULL,
  `order_subtotal` DECIMAL(12,2) UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  UNIQUE INDEX `order_id_UNIQUE` (`order_id` ASC) VISIBLE,
  INDEX `fk_Orders_Customers1_idx` (`fk_customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_Orders_Customers1`
    FOREIGN KEY (`fk_customer_id`)
    REFERENCES `mydatabase`.`customers` (`customer_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydatabase`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydatabase`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `product_name` VARCHAR(128) NULL DEFAULT NULL,
  `unit_price` DECIMAL(12,2) UNSIGNED NULL DEFAULT NULL,
  `product_msrp` DECIMAL(12,2) UNSIGNED NULL DEFAULT NULL,
  `product_description` VARCHAR(1024) NULL DEFAULT NULL,
  `product_weight` FLOAT UNSIGNED NOT NULL,
  `quantity` DECIMAL(12,0) NULL DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE INDEX `product_id_UNIQUE` (`product_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydatabase`.`order_lines`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydatabase`.`order_lines` (
  `order_line_id` INT NOT NULL AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `fk_product_id` INT NOT NULL,
  `quantity` INT UNSIGNED NULL DEFAULT NULL,
  `total_line_price` INT UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`order_line_id`, `order_id`),
  UNIQUE INDEX `idOrder Lines_UNIQUE` (`order_line_id` ASC) VISIBLE,
  INDEX `fk_Order Lines_Products_idx` (`fk_product_id` ASC) VISIBLE,
  INDEX `fk_Order Lines_Orders1_idx` (`order_id` ASC) VISIBLE,
  CONSTRAINT `fk_Order Lines_Orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `mydatabase`.`orders` (`order_id`),
  CONSTRAINT `fk_Order Lines_Products`
    FOREIGN KEY (`fk_product_id`)
    REFERENCES `mydatabase`.`products` (`product_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mydatabase`.`shipping_address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydatabase`.`shipping_address` (
  `shipping_address_id` INT NOT NULL,
  `fk_customer_id` INT NOT NULL,
  `shipping_line1` VARCHAR(128) NULL DEFAULT NULL,
  `shipping_line2` VARCHAR(128) NULL DEFAULT NULL,
  `shipping_city` VARCHAR(128) NULL DEFAULT NULL,
  `shipping_region` VARCHAR(128) NULL DEFAULT NULL,
  `shipping_country` VARCHAR(128) NULL DEFAULT NULL,
  `shipping_postal_code` VARCHAR(128) NULL DEFAULT NULL,
  PRIMARY KEY (`shipping_address_id`),
  INDEX `fk_Shipping Address_Customers1_idx` (`fk_customer_id` ASC) VISIBLE,
  CONSTRAINT `fk_Shipping Address_Customers1`
    FOREIGN KEY (`fk_customer_id`)
    REFERENCES `mydatabase`.`customers` (`customer_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
