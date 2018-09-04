-- MySQL dump 10.13  Distrib 5.6.41, for Linux (x86_64)
--
-- Host: localhost    Database: honeypot
-- ------------------------------------------------------
-- Server version	5.6.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `OpencanaryLog`
--

DROP TABLE IF EXISTS `OpencanaryLog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OpencanaryLog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dst_host` varchar(50) NOT NULL,
  `dst_port` int(11) NOT NULL,
  `honeycred` tinyint(1) DEFAULT NULL,
  `local_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `hostname` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `path` varchar(50) DEFAULT NULL,
  `skin` varchar(50) DEFAULT NULL,
  `useragent` varchar(150) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `session` varchar(50) DEFAULT NULL,
  `localversion` varchar(50) DEFAULT NULL,
  `remoteversion` varchar(50) DEFAULT NULL,
  `df` varchar(30) DEFAULT NULL,
  `idid` varchar(20) DEFAULT NULL,
  `inin` varchar(50) DEFAULT NULL,
  `lenlen` varchar(50) DEFAULT NULL,
  `mac` varchar(60) DEFAULT NULL,
  `outout` varchar(50) DEFAULT NULL,
  `prec` varchar(20) DEFAULT NULL,
  `proto` varchar(10) DEFAULT NULL,
  `res` varchar(20) DEFAULT NULL,
  `syn` varchar(10) DEFAULT NULL,
  `tos` varchar(20) DEFAULT NULL,
  `ttl` varchar(20) DEFAULT NULL,
  `urgp` varchar(5) DEFAULT NULL,
  `window` varchar(50) DEFAULT NULL,
  `logtype` varchar(50) DEFAULT NULL,
  `node_id` varchar(30) NOT NULL,
  `src_host` varchar(50) DEFAULT NULL,
  `src_port` int(11) NOT NULL,
  `white` int(2) NOT NULL DEFAULT '2',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OpencanaryLog`
--

LOCK TABLES `OpencanaryLog` WRITE;
/*!40000 ALTER TABLE `OpencanaryLog` DISABLE KEYS */;
/*!40000 ALTER TABLE `OpencanaryLog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'admin','21232f297a57a5a743894a0e4a801fc3','2018-08-07 08:52:45');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Whiteip`
--

DROP TABLE IF EXISTS `Whiteip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Whiteip` (
  `src_host` varchar(50) NOT NULL,
  PRIMARY KEY (`src_host`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Whiteip`
--

LOCK TABLES `Whiteip` WRITE;
/*!40000 ALTER TABLE `Whiteip` DISABLE KEYS */;
/*!40000 ALTER TABLE `Whiteip` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-04  5:16:56
