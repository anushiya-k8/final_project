-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 02, 2024 at 02:01 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `signup_wallet`
--

-- --------------------------------------------------------

--
-- Table structure for table `sw_admin`
--

CREATE TABLE `sw_admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sw_admin`
--

INSERT INTO `sw_admin` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `sw_register_website`
--

CREATE TABLE `sw_register_website` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `web_url` varchar(200) NOT NULL,
  `web_status` varchar(20) NOT NULL,
  `web_username` varchar(20) NOT NULL,
  `web_password` varchar(20) NOT NULL,
  `date_time` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sw_register_website`
--

INSERT INTO `sw_register_website` (`id`, `username`, `web_url`, `web_status`, `web_username`, `web_password`, `date_time`) VALUES
(1, 'taju', 'https://19hourit.com', 'Trusted', 'Taj94560', '754244', '02-02-2024, 18:18:36'),
(2, 'taju', 'https://19hourit.com', 'Trusted', 'Taj94155', '865656', '02-02-2024, 18:29:22'),
(3, 'taju', 'https://gamingzone.in.net', 'Untrusted', 'Nis74872', '521244', '02-02-2024, 18:30:57');

-- --------------------------------------------------------

--
-- Table structure for table `sw_user_profile`
--

CREATE TABLE `sw_user_profile` (
  `uid` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `father` varchar(100) NOT NULL,
  `mother` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `taluk` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `pancard` varchar(100) NOT NULL,
  `driving` varchar(100) NOT NULL,
  `voterid` varchar(100) NOT NULL,
  `bank` varchar(100) NOT NULL,
  `customername` varchar(100) NOT NULL,
  `account` varchar(100) NOT NULL,
  `card` varchar(100) NOT NULL,
  `gnumber` varchar(100) NOT NULL,
  `occupation1` varchar(100) NOT NULL,
  `occupation2` varchar(100) NOT NULL,
  `income1` varchar(100) NOT NULL,
  `income2` varchar(100) NOT NULL,
  `sslc_school` varchar(100) NOT NULL,
  `sslc_mark` varchar(100) NOT NULL,
  `sslc_year` varchar(100) NOT NULL,
  `hsc_school` varchar(100) NOT NULL,
  `hsc_mark` varchar(100) NOT NULL,
  `hsc_year` varchar(100) NOT NULL,
  `ug_college` varchar(100) NOT NULL,
  `ug_degree` varchar(100) NOT NULL,
  `ug_mark` varchar(100) NOT NULL,
  `ug_year` varchar(100) NOT NULL,
  `pg_college` varchar(100) NOT NULL,
  `pg_degree` varchar(100) NOT NULL,
  `pg_mark` varchar(100) NOT NULL,
  `pg_year` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `clocation` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `exp_period` varchar(100) NOT NULL,
  `hdata` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sw_user_profile`
--

INSERT INTO `sw_user_profile` (`uid`, `username`, `father`, `mother`, `address`, `taluk`, `district`, `pincode`, `pancard`, `driving`, `voterid`, `bank`, `customername`, `account`, `card`, `gnumber`, `occupation1`, `occupation2`, `income1`, `income2`, `sslc_school`, `sslc_mark`, `sslc_year`, `hsc_school`, `hsc_mark`, `hsc_year`, `ug_college`, `ug_degree`, `ug_mark`, `ug_year`, `pg_college`, `pg_degree`, `pg_mark`, `pg_year`, `company`, `clocation`, `designation`, `exp_period`, `hdata`) VALUES
(1, 'ramesh', 'LNH3Mk+BU39VW1esW4a1pm7jg/CZELWLsWjAjYttuKE=', 'RqpSPLWtfqM6Tdylt6UfIuVurZEJdZurLaKKjRFKqf0=', '2V7QWUgf5PZWm2VZTvU1INKpGSsmtu1jLBrf0PQRebM=', 'EhY7zHWwRylHGQrMTd5ZCZ+YyCGDKTMyGRXLIKWkmtQ=', 'czd5XuqjCB6GU5yyWlppuqXcxq6kJQmTcITVnbJS6Rk=', 'Ww9FyKYoxPgdybhPlsNVTvC0WIoW3an7hdWHzNjPhIk=', '', '', '', 'EZJBAlCB7qnBXTNN0tbDTOYmC/46nYzCzVtPliChlDI=', 'O0iF98DJOz/V+qq2nlMSCohj/t+oAG1jG0WHEx7837s=', 'Dcoq9vYftu8jAkgUnVGcYfxwIZKF9bZfLki0IXCtKVs=', 'h7HQ0uVoPzt0heN8+hKv2gFwwXvJGq1FNIBWJ/fznY8=', 'LXJRxImcnwyMWDouQRwXu8XaGraM8AjsG2Vw7vjQqNM=', '', '', '', '', 'vpyWpCQgOcNYdkdwIklH315sn427ATPI1Y97eMsakVE=', 'QoVzafsc4lbmS5GIO4MIB/FQCDm99laNNuNZQFyFFPs=', 'IY4jIRb+p5Q+zhWn3jCyjQMex5hCePzj47/HBsfPTVo=', '0vcrZ4+BAJe4DQmDQYGeTpnwzN9KXbCtAVh0LUCyeek=', 'whsK6RNw/RjPvsUAv7d5ejeHSgzh8h24NRi5zkuIw9M=', 'EWHMUMNR3H1AdSGMWcYUCgbaEpbRq2VCZjpiESj1QLQ=', 'x4xz48qYD2J+n4rC7QZ1OeDDjkR6nrm3q2OI6V+AEv8=', 'b0Kq9X2fzQR/+MMU2+FGr802CAZ06raaTphrbQG4O/Y=', 'v47AMGqo7NfEDf+EtI7/8P2KjCJ080l9AmkhiB4j9Jo=', 'bh7OtpjBXzgeKKvdo9f5Jw/XzNqnBTUi+R1Idi9yWfk=', 'oTHCtUebWn5vcNGy69TUDqc53G6G17X+HGRgbcp/7bM=', 'Tk4X6elOMjyHel4jFUgC53NQ6T39YIdx7qJmxy7/lXM=', 'fe4XMaWLxppJXqNIgzWYhAEwLMqF2wGN3EpFKK3aV70=', 'IL8OpXP0l9gpC+IPscOUXHK5/dMfj9Vr6ifFoh3AbMw=', 'osiYZjMa44F9h/OQdi1CoJKftu+5gFkNIcjTXCM7KDM=', 'FqLynw9DgLoiNVrnTZVbq2yhxKU7YsN6NKNLW9cj4TQ=', 'Ut4VKR6zBKsztTv8Hzqahk6NeZqKHGjkwC8b2tdbkJkZlf7K3OxqBymNx/lE2Dxs', 'Xo/ouMgDRowPFfHJHXXZIKIJotgsx6aVeXwAAJVYE0w=', '5217b67fa6ead00f0fb5b4fa4dbadefc'),
(2, 'taju', 'Mw/d/F1yH7ANDEQndwwSeSEQZ2Ulcwz0dmrd+93aWZ8=', 'IcncUf9OHRCuU4mk40/l8OmIGoFRRB4Wb344bj/uwjk=', 'x51PtFCF0m2FUoAaXi2uqtb8gCn3bGOShlHnpIZ7CoI=', 'OhbkOqLBggSpxBRdZei6W2291TiQvBPa2yuF6KY93d0=', 'dB2Y8VvjbIc7aw1rhFEaNXe0wcQsdVEi2Ux8tPUOrck=', '1VnLSqMScts8CBXj9AuxY2PTtGpWVusOa54upo2Jb8Q=', 'oyuFZiJZQ9voTb7LnHXSzQ9a98Ahm7IjOQ53yPXNxp8=', '', '', 'ClpF+Z0CumvoJNq6dKmEzlBdxTLeyrVfqKVfE2pjllc=', '5NsBWw2jQR1zpbI3dO2I2Is3esDp3ucI9lPr1N3MCJg=', 'YjhLXApYUZum/5dL26zg47+Q9QLGh88AgW7KbNU4X1Q=', 'MzkJJGmfKaG0HoW0FpE2hAJQriuh+9mKNMyEc+Y1ROI=', 'kKNRPojbFu0DAKOZOeRNuwUmZY0bKFYmQ9dNZr87aso=', '', '', '', '', 'f8gppstloFWaj6IpjIsdk3dgL5JC3FuyWv4U+BQ+/ic=', '22xXlZmyYX+WZ5GUHVVoblorlcOtXxQzg4ZyCUn0jVI=', '9MAUUXb5XAPUHWLVk3SaMn/E86l/iToIZWH7QrtgSUQ=', '4en+LdIjgO94ubS0mTwbVT9/1mfCbYAsSmbjyGw0ECs=', '8SE4s8sSAiIZ3H7piSrzEvZfuy0FCvkeIcCm6dq2Qog=', 'KgXWNOeLztUfw32YWA8rTc5LT9FrZA1yhSbnftknDAI=', 'HgbkJCfq3xE26PoF5Im6WGdpOAcc5xivTsXnB52C2+U=', '6HVYoaEdG9nLu2jgpNzcYv1k3ESWens7RkqcCVJbWlw=', 'RdRjEjyv/Jv8rYmGFc7PZWhJI7MqEeK1jWNHt2LGpNA=', 'eQoIlxYRB1PCAdqH+7VZ7dUCJ85H1NLpfh6Fp9yxE6U=', '40N1fI6TG/tlSntCmFm79sbp7rgkGp+8CBStvKwDekY=', '8BnKTU7fJy0xrE8IakTp5NANYTy+ComqpLg+O5bHhPk=', 'Lwq4adHeLJ8Lf3vBz0KKJiyR3qAo0muP1QqkW1vuzhg=', 'DVjfJwma5ARaGB9duHaGbB8nteaEGm8oSRGYkP+Vxic=', 'qhyxUQBw8zOLgiFtiRDVpZuttBC0pmPDbV4l1hx67Z0=', 'FBeOQVIG6kYTXbPqgxKxkJE0omZQHvWhqHTO5gPkFCg=', 'yKsVeIbtuhEsR+zNUPuQ3WH+zE3HLmjh2zPwdqcNB2w=', 'h5/dx1pY17Ax+rJU5/ANFo7c9RsAO7x35tnb9YXPTvI=', '058a9164423b96ab7424eefd03b332ea'),
(3, 'raja', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `sw_user_register`
--

CREATE TABLE `sw_user_register` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `aadhar` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `approved_status` int(11) NOT NULL,
  `register_date` varchar(100) NOT NULL,
  `otp` varchar(20) NOT NULL,
  `upi_code` varchar(100) NOT NULL,
  `middle_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `block_key` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sw_user_register`
--

INSERT INTO `sw_user_register` (`id`, `name`, `gender`, `dob`, `aadhar`, `mobile`, `email`, `username`, `password`, `approved_status`, `register_date`, `otp`, `upi_code`, `middle_name`, `last_name`, `block_key`) VALUES
(1, 'FbtBIyHa+eHsdynQKqX2fSU5pLIV/pr0F+yFGSz/5Cc=', 'gY4Qjg116WT40kbWXQc3DpPUko0tbmZ7PEWnwBV/GmU=', 'cKYiDi6EsZrrVj6hqshOi+JuE5Vu4b3bPYT2nqbVdrY=', '', 'WYAMRGAaJVFe5EdvH1FJDtt+DhOxkHXd2D6gfNevmJk=', 'PNJnEVigkVrxtXs7osHiS4LhO6nzo7tF3YdhzBKt13FgRTaiYDroB0n0gXo6zyFV', 'ramesh', 'M+PvwORs08cZlQCiLnbLyFy3TNQ6Y9rUtjz4HvjrcMs=', 0, 's+dYt4upMSWqWqlBeIn3GEJyp6xMnQnPnSUOYevKahA=', '6010', 'UDFQpG2Pf4jyPE0ZK502F/+dbPjTAE379SShzVL3b1A=', 'gNuGwLOydZ2+dRbDjgj5j9FtO11N94HKOhp1EEqVwDQ=', 'iAjn0GxUkCemBfBDIpAfcmm+ZSLGigX2crm9uxiMY5E=', 'eda908e7'),
(2, 'YgDAMMl+WyoX36Dn+OFqdQVRChlCKTgJBQe+errTe90=', 'TrwHhyGjr394FLOokOHYVjFIZ4LQmDPvaSiwd96zA14=', 'f5eCFa7z7a0LwwKAC9LkEpK0jtc0pJ/IK7KU9RkWgRI=', '20lLGQpFmFubYJvHzbiZP6Ya3i3XSJFOOphVIYiJPU0=', 'u3qJ3+hkDVbRAH+U68gAkqdV7rEPcJUcDIdC4fd7kSQ=', '9cNwU3vhDgQrOMsBXoUujkbJLIyIkoWjSg+lDv3QQXFfqt6Jf83tJJQY3JVeTxPd', 'taju', 'QxRdXZV6c3oD8LC9/uNwqqYTbap57ofYEOuxGW8nEP4=', 0, 'ag59nLCeqXBVpGWvSTlvfJc6OSg9pSbMXqG0hsoz7pE=', '9604', 'JpPGjNCcEPpdK7MPXBQxsJe6/eUMXzGeW1di9VVOmdY=', 'ZWGXKm9rHuUy8iQtTGMaiX6Mokqxoa548eXKHthXU/U=', 'GJYManjy8oqELZJtX1GYJEUSBmLAk9sb4Ja1WbwiP44=', '3445c39c'),
(3, 'arf6RHJgA2eOck7hxtRhtv8c0zk6ddUCZTPMOXMQXb4=', 'dy5QShmiIQpQtUxVo0GUsC0W+kdA3ttiIJ7oNbrJjjs=', 'cczwr2be4fs/RSvYa5BdeyxpnWu+ene50X+yoJO2Aq8=', '', 'HkixOmStuHER6A5eYSW7VtkrMxhwLpbc3QcoQtjlPLE=', 'n5UvIQZaZq4yjVG3RvE9+ZCqjB4JJ6u5e60hH8i4nYrY6xNZwTF9leltqfdMReHt', 'raja', 'qb9hjAMwAEjMEvQpQzTf2fvtUB43WgM7Eo+Wd0hsoas=', 0, 'inYjPDU8+wpp1P03GtXoZqrJyOuKL4qH/kRdUFpFdgc=', '3565', 'Cd4wziIy0MRr5XkdH4Tbg5wfookRAwYW4JJ8JGHumT4=', 'L2uVrg8jgfOQ471NVtAEl8ugdqkShv8UmmNLSYrs2gc=', 'XUfidFhe5MS2uVxLhh5PTT1Xttjpj/cGU4mdbu5iQs8=', '96ced43b');

-- --------------------------------------------------------

--
-- Table structure for table `sw_webservice`
--

CREATE TABLE `sw_webservice` (
  `id` int(11) NOT NULL,
  `web_url` varchar(200) NOT NULL,
  `form_data` text NOT NULL,
  `service_code` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sw_webservice`
--

INSERT INTO `sw_webservice` (`id`, `web_url`, `form_data`, `service_code`) VALUES
(1, 'http://19hourit.com/register.php', 'name,gender,dob,aadhar,mobile,email,address,district,pincode,ug_college,ug_degree,ug_mark,ug_year,pg_college,pg_degree,pg_mark,pg_year', '12453931'),
(2, 'https://gamingzone.in.net/register.php', 'name,mobile,email,address,district,pincode,bank,customername,account,card,gnumber', '22448831');
