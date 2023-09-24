import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2 ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2 ))
 


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
     values={
        'a': [118.24,120.09,120.09,118.13,120.24,110.79,112.7,115.46,115.14,117.87,112.79,116.63,110.5,117.51,113.65,112.39],
        'b': [116.98,116.9,112.27,116.05,111.17,108.62,113.04,114.47,112.29,111.24,116.17,109.03,110.35,111.65,107.04,111.68]
     }
     for i in range(len(values['a'])):
        self.assertEqual(getRatio(values['a'][i],values['b'][i]), values['a'][i]/values['b'][i])

  def test_getRatio_calculateRatioAnyOneStockIsZero(self):
     self.assertEqual(getRatio(0.0123,0), 0)
     self.assertEqual(getRatio(0, 0.0123), 0)
     



if __name__ == '__main__':
    unittest.main()
