-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: team_4
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activities` (
  `ID` int NOT NULL,
  `Start Time` time DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Budget` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `rooms_Room_Number` int DEFAULT NULL,
  `rooms_Buildings_Building_Number` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_activities_rooms1_idx` (`rooms_Room_Number`,`rooms_Buildings_Building_Number`),
  CONSTRAINT `fk_activities_rooms1` FOREIGN KEY (`rooms_Room_Number`, `rooms_Buildings_Building_Number`) REFERENCES `rooms` (`Room_Number`, `Buildings_Building_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
INSERT INTO `activities` VALUES (143,'09:47:00','2021-01-17','3833','Soccer',NULL,NULL),(177,'11:16:00','2021-01-17','4475','Technology',NULL,NULL),(293,'15:15:00','2021-01-18','405','Mountain Biking',103,2),(388,'09:40:00','2021-01-30','2618','Soccer',NULL,NULL),(475,'16:30:00','2021-01-11','685','Basketball',104,3),(488,'13:19:00','2021-01-17','2144','ACE',NULL,NULL),(629,'17:36:00','2021-01-01','4506','Cooking',NULL,5),(675,'13:38:00','2021-01-05','2489','Cooking',NULL,NULL),(713,'13:09:00','2021-01-25','2095','Game Design',NULL,NULL);
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-10 18:09:35
