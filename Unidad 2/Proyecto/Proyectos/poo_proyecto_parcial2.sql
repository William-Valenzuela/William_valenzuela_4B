-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-11-2025 a las 22:35:47
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `poo_proyecto_parcial2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `proveedor` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `status` tinyint(4) DEFAULT 1,
  `marca` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `nombre_producto`, `stock`, `proveedor`, `precio`, `status`, `marca`, `descripcion`, `fecha_creacion`) VALUES
(1, 'Laptop Dell XPS', 15, 'TecnoImport', 1200.00, 1, 'Dell', 'Laptop de alto rendimiento', '2025-11-07 21:35:21'),
(2, 'Mouse Inalámbrico', 50, 'ElectroSum', 25.50, 1, 'Logitech', 'Mouse ergonómico inalámbrico', '2025-11-07 21:35:21'),
(3, 'Teclado Mecánico', 30, 'TecnoImport', 80.00, 1, 'Redragon', 'Teclado mecánico RGB', '2025-11-07 21:35:21'),
(4, 'Monitor 24\"', 10, 'DisplayTech', 300.00, 1, 'Samsung', 'Monitor Full HD', '2025-11-07 21:35:21'),
(5, 'Impresora Laser', 8, 'PrintSolutions', 450.00, 1, 'HP', 'Impresora láser monocromática', '2025-11-07 21:35:21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `username`, `nombre`, `correo`, `password`, `fecha_registro`) VALUES
(1, 'admin', 'Administrador', 'admin@sistema.com', 'admin123', '2025-11-07 21:35:21'),
(2, 'juan', 'Juan Pérez', 'juan@email.com', 'juan123', '2025-11-07 21:35:21'),
(3, 'maria', 'María García', 'maria@email.com', 'maria123', '2025-11-07 21:35:21');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
