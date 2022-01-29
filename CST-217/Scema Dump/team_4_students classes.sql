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
-- Table structure for table `students classes`
--

DROP TABLE IF EXISTS `students classes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students classes` (
  `Classes_Courses_ID` varchar(7) NOT NULL,
  `Students_ID` int NOT NULL,
  PRIMARY KEY (`Classes_Courses_ID`,`Students_ID`),
  KEY `fk_Classes_has_Students_Students1_idx` (`Students_ID`),
  KEY `fk_Classes_has_Students_Classes1_idx` (`Classes_Courses_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students classes`
--

LOCK TABLES `students classes` WRITE;
/*!40000 ALTER TABLE `students classes` DISABLE KEYS */;
INSERT INTO `students classes` VALUES ('BUS-100',15940),('MAT-374',15940),('CST-217',22666),('MAT-121',22666),('PHY-113',22666),('BUS-100',24262),('MAT-374',24262),('BUS-313',42527),('CST-105',42527),('CST-217',56613),('MAT-121',56613),('PHY-113',56613),('CST-210',57283),('MAT-345',57283),('BUS-203',62382),('CST-105',62382),('CST-210',69750),('MAT-345',69750),('CST-105',74218),('CST-210',74218),('MAT-345',74218),('CST-217',88422),('MAT-121',88422);
/*!40000 ALTER TABLE `students classes` ENABLE KEYS */;
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
