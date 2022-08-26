-- MariaDB dump 10.19  Distrib 10.5.9-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: gestion
-- ------------------------------------------------------
-- Server version	10.5.9-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(30) DEFAULT NULL,
  `passwrd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','admin'),(2,'hana','hana');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `etudiant` (
  `cin` int(11) NOT NULL,
  `nom` varchar(30) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `classe` int(11) DEFAULT NULL,
  `dns` date DEFAULT NULL,
  `specialite` int(11) DEFAULT NULL,
  `sexe` varchar(1) DEFAULT NULL,
  `tel` int(8) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `adresse` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cin`),
  KEY `specialite` (`specialite`),
  CONSTRAINT `etudiant_ibfk_1` FOREIGN KEY (`specialite`) REFERENCES `specialite` (`code`),
  CONSTRAINT `f1` FOREIGN KEY (`specialite`) REFERENCES `specialite` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etudiant`
--

LOCK TABLES `etudiant` WRITE;
/*!40000 ALTER TABLE `etudiant` DISABLE KEYS */;
INSERT INTO `etudiant` VALUES (7491023,'warteni ','olfa',1,'1996-02-02',830,'f',52146780,'olfa@gmail.com','Klibia'),(40125689,'Ghizaoui','Wafa',1,'1998-02-04',120,'f',56939140,'wafa@hotmail.fr','Marsa'),(99999999,'Ghizaoui','Hana',1,'1998-07-04',120,'f',22036750,'hana@gmail.com','ariana');
/*!40000 ALTER TABLE `etudiant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matieres`
--

DROP TABLE IF EXISTS `matieres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matieres` (
  `code` int(11) NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `classe` int(11) DEFAULT NULL,
  `specialite` int(11) DEFAULT NULL,
  `semestre` int(11) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `coeff` int(11) DEFAULT NULL,
  `codemodule` int(11) DEFAULT NULL,
  PRIMARY KEY (`code`),
  KEY `specialite` (`specialite`),
  KEY `codemodule` (`codemodule`),
  CONSTRAINT `matieres_ibfk_1` FOREIGN KEY (`specialite`) REFERENCES `specialite` (`code`),
  CONSTRAINT `matieres_ibfk_2` FOREIGN KEY (`codemodule`) REFERENCES `module` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matieres`
--

LOCK TABLES `matieres` WRITE;
/*!40000 ALTER TABLE `matieres` DISABLE KEYS */;
INSERT INTO `matieres` VALUES (81,'Theorie des graphes',1,120,1,'DsExaman',NULL,NULL),(560,'Analyse Numérique',1,221,2,'DsExaman',NULL,NULL),(788,'Télécome',1,120,1,'TpDsExaman',NULL,NULL),(920,'Electrique',1,120,1,'TpDsExaman',NULL,NULL);
/*!40000 ALTER TABLE `matieres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `module` (
  `code` int(11) NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `code_mat1` int(11) DEFAULT NULL,
  `code_mat2` int(11) DEFAULT NULL,
  `code_mat3` int(11) DEFAULT NULL,
  PRIMARY KEY (`code`),
  KEY `code_mat1` (`code_mat1`),
  KEY `code_mat2` (`code_mat2`),
  KEY `code_mat3` (`code_mat3`),
  CONSTRAINT `module_ibfk_1` FOREIGN KEY (`code_mat1`) REFERENCES `matieres` (`code`),
  CONSTRAINT `module_ibfk_2` FOREIGN KEY (`code_mat2`) REFERENCES `matieres` (`code`),
  CONSTRAINT `module_ibfk_3` FOREIGN KEY (`code_mat3`) REFERENCES `matieres` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module`
--

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
INSERT INTO `module` VALUES (5632,'Math',NULL,NULL,NULL);
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `note`
--

DROP TABLE IF EXISTS `note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `note` (
  `cin` int(11) NOT NULL,
  `codem` int(11) NOT NULL,
  `tp` float DEFAULT NULL,
  `ds` float DEFAULT NULL,
  `ex` float DEFAULT NULL,
  `moy` float DEFAULT NULL,
  PRIMARY KEY (`cin`,`codem`),
  KEY `codem` (`codem`),
  CONSTRAINT `note_ibfk_1` FOREIGN KEY (`cin`) REFERENCES `etudiant` (`cin`),
  CONSTRAINT `note_ibfk_2` FOREIGN KEY (`codem`) REFERENCES `matieres` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `note`
--

LOCK TABLES `note` WRITE;
/*!40000 ALTER TABLE `note` DISABLE KEYS */;
INSERT INTO `note` VALUES (40125689,788,17,11,13.5,13.35);
/*!40000 ALTER TABLE `note` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialite`
--

DROP TABLE IF EXISTS `specialite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `specialite` (
  `code` int(11) NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `niveau` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialite`
--

LOCK TABLES `specialite` WRITE;
/*!40000 ALTER TABLE `specialite` DISABLE KEYS */;
INSERT INTO `specialite` VALUES (120,'Administration réseaux','Licence'),(221,'Genie logiciel','ing'),(400,'Embarqué','ing'),(450,'Intelligence artificielle','master'),(830,'Big data','master');
/*!40000 ALTER TABLE `specialite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `nom` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-03 22:00:49
