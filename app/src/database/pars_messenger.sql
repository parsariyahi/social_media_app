-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 06, 2022 at 01:40 PM
-- Server version: 8.0.28-0ubuntu0.20.04.3
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pars_messenger`
--

-- --------------------------------------------------------

--
-- Table structure for table `friend_requests`
--

CREATE TABLE `friend_requests` (
  `request_id` int NOT NULL,
  `from` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `to` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `status` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `friend_requests`
--

INSERT INTO `friend_requests` (`request_id`, `from`, `to`, `status`) VALUES
(1, 'mina', 'sina', 0),
(2, 'sina', 'parsa', 0),
(3, 'mmd', 'parsa', 0),
(4, 'ali', 'parsa', 0),
(5, 'mehdi', 'parsa', 0);

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `message_id` int NOT NULL,
  `from` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `to` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `title` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`message_id`, `from`, `to`, `title`, `content`) VALUES
(1, 'parsa', 'mina', 'hello mom\r\n', 'how are you?\r\nwhere are you?\r\nim ok'),
(2, 'mina', 'parsa', 'hi son\r\n', 'good for you\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `username` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `full_name` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `age` int NOT NULL,
  `email` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `phone_number` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `bio` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `privacy_status` int NOT NULL DEFAULT '0',
  `password` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `full_name`, `age`, `email`, `phone_number`, `bio`, `privacy_status`, `password`) VALUES
(1, 'parsa', 'parsa lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(2, 'mina', 'mina lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(3, 'reza', 'reza lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(4, 'sina', 'sina lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(5, 'ali', 'ali lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(6, 'mmd', 'mmd lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(7, 'mehdi', 'mehdi lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055'),
(8, 'pouria', 'pouria lastname', '29', 'example@example.com' , '09xxxxxxxxxx', 'Lorem ipsum dolor sit amet, no fuisset hendrerit expetendis usu. Mea eu quot mazim aeque, ex oblique urbanitas tincidunt nec, nam omittam referrentur definitiones ad. Has ea modo delenit, velit affert te sit, ei duo labore admodum. Aliquid expetendis per in, vis vivendum hendrerit ne. Ex duo amet utinam alienum.', 1, '81dc9bdb52d04dc20036dbd8313ed055');

-- --------------------------------------------------------

--
-- Table structure for table `vertices`
--

CREATE TABLE `vertices` (
  `vertices_id` int NOT NULL,
  `from` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `to` varchar(250) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vertices`
--

INSERT INTO `vertices` (`vertices_id`, `from`, `to`) VALUES
(1, 'parsa', 'mina'),
(2, 'mina', 'parsa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `friend_requests`
--
ALTER TABLE `friend_requests`
  ADD PRIMARY KEY (`request_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`message_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `vertices`
--
ALTER TABLE `vertices`
  ADD PRIMARY KEY (`vertices_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `friend_requests`
--
ALTER TABLE `friend_requests`
  MODIFY `request_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `message_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `vertices`
--
ALTER TABLE `vertices`
  MODIFY `vertices_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
