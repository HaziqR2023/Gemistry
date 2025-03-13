SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS `listing` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `listing`;

-- --------------------------------------------------------

--
-- Table structure for table `listing`
--

DROP TABLE IF EXISTS `listing`;
CREATE TABLE IF NOT EXISTS `listing` (
-- ListingID: INT
"ListingID" INT NOT NULL
-- ListingOwner: INT
"ListingOwner" INT NOT NULL
-- ListingName: VARCHAR
"ListingName" VARCHAR NOT NULL
-- ListingCategory: VARCHAR
"ListingCategory" VARCHAR NOT NULL
-- ListingPrice: Bool
"ListingPrice" BOOLEAN NOT NULL
-- ListingItem: FLOAT
"ListingItem" FLOAT NOT NULL
-- ListingDesc: VARCHAR
"ListingDesc" VARCHAR NOT NULL
-- isActive: Bool
"isActive" BOOLEAN NOT NULL
PRIMARY KEY ("ListingID")

--   `title` varchar(64) NOT NULL,
--   `isbn13` char(13) NOT NULL,
--   `price` decimal(10,2) NOT NULL,
--   `availability` int(11) DEFAULT NULL,
--   PRIMARY KEY (`isbn13`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `listing`
--

-- INSERT INTO `book` (`title`, `isbn13`, `price`, `availability`) VALUES
-- ('SQL in Nutshell', '9781129474251', '21.50', 2),
-- ('Understanding People', '9781349471231', '99.40', 25),
-- ('Happy in Workplace', '9781434474234', '94.00', 1),
-- ('PHP Soup', '9781442374221', '20.50', 2),
-- ('Brief History of Time', '9781449474211', '20.00', 23),
-- ('It', '9781449474212', '1.00', 2),
-- ('Founder of Php', '9781449474221', '34.00', 1),
-- ('Albert Enstein\'s Works', '9781449474223', '18.00', 7),
-- ('Interstellar', '9781449474254', '10.00', 4),
-- ('Milk and Honey', '9781449474256', '25.00', 18),
-- ('Cooking Book', '9781449474323', '99.90', 4),
-- ('The Gathering', '9781449474342', '20.00', 50);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;