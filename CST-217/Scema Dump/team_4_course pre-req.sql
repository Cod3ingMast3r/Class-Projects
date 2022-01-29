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
-- Table structure for table `course pre-req`
--

DROP TABLE IF EXISTS `course pre-req`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course pre-req` (
  `Courses_ID` varchar(7) NOT NULL,
  `Course_Pre-rec` varchar(7) NOT NULL DEFAULT 'Null',
  PRIMARY KEY (`Courses_ID`,`Course_Pre-rec`),
  KEY `fk_Courses_has_Courses_Courses2_idx` (`Course_Pre-rec`),
  KEY `fk_Courses_has_Courses_Courses1_idx` (`Courses_ID`),
  CONSTRAINT `fk_Courses_has_Courses_Courses1` FOREIGN KEY (`Courses_ID`) REFERENCES `courses` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course pre-req`
--

LOCK TABLES `course pre-req` WRITE;
/*!40000 ALTER TABLE `course pre-req` DISABLE KEYS */;
INSERT INTO `course pre-req` VALUES ('BUS-203','BUS-100'),('BUS-313','BUS-203'),('CST-210','CST-105'),('CST-217','CST-210'),('MAT-345','MAT-121'),('MAT-374','MAT-345'),('BUS-100','Null'),('CST-105','Null'),('MAT-121','Null'),('PHY-113','Null');
/*!40000 ALTER TABLE `course pre-req` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-27 19:12:05
