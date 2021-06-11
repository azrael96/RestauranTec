-- phpMyAdmin SQL Dump
-- version 4.6.6
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 11, 2021 at 04:53 AM
-- Server version: 5.7.17-log
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `restaurantec`
--

-- --------------------------------------------------------

--
-- Table structure for table `factura`
--

CREATE TABLE `factura` (
  `Cod_Fac` int(5) NOT NULL,
  `NomC_Fac` varchar(25) NOT NULL,
  `Tipo_Fac` varchar(25) NOT NULL,
  `CC_Fac` varchar(12) NOT NULL,
  `Tel_Fac` varchar(10) NOT NULL,
  `Meto_Fac` varchar(20) NOT NULL,
  `Camb_Fac` int(15) NOT NULL,
  `Pagdo_Fac` int(15) NOT NULL,
  `Cod_Ped` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `factura`
--

INSERT INTO `factura` (`Cod_Fac`, `NomC_Fac`, `Tipo_Fac`, `CC_Fac`, `Tel_Fac`, `Meto_Fac`, `Camb_Fac`, `Pagdo_Fac`, `Cod_Ped`) VALUES
(1, 'juana perez', 'CEDULA CIUDADANIA', '99999999', '999999999', 'EFECTIVO', 7500, 20000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `pedido`
--

CREATE TABLE `pedido` (
  `Cod_Ped` int(5) NOT NULL,
  `Mesa_Ped` int(3) NOT NULL,
  `Est_Ped` varchar(20) NOT NULL,
  `Pago_Ped` varchar(20) NOT NULL,
  `Fec_Ped` date NOT NULL,
  `Tot_Ped` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pedido`
--

INSERT INTO `pedido` (`Cod_Ped`, `Mesa_Ped`, `Est_Ped`, `Pago_Ped`, `Fec_Ped`, `Tot_Ped`) VALUES
(1, 1, 'ENTREGADO', 'PAGADO', '2021-06-10', 500),
(2, 1, 'EN COCINA', 'NO PAGADO', '2021-06-10', 20000),
(3, 1, 'EN COCINA', 'NO PAGADO', '2021-06-10', 3000);

-- --------------------------------------------------------

--
-- Table structure for table `pedidoplato`
--

CREATE TABLE `pedidoplato` (
  `Cod_PP` int(5) NOT NULL,
  `Cod_Ped` int(5) NOT NULL,
  `Cod_Pla` int(5) NOT NULL,
  `Cant_PP` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pedidoplato`
--

INSERT INTO `pedidoplato` (`Cod_PP`, `Cod_Ped`, `Cod_Pla`, `Cant_PP`) VALUES
(1, 2, 1, 2),
(2, 3, 3, 1),
(3, 3, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `plato`
--

CREATE TABLE `plato` (
  `Cod_Pla` int(5) NOT NULL,
  `Nom_Pla` varchar(40) NOT NULL,
  `Prec_Pla` int(15) NOT NULL,
  `Desc_Pla` varchar(80) NOT NULL,
  `Tipo_Pla` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `plato`
--

INSERT INTO `plato` (`Cod_Pla`, `Nom_Pla`, `Prec_Pla`, `Desc_Pla`, `Tipo_Pla`) VALUES
(1, 'Carne oreada', 10000, 'carne que se oreo', 'PRINCIPAL'),
(2, 'Limonada', 500, 'limon agua y azucar', 'BEBIDA'),
(3, 'Miniempanada', 2000, 'empanadas pequeñas ', 'ENTRADA');

-- --------------------------------------------------------

--
-- Table structure for table `seguridad`
--

CREATE TABLE `seguridad` (
  `Cod_Seg` int(11) NOT NULL,
  `Nick_Seg` varchar(50) NOT NULL,
  `Clav_Seg` varchar(20) NOT NULL,
  `Rol_Seg` varchar(50) NOT NULL,
  `Est_Seg` int(1) NOT NULL,
  `Cod_Usu` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `seguridad`
--

INSERT INTO `seguridad` (`Cod_Seg`, `Nick_Seg`, `Clav_Seg`, `Rol_Seg`, `Est_Seg`, `Cod_Usu`) VALUES
(1, 'juan', '1234', 'ADMON', 0, 1),
(2, 'luis666', '4321', 'WORKER', 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `Cod_Usu` int(11) NOT NULL,
  `Nom_Usu` varchar(50) NOT NULL,
  `Ape1_Usu` varchar(50) NOT NULL,
  `Ape2_Usu` varchar(50) NOT NULL,
  `Tel_Usu` varchar(20) NOT NULL,
  `Dir_Usu` varchar(50) NOT NULL,
  `Tipo_Usu` varchar(20) NOT NULL,
  `CC_Usu` varchar(12) NOT NULL,
  `Mail_Usu` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`Cod_Usu`, `Nom_Usu`, `Ape1_Usu`, `Ape2_Usu`, `Tel_Usu`, `Dir_Usu`, `Tipo_Usu`, `CC_Usu`, `Mail_Usu`) VALUES
(1, 'juan ', 'limon', 'azufre', '3208900987', 'cll 23 n 9 55', 'Cedula Ciudadania', '91919191', 'fake@mail.com'),
(2, 'luis', 'sana', 'bris', '39009485', 'cr 12 n 45 44', 'Cedula Ciudadania', '999999999', 'fake2@mail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `factura`
--
ALTER TABLE `factura`
  ADD PRIMARY KEY (`Cod_Fac`),
  ADD KEY `Cod_Ped` (`Cod_Ped`);

--
-- Indexes for table `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`Cod_Ped`);

--
-- Indexes for table `pedidoplato`
--
ALTER TABLE `pedidoplato`
  ADD PRIMARY KEY (`Cod_PP`),
  ADD KEY `Cod_PP` (`Cod_PP`),
  ADD KEY `Cod_PP_2` (`Cod_PP`),
  ADD KEY `Cod_Ped` (`Cod_Ped`),
  ADD KEY `pedidoplato_ibfk_2` (`Cod_Pla`);

--
-- Indexes for table `plato`
--
ALTER TABLE `plato`
  ADD PRIMARY KEY (`Cod_Pla`);

--
-- Indexes for table `seguridad`
--
ALTER TABLE `seguridad`
  ADD PRIMARY KEY (`Cod_Seg`),
  ADD KEY `seguridad_ibfk_1` (`Cod_Usu`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`Cod_Usu`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pedidoplato`
--
ALTER TABLE `pedidoplato`
  MODIFY `Cod_PP` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `plato`
--
ALTER TABLE `plato`
  MODIFY `Cod_Pla` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `seguridad`
--
ALTER TABLE `seguridad`
  MODIFY `Cod_Seg` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `factura`
--
ALTER TABLE `factura`
  ADD CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`Cod_Ped`) REFERENCES `pedido` (`Cod_Ped`);

--
-- Constraints for table `pedidoplato`
--
ALTER TABLE `pedidoplato`
  ADD CONSTRAINT `pedidoplato_ibfk_1` FOREIGN KEY (`Cod_Ped`) REFERENCES `pedido` (`Cod_Ped`),
  ADD CONSTRAINT `pedidoplato_ibfk_2` FOREIGN KEY (`Cod_Pla`) REFERENCES `plato` (`Cod_Pla`);

--
-- Constraints for table `seguridad`
--
ALTER TABLE `seguridad`
  ADD CONSTRAINT `seguridad_ibfk_1` FOREIGN KEY (`Cod_Usu`) REFERENCES `usuario` (`Cod_Usu`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
