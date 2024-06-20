-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 20, 2024 at 12:52 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tiket_kereta`
--

CREATE DATABASE IF NOT EXISTS `tiket_kereta`;
USE tiket_kereta;

-- --------------------------------------------------------

--
-- Table structure for table `kereta_api`
--

CREATE TABLE `kereta_api` (
  `id_kereta` char(4) COLLATE utf8mb4_general_ci NOT NULL,
  `nama_kereta` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  `kelas` enum('ekonomi','eksekutif','luxury') COLLATE utf8mb4_general_ci NOT NULL,
  `tujuan` varchar(50) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kereta_api`
--

INSERT INTO `kereta_api` (`id_kereta`, `nama_kereta`, `kelas`, `tujuan`) VALUES
('KAAB', 'Argo Bromo', 'eksekutif', 'Gambir'),
('KAAP', 'Argo Parahyangan', 'ekonomi', 'Bandung'),
('KAAW', 'Argo Wilis', 'luxury', 'Surabaya Gubeng'),
('KAGA', 'Gajayana', 'eksekutif', 'Malang'),
('KATA', 'Taksaka', 'ekonomi', 'Yogyakarta');

-- --------------------------------------------------------

--
-- Table structure for table `pembelian`
--

CREATE TABLE `pembelian` (
  `id_pembelian` int NOT NULL,
  `id_penumpang` int NOT NULL,
  `id_tiket` char(4) COLLATE utf8mb4_general_ci NOT NULL,
  `no_kursi` int NOT NULL,
  `tgl_pembelian` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pembelian`
--

INSERT INTO `pembelian` (`id_pembelian`, `id_penumpang`, `id_tiket`, `no_kursi`, `tgl_pembelian`) VALUES
(1, 1, 'SBAB', 10, '2024-06-10 03:00:00'),
(2, 2, 'PUAP', 20, '2024-06-11 04:00:00'),
(3, 3, 'SRAW', 30, '2024-06-12 05:00:00'),
(4, 4, 'KLTA', 35, '2024-06-13 06:00:00'),
(5, 5, 'SJGA', 40, '2024-06-14 07:00:00'),
(6, 1, 'PUAP', 5, '2024-06-15 08:00:00'),
(7, 2, 'SRAW', 15, '2024-06-16 09:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `penumpang`
--

CREATE TABLE `penumpang` (
  `id_penumpang` int NOT NULL,
  `no_nik` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `nama` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `alamat` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penumpang`
--

INSERT INTO `penumpang` (`id_penumpang`, `no_nik`, `password`, `nama`, `alamat`) VALUES
(1, '1234567890123456', 'budi123', 'Budi Santoso', 'Jl. Lawu No. 1, Karanganyar'),
(2, '2345678901234567', 'siti234', 'Siti Aminah', 'Jl. Slamet Riyadi No. 2, Surakarta'),
(3, '3456789012345678', 'ahmad345', 'Ahmad Yani', 'Jl. Adi Sucipto No. 3, Karanganyar'),
(4, '4567890123456789', 'dewi456', 'Dewi Sartika', 'Jl. Gatot Subroto No. 4, Surakarta'),
(5, '5678901234567890', 'rudi567', 'Rudi Hartono', 'Jl. Kolonel Sutarto No. 5, Karanganyar'),
(6, '1231231231231231', 'denny678', 'Denny Absori', 'Jl. Duwetan No. 13, Surakarta'),
(9, '1122334455667788', 'aabbcc123', 'Ruckus', 'Jl. Washington No. 14 United States');

-- --------------------------------------------------------

--
-- Table structure for table `tiket`
--

CREATE TABLE `tiket` (
  `id_tiket` char(4) COLLATE utf8mb4_general_ci NOT NULL,
  `id_kereta` char(4) COLLATE utf8mb4_general_ci NOT NULL,
  `berangkat` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `waktu_berangkat` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tiket`
--

INSERT INTO `tiket` (`id_tiket`, `id_kereta`, `berangkat`, `waktu_berangkat`) VALUES
('KLTA', 'KATA', 'Klaten', '2024-07-04 11:00:00'),
('PUAP', 'KAAP', 'Purwosari', '2024-07-02 09:00:00'),
('SBAB', 'KAAB', 'Solo Balapan', '2024-07-01 08:00:00'),
('SJGA', 'KAGA', 'Solo Jebres', '2024-07-05 12:00:00'),
('SRAW', 'KAAW', 'Sragen', '2024-07-03 10:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kereta_api`
--
ALTER TABLE `kereta_api`
  ADD PRIMARY KEY (`id_kereta`);

--
-- Indexes for table `pembelian`
--
ALTER TABLE `pembelian`
  ADD PRIMARY KEY (`id_pembelian`),
  ADD KEY `melakukan` (`id_penumpang`),
  ADD KEY `memilih` (`id_tiket`);

--
-- Indexes for table `penumpang`
--
ALTER TABLE `penumpang`
  ADD PRIMARY KEY (`id_penumpang`),
  ADD UNIQUE KEY `no_nik` (`no_nik`);

--
-- Indexes for table `tiket`
--
ALTER TABLE `tiket`
  ADD PRIMARY KEY (`id_tiket`),
  ADD KEY `memiliki` (`id_kereta`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pembelian`
--
ALTER TABLE `pembelian`
  MODIFY `id_pembelian` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `penumpang`
--
ALTER TABLE `penumpang`
  MODIFY `id_penumpang` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pembelian`
--
ALTER TABLE `pembelian`
  ADD CONSTRAINT `melakukan` FOREIGN KEY (`id_penumpang`) REFERENCES `penumpang` (`id_penumpang`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `memilih` FOREIGN KEY (`id_tiket`) REFERENCES `tiket` (`id_tiket`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tiket`
--
ALTER TABLE `tiket`
  ADD CONSTRAINT `memiliki` FOREIGN KEY (`id_kereta`) REFERENCES `kereta_api` (`id_kereta`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
