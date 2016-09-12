Name: Mounika Madireddy

Ip address: http://104.236.230.244/

Link to phpmyadmin : http://104.236.230.244/phpmyadmin

#gift_options.sql

"""

CREATE TABLE IF NOT EXISTS `gift_options` (
  `itemId` int(32) NOT NULL,
  
  `allowGiftWrap` tinyint(1) NOT NULL,
  
  `allowGiftMessage` tinyint(1) NOT NULL,
  
  `allowGiftReceipt` tinyint(1) NOT NULL,
  
  PRIMARY KEY (`itemId`)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

"""


#image_entities.sql

"""CREATE TABLE IF NOT EXISTS `image_entities` (

  `itemId` int(32) NOT NULL,
  
  `thumbnailImage` varchar(128) NOT NULL,
  
  `mediumImage` varchar(128) NOT NULL,
  
  `largeImage` varchar(128) NOT NULL,
  
  `entityType` tinytext NOT NULL,
  
  PRIMARY KEY (`itemId`)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""

#market_place_price

"""CREATE TABLE IF NOT EXISTS `market_place_price` (

  `itemId` int(32) NOT NULL,
  
  `price` float(6,2) NOT NULL,
  
  `sellerInfo` varchar(64) NOT NULL,
  
  `standardShipRate` int(32) NOT NULL,
  
  `twoThreeDayShippingRate` float(6,2) NOT NULL,
  
  `availableOnline` tinyint(1) NOT NULL,
  
  `clearance` tinyint(1) NOT NULL,
  
  `offerType` varchar(32) NOT NULL,
  
  PRIMARY KEY (`itemId`)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""

#products.sql

"""
CREATE TABLE IF NOT EXISTS `products` (

  `itemId` int(64) NOT NULL,
  
  `parentItemId` int(64) NOT NULL,
  
  `name` varchar(64) NOT NULL,
  
  `salePrice` float(6,2) NOT NULL,
  
  `upc` int(32) NOT NULL,
  
  `categoryPath` tinytext NOT NULL,
  
  `shortDescription` varchar(128) NOT NULL,
  
  `longDescription` varchar(128) NOT NULL,
  
  `brandName` tinytext NOT NULL,
  
  
  `thumbnailImage` varchar(128) NOT NULL,
  
  `mediumImage` varchar(128) NOT NULL,
  
  `largeImage` varchar(128) NOT NULL,
  
  `productTrackingUrl` varchar(128) NOT NULL,
  
  `modelNumber` varchar(8) NOT NULL,
  
  `productUrl` varchar(128) NOT NULL,
  
  `categoryNode` varchar(16) NOT NULL,
  
  `stock` varchar(16) NOT NULL,
  
  `addToCartUrl` varchar(128) NOT NULL,
  
  `affiliateAddToCartUrl` varchar(128) NOT NULL,
  
  `offerType` varchar(16) NOT NULL,
  
  `msrp` float(4,2) NOT NULL,
  
  `standardShipRate` float(4,2) NOT NULL,
  
  `color` tinytext NOT NULL,
  
  `customerRating` float(6,3) NOT NULL,
  
  `numReviews` int(32) NOT NULL,
  
  `customerRatingImage` varchar(64) NOT NULL,
  
  `maxItemsInOrder` int(32) NOT NULL,
  
  `size` varchar(16) NOT NULL,
  
  `sellerInfo` varchar(32) NOT NULL,
  
  `age` varchar(8) NOT NULL,
  
  `gender` tinytext NOT NULL,
  
  `isbn` bigint(64) NOT NULL,
  
  `preOrderShipsOn` varchar(16) NOT NULL,
  
  PRIMARY KEY (`itemId`),
  
  UNIQUE KEY `itemId` (`itemId`),
  
  UNIQUE KEY `parentItemId` (`parentItemId`)
  
) ENGINE=InnoDB DEFAULT CHARSET=latin1;  """
