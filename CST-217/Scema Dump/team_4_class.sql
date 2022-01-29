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
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `ID` varchar(7) NOT NULL,
  `Class Time` time DEFAULT NULL,
  `Class Start Date` date DEFAULT NULL,
  `Class End Date` date DEFAULT NULL,
  `Class Meeting Days` varchar(45) DEFAULT NULL,
  `Professor_ID` int NOT NULL,
  `Courses_ID` varchar(7) NOT NULL,
  `rooms_Room Number` int DEFAULT NULL,
  `rooms_Buildings_Building Number` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_Classes_Professor1_idx` (`Professor_ID`),
  KEY `fk_Classes_Courses1_idx` (`Courses_ID`),
  KEY `fk_class_rooms1_idx` (`rooms_Room Number`,`rooms_Buildings_Building Number`),
  CONSTRAINT `fk_class_rooms1` FOREIGN KEY (`rooms_Room Number`, `rooms_Buildings_Building Number`) REFERENCES `rooms` (`Room Number`, `Buildings_Building Number`),
  CONSTRAINT `fk_Classes_Courses1` FOREIGN KEY (`Courses_ID`) REFERENCES `courses` (`ID`),
  CONSTRAINT `fk_Classes_Professor1` FOREIGN KEY (`Professor_ID`) REFERENCES `professor` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES ('1251','15:00:00','2021-01-04','2022-05-06','Mon, Fri',69134,'BUS-100',101,4),('1348','14:20:00','2021-01-04','2022-05-04','Fri, Mon',60412,'CST-210',103,5),('1425','16:30:00','2021-01-04','2022-05-08','Fri, Mon',91574,'BUS-313',102,4),('1497','09:00:00','2021-01-04','2022-05-09','Tues, Wed',98670,'PHY-113',102,3),('1709','18:00:00','2021-01-04','2022-05-02','Mon, Wed',52385,'MAT-374',104,3),('1778','13:00:00','2021-01-04','2022-05-05','Fri, Tues',65626,'CST-217',105,5),('1802','07:45:00','2021-01-04','2022-05-07','Fri, Thur',82377,'BUS-203',103,4),('1920','13:00:00','2021-01-04','2022-05-01','Thur, Fri',18309,'MAT-121',103,3),('1934','10:45:00','2021-01-04','2022-04-30','Thur, Fri',16391,'MAT-345',102,3),('1948','15:30:00','2021-01-04','2022-05-03','Tues, Wed',53654,'CST-105',101,5);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
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
