CREATE DATABASE IF NOT EXISTS `LJPS_DB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `LJPS_DB`;

#Courses
DROP TABLE IF EXISTS `Courses`;
CREATE TABLE IF NOT EXISTS `Courses` (
  `course_id` VARCHAR(20) NOT NULL,
  `course_name` VARCHAR(50) NOT NULL,
  `course_desc` VARCHAR(255) NOT NULL,
  `course_status` VARCHAR(15) NOT NULL,
  `course_type` VARCHAR(10) NOT NULL,
  `course_category` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Courses` (`course_id`, `course_name`, `course_desc`, `course_status`, `course_type`, `course_category`) VALUES
('COR001', 'Systems Thinking and Design', 'This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking,', 'Active', 'Internal', 'Core'),
('COR006', 'Manage Change', 'Identify risks associated with change and develop risk mitigation plans.', 'Retired', 'External', 'Core'),
('FIN001', 'Data Collection and Analysis', 'Data is meaningless unless insights and analysis can be drawn to provide useful information for business decision-making. It is imperative that data quality, integrity and security ', 'Active', 'External', 'Finance');
COMMIT;
select * from LJPS_DB.Courses;

#Role
DROP TABLE IF EXISTS `Role`;
CREATE TABLE IF NOT EXISTS `Role` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Role` (`role_id`, `role_name`) VALUES
('1','Admin'),
('2','User'),
('3','Manager'),
('4','Trainer');
COMMIT;
select * from LJPS_DB.Role;
#DELETE FROM `Role` where `role_id` = '201'; 

#Staff
DROP TABLE IF EXISTS `Staff`;
CREATE TABLE IF NOT EXISTS `Staff` (
  `staff_id` INT NOT NULL AUTO_INCREMENT,
  `staff_fname` VARCHAR(50) NOT NULL,
  `staff_lname` VARCHAR(50) NOT NULL,
  `dept` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `role` INT,
  PRIMARY KEY (`staff_id`),
  CONSTRAINT `role` FOREIGN KEY (`role`) REFERENCES `Role` (`role_id`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Staff` (`staff_id`, `staff_fname`, `staff_lname`, `dept`, `email`, `role`) VALUES
('130001', 'John', 'Sim', 'Chariman', 'jack.sim@allinone.com.sg', '1'),
('140001', 'Derek', 'Tan', 'Sales', 'Derek.Tan@allinone.com.sg', '3');
COMMIT;
select * from LJPS_DB.Staff;

#Registration
DROP TABLE IF EXISTS `Registration`;
CREATE TABLE IF NOT EXISTS `Registration` (
  `reg_id` INT NOT NULL,
  `course_id` VARCHAR(20) NOT NULL,
  `staff_id` INT NOT NULL,
  `reg_status` VARCHAR(20) NOT NULL,
  `completion_status` VARCHAR(20),
  PRIMARY KEY (`reg_id`),
  CONSTRAINT `course_id` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`)  ON DELETE CASCADE,
  CONSTRAINT `staff_id` FOREIGN KEY (`staff_id`) REFERENCES `Staff` (`staff_id`)  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Registration` (`reg_id`, `course_id`, `staff_id`, `reg_status`, `completion_status`) VALUES
('245', 'COR001', '130001', 'Registered', 'Completed'),
('246', 'COR006', '140001', 'Rejected', 'Completed'),
('247', 'COR001', '140001', 'Registered', 'Ongoing'),
('248', 'FIN001', '140001', 'Registered', 'Ongoing'),
('249', 'COR006', '140001', 'Waitlist', '');

COMMIT;
select * from LJPS_DB.Registration;


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Skills
DROP TABLE IF EXISTS `Skill`;
CREATE TABLE IF NOT EXISTS `Skill` (
  `skill_id` INT NOT NULL AUTO_INCREMENT,
  `skill_name` VARCHAR(100) NOT NULL,
  `skill_desc` TEXT NOT NULL,
  `skill_status` INT NOT NULL,
  PRIMARY KEY (`skill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Skill` (`skill_id`, `skill_name`, `skill_desc`, `skill_status`) VALUES
('501','Python 3','Python 3 is the latest programming language that you should know.','0'),
('502','Data Analytics','Data Analytics refers to the ability to derive insights from data, using analytical tools.','0'),
('503','Machine learning','Machine learning trains models using data','0'),
('504','HTML','Hyper-text Markup Language for web dev','0'),
('505','Javascript','Used in web development','0'),
('506','CSS','Cascading Style Sheet, used in designing for web dev','0');
COMMIT;
select * from LJPS_DB.Skill;

#Job Role
DROP TABLE IF EXISTS `Job_Role`;
CREATE TABLE IF NOT EXISTS `Job_Role` (
  `job_role_id` INT NOT NULL AUTO_INCREMENT,
  `job_role_name` VARCHAR(50) NOT NULL,
  `job_role_desc` varchar(255) NOT NULL,
  `job_role_status` INT NOT NULL,
  PRIMARY KEY (`job_role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Job_Role` (`job_role_id`, `job_role_name`,`job_role_desc`, `job_role_status`) VALUES
('601','Software Developer','Full Stack Software developer with MERN stack','0'),
('602','Data Analyst','Use your analytical skills and tools to derive new insights for our company','0'),
('603','Frontend Developer','Use frontend skills and tools in web design','0'),
('604','Full Stack Developer','Use web development skills and tools in web development','0'),
('605','Machine Learning Engineer','Leverage machine learning models to derive new insights','0');
COMMIT;
select * from LJPS_DB.Job_Role;

#Learning Journey
DROP TABLE IF EXISTS `Journey`;
CREATE TABLE IF NOT EXISTS `Journey` (
  `journey_id` INT NOT NULL AUTO_INCREMENT,
  `journey_name` VARCHAR(100) NOT NULL,
  `journey_status` VARCHAR(100) NOT NULL,
  `j_fk_staff_id` INT,
  `j_fk_job_role_id` INT,
  PRIMARY KEY (`journey_id`),
  CONSTRAINT `j_fk_staff_id` FOREIGN KEY (`j_fk_staff_id`) REFERENCES `Staff` (`staff_id`) ON DELETE CASCADE,
  CONSTRAINT `j_fk_job_role_id` FOREIGN KEY (`j_fk_job_role_id`) REFERENCES `Job_Role` (`job_role_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Journey` (`journey_id`, `journey_name`, `journey_status`, `j_fk_staff_id`, `j_fk_job_role_id`) VALUES
('701','Learning Journey test','In-Progress','130001','601'),
('702','Learning Journey testers','In-Progress','140001','602');
COMMIT;
select * from LJPS_DB.Journey;

#Role_Map
DROP TABLE IF EXISTS `Role_Map`;
CREATE TABLE IF NOT EXISTS `Role_Map` (
  `rm_fk_job_role_id` INT NOT NULL,
  `rm_fk_skill_id` INT NOT NULL,
  CONSTRAINT `rm_fk_job_role_id` FOREIGN KEY (`rm_fk_job_role_id`) REFERENCES `Job_Role` (`job_role_id`) ON DELETE CASCADE,
  CONSTRAINT `rm_fk_skill_id` FOREIGN KEY (`rm_fk_skill_id`) REFERENCES `Skill` (`skill_id`) ON DELETE CASCADE,
  PRIMARY KEY (`rm_fk_job_role_id`, `rm_fk_skill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Role_Map` (`rm_fk_job_role_id`, `rm_fk_skill_id`) VALUES
('601','501'),
('602','501'),
('602','502'),
('603','504'),
('603','505'),
('603','506'),
('604','501'),
('604','504'),
('604','505'),
('604','506'),
('605','501'),
('605','502'),
('605','503');
COMMIT;
select * from LJPS_DB.Role_Map;

#Journey_Map
DROP TABLE IF EXISTS `Journey_Map`;
CREATE TABLE IF NOT EXISTS `Journey_Map` (
  `jm_fk_journey_id` INT NOT NULL AUTO_INCREMENT,
  `jm_fk_course_id` VARCHAR(20) NOT NULL,
  CONSTRAINT `jm_fk_journey_id` FOREIGN KEY (`jm_fk_journey_id`) REFERENCES `Journey` (`journey_id`) ON DELETE CASCADE,
  CONSTRAINT `jm_fk_course_id` FOREIGN KEY (`jm_fk_course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE,
  PRIMARY KEY (`jm_fk_journey_id`, `jm_fk_course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Journey_Map` (`jm_fk_journey_id`, `jm_fk_course_id`) VALUES
('701','COR001'),
('701','COR006'),
('702','FIN001');
COMMIT;
select * from LJPS_DB.Journey_Map;

#Course_Map
DROP TABLE IF EXISTS `Course_Map`;
CREATE TABLE IF NOT EXISTS `Course_Map` (
  `cm_fk_course_id` VARCHAR(20) NOT NULL,
  `cm_fk_skill_id` INT NOT NULL,
  CONSTRAINT `cm_fk_course_id` FOREIGN KEY (`cm_fk_course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE,
  CONSTRAINT `cm_fk_skill_id` FOREIGN KEY (`cm_fk_skill_id`) REFERENCES `Skill` (`skill_id`) ON DELETE CASCADE,
  PRIMARY KEY (`cm_fk_course_id`, `cm_fk_skill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Course_Map` (`cm_fk_course_id`, `cm_fk_skill_id`) VALUES
('COR001','501'),
('COR001','502'),
('COR006','501');
COMMIT;
select * from LJPS_DB.Course_Map;

#Skill_Map
DROP TABLE IF EXISTS `Skill_Map`;
CREATE TABLE IF NOT EXISTS `Skill_Map` (
  `sm_fk_skill_id` INT NOT NULL,
  `sm_fk_staff_id` INT NOT NULL,
  CONSTRAINT `sm_fk_skill_id` FOREIGN KEY (`sm_fk_skill_id`) REFERENCES `Skill` (`skill_id`) ON DELETE CASCADE,
  CONSTRAINT `sm_fk_staff_id` FOREIGN KEY (`sm_fk_staff_id`) REFERENCES `Staff` (`staff_id`) ON DELETE CASCADE,
  PRIMARY KEY (`sm_fk_skill_id`, `sm_fk_staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Skill_Map` (`sm_fk_skill_id`, `sm_fk_staff_id`) VALUES
('501','130001'),
('502','130001'),
('501','140001');
COMMIT;
select * from LJPS_DB.Skill_Map;