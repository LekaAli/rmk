-- Adminer 4.2.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `city`;
CREATE TABLE `city` (
  `city_id` int(3) NOT NULL AUTO_INCREMENT,
  `state_id` int(3) NOT NULL,
  `city_name` varchar(35) NOT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `city` (`city_id`, `state_id`, `city_name`) VALUES
(1,	1,	'Surat'),
(2,	1,	'Ahmedabad'),
(3,	2,	'Pune'),
(4,	2,	'Mumbai'),
(5,	3,	'royston'),
(6,	3,	'bedford'),
(7,	4,	'Litherland'),
(8,	4,	'ST. helens'),
(9,	5,	'Abbeville'),
(10,	5,	'Alpine'),
(11,	6,	'Angoon'),
(12,	6,	'Aniak'),
(13,	7,	'Aprelevka'),
(14,	7,	'Balashikha'),
(15,	8,	'Lukhovitsy'),
(16,	8,	'Lytkarino');

DROP TABLE IF EXISTS `country`;
CREATE TABLE `country` (
  `country_id` int(3) NOT NULL AUTO_INCREMENT,
  `country_name` varchar(25) NOT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `country` (`country_id`, `country_name`) VALUES
(1,	'India'),
(2,	'United kingdom'),
(3,	'United States'),
(4,	'Russia');

DROP TABLE IF EXISTS `state`;
CREATE TABLE `state` (
  `state_id` int(3) NOT NULL AUTO_INCREMENT,
  `country_id` int(3) NOT NULL,
  `state_name` varchar(35) NOT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `state` (`state_id`, `country_id`, `state_name`) VALUES
(1,	1,	'Gujarat'),
(2,	1,	'Maharashtra'),
(3,	2,	'Cambridge'),
(4,	2,	'Liverpool'),
(5,	3,	'Alabama'),
(6,	3,	'Alaska'),
(7,	4,	'Abakan'),
(8,	4,	'Moscow');

-- 2015-11-14 09:17:55
