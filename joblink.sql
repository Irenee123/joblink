-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 08, 2023 at 11:45 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `edu_connect`
--

-- --------------------------------------------------------

--
-- Table structure for table `applications`
--

CREATE TABLE `applications` (
  `app_id` int(11) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `job_id` varchar(255) NOT NULL,
  `date_done` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `applications`
--

INSERT INTO `applications` (`app_id`, `user_email`, `job_id`, `date_done`) VALUES
(1, 'sauveurloue2@gmail.com', '2', '2023-12-08 09:14:53'),
(2, 'sauveurloue2@gmail.com', '2', '2023-12-08 09:29:39');

-- --------------------------------------------------------

--
-- Table structure for table `org`
--

CREATE TABLE `org` (
  `cp_id` int(11) NOT NULL,
  `posted_by` varchar(255) NOT NULL,
  `cp_name` varchar(255) NOT NULL,
  `cp_industry` varchar(255) NOT NULL,
  `job_title` varchar(255) NOT NULL,
  `job_description` varchar(255) NOT NULL,
  `job_doc` varchar(255) NOT NULL,
  `contract` varchar(255) NOT NULL,
  `date_added` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `org`
--

INSERT INTO `org` (`cp_id`, `posted_by`, `cp_name`, `cp_industry`, `job_title`, `job_description`, `job_doc`, `contract`, `date_added`) VALUES
(1, 'black', 'MIN VERSE', 'TECH', 'CEO', 'CODE', 'CV', 'YES', '2023-12-08 07:22:16'),
(2, 'jacky', 'META VERSE', 'TECH', 'COO', 'PROGRAM', 'CV', 'NO', '2023-12-08 09:56:36'),
(3, 'black', 'GOOGLE', 'TECH', 'COF', 'Coding', 'CV', 'yes', '2023-12-08 10:00:32');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `education_level` varchar(255) NOT NULL,
  `school` varchar(255) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `uname`, `email`, `password`, `phone`, `country`, `education_level`, `school`, `date`) VALUES
(1, 'black', 'sauveurloue2@gmail.com', '123', '078835123', 'Rwanda', 'BSE', 'ALU', '2023-12-08 07:20:49'),
(2, 'jacky', 'sauveurloue1@gmail.com', '123', '07834212', 'burundi', 'BSE', 'ALU', '2023-12-08 09:56:21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applications`
--
ALTER TABLE `applications`
  ADD PRIMARY KEY (`app_id`);

--
-- Indexes for table `org`
--
ALTER TABLE `org`
  ADD PRIMARY KEY (`cp_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applications`
--
ALTER TABLE `applications`
  MODIFY `app_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `org`
--
ALTER TABLE `org`
  MODIFY `cp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
