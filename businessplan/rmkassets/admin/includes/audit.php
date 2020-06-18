SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `auditTest` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;
USE `auditTest` ;

-- -----------------------------------------------------
-- Table `auditTest`.`users`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`users` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`auditTasks`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`auditTasks` (
  `task` CHAR(1) NOT NULL ,
  `name` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`task`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audits`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audits` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `users_id` INT UNSIGNED NULL ,
  `dateChanged` DATETIME NOT NULL ,
  `dbUser` VARCHAR(45) NOT NULL ,
  `requesting_ip` CHAR(15) NULL ,
  `tableName` VARCHAR(45) NOT NULL ,
  `task` CHAR(1) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_audits_users_idx` (`users_id` ASC) ,
  INDEX `fk_audits_tasks1_idx` (`task` ASC) ,
  CONSTRAINT `fk_audits_users`
    FOREIGN KEY (`users_id` )
    REFERENCES `auditTest`.`users` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_audits_tasks1`
    FOREIGN KEY (`task` )
    REFERENCES `auditTest`.`auditTasks` (`task` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audits_1pk`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audits_1pk` (
  `audits_id` INT UNSIGNED NOT NULL ,
  `pk1` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`audits_id`) ,
  CONSTRAINT `fk_audits_1pk_audits1`
    FOREIGN KEY (`audits_id` )
    REFERENCES `auditTest`.`audits` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audits_2pk`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audits_2pk` (
  `audits_id` INT UNSIGNED NOT NULL ,
  `pk1` VARCHAR(45) NOT NULL ,
  `pk2` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`audits_id`) ,
  CONSTRAINT `fk_audits_2pk_audits1`
    FOREIGN KEY (`audits_id` )
    REFERENCES `auditTest`.`audits` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audits_3pk`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audits_3pk` (
  `audits_id` INT UNSIGNED NOT NULL ,
  `pk1` VARCHAR(45) NOT NULL ,
  `pk2` VARCHAR(45) NOT NULL ,
  `pk3` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`audits_id`) ,
  CONSTRAINT `fk_audits_3pk_audits1`
    FOREIGN KEY (`audits_id` )
    REFERENCES `auditTest`.`audits` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audit_int`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audit_int` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `audits_id` INT UNSIGNED NOT NULL ,
  `columnName` VARCHAR(45) NOT NULL ,
  `oldValue` INT NULL ,
  `newValue` INT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_audit_int_audits1_idx` (`audits_id` ASC) ,
  CONSTRAINT `fk_audit_int_audits1`
    FOREIGN KEY (`audits_id` )
    REFERENCES `auditTest`.`audits` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audit_text`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audit_text` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `audits_id` INT UNSIGNED NOT NULL ,
  `columnName` VARCHAR(45) NOT NULL ,
  `oldValue` TEXT NULL ,
  `newValue` TEXT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_audit_int_audits1_idx` (`audits_id` ASC) ,
  CONSTRAINT `fk_audit_int_audits10`
    FOREIGN KEY (`audits_id` )
    REFERENCES `auditTest`.`audits` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`audit_var_45`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`audit_var_45` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `audits_id` INT UNSIGNED NOT NULL ,
  `columnName` VARCHAR(45) NOT NULL ,
  `oldValue` VARCHAR(45) NULL ,
  `newValue` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_audit_int_audits1_idx` (`audits_id` ASC) ,
  CONSTRAINT `fk_audit_int_audits100`
    FOREIGN KEY (`audits_id` )
    REFERENCES `auditTest`.`audits` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`students`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`students` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `ssn` CHAR(10) NOT NULL ,
  `notes` TEXT NULL ,
  `nickname` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`courses`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`courses` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `course_number` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `auditTest`.`courses_has_students`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `auditTest`.`courses_has_students` (
  `courses_id` INT UNSIGNED NOT NULL ,
  `students_id` INT UNSIGNED NOT NULL ,
  `other_int` INT NULL ,
  PRIMARY KEY (`courses_id`, `students_id`) ,
  INDEX `fk_courses_has_students_students1_idx` (`students_id` ASC) ,
  INDEX `fk_courses_has_students_courses1_idx` (`courses_id` ASC) ,
  CONSTRAINT `fk_courses_has_students_courses1`
    FOREIGN KEY (`courses_id` )
    REFERENCES `auditTest`.`courses` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_courses_has_students_students1`
    FOREIGN KEY (`students_id` )
    REFERENCES `auditTest`.`students` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `auditTest`;

DELIMITER $$
USE `auditTest`$$


CREATE TRIGGER tg_students_ins AFTER INSERT ON students
FOR EACH ROW 
BEGIN
    INSERT INTO audits(tableName,task,dateChanged,users_id,dbUser,requesting_ip) VALUES ('students', 'i', NOW(), @users_id, USER(), @requesting_ip );
    SET @AID=LAST_INSERT_ID();
    INSERT INTO audits_1pk(audits_id,pk1) VALUES (@AID,NEW.id );
    IF NEW.name IS NOT NULL THEN
        INSERT INTO audit_var_45(audits_id,columnName,oldValue,newValue) VALUES (@AID,'name',NULL,NEW.name);
    END IF;
    IF NEW.ssn IS NOT NULL THEN
        INSERT INTO audit_var_45(audits_id,columnName,oldValue,newValue) VALUES (@AID,'ssn',NULL,NEW.ssn);
    END IF;
    IF NEW.notes IS NOT NULL THEN
        INSERT INTO audit_text(audits_id,columnName,oldValue,newValue) VALUES (@AID,'notes',NULL,NEW.notes);
    END IF;
END$$

USE `auditTest`$$


CREATE TRIGGER tg_students_upd AFTER UPDATE ON students
FOR EACH ROW 
BEGIN
    IF NOT NEW.name <=> OLD.name OR NOT NEW.ssn <=> OLD.ssn OR NOT NEW.notes <=> OLD.notes THEN
        INSERT INTO audits(tableName,task,dateChanged,users_id,dbUser,requesting_ip) VALUES ('students', 'u', NOW(), @users_id, USER(), @requesting_ip );
        SET @AID=LAST_INSERT_ID();
        INSERT INTO audits_1pk(audits_id,pk1) VALUES (@AID,NEW.id );
        IF NOT NEW.name <=> OLD.name THEN
            INSERT INTO audit_var_45(audits_id,columnName,oldValue,newValue) VALUES (@AID,'name',OLD.name,NEW.name);
        END IF;
        IF NOT NEW.ssn <=> OLD.ssn THEN
            INSERT INTO audit_var_45(audits_id,columnName,oldValue,newValue) VALUES (@AID,'ssn',OLD.ssn,NEW.ssn);
        END IF;
        IF NOT NEW.notes <=> OLD.notes THEN
            INSERT INTO audit_text(audits_id,columnName,oldValue,newValue) VALUES (@AID,'notes',OLD.notes,NEW.notes);
        END IF;
    END IF;
END$$

USE `auditTest`$$


CREATE TRIGGER tg_students_del AFTER DELETE ON students
FOR EACH ROW 
BEGIN
    INSERT INTO audits(tableName,task,dateChanged,users_id,dbUser,requesting_ip) VALUES ('students', 'd', NOW(), @users_id, USER(), @requesting_ip );
    SET @AID=LAST_INSERT_ID();
    INSERT INTO audits_1pk(audits_id,pk1) VALUES (@AID,OLD.id );
END$$


DELIMITER ;

DELIMITER $$
USE `auditTest`$$


CREATE TRIGGER tg_courses_has_students_ins AFTER INSERT ON courses_has_students
FOR EACH ROW 
BEGIN
    INSERT INTO audits(tableName,task,dateChanged,users_id,dbUser,requesting_ip) VALUES ('courses_has_students', 'i', NOW(), @users_id, USER(), @requesting_ip );
    SET @AID=LAST_INSERT_ID();
    INSERT INTO audits_2pk(audits_id,pk1,pk2) VALUES (@AID,NEW.courses_id,NEW.students_id);
    IF NEW.other_int IS NOT NULL THEN
        INSERT INTO audit_int(audits_id,columnName,oldValue,newValue) VALUES (@AID,'other_int',NULL,NEW.other_int);
    END IF;
END$$

USE `auditTest`$$


CREATE TRIGGER tg_courses_has_students_upt AFTER UPDATE ON courses_has_students
FOR EACH ROW 
BEGIN
    IF NOT NEW.other_int <=> OLD.other_int THEN
        INSERT INTO audits(tableName,task,dateChanged,users_id,dbUser,requesting_ip) VALUES ('courses_has_students', 'u', NOW(), @users_id, USER(), @requesting_ip );
        SET @AID=LAST_INSERT_ID();
        INSERT INTO audits_2pk(audits_id,pk1,pk2) VALUES (@AID,NEW.courses_id,NEW.students_id);
        IF NOT NEW.other_int <=> OLD.other_int THEN
            INSERT INTO audit_int(audits_id,columnName,oldValue,newValue) VALUES (@AID,'other_int',OLD.other_int,NEW.other_int);
        END IF;
    END IF;
END$$

USE `auditTest`$$


CREATE TRIGGER tg_courses_has_students_del AFTER DELETE ON courses_has_students
FOR EACH ROW 
BEGIN
    INSERT INTO audits(tableName,task,dateChanged,users_id,dbUser,requesting_ip) VALUES ('courses_has_students', 'd', NOW(), @users_id, USER(), @requesting_ip );
    SET @AID=LAST_INSERT_ID();
    INSERT INTO audits_2pk(audits_id,pk1,pk2) VALUES (@AID,OLD.courses_id,OLD.students_id);
END$$


DELIMITER ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



-- Required by audit tables

INSERT INTO auditTasks (task,name) VALUES ('i','insert');
INSERT INTO auditTasks (task,name) VALUES ('u','update');
INSERT INTO auditTasks (task,name) VALUES ('d','delete');

-- Get some business records

INSERT INTO users (id,name) VALUES (0,'John Doe');
INSERT INTO users (id,name) VALUES (0,'Jane Doe');

INSERT INTO courses (id,name,course_number) VALUES (0,'Math','123abc');
INSERT INTO courses (id,name,course_number) VALUES (0,'English','123abc');

-- Set by PHP application
SET @requesting_ip='555.555.555.555';
SET @users_id=1;

-- Start normal routines
INSERT INTO students (id,name,ssn,notes,nickname) VALUES (0,'Billy Bob','555-55-5555',NULL,'Bebop');
UPDATE students SET name='Bill Bob',notes='Some notes' WHERE id=1;
INSERT INTO courses_has_students (courses_id,students_id) VALUES (1,1);
INSERT INTO courses_has_students (courses_id,students_id) VALUES (2,1);
DELETE FROM courses_has_students WHERE courses_id=1 AND students_id=1;
DELETE FROM courses_has_students WHERE courses_id=2 AND students_id=1;
DELETE FROM students WHERE id=1;

-- Audit database

SELECT u.name AS user_name, at.name AS task, a.dateChanged, a.tableName, af.columnName, af.oldValue AS oldValue_text, af.newValue AS newValue_text, null AS oldValue_val_45, null AS newValue_val_45
FROM audits AS a
INNER JOIN users AS u ON u.id=a.users_id
INNER JOIN auditTasks AS at ON at.task=a.task
INNER JOIN audits_1pk AS apk ON apk.audits_id=a.id
LEFT OUTER JOIN audit_text AS af ON af.audits_id=a.id
WHERE a.tableName='students' AND apk.pk1=1
UNION
SELECT u.name AS user_name, at.name AS task, a.dateChanged, a.tableName, af.columnName, null AS oldValue_text, null AS newValue_text, af.oldValue AS oldValue_val_45, af.newValue AS newValue_val_45
FROM audits AS a
INNER JOIN users AS u ON u.id=a.users_id
INNER JOIN auditTasks AS at ON at.task=a.task
INNER JOIN audits_1pk AS apk ON apk.audits_id=a.id
LEFT OUTER JOIN audit_var_45 AS af ON af.audits_id=a.id
WHERE a.tableName='students' AND apk.pk1=1
ORDER BY dateChanged ASC;

SELECT u.name AS user_name, at.name AS task, a.dateChanged, a.tableName, af.columnName, af.oldValue, af.newValue
FROM audits AS a
INNER JOIN users AS u ON u.id=a.users_id
INNER JOIN auditTasks AS at ON at.task=a.task
INNER JOIN audits_2pk AS apk ON apk.audits_id=a.id
LEFT OUTER JOIN audit_int AS af ON af.audits_id=a.id
WHERE a.tableName='courses_has_students' AND apk.pk1=1 AND apk.pk2=1
ORDER BY dateChanged ASC;