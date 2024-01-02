-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2024 at 12:25 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stationery membership registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Cus_First_Name` varchar(30) NOT NULL,
  `Cus_Last_Name` varchar(30) NOT NULL,
  `Cus_Title` varchar(3) NOT NULL,
  `Cus_Gender` varchar(6) NOT NULL,
  `Cus_Birth_Day` int(2) NOT NULL,
  `Cus_Birth_Month` int(2) NOT NULL,
  `Cus_Birth_Year` int(4) NOT NULL,
  `Cus_Age` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Cus_First_Name`, `Cus_Last_Name`, `Cus_Title`, `Cus_Gender`, `Cus_Birth_Day`, `Cus_Birth_Month`, `Cus_Birth_Year`, `Cus_Age`) VALUES
('Hidayati', 'Jakaria', 'Ms.', 'Female', 2, 8, 2004, 19),
('Hidayati', 'Jakaria', 'Ms.', 'Female', 2, 8, 2004, 19),
('cus_first_name', 'cus_last_name', 'cus', 'cus_ge', 0, 0, 0, 0),
('cus_first_name', 'cus_last_name', 'cus', 'cus_ge', 0, 0, 0, 0),
('cus_first_name', 'cus_last_name', 'cus', 'cus_ge', 0, 0, 0, 0),
('cus_first_name', 'cus_last_name', 'cus', 'cus_ge', 0, 0, 0, 0),
('cus_first_name', 'cus_last_name', 'cus', 'cus_ge', 0, 0, 0, 0),
('cus_first_name', 'cus_last_name', 'cus', 'cus_ge', 0, 0, 0, 0),
('Cus_First_Name', 'Cus_Last_Name', 'Cus', 'Cus_Ge', 0, 0, 0, 0),
('DANIAL', 'JAKARIA', 'Mr.', 'Male', 12, 4, 2008, 15),
('YUSNAH', 'YUSOF', 'Mrs', 'Female', 19, 10, 1974, 49),
('Dhiya', 'Jack', 'Ms.', 'Female', 2, 8, 2004, 19),
('Ally', 'Samson', 'Mrs', 'Female', 23, 5, 1987, 36);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
