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
-- Table structure for table `Host`
--

DROP TABLE IF EXISTS `Host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Host` (
  `id` varchar(50) NOT NULL,
  `last_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `hostname` varchar(50) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_hostname_ip` (`hostname`,`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Host`
--

LOCK TABLES `Host` WRITE;
/*!40000 ALTER TABLE `Host` DISABLE KEYS */;
INSERT INTO `Host` VALUES ('0c715140c9fbbc6bf9aaef73fb63ad86','2018-12-25 19:46:21','opencanary-1','172.18.114.241','online'),('1ace5853dfe644d18d1d1eb1a72658c5','2018-12-25 20:03:39','opencanary-1','172.18.215.191','online');
/*!40000 ALTER TABLE `Host` ENABLE KEYS */;
UNLOCK TABLES;

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
  `useragent` varchar(250) DEFAULT NULL,
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
  `white` int(11) NOT NULL,
  `repo` varchar(150) DEFAULT NULL,
  `ntp_cmd` varchar(150) DEFAULT NULL,
  `args` varchar(150) DEFAULT NULL,
  `cmd` varchar(150) DEFAULT NULL,
  `banner_id` varchar(30) DEFAULT NULL,
  `data` varchar(150) DEFAULT NULL,
  `function` varchar(150) DEFAULT NULL,
  `vnc_client_response` varchar(150) DEFAULT NULL,
  `vnc_password` varchar(50) DEFAULT NULL,
  `vnc_server_challenge` varchar(150) DEFAULT NULL,
  `inputs` varchar(150) DEFAULT NULL,
  `domain` varchar(150) DEFAULT NULL,
  `headers_call_id` varchar(150) DEFAULT NULL,
  `headers_content_length` varchar(150) DEFAULT NULL,
  `headers_cseq` varchar(150) DEFAULT NULL,
  `headers_from` varchar(150) DEFAULT NULL,
  `headers_to` varchar(150) DEFAULT NULL,
  `headers_via` varchar(150) DEFAULT NULL,
  `community_string` varchar(50) DEFAULT NULL,
  `requests` varchar(50) DEFAULT NULL,
  `urg` varchar(50) DEFAULT NULL,
  `psh` varchar(50) DEFAULT NULL,
  `fin` varchar(50) DEFAULT NULL,
  `appname` varchar(150) DEFAULT NULL,
  `cltintname` varchar(150) DEFAULT NULL,
  `database` varchar(50) DEFAULT NULL,
  `language` varchar(50) DEFAULT NULL,
  `servername` varchar(50) DEFAULT NULL,
  `domainname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OpencanaryLog`
--

LOCK TABLES `OpencanaryLog` WRITE;
/*!40000 ALTER TABLE `OpencanaryLog` DISABLE KEYS */;
INSERT INTO `OpencanaryLog` VALUES (2,'172.18.200.58',1433,0,'2019-01-07 01:04:59','Piroguehost','sa123456','','','','sa','','','','','','','','','','','','','','','','','','9001','opencanary-1','172.18.205.14',64344,2,'','','','','','','','','','','','','','','','','','','','','','','','SQLPro for MSSQL (hankinsoft.com)','DB-Library','test','us_english','172.18.200.58:1433',''),(3,'172.18.200.58',1433,0,'2019-01-07 01:13:29','','','','','','','','','','','','','','','','','','','','','','','','9002','opencanary-1','172.18.205.14',64499,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(4,'192.168.1.7',5060,0,'2019-01-06 08:51:08','','','','','','','','','','','26441','eth1','40','08:00:27:da:4c:e2:6c:96:cf:dd:ee:bd:08:00','','0x00','TCP','0x00','','0x00','50','0','1024','5003','opencanary-1','192.168.1.6',58015,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(5,'192.168.1.7',139,0,'2019-01-06 08:48:46','','','','','','','','','','','19984','eth1','40','08:00:27:da:4c:e2:6c:96:cf:dd:ee:bd:08:00','','0x00','TCP','0x00','','0x00','56','0','1024','5004','opencanary-1','192.168.1.6',50913,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(6,'192.168.1.7',23,0,'2019-01-06 08:46:18','','','','','','','','','','','29768','eth1','40','08:00:27:da:4c:e2:6c:96:cf:dd:ee:bd:08:00','','0x00','TCP','0x00','','0x00','59','0','1024','5005','opencanary-1','192.168.1.6',35116,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(7,'192.168.1.7',21,0,'2019-01-06 08:35:24','','','','','','','','','','','51918','eth1','56','08:00:27:da:4c:e2:6c:96:cf:dd:ee:bd:08:00','','0x00','TCP','0x00','','0x00','58','0','512','5001','opencanary-1','192.168.1.6',40088,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(8,'192.168.1.7',21,0,'2019-01-06 08:35:24','','','','','','','','','','','37499','eth1','60','08:00:27:da:4c:e2:6c:96:cf:dd:ee:bd:08:00','','0x00','TCP','0x00','','0x00','56','0','256','5002','opencanary-1','192.168.1.6',40098,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(9,'0.0.0.0',161,0,'2019-01-06 03:17:27','','','','','','','','','','','','','','','','','','','','','','','','13001','opencanary-1','192.168.1.7',47112,2,'','','','','','','','','','','','','','','','','','','password','1.3.6.1.2.1.1.1','','','','','','','','',''),(10,'0.0.0.0',5060,0,'2019-01-06 01:55:13','','','','','','','','','','','','','','','','','','','','','','','','15001','opencanary-1','192.168.1.7',46759,2,'','','','','','','','','','','','','1337@192.168.1.7','','1 REGISTER','<sip:adminsip@192.168.1.7>','<sip:adminsip@192.168.1.7>','SIP/2.0/UDP 10.0.2.15:46759;received=192.168.1.7','','','','','','','','','','',''),(11,'192.168.1.7',3389,0,'2019-01-06 00:59:14','HelloHost','helloword','','','','administrator1','','','','','','','','','','','','','','','','','','14001','opencanary-1','192.168.1.6',59955,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(12,'192.168.1.7',3389,0,'2019-01-06 00:59:27','','','','','','','','','','','','','','','','','','','','','','','','14001','opencanary-1','192.168.1.6',59955,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(13,'192.168.1.7',5000,0,'2019-01-06 00:21:29','','','','','','','','','','','','','','','','','','','','','','','','12001','opencanary-1','192.168.1.6',54634,2,'','','','','','','','58c00be9ee5b7f3b666771dd2bda9309','<Password was not in the common list>','953e2dff7e4d3a3114527c282817ce1d','','','','','','','','','','','','','','','','','','',''),(14,'192.168.1.6',8001,0,'2019-01-05 09:19:13','','','','','','','','','','','','','','','','','','','','','','','','18004','opencanary-1','192.168.1.3',59176,2,'','','','','1','','DATA_RECEIVED','','','','','','','','','','','','','','','','','','','','','',''),(15,'192.168.1.6',8001,0,'2019-01-05 09:18:52','','','','','','','','','','','','','','','','','','','','','','','','18002','opencanary-1','192.168.1.3',59176,2,'','','','','1','','CONNECTION_MADE','','','','','','','','','','','','','','','','','','','','','',''),(16,'192.168.1.7',6379,0,'2019-01-05 08:10:10','','','','','','','','','','','','','','','','','','','','','','','','17001','opencanary-1','192.168.1.6',34471,2,'','','admin','AUTH','','','','','','','','','','','','','','','','','','','','','','','','',''),(17,'192.168.1.7',6379,0,'2019-01-05 08:09:36','','','','','','','','','','','','','','','','','','','','','','','','17001','opencanary-1','192.168.1.6',34471,2,'','','get requirepass','CONFIG','','','','','','','','','','','','','','','','','','','','','','','','',''),(18,'192.168.1.7',6379,0,'2019-01-05 08:08:15','','','','','','','','','','','','','','','','','','','','','','','','17001','opencanary-1','192.168.1.6',34471,2,'','','*','KEYS','','','','','','','','','','','','','','','','','','','','','','','','',''),(19,'192.168.1.7',6379,0,'2019-01-05 08:05:12','','','','','','','','','','','','','','','','','','','','','','','','17001','opencanary-1','192.168.1.6',34471,2,'','','','COMMAND','','','','','','','','','','','','','','','','','','','','','','','','',''),(20,'0.0.0.0',123,0,'2019-01-05 07:58:52','','','','','','','','','','','','','','','','','','','','','','','','11001','opencanary-1','192.168.1.6',57886,2,'','monlist','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(21,'192.168.1.7',9418,0,'2019-01-05 07:38:46','','','','','','','','','','','','','','','','','','','','','','','','16001','opencanary-1','192.168.1.3',57606,2,'tmp.git','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(22,'172.18.200.58',8080,0,'2019-01-07 05:26:48','','passsquid','','','','squidadmin','','','','','','','','','','','','','','','','','','7001','opencanary-1','172.18.205.14',53798,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(23,'172.18.200.58',80,0,'2019-01-07 05:47:46','172.18.200.58','admin888','/index.html','nasLogin','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:61.0) Gecko/20100101 Firefox/61.0','admin','','','','','','','','','','','','','','','','','','3001','opencanary-1','172.18.205.14',54488,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(24,'172.18.200.58',21,0,'2019-01-07 05:50:54','','admin123','','','','ftpadmin','','','','','','','','','','','','','','','','','','2000','opencanary-1','172.18.205.14',54573,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(25,'172.18.200.58',2222,0,'2019-01-07 05:54:28','','','','','','','3','','','','','','','','','','','','','','','','','4000','opencanary-1','172.18.205.14',54639,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(26,'172.18.200.58',2222,0,'2019-01-07 05:54:28','','','','','','','','SSH-2.0-OpenSSH_5.1p1 Debian-4','SSH-2.0-OpenSSH_7.0 ZOC_7.16.1','','','','','','','','','','','','','','','4001','opencanary-1','172.18.205.14',54639,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','',''),(27,'172.18.200.58',2222,0,'2019-01-07 05:54:32','','root123','','','','root','','SSH-2.0-OpenSSH_5.1p1 Debian-4','SSH-2.0-OpenSSH_7.0 ZOC_7.16.1','','','','','','','','','','','','','','','4002','opencanary-1','172.18.205.14',54639,2,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','');
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

--
-- Table structure for table `Whiteport`
--

DROP TABLE IF EXISTS `Whiteport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Whiteport` (
  `dst_port` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`dst_port`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Whiteport`
--

LOCK TABLES `Whiteport` WRITE;
/*!40000 ALTER TABLE `Whiteport` DISABLE KEYS */;
/*!40000 ALTER TABLE `Whiteport` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-07 22:20:47
