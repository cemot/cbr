-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 26 Agu 2018 pada 15.26
-- Versi server: 10.1.33-MariaDB
-- Versi PHP: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_cbr_python`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `basis_kasus`
--

CREATE TABLE `basis_kasus` (
  `id` int(11) NOT NULL,
  `no_kasus` int(11) DEFAULT NULL,
  `id_penyakit` int(11) DEFAULT NULL,
  `id_gejala` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `basis_kasus`
--

INSERT INTO `basis_kasus` (`id`, `no_kasus`, `id_penyakit`, `id_gejala`) VALUES
(1, 1, 1, 2),
(2, 1, 1, 6),
(3, 2, 1, 2),
(4, 2, 1, 6),
(5, 2, 1, 7),
(6, 3, 2, 1),
(7, 3, 2, 3),
(8, 3, 2, 4),
(9, 3, 2, 8),
(10, 4, 2, 3),
(11, 4, 2, 4),
(12, 4, 2, 8),
(13, 5, 3, 1),
(14, 5, 3, 6),
(15, 5, 3, 7),
(16, 6, 3, 1),
(17, 6, 3, 2),
(18, 6, 3, 6),
(19, 6, 3, 7),
(20, 7, 4, 1),
(21, 7, 4, 2),
(22, 7, 4, 3),
(23, 7, 4, 4),
(24, 7, 4, 5),
(25, 7, 4, 6),
(26, 7, 4, 7),
(27, 8, 4, 1),
(28, 8, 4, 2),
(29, 8, 4, 3),
(30, 8, 4, 5),
(31, 8, 4, 6),
(32, 8, 4, 7),
(33, 8, 4, 8),
(34, 9, 4, 1),
(35, 9, 4, 3),
(36, 9, 4, 4),
(37, 9, 4, 5),
(38, 9, 4, 6),
(39, 9, 4, 7),
(40, 9, 4, 8);

-- --------------------------------------------------------

--
-- Struktur dari tabel `gejala`
--

CREATE TABLE `gejala` (
  `id_gejala` int(11) NOT NULL,
  `nama_gejala` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `gejala`
--

INSERT INTO `gejala` (`id_gejala`, `nama_gejala`) VALUES
(1, 'Badan Panas'),
(4, 'Batuk'),
(5, 'Pilek, Hidung Buntu'),
(6, 'Badan Lemas'),
(7, 'Kedinginan'),
(3, 'Bersin-Bersin'),
(2, 'Sakit Kepala'),
(8, 'Tenggorokan Sakit');

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('admin', '123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `penyakit`
--

CREATE TABLE `penyakit` (
  `id_penyakit` int(11) NOT NULL,
  `nama_penyakit` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `penyakit`
--

INSERT INTO `penyakit` (`id_penyakit`, `nama_penyakit`) VALUES
(1, 'Anemia'),
(2, 'Bronkhitis'),
(4, 'Flu'),
(3, 'Demam');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `basis_kasus`
--
ALTER TABLE `basis_kasus`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `gejala`
--
ALTER TABLE `gejala`
  ADD PRIMARY KEY (`id_gejala`);

--
-- Indeks untuk tabel `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `penyakit`
--
ALTER TABLE `penyakit`
  ADD PRIMARY KEY (`id_penyakit`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `basis_kasus`
--
ALTER TABLE `basis_kasus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT untuk tabel `gejala`
--
ALTER TABLE `gejala`
  MODIFY `id_gejala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT untuk tabel `penyakit`
--
ALTER TABLE `penyakit`
  MODIFY `id_penyakit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
