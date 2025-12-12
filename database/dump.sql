CREATE DATABASE  IF NOT EXISTS `finaldbcselec` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `finaldbcselec`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: finaldbcselec
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attribute`
--

DROP TABLE IF EXISTS `attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attribute` (
  `attribute_id` int NOT NULL AUTO_INCREMENT,
  `attribute_type` varchar(15) NOT NULL,
  PRIMARY KEY (`attribute_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attribute`
--

LOCK TABLES `attribute` WRITE;
/*!40000 ALTER TABLE `attribute` DISABLE KEYS */;
INSERT INTO `attribute` VALUES (1,'Agility'),(2,'Intelligence'),(3,'Strength'),(4,'Universal');
/*!40000 ALTER TABLE `attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hero`
--

DROP TABLE IF EXISTS `hero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hero` (
  `hero_id` int NOT NULL AUTO_INCREMENT,
  `hero_name` varchar(45) NOT NULL,
  `attack_type` varchar(45) NOT NULL,
  `ATTRIBUTE_attribute_id` int NOT NULL,
  `ROLE_role_id` int NOT NULL,
  PRIMARY KEY (`hero_id`),
  KEY `fk_HERO_ATTRIBUTE_idx` (`ATTRIBUTE_attribute_id`),
  KEY `fk_HERO_ROLE1_idx` (`ROLE_role_id`),
  CONSTRAINT `fk_HERO_ATTRIBUTE` FOREIGN KEY (`ATTRIBUTE_attribute_id`) REFERENCES `attribute` (`attribute_id`),
  CONSTRAINT `fk_HERO_ROLE1` FOREIGN KEY (`ROLE_role_id`) REFERENCES `role` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hero`
--

LOCK TABLES `hero` WRITE;
/*!40000 ALTER TABLE `hero` DISABLE KEYS */;
INSERT INTO `hero` VALUES (1,'Axe','Melee',1,5),(2,'Sven','Melee',1,1),(3,'Centaur Warrunner','Melee',1,6),(4,'Earthshaker','Melee',1,5),(5,'Tiny','Melee',1,3),(6,'Juggernaut','Melee',2,1),(7,'Drow Ranger','Ranged',2,8),(8,'Phantom Assassin','Melee',2,1),(9,'Sniper','Ranged',2,1),(10,'Riki','Melee',2,7),(11,'Crystal Maiden','Ranged',3,2),(12,'Lina','Ranged',3,3),(13,'Lion','Ranged',3,4),(14,'Witch Doctor','Ranged',3,2),(15,'Storm Spirit','Ranged',3,7),(16,'Nature\'s Prophet','Ranged',4,8),(17,'Invoker','Ranged',4,3),(18,'Void Spirit','Melee',4,7),(19,'Snapfire','Ranged',4,2),(20,'Marci','Melee',4,6);
/*!40000 ALTER TABLE `hero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(45) NOT NULL,
  `cost` int NOT NULL,
  `item_description` text NOT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,'Blink Dagger',2250,'Teleports you a short distance to escape or initiate.'),(2,'Black King Bar',4050,'Grants spell immunity for a short duration.'),(3,'Power Treads',1400,'Switch between attributes and increase attack speed.'),(4,'Aghanim\'s Scepter',4200,'Upgrades your ultimate or grants a new ability.'),(5,'Shadow Blade',3000,'Grants invisibility and bonus damage on attack.'),(6,'Manta Style',4600,'Creates two illusions of your hero and dispels debuffs.'),(7,'Heart of Tarrasque',5000,'Massively increases health and regeneration.'),(8,'Butterfly',4975,'Increases agility, damage, and evasion.'),(9,'Battle Fury',4100,'Increases cleave damage and farming speed.'),(10,'Arcane Boots',1300,'Restores mana to nearby allies.'),(11,'Glimmer Cape',1950,'Provides invisibility and magic resistance.'),(12,'Force Staff',2250,'Pushes a unit forward, useful for saves and escapes.'),(13,'Daedalus',5150,'Greatly increases critical hit damage.'),(14,'Linken\'s Sphere',4600,'Blocks most targeted spells every few seconds.'),(15,'Assault Cuirass',5125,'Increases armor and attack speed for allies.');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(20) NOT NULL,
  `role_description` text NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Carry','Focuses on farming and dealing high damage later in the game'),(2,'Support','Helps teammates, provides vision, and controls the map'),(3,'Nuker','Deals high burst damage with abilities'),(4,'Disabler','Has abilities that disable or control enemies'),(5,'Initiator','Starts team fights with crowd control or gap-closing abilities'),(6,'Durable','Can absorb large amounts of damage'),(7,'Escape','Has mobility or invisibility skills to avoid danger'),(8,'Pusher','Excels at destroying towers and structures'),(9,'Jungler','Farms neutral camps efficiently');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-12 12:31:44
