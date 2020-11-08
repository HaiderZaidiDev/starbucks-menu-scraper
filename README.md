# starbucks-menu-scraper
Scrapes items (food, drinks, sizes, prices) from Starbucks' menu, and runs monte carlo simulations to estimate yearly revenues.

## Background
Wanted to play around with scraping; also for my business class we were tasked with using guesstimation to predict average revenue for a store in a year, rather than visting a store in person for data I used monte carlo simulations instead based on a few assumptions.

## Monte Carlo Controls:
[Average number of customers at a Starbucks a day assumed to be between 600-700 people.](https://www.businessinsider.com/how-many-customers-starbucks-will-have-2013-10#:~:text=Trefis%20has%20released%20a%20report,2020%2C%20according%20to%20the%20report.)
Average number of items a Starbucks customer purchases is between 1-3 items.

## Accuracy
For increased accuracy, it would be beneficial to add types (i.e whether an item is a food or drink) to predict realistic combinations of item purchases (e.g if a customer buys more than 2 items, create a 50% chance of the two items being two different types). Currently, items are randomly selected from a list, resulting in possible purchases where multiple items (e.g 3 drinks) could be purchased, which is less likely than per say someone purchasing a drink and a food item.

## Scraper Output
```
{
   "Caffe Latte":{
      "Tall":2.95,
      "Grande":3.65,
      "Venti":4.15
   },
   "Caffe Mocha":{
      "Tall":3.45,
      "Grande":4.15,
      "Venti":4.65
   },
   "White Chocolate Mocha":{
      "Tall":3.75,
      "Grande":4.45,
      "Venti":4.75
   },
   "Freshly Brewed Coffee":{
      "Tall":1.85,
      "Grande":2.1,
      "Venti":2.45
   },
   "Cinnamon Dolce Latte":{
      "Tall":3.65,
      "Grande":4.25,
      "Venti":4.65
   },
   "Skinny Vanilla Latte":{
      "Tall":3.45,
      "Grande":4.15,
      "Venti":4.65
   },
   "Caramel Macchiato":{
      "Tall":3.75,
      "Grande":4.45,
      "Venti":4.75
   },
   "Caramel Flan Latte":{
      "Tall":3.75,
      "Grande":4.55,
      "Venti":4.75
   },
   "Teavana® Oprah Cinnamon Chai Tea Latte":{
      "Tall":3.65,
      "Grande":4.25,
      "Venti":4.65
   },
   "Flat White":{
      "Tall":3.75
   },
   "Skinny Peppermint Mocha ":{
      "Tall":3.95,
      "Grande":4.65,
      "Venti":4.95
   },
   "Pumpkin Spice Latte (Limited Time)":{
      "Tall":4.25,
      "Grande":4.95,
      "Venti":5.25
   },
   "Salted Caramel Mocha (Limited Time)":{
      "Tall":4.25,
      "Grande":4.95,
      "Venti":5.25
   },
   "Toasted Graham Latte (Limited Time)":{
      "Tall":4.25,
      "Grande":4.95,
      "Venti":5.25
   },
   "Iced Coffee (with or without Milk)":{
      "Tall":2.25,
      "Grande":2.65,
      "Venti":2.95,
      "Trenta":3.45
   },
   "Caramel Frappuccino":{
      "Mini":3.75,
      "Tall":3.95,
      "Grande":4.45,
      "Venti":4.95
   },
   "Mocha Frappuccino":{
      "Mini":3.75,
      "Tall":3.95,
      "Grande":4.45,
      "Venti":4.95
   },
   "Strawberries & Creme Frappuccino":{
      "Mini":3.75,
      "Tall":3.95,
      "Grande":4.45,
      "Venti":4.95
   },
   "Coffee Frappuccino":{
      "Mini":2.95,
      "Tall":3.25,
      "Grande":3.95,
      "Venti":4.45
   },
   "Vanilla Bean Crème Frappuccino":{
      "Mini":2.95,
      "Tall":3.25,
      "Grande":3.95,
      "Venti":4.45
   },
   "Iced Caramel Macchiato":{
      "Tall":3.75,
      "Grande":4.45,
      "Venti":4.95
   },
   "Salted Caramel Mocha Frappuccino (Limited Time)":{
      "Tall":4.25,
      "Grande":4.95,
      "Venti":5.25
   },
   "Cool Lime or Very Berry Starbucks Refreshers™ ":{
      "Tall":2.95,
      "Grande":3.45,
      "Venti":3.95,
      "Trenta":4.45
   },
   "Teavana® Shaken Iced Tea":{
      "Tall":1.75,
      "Grande":2.25,
      "Venti":2.65,
      "Trenta":2.95
   },
   "Teavana® Shaken Iced Peach Green Tea Lemonade":{
      "Tall":2.75,
      "Grande":3.25,
      "Venti":3.75,
      "Trenta":4.25
   },
   "Teavana® Shaken Iced Black Tea Lemonade":{
      "Tall":2.45,
      "Grande":2.95,
      "Venti":3.45,
      "Trenta":3.95
   },
   "Evolution Fresh":{
      "Grande":5.95
   },
   "Ham & Cheese Savory Foldover":{
      "None":3.45
   },
   "Wheat Spinach Savory Foldover":{
      "None":3.45
   },
   "Pepperoni & Tomato Savory Foldover":{
      "None":3.45
   },
   "Cheese Danish":{
      "None":2.45
   },
   "Butter Croissant":{
      "None":2.45
   },
   "Chocolate Croissant":{
      "None":2.75
   },
   "Blueberry Scone":{
      "None":2.45
   },
   "Banana Nut Bread":{
      "None":2.75
   },
   "Iced Lemon Pound Cake":{
      "None":2.45
   },
   "Morning Bun":{
      "None":2.45
   },
   "Chocolate Chip Cookie":{
      "None":1.95
   },
   "Double Chocolate Chunk Brownie":{
      "None":2.35
   },
   "Pumpkin Scone (Limited Time)":{
      "None":2.95
   },
   "Pumpkin Cream Cheese Muffin (Limited Time)":{
      "None":2.95
   },
   "Washington Apple Pound Cake (Limited Time)":{
      "None":2.95
   },
   "Hearty Blueberry Oatmeal":{
      "None":3.45
   },
   "Bacon & Gouda Breakfast Sandwich":{
      "None":3.75
   },
   "Sausage & Cheddar Breakfast Sandwich":{
      "None":3.45
   },
   "Spinach & Feta Breakfast Wrap":{
      "None":3.75
   },
   "Reduced-Fat Turkey Bacon Breakfast Sandwich":{
      "None":3.75
   },
   "Slow-Roasted Ham & Swiss on Croissant Bun":{
      "None":4.75
   },
   "Double-Smoked Bacon, Cheddar & Egg on Croissant Bun (Limited Time)":{
      "None":4.75
   },
   "Protein Bistro Box":{
      "None":5.25
   },
   "Cheese & Fruit Bistro Box":{
      "None":4.95
   },
   "Omega-3 Bistro Box":{
      "None":5.95
   },
   "PB&J on Wheat Bistro Box":{
      "None":5.25
   },
   "Turkey Rustico Panini":{
      "None":6.45
   },
   "Turkey Pesto Panini":{
      "None":6.45
   },
   "Ham & Swiss Panini":{
      "None":5.95
   },
   "Chicken Santa Fe Flatbread":{
      "None":5.95
   },
   "Chicken BLT Salad Deli Sandwich":{
      "None":5.95
   },
   "Roasted Tomato & Mozzarella Panini":{
      "None":5.55
   },
   "Chicken Artichoke Panini (Limited Time)":{
      "None":6.45
   },
   "Old-Fashioned Grilled Cheese":{
      "None":5.25
   },
   "Edamame Hummus Wrap (Limited Time)":{
      "None":5.95
   },
   "Thai-Style Peanut Chicken Wrap (Limited Time)":{
      "None":5.95
   },
   "Salted Caramel or Birthday Cake Pop":{
      "None":1.95,
      "2 Pc.":3.5
   }
}
```
## Estimated Yearly Revenue Output
```
Revenue for Day #0: $4849.749999999982
Revenue for Day #1: $4907.049999999981
Revenue for Day #2: $4954.099999999981
Revenue for Day #3: $4932.8499999999885
Revenue for Day #4: $5007.449999999985
Revenue for Day #5: $5004.999999999986
Revenue for Day #6: $4929.8999999999805
Revenue for Day #7: $4906.499999999982
Revenue for Day #8: $4980.099999999982
Revenue for Day #9: $4993.949999999986
Revenue for Day #10: $4912.849999999985
Revenue for Day #11: $4888.899999999977
Revenue for Day #12: $4936.999999999981
Revenue for Day #13: $5033.74999999998
Revenue for Day #14: $4990.199999999984
Revenue for Day #15: $5234.4999999999845
Revenue for Day #16: $4977.4499999999825
Revenue for Day #17: $5020.949999999985
Revenue for Day #18: $4806.04999999998
Revenue for Day #19: $4930.699999999983
Revenue for Day #20: $5051.999999999983
Revenue for Day #21: $5008.199999999978
Revenue for Day #22: $4886.299999999983
Revenue for Day #23: $4871.34999999998
Revenue for Day #24: $4966.049999999987
Revenue for Day #25: $4973.8999999999805
Revenue for Day #26: $5045.249999999981
Revenue for Day #27: $4910.549999999985
Revenue for Day #28: $4900.149999999987
Revenue for Day #29: $4935.49999999998
Revenue for Day #30: $4848.999999999986
Revenue for Day #31: $4860.299999999987
Revenue for Day #32: $4975.49999999998
Revenue for Day #33: $4936.049999999985
Revenue for Day #34: $4818.549999999981
Revenue for Day #35: $5024.699999999979
Revenue for Day #36: $4981.1499999999805
Revenue for Day #37: $4954.699999999982
Revenue for Day #38: $5058.999999999986
Revenue for Day #39: $4916.499999999982
Revenue for Day #40: $5039.949999999984
Revenue for Day #41: $4975.049999999977
Revenue for Day #42: $4892.499999999983
Revenue for Day #43: $4914.949999999977
Revenue for Day #44: $4767.999999999983
Revenue for Day #45: $4934.349999999974
Revenue for Day #46: $4773.349999999985
Revenue for Day #47: $5059.1499999999805
Revenue for Day #48: $4967.399999999983
Revenue for Day #49: $4901.849999999989
Revenue for Day #50: $5085.29999999998
Revenue for Day #51: $5075.699999999985
Revenue for Day #52: $4828.449999999983
Revenue for Day #53: $4864.09999999998
Revenue for Day #54: $4894.249999999984
Revenue for Day #55: $4904.399999999976
Revenue for Day #56: $4794.49999999998
Revenue for Day #57: $4799.749999999985
Revenue for Day #58: $5007.049999999982
Revenue for Day #59: $5021.049999999981
Revenue for Day #60: $4834.74999999998
Revenue for Day #61: $4980.699999999977
Revenue for Day #62: $4947.54999999998
Revenue for Day #63: $5070.699999999982
Revenue for Day #64: $4921.499999999981
Revenue for Day #65: $5017.049999999973
Revenue for Day #66: $4917.299999999984
Revenue for Day #67: $4946.749999999979
Revenue for Day #68: $4877.299999999983
Revenue for Day #69: $4995.799999999984
Revenue for Day #70: $4876.499999999985
Revenue for Day #71: $5074.94999999998
Revenue for Day #72: $4844.349999999983
Revenue for Day #73: $4880.699999999983
Revenue for Day #74: $4935.999999999978
Revenue for Day #75: $4874.44999999998
Revenue for Day #76: $4900.999999999982
Revenue for Day #77: $4822.749999999983
Revenue for Day #78: $4794.449999999978
Revenue for Day #79: $4934.199999999976
Revenue for Day #80: $4816.099999999985
Revenue for Day #81: $4927.649999999984
Revenue for Day #82: $4892.649999999987
Revenue for Day #83: $4938.749999999983
Revenue for Day #84: $4843.649999999987
Revenue for Day #85: $4866.449999999983
Revenue for Day #86: $4929.199999999979
Revenue for Day #87: $4861.599999999987
Revenue for Day #88: $5080.499999999984
Revenue for Day #89: $4986.599999999974
Revenue for Day #90: $5082.049999999981
Revenue for Day #91: $4842.499999999984
Revenue for Day #92: $4815.499999999986
Revenue for Day #93: $4923.849999999981
Revenue for Day #94: $4884.699999999982
Revenue for Day #95: $4950.349999999986
Revenue for Day #96: $4864.999999999982
Revenue for Day #97: $4788.1999999999825
Revenue for Day #98: $5080.049999999982
Revenue for Day #99: $4979.699999999975
Revenue for Day #100: $4932.999999999984
Revenue for Day #101: $5021.499999999975
Revenue for Day #102: $5027.299999999977
Revenue for Day #103: $4846.449999999981
Revenue for Day #104: $4902.399999999983
Revenue for Day #105: $4831.4499999999825
Revenue for Day #106: $4905.049999999983
Revenue for Day #107: $4870.399999999983
Revenue for Day #108: $4898.549999999984
Revenue for Day #109: $4894.099999999987
Revenue for Day #110: $5044.149999999975
Revenue for Day #111: $4902.69999999998
Revenue for Day #112: $4816.949999999979
Revenue for Day #113: $4996.399999999983
Revenue for Day #114: $4798.449999999985
Revenue for Day #115: $4887.549999999979
Revenue for Day #116: $4882.449999999982
Revenue for Day #117: $4927.649999999984
Revenue for Day #118: $4927.449999999986
Revenue for Day #119: $4847.549999999981
Revenue for Day #120: $4943.199999999978
Revenue for Day #121: $4827.999999999978
Revenue for Day #122: $4914.14999999998
Revenue for Day #123: $4818.749999999982
Revenue for Day #124: $5027.499999999983
Revenue for Day #125: $5046.849999999979
Revenue for Day #126: $4885.299999999979
Revenue for Day #127: $4900.599999999985
Revenue for Day #128: $4973.149999999983
Revenue for Day #129: $4742.199999999983
Revenue for Day #130: $4956.999999999982
Revenue for Day #131: $4971.799999999986
Revenue for Day #132: $4980.549999999982
Revenue for Day #133: $4885.1999999999825
Revenue for Day #134: $5085.099999999984
Revenue for Day #135: $4980.299999999977
Revenue for Day #136: $4900.599999999982
Revenue for Day #137: $4895.84999999998
Revenue for Day #138: $4828.449999999984
Revenue for Day #139: $4866.349999999983
Revenue for Day #140: $4757.6499999999805
Revenue for Day #141: $4817.949999999982
Revenue for Day #142: $5028.449999999981
Revenue for Day #143: $4855.799999999986
Revenue for Day #144: $5250.049999999982
Revenue for Day #145: $4803.1999999999825
Revenue for Day #146: $4969.449999999975
Revenue for Day #147: $5062.149999999983
Revenue for Day #148: $4925.4999999999845
Revenue for Day #149: $4958.649999999982
Revenue for Day #150: $4839.749999999984
Revenue for Day #151: $4951.4499999999825
Revenue for Day #152: $5027.049999999983
Revenue for Day #153: $4967.249999999985
Revenue for Day #154: $4907.649999999979
Revenue for Day #155: $4820.5499999999865
Revenue for Day #156: $4958.549999999979
Revenue for Day #157: $4879.449999999989
Revenue for Day #158: $5107.299999999977
Revenue for Day #159: $4864.599999999986
Revenue for Day #160: $4866.549999999981
Revenue for Day #161: $4829.249999999979
Revenue for Day #162: $4878.749999999984
Revenue for Day #163: $4809.699999999981
Revenue for Day #164: $5077.349999999988
Revenue for Day #165: $5032.649999999987
Revenue for Day #166: $4701.449999999985
Revenue for Day #167: $4907.649999999986
Revenue for Day #168: $4986.499999999979
Revenue for Day #169: $4971.649999999981
Revenue for Day #170: $4914.049999999983
Revenue for Day #171: $4830.59999999998
Revenue for Day #172: $4991.849999999979
Revenue for Day #173: $4869.09999999998
Revenue for Day #174: $4869.449999999984
Revenue for Day #175: $5150.149999999992
Revenue for Day #176: $4882.799999999984
Revenue for Day #177: $4844.699999999984
Revenue for Day #178: $4858.6999999999825
Revenue for Day #179: $4753.949999999988
Revenue for Day #180: $4894.749999999983
Revenue for Day #181: $5154.049999999984
Revenue for Day #182: $4887.049999999976
Revenue for Day #183: $4820.649999999982
Revenue for Day #184: $4844.999999999983
Revenue for Day #185: $4905.299999999979
Revenue for Day #186: $4905.199999999985
Revenue for Day #187: $4886.049999999982
Revenue for Day #188: $4811.9499999999825
Revenue for Day #189: $5044.049999999983
Revenue for Day #190: $4820.649999999985
Revenue for Day #191: $4894.099999999987
Revenue for Day #192: $4831.449999999983
Revenue for Day #193: $4876.649999999986
Revenue for Day #194: $4991.199999999989
Revenue for Day #195: $5060.499999999981
Revenue for Day #196: $4839.6999999999825
Revenue for Day #197: $4891.599999999985
Revenue for Day #198: $5051.649999999983
Revenue for Day #199: $4979.449999999983
Revenue for Day #200: $4949.749999999979
Revenue for Day #201: $4904.3999999999805
Revenue for Day #202: $4792.399999999983
Revenue for Day #203: $4873.349999999986
Revenue for Day #204: $4931.649999999982
Revenue for Day #205: $4887.3999999999805
Revenue for Day #206: $4955.149999999982
Revenue for Day #207: $4962.499999999978
Revenue for Day #208: $5003.199999999982
Revenue for Day #209: $5022.049999999981
Revenue for Day #210: $5090.149999999982
Revenue for Day #211: $4843.249999999988
Revenue for Day #212: $4957.249999999983
Revenue for Day #213: $5012.449999999984
Revenue for Day #214: $5081.5999999999785
Revenue for Day #215: $4825.799999999984
Revenue for Day #216: $5064.499999999983
Revenue for Day #217: $4800.949999999979
Revenue for Day #218: $4941.199999999978
Revenue for Day #219: $5027.299999999988
Revenue for Day #220: $4932.299999999984
Revenue for Day #221: $5008.64999999998
Revenue for Day #222: $5013.599999999983
Revenue for Day #223: $4843.4499999999825
Revenue for Day #224: $4889.399999999979
Revenue for Day #225: $5006.949999999978
Revenue for Day #226: $5031.64999999998
Revenue for Day #227: $4931.649999999984
Revenue for Day #228: $4981.049999999978
Revenue for Day #229: $4915.449999999982
Revenue for Day #230: $4980.949999999988
Revenue for Day #231: $4793.4999999999845
Revenue for Day #232: $5002.699999999977
Revenue for Day #233: $4994.799999999983
Revenue for Day #234: $5022.949999999981
Revenue for Day #235: $4895.699999999976
Revenue for Day #236: $4878.349999999986
Revenue for Day #237: $5050.599999999983
Revenue for Day #238: $4912.749999999982
Revenue for Day #239: $4995.899999999976
Revenue for Day #240: $4841.749999999984
Revenue for Day #241: $5036.199999999982
Revenue for Day #242: $4868.899999999979
Revenue for Day #243: $4957.799999999981
Revenue for Day #244: $4871.549999999979
Revenue for Day #245: $4894.149999999982
Revenue for Day #246: $4994.549999999979
Revenue for Day #247: $4988.2499999999845
Revenue for Day #248: $4962.399999999978
Revenue for Day #249: $4922.349999999982
Revenue for Day #250: $4839.899999999986
Revenue for Day #251: $4903.5499999999865
Revenue for Day #252: $4882.599999999981
Revenue for Day #253: $4907.449999999983
Revenue for Day #254: $4836.749999999983
Revenue for Day #255: $4778.799999999982
Revenue for Day #256: $4897.399999999976
Revenue for Day #257: $4794.949999999985
Revenue for Day #258: $4905.09999999998
Revenue for Day #259: $4901.099999999977
Revenue for Day #260: $4993.599999999981
Revenue for Day #261: $4860.899999999981
Revenue for Day #262: $4805.9499999999825
Revenue for Day #263: $4871.89999999998
Revenue for Day #264: $4947.6499999999805
Revenue for Day #265: $4926.399999999989
Revenue for Day #266: $4867.74999999999
Revenue for Day #267: $4926.3999999999805
Revenue for Day #268: $4946.49999999998
Revenue for Day #269: $5029.049999999979
Revenue for Day #270: $4836.9999999999845
Revenue for Day #271: $4887.149999999983
Revenue for Day #272: $5077.299999999982
Revenue for Day #273: $5015.049999999986
Revenue for Day #274: $4858.149999999982
Revenue for Day #275: $4936.599999999989
Revenue for Day #276: $4926.649999999982
Revenue for Day #277: $4980.949999999979
Revenue for Day #278: $4842.399999999975
Revenue for Day #279: $4878.399999999985
Revenue for Day #280: $4878.699999999983
Revenue for Day #281: $5016.54999999998
Revenue for Day #282: $4948.449999999981
Revenue for Day #283: $4941.99999999998
Revenue for Day #284: $4967.449999999975
Revenue for Day #285: $4946.599999999982
Revenue for Day #286: $5039.799999999986
Revenue for Day #287: $4932.149999999991
Revenue for Day #288: $4802.149999999982
Revenue for Day #289: $4922.799999999991
Revenue for Day #290: $5011.749999999983
Revenue for Day #291: $5001.499999999983
Revenue for Day #292: $4873.199999999981
Revenue for Day #293: $4837.849999999984
Revenue for Day #294: $4861.3999999999805
Revenue for Day #295: $4940.799999999981
Revenue for Day #296: $5005.099999999977
Revenue for Day #297: $4964.5499999999765
Revenue for Day #298: $5008.449999999981
Revenue for Day #299: $4984.499999999981
Revenue for Day #300: $4978.199999999985
Revenue for Day #301: $4939.949999999983
Revenue for Day #302: $5005.549999999983
Revenue for Day #303: $4804.4999999999845
Revenue for Day #304: $4958.499999999984
Revenue for Day #305: $5012.899999999981
Revenue for Day #306: $4973.249999999988
Revenue for Day #307: $4944.8999999999805
Revenue for Day #308: $4816.999999999986
Revenue for Day #309: $4956.39999999998
Revenue for Day #310: $4893.349999999994
Revenue for Day #311: $4922.049999999985
Revenue for Day #312: $4984.199999999985
Revenue for Day #313: $4802.299999999986
Revenue for Day #314: $4835.4499999999825
Revenue for Day #315: $4885.4499999999825
Revenue for Day #316: $4929.549999999983
Revenue for Day #317: $5131.949999999982
Revenue for Day #318: $5000.399999999972
Revenue for Day #319: $4764.399999999987
Revenue for Day #320: $4882.899999999983
Revenue for Day #321: $4894.599999999984
Revenue for Day #322: $4904.699999999986
Revenue for Day #323: $4848.649999999979
Revenue for Day #324: $4926.199999999976
Revenue for Day #325: $5076.849999999983
Revenue for Day #326: $5049.049999999983
Revenue for Day #327: $4863.849999999979
Revenue for Day #328: $5048.2999999999765
Revenue for Day #329: $5027.249999999978
Revenue for Day #330: $4893.149999999985
Revenue for Day #331: $4962.0999999999785
Revenue for Day #332: $5035.549999999979
Revenue for Day #333: $4970.899999999978
Revenue for Day #334: $4925.299999999987
Revenue for Day #335: $4966.249999999982
Revenue for Day #336: $4999.699999999987
Revenue for Day #337: $4906.199999999986
Revenue for Day #338: $4875.849999999993
Revenue for Day #339: $4824.799999999984
Revenue for Day #340: $4886.799999999987
Revenue for Day #341: $5053.7499999999845
Revenue for Day #342: $4945.599999999982
Revenue for Day #343: $4884.3999999999805
Revenue for Day #344: $4872.599999999981
Revenue for Day #345: $4860.449999999983
Revenue for Day #346: $4871.199999999981
Revenue for Day #347: $4961.4499999999825
Revenue for Day #348: $4905.949999999985
Revenue for Day #349: $5018.799999999983
Revenue for Day #350: $4893.199999999985
Revenue for Day #351: $5089.099999999982
Revenue for Day #352: $4778.149999999981
Revenue for Day #353: $4870.849999999988
Revenue for Day #354: $5066.549999999981
Revenue for Day #355: $5002.299999999984
Revenue for Day #356: $4943.649999999982
Revenue for Day #357: $4897.749999999984
Revenue for Day #358: $4818.849999999982
Revenue for Day #359: $4842.799999999983
Revenue for Day #360: $4847.799999999988
Revenue for Day #361: $4956.749999999976
Revenue for Day #362: $4927.449999999982
Revenue for Day #363: $4860.4499999999825
Revenue for Day #364: $4994.799999999983
Yearly revenue is: $1798960.799999994
```
