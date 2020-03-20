&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/flaskex.svg)](https://github.com/utkarshut/portfoliogreyamptest/issues)

<br><br>

# Portfolio

**Database** 

ClearDB , ClearDB on Heroku enables you to build your apps using native MySQL databases
[Clear DB Details](https://elements.heroku.com/addons/cleardb)

**REST Framework**

FLASK , Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs. It is a lightweight abstraction that works with your existing ORM/libraries. Flask-RESTful encourages best practices with minimal setup
[Flask Details](https://flask-restful.readthedocs.io/en/latest/)

**Deployment Server**

Heroku, Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud
[Heroku Details](www.heroku.com)

**File/Folder Details** 
- Media - Media folder contains all the screenshot images.
[Media folder](https://github.com/utkarshut/portfoliogreyamptest/tree/master/Media)
- Sql - Sql folder contains the sql files to create tables.
[Sql folder](https://github.com/utkarshut/portfoliogreyamptest/tree/master/Sql)
- Config - Config folder contains the database configuration files.
[Config folder](https://github.com/utkarshut/portfoliogreyamptest/tree/master/config)
- Static - Static folder contains the static error messages.
[Static folder](https://github.com/utkarshut/portfoliogreyamptest/tree/master/static)
- app.py - It contains all the route param with function defined for each route param.In this file only all the errors are
handled. [app.py file](https://github.com/utkarshut/portfoliogreyamptest/blob/master/app.py)
- requirement.txt - Requirement file has all the dependencies for the application.
[requirement.txt file](https://github.com/utkarshut/portfoliogreyamptest/blob/master/requirements.txt)



## Features

### Portfolio

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio
- Method - GET
- Example :

<img src="./Media/API_SAMPLE_IMAGES/portfolio.png" alt="Final Output"/>


### Portfolio Holdings

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio/holdings
- Method - GET
- Example :

<img src="./Media/API_SAMPLE_IMAGES/portfolio_holdings.png" alt="Final Output"/>


### Portfolio Returns

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio/returns
- Method - GET
- Example :
<img src="./Media/API_SAMPLE_IMAGES/portfolio_returns.png" alt="Final Output"/>


### Portfolio Add Trade

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio/addTrade
- Method - POST
- Payload Sample - 
{
    "date": "2020-03-20",
    "quantity": 50,
    "rate": 800,
    "trade": "BUY",
    "stock_name":"RELIANCE"
}
- Example :

<img src="./Media/API_SAMPLE_IMAGES/portfolio_add_trade.png" alt="Final Output"/>


### Portfolio Update Trade

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio/updateTrade
- Method - POST
- Payload Sample -
{
    "date": "2020-02-20",
    "quantity": 100,
    "rate": 500,
    "trade": "BUY",
    "stock_name":"RELIANCE",
    "trade_id":1
}
- Example :

<img src="./Media/API_SAMPLE_IMAGES/portfolio_update_trade.png" alt="Final Output"/>


### Portfolio Remove trade

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio/removeTrade
- Method - POST
- Payload Sample -
{
    "trade_id":42
}
- Example :

<img src="./Media/API_SAMPLE_IMAGES/portfolio_remove_trade.png" alt="Final Output"/>

### Portfolio Add Stock Name

- Endpoint - https://portfoliogreyamptest.herokuapp.com/portfolio/insertStock
- Method - POST
- Payload Sample -
{
	"stock_name":"AXISBANK"
}
- Example :

<img src="./Media/API_SAMPLE_IMAGES/portfolio_insert_stock_name.png" alt="Final Output"/>

**Note** : 
1. Date format should be "YYY-MM-DD" format in post calls.
2. To add trade with different stock name , user have to insert Stock using portfolio Add Stock Name API.
3. In case of post calls rate and quantity should have positive integer value.
4. In case of post calls trade can only have value 'BUY' or 'SELL'.


## Error Handling

- In case of add/update trade , trade value can have only BUY or SELL.
<img src="./Media/Error_Handling_Cases/invalide_Trade.png" alt="Final Output"/>

- In case of add/update trade , quantity and rate can have only positive values.
<img src="./Media/Error_Handling_Cases/negative_fields.png" alt="Final Output"/>

- In case of add/update trade , user have to provide valid stock name to update the trade.
<img src="./Media/Error_Handling_Cases/invalid_stockname.png" alt="Final Output"/>

- In case of update trade ,user have to provide valid trade id.
<img src="./Media/Error_Handling_Cases/update_invalide_trade_ID.png" alt="Final Output"/>

- In case of remove trade , user have to provide valid trade id to remove it.
<img src="./Media/Error_Handling_Cases/remove_invalide_trade_id.png" alt="Final Output"/>

- In case of inserting stock , user have to provide different stock name.
<img src="./Media/Error_Handling_Cases/inserting_exsiting_stock.png" alt="Final Output"/>

## Setup
``` 
https://github.com/utkarshut/portfoliogreyamptest
cd portfoliogreyamptest
pip install -r requirements.txt
python app.py
```
