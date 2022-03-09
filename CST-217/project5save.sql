-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema team_4
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema team_4
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `team_4` DEFAULT CHARACTER SET utf8 ;
USE `team_4` ;

-- -----------------------------------------------------
-- Table `team_4`.`buildings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`buildings` (
  `Building_Number` INT NOT NULL,
  `Name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Building_Number`),
  UNIQUE INDEX `Building Number_UNIQUE` (`Building_Number` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`rooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`rooms` (
  `Room_Number` INT NOT NULL,
  `Buildings_Building_Number` INT NOT NULL,
  `Occupancy` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Room_Number`, `Buildings_Building_Number`),
  INDEX `fk_Rooms_Buildings1_idx` (`Buildings_Building_Number` ASC)  ,
  CONSTRAINT `fk_Rooms_Buildings1`
    FOREIGN KEY (`Buildings_Building_Number`)
    REFERENCES `team_4`.`buildings` (`Building_Number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`activities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`activities` (
  `ID` INT NOT NULL,
  `Start Time` TIME NULL DEFAULT NULL,
  `Date` DATE NULL DEFAULT NULL,
  `Budget` VARCHAR(45) NULL DEFAULT NULL,
  `Name` VARCHAR(45) NULL DEFAULT NULL,
  `rooms_Room_Number` INT NULL DEFAULT NULL,
  `rooms_Buildings_Building_Number` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_activities_rooms1_idx` (`rooms_Room_Number` ASC, `rooms_Buildings_Building_Number` ASC)  ,
  CONSTRAINT `fk_activities_rooms1`
    FOREIGN KEY (`rooms_Room_Number` , `rooms_Buildings_Building_Number`)
    REFERENCES `team_4`.`rooms` (`Room_Number` , `Buildings_Building_Number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`courses` (
  `ID` VARCHAR(7) NOT NULL,
  `Name` VARCHAR(45) NULL DEFAULT NULL,
  `Description` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC)  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`professor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`professor` (
  `ID` INT NOT NULL,
  `fName` VARCHAR(45) NOT NULL,
  `lName` VARCHAR(45) NOT NULL,
  `Sex` ENUM('M', 'F') NOT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Phone` VARCHAR(45) NULL DEFAULT NULL,
  `Date_of_Birth` VARCHAR(45) NULL DEFAULT NULL,
  `Salary` DOUBLE NULL DEFAULT NULL,
  `Department` VARCHAR(45) NULL DEFAULT NULL,
  `Degree` VARCHAR(45) NULL DEFAULT NULL,
  `Street_Address` VARCHAR(45) NULL DEFAULT NULL,
  `City` VARCHAR(45) NULL DEFAULT NULL,
  `Zip` VARCHAR(45) NULL DEFAULT NULL,
  `Country` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC)  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`class` (
  `ID` VARCHAR(7) NOT NULL,
  `Class_Time` TIME NULL DEFAULT NULL,
  `Class_Start_Date` DATE NULL DEFAULT NULL,
  `Class_End_Date` DATE NULL DEFAULT NULL,
  `Class_Meeting_Days` VARCHAR(45) NULL DEFAULT NULL,
  `Professor_ID` INT NOT NULL,
  `Courses_ID` VARCHAR(7) NOT NULL,
  `rooms_Room_Number` INT NULL DEFAULT NULL,
  `rooms_Buildings_Building_Number` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Classes_Professor1_idx` (`Professor_ID` ASC)  ,
  INDEX `fk_Classes_Courses1_idx` (`Courses_ID` ASC)  ,
  INDEX `fk_class_rooms1_idx` (`rooms_Room_Number` ASC, `rooms_Buildings_Building_Number` ASC)  ,
  CONSTRAINT `fk_class_rooms1`
    FOREIGN KEY (`rooms_Room_Number` , `rooms_Buildings_Building_Number`)
    REFERENCES `team_4`.`rooms` (`Room_Number` , `Buildings_Building_Number`),
  CONSTRAINT `fk_Classes_Courses1`
    FOREIGN KEY (`Courses_ID`)
    REFERENCES `team_4`.`courses` (`ID`),
  CONSTRAINT `fk_Classes_Professor1`
    FOREIGN KEY (`Professor_ID`)
    REFERENCES `team_4`.`professor` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`students` (
  `ID` INT NOT NULL,
  `fName` VARCHAR(45) NOT NULL,
  `lName` VARCHAR(45) NOT NULL,
  `Sex` ENUM('M', 'F') NOT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Phone` VARCHAR(45) NULL DEFAULT NULL,
  `Date_of_Birth` VARCHAR(45) NULL DEFAULT NULL,
  `Major` VARCHAR(45) NULL DEFAULT NULL,
  `Street_Address` VARCHAR(45) NULL DEFAULT NULL,
  `City` VARCHAR(45) NULL DEFAULT NULL,
  `Zip` VARCHAR(45) NULL DEFAULT NULL,
  `Country` VARCHAR(45) NULL DEFAULT NULL,
  `rooms_Room_Number` INT NULL DEFAULT NULL,
  `rooms_Buildings_Building_Number` INT NULL DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC)  ,
  INDEX `fk_students_rooms1_idx` (`rooms_Room_Number` ASC, `rooms_Buildings_Building_Number` ASC)  ,
  CONSTRAINT `fk_students_rooms1`
    FOREIGN KEY (`rooms_Room_Number` , `rooms_Buildings_Building_Number`)
    REFERENCES `team_4`.`rooms` (`Room_Number` , `Buildings_Building_Number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`students_has_activities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`students_has_activities` (
  `Students_ID` INT NOT NULL,
  `Activities_ID` INT NOT NULL,
  PRIMARY KEY (`Students_ID`, `Activities_ID`),
  INDEX `fk_Students_has_Activities_Activities1_idx` (`Activities_ID` ASC)  ,
  INDEX `fk_Students_has_Activities_Students1_idx` (`Students_ID` ASC)  ,
  CONSTRAINT `fk_Students_has_Activities_Activities1`
    FOREIGN KEY (`Activities_ID`)
    REFERENCES `team_4`.`activities` (`ID`),
  CONSTRAINT `fk_Students_has_Activities_Students1`
    FOREIGN KEY (`Students_ID`)
    REFERENCES `team_4`.`students` (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`students_classes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`students_classes` (
  `students_ID` INT NOT NULL,
  `class_ID` VARCHAR(7) NOT NULL,
  PRIMARY KEY (`students_ID`, `class_ID`),
  INDEX `fk_students_has_class_class1_idx` (`class_ID` ASC)  ,
  INDEX `fk_students_has_class_students1_idx` (`students_ID` ASC)  ,
  CONSTRAINT `fk_students_has_class_students1`
    FOREIGN KEY (`students_ID`)
    REFERENCES `team_4`.`students` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_students_has_class_class1`
    FOREIGN KEY (`class_ID`)
    REFERENCES `team_4`.`class` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `team_4`.`course_pre-req`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `team_4`.`course_pre-req` (
  `courses_ID` VARCHAR(7) NOT NULL,
  `course_pre-req` VARCHAR(7) NOT NULL,
  PRIMARY KEY (`courses_ID`, `course_pre-req`),
  INDEX `fk_courses_has_courses_courses2_idx` (`course_pre-req` ASC)  ,
  INDEX `fk_courses_has_courses_courses1_idx` (`courses_ID` ASC)  ,
  CONSTRAINT `fk_courses_has_courses_courses1`
    FOREIGN KEY (`courses_ID`)
    REFERENCES `team_4`.`courses` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_courses_has_courses_courses2`
    FOREIGN KEY (`course_pre-req`)
    REFERENCES `team_4`.`courses` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
