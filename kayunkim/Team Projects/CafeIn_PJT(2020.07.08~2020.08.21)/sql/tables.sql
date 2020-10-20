CREATE DATABASE `cafeproject` ;

use cafeproject

CREATE TABLE `cafe` (
  `cafeno` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `status` varchar(45) DEFAULT '영업중',
  `address` varchar(45),
  `tel` varchar(45),
  `business_hours` varchar(45),
  PRIMARY KEY (`cafeno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `user` (
  `id` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `name` varchar(30),
  `gender` varchar(6),
  `phone` varchar(20),
  `birth` datetime,
  `survey` varchar(30),
  `auth` varchar(30) DEFAULT 'user',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `post` (
  `pno` int NOT NULL AUTO_INCREMENT,
  `uid` varchar(45) NOT NULL,
  `cafeno` int NOT NULL,
  `contents` varchar(200),
  `image` varchar(100),
  `taste`  varchar(45),
  `mood`  varchar(45),
  `clean` varchar(45),
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pno`),
  CONSTRAINT `post_writer_fk` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `post_cafeno_fk` FOREIGN KEY (`cafeno`) REFERENCES `cafe` (`cafeno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `comment` (
  `cno` int NOT NULL AUTO_INCREMENT,
  `contents` varchar(45) NOT NULL,
  `pno` int NOT NULL,
  `uid` varchar(20) NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cno`),
  KEY `comment_pno_fk_idx` (`pno`),
  CONSTRAINT `comment_pno_fk` FOREIGN KEY (`pno`) REFERENCES `post` (`pno`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comment_uid_fk` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `like` (
  `lno` int NOT NULL AUTO_INCREMENT,
  `cafeno` int NOT NULL,
  `uid` varchar(45) NOT NULL,
  PRIMARY KEY (`lno`),
  KEY `like_cafeno_fk_idx` (`cafeno`),
  KEY `like_uid_fk_idx` (`uid`),
  CONSTRAINT `like_cafeno_fk` FOREIGN KEY (`cafeno`) REFERENCES `cafe` (`cafeno`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `like_uid_fk` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `stamp` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `cafeno` int NOT NULL,
  `uid` varchar(45) NOT NULL,
  PRIMARY KEY (`sno`),
  KEY `stamp_cafeno_fk_idx` (`cafeno`),
  KEY `stamp_uid_fk_idx` (`uid`),
  CONSTRAINT `stamp_cafeno_fk` FOREIGN KEY (`cafeno`) REFERENCES `cafe` (`cafeno`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `stamp_uid_fk` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `follow` (
  `fno` int NOT NULL AUTO_INCREMENT,
  `uid` varchar(45) NOT NULL,
  `followingid` varchar(45) NOT NULL,
  PRIMARY KEY (`fno`),
  KEY `follow_uid_fk_idx` (`uid`),
  KEY `follow_followingid_fk_idx` (`followingid`),
  CONSTRAINT `follow_uid_fk` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `follow_followingid_fk` FOREIGN KEY (`followingid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `menu` (
  `mno` int NOT NULL AUTO_INCREMENT,
  `cafeno` int NOT NULL,
  `item` varchar(45) NOT NULL,
  `price` int,
  PRIMARY KEY (`mno`),
  CONSTRAINT `menu` FOREIGN KEY (`cafeno`) REFERENCES `cafe` (`cafeno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

show tables;

