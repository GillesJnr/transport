-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 27, 2020 at 11:16 AM
-- Server version: 5.7.32
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cagl_trans`
--

-- --------------------------------------------------------

--
-- Table structure for table `addresses`
--

CREATE TABLE `addresses` (
  `id` int(10) UNSIGNED NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `address` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `addresses`
--

INSERT INTO `addresses` (`id`, `customer_id`, `address`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 4, 'Tema', NULL, '2020-07-06 17:04:38', '2020-07-06 17:04:38'),
(2, 4, 'Accra', NULL, '2020-07-06 17:04:38', '2020-07-06 17:04:38'),
(3, 5, 'Accra', NULL, '2020-07-07 00:40:25', '2020-07-07 00:40:25');

-- --------------------------------------------------------

--
-- Table structure for table `allocation`
--

CREATE TABLE `allocation` (
  `id` int(11) NOT NULL,
  `month` tinytext NOT NULL,
  `amount` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `allocation`
--

INSERT INTO `allocation` (`id`, `month`, `amount`) VALUES
(1, 'January', 50000);

-- --------------------------------------------------------

--
-- Table structure for table `api_settings`
--

CREATE TABLE `api_settings` (
  `id` int(10) UNSIGNED NOT NULL,
  `key_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `key_value` text COLLATE utf8_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `api_settings`
--

INSERT INTO `api_settings` (`id`, `key_name`, `key_value`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'api', '0', '2020-06-15 15:50:14', '2020-08-04 21:16:20', NULL),
(2, 'anyone_register', '0', '2020-06-15 15:50:14', '2020-08-04 21:16:20', NULL),
(3, 'region_availability', 'region one, region two, region three', '2020-06-15 15:50:14', '2020-08-04 21:16:20', NULL),
(4, 'driver_review', '0', '2020-06-15 15:50:14', '2020-08-04 21:16:20', NULL),
(5, 'booking', '3', '2020-06-15 15:50:14', '2020-08-04 21:16:20', NULL),
(6, 'cancel', '2', '2020-06-15 15:50:14', '2020-08-04 21:16:20', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `id` int(10) UNSIGNED NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `driver_id` int(11) DEFAULT NULL,
  `pickup` timestamp NULL DEFAULT NULL,
  `dropoff` timestamp NULL DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `pickup_addr` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `dest_addr` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `note` text COLLATE utf8_unicode_ci,
  `travellers` int(11) NOT NULL DEFAULT '1',
  `status` int(11) NOT NULL DEFAULT '0',
  `payment` int(11) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`id`, `customer_id`, `user_id`, `vehicle_id`, `driver_id`, `pickup`, `dropoff`, `duration`, `pickup_addr`, `dest_addr`, `note`, `travellers`, `status`, `payment`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 5, 1, 1, 7, '2020-05-31 07:58:56', '2020-06-01 17:28:02', 2880, '91158 Luigi Cliffs\n							Lake Darby, MA 39627-1727', '91158 Luigi Cliffs\n							Lake Darby, MA 39627-1727', 'sample note', 1, 1, 0, '2020-06-15 15:50:13', '2020-06-15 15:50:14', NULL),
(2, 5, 1, 1, 6, '2020-06-07 11:55:59', '2020-06-08 08:55:23', 2880, '91158 Luigi Cliffs\n							Lake Darby, MA 39627-1727', '91158 Luigi Cliffs\n							Lake Darby, MA 39627-1727', 'sample note', 3, 0, 0, '2020-06-15 15:50:13', '2020-07-06 17:07:19', '2020-07-06 17:07:19'),
(3, 4, 1, 1, 6, '2020-07-08 10:00:04', '2020-07-08 14:00:00', 239, 'Tema', 'Accra', 'Cocoa', 1, 0, 0, '2020-07-06 17:04:38', '2020-07-06 17:04:38', NULL),
(4, 5, 4, 3, 7, '2020-07-07 00:39:49', '2020-07-07 00:39:49', 0, 'Accra', 'Accra', NULL, 1, 0, 0, '2020-07-07 00:40:25', '2020-07-07 00:40:25', NULL),
(5, 4, 8, 1, 6, '2020-10-22 14:47:33', '2020-10-22 14:47:33', 0, 'Tema', 'Accra', NULL, 1, 0, 0, '2020-10-22 14:48:01', '2020-10-22 14:48:01', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `bookings_meta`
--

CREATE TABLE `bookings_meta` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(10) UNSIGNED NOT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'null',
  `key` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `value` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `bookings_meta`
--

INSERT INTO `bookings_meta` (`id`, `booking_id`, `type`, `key`, `value`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 1, 'integer', 'customerid', '4', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(2, 1, 'integer', 'vehicleid', '1', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(3, 1, 'integer', 'day', '1', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(4, 1, 'integer', 'mileage', '10', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(5, 1, 'integer', 'waiting_time', '0', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(6, 1, 'string', 'date', '2020-06-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(7, 1, 'integer', 'total', '500', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14');

-- --------------------------------------------------------

--
-- Table structure for table `booking_income`
--

CREATE TABLE `booking_income` (
  `id` int(10) UNSIGNED NOT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `income_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `booking_income`
--

INSERT INTO `booking_income` (`id`, `booking_id`, `income_id`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 1, 3, '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `driver_vehicle`
--

CREATE TABLE `driver_vehicle` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `driver_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `driver_vehicle`
--

INSERT INTO `driver_vehicle` (`id`, `vehicle_id`, `driver_id`, `created_at`, `updated_at`) VALUES
(1, 1, 6, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(2, 3, 7, '2020-06-15 16:10:40', '2020-06-15 16:10:40');

-- --------------------------------------------------------

--
-- Table structure for table `email_content`
--

CREATE TABLE `email_content` (
  `id` int(10) UNSIGNED NOT NULL,
  `key` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `value` text COLLATE utf8_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `email_content`
--

INSERT INTO `email_content` (`id`, `key`, `value`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'insurance', 'vehicle insurance email content', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(2, 'vehicle_licence', 'vehicle licence email content', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(3, 'driving_licence', 'driving licence email content', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(4, 'registration', 'vehicle registration email content', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(5, 'service_reminder', 'service reminder email content', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(6, 'users', 'a:1:{i:0;s:1:\"2\";}', '2020-06-15 15:50:14', '2020-06-15 15:58:09', NULL),
(7, 'options', 'a:3:{i:0;s:1:\"3\";i:1;s:1:\"4\";i:2;s:1:\"5\";}', '2020-06-15 15:50:14', '2020-06-15 15:58:09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

CREATE TABLE `expense` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `exp_id` int(11) DEFAULT NULL,
  `amount` double(10,2) NOT NULL DEFAULT '0.00',
  `user_id` int(11) DEFAULT NULL,
  `expense_type` int(11) DEFAULT NULL,
  `comment` text COLLATE utf8_unicode_ci,
  `date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`id`, `vehicle_id`, `exp_id`, `amount`, `user_id`, `expense_type`, `comment`, `date`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 1, NULL, 2071.00, 2, 1, 'Sample Comment', '2020-06-14', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(2, 2, NULL, 3809.00, 3, 4, 'Sample Comment', '2020-06-10', '2020-06-15 15:50:14', '2020-07-06 16:52:03', '2020-07-06 16:52:03'),
(3, 1, 1, 500.00, 2, 8, 'Sample Comment', '2020-06-13', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(4, 1, 2, 500.00, 2, 8, 'Sample Comment', '2020-06-25', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(5, 1, NULL, 50.00, 8, 1, NULL, '2020-10-23', '2020-10-23 17:21:57', '2020-10-23 17:21:57', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `expense_cat`
--

CREATE TABLE `expense_cat` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `type` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `expense_cat`
--

INSERT INTO `expense_cat` (`id`, `name`, `user_id`, `type`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Insurance', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(2, 'Patente', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(3, 'Mechanics', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(4, 'Car wash', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(5, 'Vignette', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(6, 'Maintenance', 14, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(7, 'Parking', 14, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(8, 'Fuel', 15, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(9, 'Car Services', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `fare_settings`
--

CREATE TABLE `fare_settings` (
  `id` int(10) UNSIGNED NOT NULL,
  `key_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `key_value` text COLLATE utf8_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `fare_settings`
--

INSERT INTO `fare_settings` (`id`, `key_name`, `key_value`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'base_fare', '500', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(2, 'base_km', '10', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(3, 'base_time', '2', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(4, 'std_fare', '20', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(5, 'weekend_base_fare', '500', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(6, 'weekend_base_km', '10', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(7, 'weekend_wait_time', '2', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(8, 'weekend_std_fare', '20', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(9, 'night_base_fare', '500', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(10, 'night_base_km', '10', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(11, 'night_wait_time', '2', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(12, 'night_std_fare', '20', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `fuel`
--

CREATE TABLE `fuel` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `start_meter` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_meter` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `reference` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `province` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `note` text COLLATE utf8_unicode_ci,
  `vendor_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `fuel_from` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cost_per_unit` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `consumption` int(11) DEFAULT NULL,
  `complete` int(11) DEFAULT '0',
  `date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `fuel`
--

INSERT INTO `fuel` (`id`, `vehicle_id`, `user_id`, `start_meter`, `end_meter`, `reference`, `province`, `note`, `vendor_name`, `qty`, `fuel_from`, `cost_per_unit`, `consumption`, `complete`, `date`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 1, 2, '1000', '2000', NULL, 'Gujarat', 'sample note', NULL, 10, 'Fuel Tank', '50', 100, 0, '2020-06-13', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(2, 1, 2, '2000', '0', NULL, 'Gujarat', 'sample note', NULL, 10, 'Fuel Tank', '50', 0, 0, '2020-06-25', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `income_id` int(11) DEFAULT NULL,
  `amount` double(10,2) NOT NULL DEFAULT '0.00',
  `user_id` int(11) DEFAULT NULL,
  `income_cat` int(11) DEFAULT NULL,
  `mileage` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`id`, `vehicle_id`, `income_id`, `amount`, `user_id`, `income_cat`, `mileage`, `date`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 1, NULL, 4878.00, 2, 1, NULL, '2020-06-10', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(2, 2, NULL, 4117.00, 3, 1, NULL, '2020-06-14', '2020-06-15 15:50:14', '2020-07-06 16:52:03', '2020-07-06 16:52:03'),
(3, 1, 1, 500.00, 1, 1, 10, '2020-06-15', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(4, 1, NULL, 150.00, 8, 1, 45464, '2020-10-23', '2020-10-23 17:21:06', '2020-10-23 17:21:06', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `income_cat`
--

CREATE TABLE `income_cat` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `type` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `income_cat`
--

INSERT INTO `income_cat` (`id`, `name`, `user_id`, `type`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Booking', 1, 'd', '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `maintanance`
--

CREATE TABLE `maintanance` (
  `id` int(10) UNSIGNED NOT NULL,
  `service_id` int(11) DEFAULT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `cost` double(8,2) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `id` int(10) UNSIGNED NOT NULL,
  `fcm_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `message` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2017_06_03_134331_create_expense_table', 1),
(2, '2017_06_03_134332_create_expense_cat_table', 1),
(3, '2017_06_03_134332_create_income_table', 1),
(4, '2017_06_03_134333_create_income_cat_table', 1),
(5, '2017_06_03_134333_create_maintanance_table', 1),
(6, '2017_06_03_134334_create_mileage_table', 1),
(7, '2017_06_03_134336_create_password_resets_table', 1),
(8, '2017_06_03_134337_create_users_table', 1),
(9, '2017_06_03_134338_create_vehicles_table', 1),
(10, '2017_07_24_080537_create_booking_table', 1),
(11, '2017_07_24_080643_create_settings_table', 1),
(12, '2017_08_01_073926_create_booking_income_table', 1),
(13, '2017_10_30_064357_create_notifications_table', 1),
(14, '2017_10_30_094858_create_fuel_table', 1),
(15, '2017_11_09_105729_create_vendors_table', 1),
(16, '2017_11_10_062609_create_work_orders_table', 1),
(17, '2017_11_10_095438_create_notes_table', 1),
(18, '2017_11_22_093559_create_vehicle_group_table', 1),
(19, '2017_12_28_091600_create_service_items_table', 1),
(20, '2017_12_28_122952_create_service_reminder_table', 1),
(21, '2017_12_28_174333_create_api_settings_table', 1),
(22, '2018_01_08_062105_create_driver_vehicle_table', 1),
(23, '2018_01_10_130517_users_meta', 1),
(24, '2018_01_13_050018_bookings_meta', 1),
(25, '2018_01_16_095657_fare_settings', 1),
(26, '2018_01_25_050939_create_vehicles_meta_table', 1),
(27, '2018_02_06_052302_create_message_table', 1),
(28, '2018_02_06_125252_create_reviews_table', 1),
(29, '2018_03_13_124424_create_addresses_table', 1),
(30, '2018_03_28_085735_create_reasons_table', 1),
(31, '2018_04_28_073004_create_email_content_table', 1);

-- --------------------------------------------------------

--
-- Table structure for table `mileage`
--

CREATE TABLE `mileage` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `mileage` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notes`
--

CREATE TABLE `notes` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `note` text COLLATE utf8_unicode_ci,
  `submitted_on` date DEFAULT NULL,
  `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `id` char(36) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `notifiable_type` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `notifiable_id` bigint(20) UNSIGNED NOT NULL,
  `data` text COLLATE utf8_unicode_ci NOT NULL,
  `read_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reasons`
--

CREATE TABLE `reasons` (
  `id` int(10) UNSIGNED NOT NULL,
  `reason` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `reasons`
--

INSERT INTO `reasons` (`id`, `reason`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 'Late', NULL, '2020-06-15 15:57:26', '2020-06-15 15:57:26'),
(2, 'Order changed', NULL, '2020-07-07 00:36:25', '2020-07-07 00:36:25');

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `driver_id` int(11) DEFAULT NULL,
  `ratings` double(8,2) DEFAULT NULL,
  `review_text` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `service_items`
--

CREATE TABLE `service_items` (
  `id` int(10) UNSIGNED NOT NULL,
  `description` text COLLATE utf8_unicode_ci,
  `time_interval` varchar(255) COLLATE utf8_unicode_ci DEFAULT 'off',
  `overdue_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `overdue_unit` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `meter_interval` varchar(255) COLLATE utf8_unicode_ci DEFAULT 'off',
  `overdue_meter` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `show_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT 'off',
  `duesoon_time` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `duesoon_unit` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `show_meter` varchar(255) COLLATE utf8_unicode_ci DEFAULT 'off',
  `duesoon_meter` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `service_items`
--

INSERT INTO `service_items` (`id`, `description`, `time_interval`, `overdue_time`, `overdue_unit`, `meter_interval`, `overdue_meter`, `show_time`, `duesoon_time`, `duesoon_unit`, `show_meter`, `duesoon_meter`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 'Change oil', 'on', '60', 'day(s)', 'off', NULL, 'on', '2', 'day(s)', 'off', NULL, NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14');

-- --------------------------------------------------------

--
-- Table structure for table `service_reminder`
--

CREATE TABLE `service_reminder` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `last_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_meter` int(11) DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int(10) UNSIGNED NOT NULL,
  `label` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `value` longtext COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `label`, `name`, `value`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Website Name', 'app_name', 'CAGL Transport', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(2, 'Business Address 1', 'badd1', 'Company Address 1', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(3, 'Business Address 2', 'badd2', 'Company Address 2', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(4, 'Email Address', 'email', 'sirvictorapeanyo@gmail.com', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(5, 'City', 'city', 'Tema', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(6, 'State', 'state', 'Greater-Accra', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(7, 'Country', 'country', 'Ghana', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(8, 'Distence Format', 'dis_format', 'km', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(9, 'Language', 'language', 'English-en', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(10, 'Currency', 'currency', 'GHS', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(11, 'Tax No', 'tax_no', '00000123', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(12, 'Invoice Text', 'invoice_text', 'Transporting with Xcellence', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(13, 'Small Logo', 'icon_img', '28c69d3b-3b82-41fe-8f52-b3779d15b2cd.png', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL),
(14, 'Main Logo', 'logo_img', 'e2a5bbd7-7335-447c-bca0-34758aed688d.png', '2020-06-15 15:50:14', '2020-06-15 15:56:48', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `api_token` varchar(60) COLLATE utf8_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `user_type`, `group_id`, `api_token`, `remember_token`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Victor Apeanyo', 'sirvictorapeanyo@gmail.com', '$2y$10$123pCaXds0PVDB6E1Sn8iOxu6oEz5rkrtJuxMlZAK69PwC6qR5.G.', 'S', NULL, '3JYo3ZrubjFw415AuF03f5RW7KvWOSNY1vxNuygVZw987DyhE1vgoeGCfrzf', 'wMpJdmP2VFRkI6nwgqoxnaDkGAyQOcJAOauuxaEyTuCRIv9nhJsPtRjZwJ1I', '2020-06-15 15:50:13', '2020-07-06 16:55:14', NULL),
(2, 'Isaac Amoako-Mensah', 'isaac@cagl.com', '$2y$10$j7E7LjI/YkYD1kg6VgfSYOkJ1ozN9VXnKUIYdN.feIDqR6y0gCrmu', 'O', 1, 'Siu8tjLgZ3dsWyGe9KhzK1b1E6zbJ2AJ7pEcTgwVH9DY9LWtV9lSONzaJuQm', '21RJka6DkS2diFUPNAAYFclNKZV0Tokn5tbJNobn5w1mUL9pFuvrlGSHsKg6', '2020-06-15 15:50:13', '2020-07-06 17:08:51', NULL),
(3, 'User Two', 'user2@admin.com', '$2y$10$vvBact5mzt7X6bRCD1CAc.mQN0/prCt4MAFnycHKKbpC4O/dgLCAW', 'O', 1, 'HgTBzbcWW89rMIPPT5PtQWlLnym7MiIVZ6ppZZ5jZtMlgyCrrZm9draZZIu3', NULL, '2020-06-15 15:50:14', '2020-07-06 16:56:18', '2020-07-06 16:56:18'),
(4, 'Customer One', 'customer1@gmail.com', '$2y$10$KTQw6LwupiUgRL54zoBlFuZoilxpNMNOKpkK7Tb2XFHUZjyxCgvNK', 'C', NULL, 'ImGpLaDaPPye840phRaSh1znJFBKcVoCYpzd2g0EkhbvLeY8dSkAamieW0yR', 'sEAZr5YvNp2oulX9tJLdpzPKqxaeDJlQvFClgQXlYpGI00MZ05umWZZHN0Js', '2020-06-15 15:50:14', '2020-07-07 00:37:57', NULL),
(5, 'Customer Two', 'customer2@gmail.com', '$2y$10$nD/4eTBv8cStj3YAKtu4WuffSAZc1qr0c8ojSKTTHL6LrYrZkeSta', 'C', NULL, 'iB6B1g942X9jkK6AcNkYWMtNaeG8Krp22GIXvRm1bJPvAYIxNoB4dEKgXYzK', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14', NULL),
(6, 'Moses Anim', 'manim@cagl.com', '$2y$10$2uM6.nYqqj/DRhquGN26f.8W9OU4OJXa3k/rOcDJBDqVrjOVnpgT2', 'D', NULL, 'u1mxgQ27jZ3iiWmhhtJGI9atjcql7WwaDlq7NI8gZnzwYgdYBBGuXpsh8geD', 'vrZXWw5zcV', '2020-06-15 15:50:14', '2020-07-07 00:41:33', NULL),
(7, 'Albert Quansah', 'aquansah@cagl.com', '$2y$10$rKAllF1VLPtUA8JiwvJHhe7/4wsOix.00XPUN6H1SMyadEGXxTejC', 'D', NULL, 'zBvSoVhALWJ1ATTXKblK8nqaJX7dutKbBdDgjiyKom0HBgkknF5b0lqT0Ri9', 'QFyGTlChTd', '2020-06-15 15:50:14', '2020-06-15 16:12:00', NULL),
(8, 'Gabriel Gilles', 'gabbygilles1@gmail.com', '$2y$10$dck9NIwpu7KZ9TaSi9Hmv.JyLOuBqBnNaQa/hJPIgGNHWz5MXPKCW', 'S', 1, 'iuN3eqTIN6z0WsCPxIfnTd5m1EAn8WWiTm6KUfnDzhOgqyooTHfs3l6dE6m0', 'w6TbXjLi4Cq4CCUJ8wL11rOVFMsIBlZmTSqT1XGYGfNmp6zilDG8OT1bqvaK', '2020-08-04 20:47:46', '2020-10-01 16:29:35', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users_meta`
--

CREATE TABLE `users_meta` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'null',
  `key` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `value` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users_meta`
--

INSERT INTO `users_meta` (`id`, `user_id`, `type`, `key`, `value`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 1, 'string', 'profile_image', 'no-user.jpg', NULL, '2020-06-15 15:50:13', '2020-06-15 15:50:13'),
(2, 1, 'string', 'module', 'a:11:{i:0;s:1:\"0\";i:1;s:1:\"1\";i:2;s:1:\"2\";i:3;s:1:\"3\";i:4;s:1:\"4\";i:5;s:1:\"5\";i:6;s:1:\"6\";i:7;s:1:\"7\";i:8;s:1:\"8\";i:9;s:1:\"9\";i:10;s:2:\"10\";}', NULL, '2020-06-15 15:50:13', '2020-07-06 16:55:14'),
(3, 2, 'string', 'module', 'a:11:{i:0;s:1:\"0\";i:1;s:1:\"1\";i:2;s:1:\"2\";i:3;s:1:\"3\";i:4;s:1:\"4\";i:5;s:1:\"5\";i:6;s:1:\"6\";i:7;s:1:\"7\";i:8;s:1:\"8\";i:9;s:1:\"9\";i:10;s:2:\"10\";}', NULL, '2020-06-15 15:50:13', '2020-07-06 16:56:01'),
(4, 3, 'string', 'module', 'a:11:{i:0;i:0;i:1;i:1;i:2;i:2;i:3;i:3;i:4;i:4;i:5;i:5;i:6;i:6;i:7;i:7;i:8;i:8;i:9;i:9;i:10;i:10;}', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(5, 4, 'string', 'first_name', 'Customer', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(6, 4, 'string', 'last_name', 'One', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(7, 4, 'string', 'address', 'accra', NULL, '2020-06-15 15:50:14', '2020-07-07 00:37:20'),
(62, 8, 'string', 'module', 'a:11:{i:0;s:1:\"0\";i:1;s:1:\"1\";i:2;s:1:\"2\";i:3;s:1:\"3\";i:4;s:1:\"4\";i:5;s:1:\"5\";i:6;s:1:\"6\";i:7;s:1:\"7\";i:8;s:1:\"8\";i:9;s:1:\"9\";i:10;s:2:\"10\";}', NULL, '2020-08-04 20:47:46', '2020-08-04 20:47:46'),
(8, 4, 'string', 'mobno', '0256654321', NULL, '2020-06-15 15:50:14', '2020-07-07 00:37:20'),
(9, 5, 'string', 'first_name', 'Customer', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(10, 5, 'string', 'last_name', 'Two', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(11, 5, 'string', 'address', 'kumasi', NULL, '2020-06-15 15:50:14', '2020-07-07 00:37:45'),
(12, 5, 'string', 'mobno', '0267765678', NULL, '2020-06-15 15:50:14', '2020-07-07 00:37:45'),
(13, 6, 'string', 'first_name', 'Moses', NULL, '2020-06-15 15:50:14', '2020-07-06 16:54:10'),
(14, 6, 'string', 'last_name', 'Anim', NULL, '2020-06-15 15:50:14', '2020-07-06 16:54:10'),
(15, 6, 'string', 'address', 'tema', NULL, '2020-06-15 15:50:14', '2020-07-06 16:54:10'),
(16, 6, 'string', 'phone', '0242022459', NULL, '2020-06-15 15:50:14', '2020-07-06 16:54:10'),
(17, 6, 'string', 'issue_date', '2020-06-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(18, 6, 'string', 'exp_date', '2020-08-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(19, 6, 'string', 'start_date', '2020-06-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(20, 6, 'string', 'end_date', '2020-07-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(21, 6, 'string', 'license_number', '400193', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:22'),
(22, 6, 'string', 'contract_number', '1496', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:22'),
(23, 6, 'string', 'emp_id', '10', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:22'),
(24, 7, 'string', 'first_name', 'Albert', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:00'),
(25, 7, 'string', 'last_name', 'Quansah', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:00'),
(26, 7, 'string', 'address', 'Takoradi', NULL, '2020-06-15 15:50:14', '2020-07-06 16:54:38'),
(27, 7, 'string', 'phone', '0245569879', NULL, '2020-06-15 15:50:14', '2020-07-06 16:54:38'),
(28, 7, 'string', 'issue_date', '2020-06-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(29, 7, 'string', 'exp_date', '2020-08-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(30, 7, 'string', 'start_date', '2020-06-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(31, 7, 'string', 'end_date', '2020-07-15', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(32, 7, 'string', 'license_number', '419470', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:00'),
(33, 7, 'string', 'contract_number', '6989', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:00'),
(34, 7, 'string', 'emp_id', '8672851', NULL, '2020-06-15 15:50:14', '2020-06-15 16:12:00'),
(35, 1, 'string', 'language', 'English-en', NULL, '2020-06-15 15:56:48', '2020-06-15 15:56:48'),
(36, 7, 'string', 'vehicle_id', '3', NULL, '2020-06-15 16:10:40', '2020-06-15 16:10:40'),
(37, 7, 'string', '_method', 'PATCH', NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(38, 7, 'string', '_token', '0BmHzUDKbadWuVjiTcytIAlVDRMvxuplKhiGWzsU', NULL, '2020-06-15 16:12:00', '2020-07-06 16:54:38'),
(39, 7, 'string', 'id', '7', NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(40, 7, 'string', 'edit', '1', NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(41, 7, 'string', 'detail_id', '7', NULL, '2020-06-15 16:12:00', '2020-07-06 16:54:38'),
(42, 7, 'string', 'user_id', '1', NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(43, 7, 'NULL', 'middle_name', NULL, NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(44, 7, 'string', 'email', 'aquansah@cagl.com', NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(45, 7, 'string', 'gender', '1', NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(46, 7, 'NULL', 'econtact', NULL, NULL, '2020-06-15 16:12:00', '2020-06-15 16:12:00'),
(47, 7, 'integer', 'is_active', '1', NULL, '2020-06-15 16:12:07', '2020-06-15 16:12:07'),
(48, 6, 'string', '_method', 'PATCH', NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(49, 6, 'string', '_token', '0BmHzUDKbadWuVjiTcytIAlVDRMvxuplKhiGWzsU', NULL, '2020-06-15 16:12:22', '2020-07-06 16:54:10'),
(50, 6, 'string', 'id', '6', NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(51, 6, 'string', 'edit', '1', NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(52, 6, 'string', 'detail_id', '6', NULL, '2020-06-15 16:12:22', '2020-07-06 16:54:10'),
(53, 6, 'string', 'user_id', '1', NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(54, 6, 'NULL', 'middle_name', NULL, NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(55, 6, 'string', 'email', 'manim@cagl.com', NULL, '2020-06-15 16:12:22', '2020-07-06 16:54:10'),
(56, 6, 'string', 'gender', '1', NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(57, 6, 'NULL', 'econtact', NULL, NULL, '2020-06-15 16:12:22', '2020-06-15 16:12:22'),
(58, 6, 'integer', 'is_active', '1', NULL, '2020-06-15 16:12:27', '2020-06-15 16:12:27'),
(59, 6, 'string', 'driver_image', 'd4091a24-ac73-455c-bafc-5f0df019fe4c.jpg', NULL, '2020-07-06 16:54:10', '2020-07-06 16:54:10'),
(60, 6, 'string', 'license_image', '9faae6e8-ad30-47e6-9ec1-96072c00bbcc.jpg', NULL, '2020-07-06 16:54:10', '2020-07-06 16:54:10'),
(61, 6, 'string', 'id_proof_type', 'License', NULL, '2020-07-06 16:54:10', '2020-07-06 16:54:10'),
(63, 8, 'string', 'language', 'English-en', NULL, '2020-08-04 20:47:46', '2020-08-04 20:47:46');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `id` int(10) UNSIGNED NOT NULL,
  `make` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `model` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `year` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `lic_exp_date` date DEFAULT NULL,
  `reg_exp_date` date DEFAULT NULL,
  `vehicle_image` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `engine_type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `horse_power` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `color` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `vin` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `license_plate` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `mileage` int(11) DEFAULT NULL,
  `in_service` tinyint(4) DEFAULT '0',
  `user_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `int_mileage` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`id`, `make`, `model`, `type`, `year`, `group_id`, `lic_exp_date`, `reg_exp_date`, `vehicle_image`, `engine_type`, `horse_power`, `color`, `vin`, `license_plate`, `mileage`, `in_service`, `user_id`, `created_at`, `updated_at`, `deleted_at`, `int_mileage`) VALUES
(1, 'Sinotruk', 'Howo', 'Flatbed', '2015', 1, '2021-02-20', '2020-11-12', '8766a56d-e2ee-4f26-bd02-3096a9efa1a7.jpg', 'Diesel', '190', 'yellow', '2342342', 'GT 7868 19', 45464, 1, 1, '2020-06-15 15:50:14', '2020-07-06 16:52:23', NULL, 50),
(2, 'Tata', 'NANO', 'car', '2012', 1, '2021-06-15', '2020-09-13', 'car2.jpeg', 'Petrol', '150', 'white', '124578', '1245ab', 45464, 1, 1, '2020-06-15 15:50:14', '2020-07-06 16:52:03', '2020-07-06 16:52:03', 40),
(3, 'Scania', 'Z709', 'Haulage', '2015', 1, '2021-06-15', '2021-03-15', NULL, 'Diesel', '16', 'White', 'GT 7898 18', 'GT 7898 18', NULL, 1, 1, '2020-06-15 16:09:56', '2020-06-15 16:19:05', NULL, 125447);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_meta`
--

CREATE TABLE `vehicles_meta` (
  `id` int(10) UNSIGNED NOT NULL,
  `vehicle_id` int(10) UNSIGNED NOT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'null',
  `key` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `value` longtext COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vehicles_meta`
--

INSERT INTO `vehicles_meta` (`id`, `vehicle_id`, `type`, `key`, `value`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 1, 'integer', 'driver_id', '6', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(2, 1, 'string', 'ins_number', '70651', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(3, 1, 'string', 'ins_exp_date', '2020-12-22', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(4, 2, 'string', 'ins_number', '36945', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(5, 2, 'string', 'ins_exp_date', '2020-12-22', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(6, 3, 'string', 'ins_number', '', NULL, '2020-06-15 16:09:56', '2020-06-15 16:09:56'),
(7, 3, 'string', 'ins_exp_date', '', NULL, '2020-06-15 16:09:56', '2020-06-15 16:09:56'),
(8, 3, 'string', 'documents', '', NULL, '2020-06-15 16:09:56', '2020-06-15 16:09:56'),
(9, 3, 'string', 'purchase_info', 'a:1:{i:0;a:2:{s:8:\"exp_name\";s:5:\"Asset\";s:10:\"exp_amount\";s:6:\"650000\";}}', NULL, '2020-06-15 16:10:31', '2020-06-15 16:10:31'),
(10, 3, 'string', 'driver_id', '7', NULL, '2020-06-15 16:10:40', '2020-06-15 16:10:40');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_group`
--

CREATE TABLE `vehicle_group` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8_unicode_ci,
  `note` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vehicle_group`
--

INSERT INTO `vehicle_group` (`id`, `name`, `description`, `note`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 'Default', 'Default vehicle group', 'Default vehicle group', NULL, '2020-06-15 15:50:13', '2020-06-15 15:50:13');

-- --------------------------------------------------------

--
-- Table structure for table `vendors`
--

CREATE TABLE `vendors` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `photo` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `custom_type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `note` text COLLATE utf8_unicode_ci,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `province` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `vendors`
--

INSERT INTO `vendors` (`id`, `name`, `photo`, `type`, `website`, `custom_type`, `note`, `phone`, `address1`, `address2`, `city`, `province`, `email`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 'Muhammad Gislason', NULL, 'Parts', 'http://hane.biz/', NULL, 'default vendor', '+1104866565935', '641 Flatley Cliffs Suite 320\nSouth Yoshikotown, KY 89709-9837', NULL, 'Lilianahaven', NULL, 'bogan.adrienne@example.net', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(2, 'Teresa Trantow', NULL, 'Fuel', 'http://mante.org/iusto-ratione-iste-at-aut-facere-ad-autem.html', NULL, 'default vendor', '+9927223602105', '1333 Rasheed Freeway Apt. 951\nShannahaven, GA 64238-8852', NULL, 'North Claudie', NULL, 'treva.bogisich@example.net', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14');

-- --------------------------------------------------------

--
-- Table structure for table `work_orders`
--

CREATE TABLE `work_orders` (
  `id` int(10) UNSIGNED NOT NULL,
  `created_on` date DEFAULT NULL,
  `required_by` date DEFAULT NULL,
  `vehicle_id` int(11) DEFAULT NULL,
  `vendor_id` int(11) DEFAULT NULL,
  `price` double(8,2) DEFAULT NULL,
  `status` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8_unicode_ci,
  `meter` int(11) DEFAULT NULL,
  `note` text COLLATE utf8_unicode_ci,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `work_orders`
--

INSERT INTO `work_orders` (`id`, `created_on`, `required_by`, `vehicle_id`, `vendor_id`, `price`, `status`, `description`, `meter`, `note`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, '2020-06-15', '2020-06-20', 1, 1, 2000.00, 'Completed', 'Sample work order', 1214, 'sample work order', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14'),
(2, '2020-06-15', '2020-06-20', 1, 2, 3000.00, 'Pending', 'Sample work order', 1788, 'sample work order', NULL, '2020-06-15 15:50:14', '2020-06-15 15:50:14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addresses`
--
ALTER TABLE `addresses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `allocation`
--
ALTER TABLE `allocation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `api_settings`
--
ALTER TABLE `api_settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bookings_meta`
--
ALTER TABLE `bookings_meta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bookings_meta_booking_id_index` (`booking_id`),
  ADD KEY `bookings_meta_key_index` (`key`);

--
-- Indexes for table `booking_income`
--
ALTER TABLE `booking_income`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `driver_vehicle`
--
ALTER TABLE `driver_vehicle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `email_content`
--
ALTER TABLE `email_content`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expense`
--
ALTER TABLE `expense`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expense_cat`
--
ALTER TABLE `expense_cat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fare_settings`
--
ALTER TABLE `fare_settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fuel`
--
ALTER TABLE `fuel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `income_cat`
--
ALTER TABLE `income_cat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `maintanance`
--
ALTER TABLE `maintanance`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mileage`
--
ALTER TABLE `mileage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notes`
--
ALTER TABLE `notes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notifications_notifiable_type_notifiable_id_index` (`notifiable_type`,`notifiable_id`);

--
-- Indexes for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD KEY `password_resets_email_index` (`email`);

--
-- Indexes for table `reasons`
--
ALTER TABLE `reasons`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `service_items`
--
ALTER TABLE `service_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `service_reminder`
--
ALTER TABLE `service_reminder`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `settings_name_unique` (`name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_api_token_unique` (`api_token`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- Indexes for table `users_meta`
--
ALTER TABLE `users_meta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_meta_user_id_index` (`user_id`),
  ADD KEY `users_meta_key_index` (`key`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicles_meta`
--
ALTER TABLE `vehicles_meta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicles_meta_vehicle_id_index` (`vehicle_id`),
  ADD KEY `vehicles_meta_key_index` (`key`);

--
-- Indexes for table `vehicle_group`
--
ALTER TABLE `vehicle_group`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendors`
--
ALTER TABLE `vendors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `work_orders`
--
ALTER TABLE `work_orders`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addresses`
--
ALTER TABLE `addresses`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `allocation`
--
ALTER TABLE `allocation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `api_settings`
--
ALTER TABLE `api_settings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `bookings_meta`
--
ALTER TABLE `bookings_meta`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `booking_income`
--
ALTER TABLE `booking_income`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `driver_vehicle`
--
ALTER TABLE `driver_vehicle`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `email_content`
--
ALTER TABLE `email_content`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `expense`
--
ALTER TABLE `expense`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `expense_cat`
--
ALTER TABLE `expense_cat`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `fare_settings`
--
ALTER TABLE `fare_settings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `fuel`
--
ALTER TABLE `fuel`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `income`
--
ALTER TABLE `income`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `income_cat`
--
ALTER TABLE `income_cat`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `maintanance`
--
ALTER TABLE `maintanance`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `mileage`
--
ALTER TABLE `mileage`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notes`
--
ALTER TABLE `notes`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `reasons`
--
ALTER TABLE `reasons`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `service_items`
--
ALTER TABLE `service_items`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `service_reminder`
--
ALTER TABLE `service_reminder`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `users_meta`
--
ALTER TABLE `users_meta`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `vehicles_meta`
--
ALTER TABLE `vehicles_meta`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `vehicle_group`
--
ALTER TABLE `vehicle_group`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vendors`
--
ALTER TABLE `vendors`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `work_orders`
--
ALTER TABLE `work_orders`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
