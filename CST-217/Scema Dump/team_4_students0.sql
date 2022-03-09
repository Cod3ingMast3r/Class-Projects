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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `ID` int NOT NULL,
  `fName` varchar(45) NOT NULL,
  `lName` varchar(45) NOT NULL,
  `Sex` enum('M','F') NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Date_of_Birth` varchar(45) DEFAULT NULL,
  `Major` varchar(45) DEFAULT NULL,
  `Street_Address` varchar(45) DEFAULT NULL,
  `City` varchar(45) DEFAULT NULL,
  `Zip` varchar(45) DEFAULT NULL,
  `Country` varchar(45) DEFAULT NULL,
  `rooms_Room_Number` int DEFAULT NULL,
  `rooms_Buildings_Building_Number` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`),
  KEY `fk_students_rooms1_idx` (`rooms_Room_Number`,`rooms_Buildings_Building_Number`),
  CONSTRAINT `fk_students_rooms1` FOREIGN KEY (`rooms_Room_Number`, `rooms_Buildings_Building_Number`) REFERENCES `rooms` (`Room_Number`, `Buildings_Building_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (15940,'Isaac','Barlow','F','isaac.barlow9083@gcu.edu','(468) 223-3653','7/17/1986','Chemistry','Ap #846-1249 Et Rd.','Gasteiz','4632','Mexico',101,1),(22666,'Chiquita','Joyner','F','j.chiquita353@gcu.edu','(941) 218-4877','2/11/1956','Business Administration','502-3334 Nec Av.','Falerone','XC4 6QM','Ireland',101,2),(24262,'Melinda','Reid','F','reid-melinda@gcu.edu','(293) 731-7725','4/17/1981','Civil Engineering','P.O. Box 829, 1735 Consectetuer Ave','Gualdo Tadino','52765','Italy',101,1),(42527,'Jarrod','Vargas','F','vargas-jarrod@gcu.edu','(657) 109-1998','2/5/1985','Business Administration','Ap #876-5449 Massa. St.','Ravensburg','518448','Canada',101,1),(56613,'Lael','Clemons','M','clemons.lael6882@gcu.edu','(455) 973-9947','6/11/1958','Electrical Engineering','707-1731 Placerat Rd.','Huaraz','1116','United Kingdom',102,1),(57283,'Stephen','Jennings','F','stephen-jennings7514@gcu.edu','(669) 368-7342','10/4/1985','Computer Science','Ap #992-8738 Nibh. Rd.','Cusco','671722','Spain',103,2),(62382,'Solomon','Kennedy','M','solomonkennedy1774@gcu.edu','(184) 751-0204','1/27/1972','Chemistry','128-1625 Mi Rd.','SÃ¶dertÃ¤lje','34-811','United States',104,2),(69750,'Nadine','Reyes','M','n.reyes@gcu.edu','(186) 624-3237','2/3/1959','Exercise Science','Ap #502-9178 Posuere Av.','Leersum','34435','Germany',105,2),(74218,'Constance','Juarez','M','juarez.constance4915@gcu.edu','(584) 492-4532','2/14/1959','Computer Science','580-2985 Sapien, St.','Gasteiz','41535','Costa Rica',105,2),(88422,'Rose','Mclaughlin','M','r_mclaughlin@gcu.edu','(632) 985-2631','12/3/1995','Computer Science','P.O. Box 701, 2496 Adipiscing St.','SÃ¶ke','275547','New Zealand',105,1);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
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
