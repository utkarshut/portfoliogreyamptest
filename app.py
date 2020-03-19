from __init__ import app
from config.db import mysql
from flask import request
from static.error_messages import ErrorMsg
import json
import pymysql
from flask import json
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequest


@app.route('/portfolio', methods=['GET'])
@app.route('/portfolio/<portfolio_type>', methods=['GET'])
def portfolio(portfolio_type=None):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        portfolio_data = {}
        if portfolio_type == 'returns' or portfolio_type is None:
            cursor.execute(
                "select * from stock_list stock  inner join user_trade usr_trade on  stock.id=usr_trade.stock_id")
            rows1 = cursor.fetchall()
            stock_data = []
            for result in rows1:
                stock_data.append(result)
            portfolio_data['stocks'] = stock_data
        if portfolio_type == 'holdings' or portfolio_type is None:
            cursor.execute("select buy_average.name,buy_avg,sum_quant from\
                     (select name,AVG(rate) as buy_avg from stock_list stock  inner join user_trade usr_trade\
                      on  stock.id=usr_trade.stock_id where usr_trade.trade='BUY' group by name ) buy_average \
                      inner join (select name,SUM(quantity * IF(trade = 'SELL', -1, 1)) as sum_quant from \
                      stock_list stock  inner join user_trade usr_trade on  stock.id=usr_trade.stock_id  group by name ) \
                      sum_quantity on buy_average.name=sum_quantity.name")
            rows2 = cursor.fetchall()
            holdings = []
            for result in rows2:
                result["buy_avg"] = round(result["buy_avg"], 0)
                holdings.append(result)
            portfolio_data['holdings'] = holdings
        response_data = {"success": True}
        response_data['data'] = portfolio_data
        return json.dumps(response_data, indent=4, sort_keys=True, default=str)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/portfolio/addTrade', methods=['POST'])
def add_trade():
    conn = None
    cursor = None
    try:
        request_obj = request.get_json()
        rate = request_obj['rate']
        trade = request_obj['trade']
        quantity = request_obj['quantity']
        date = request_obj['date']
        stock_name = request_obj['stock_name']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if type(rate) is not int or type(quantity) is not int:
            return ErrorMsg.NonIntegerValueError
        if rate < 0 or quantity < 0:
            return ErrorMsg.NegativeValueError
        if trade not in ['BUY', 'SELL']:
            return ErrorMsg.TradeOptionSupport
        cursor.execute("SELECT id from stock_list WHERE name=%s", stock_name)
        rows = cursor.fetchall()
        if len(rows) != 0:
            stock_id = rows[0]['id']
            cursor.execute("INSERT INTO user_trade(rate,trade,quantity,date,stock_id) VALUES \
            (%s,%s,%s,%s,%s)", (rate, trade, quantity, date, stock_id))
            conn.commit()
            return ErrorMsg.InsertSuccess
        else:
            return ErrorMsg.StockNotAvailable
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/portfolio/updateTrade', methods=['POST'])
def update_trade():
    conn = None
    cursor = None
    try:
        request_obj = request.get_json()

        rate = request_obj['rate']
        trade = request_obj['trade']
        quantity = request_obj['quantity']
        date = request_obj['date']
        stock_name = request_obj['stock_name']
        trade_id = request_obj['trade_id']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if type(rate) is not int or type(quantity) is not int:
            return ErrorMsg.NonIntegerValueError
        if rate < 0 or quantity < 0:
            return ErrorMsg.NegativeValueError
        if trade not in ['BUY', 'SELL']:
            return ErrorMsg.TradeOptionSupport
        cursor.execute("SELECT id from stock_list WHERE name=%s", stock_name)
        rows = cursor.fetchall()
        print(rows)
        if len(rows) != 0:
            stock_id = rows[0]['id']
            cursor.execute("UPDATE user_trade set rate=%s,trade=%s,quantity=%s,date=%s,\
            stock_id= %s where id =%s", (rate, trade, quantity, date, stock_id, trade_id))
            conn.commit()
            return ErrorMsg.UpdateSuccess
        else:
            return ErrorMsg.StockNotAvailable
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/portfolio/removeTrade', methods=['POST'])
def remove_trade():
    conn = None
    cursor = None
    try:
        request_obj = request.get_json()
        trade_id = request_obj['trade_id']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM user_trade WHERE id=%s", trade_id)
        rows = cursor.fetchall()
        rowcount = cursor.rowcount
        conn.commit()
        ErrorMsg.RemovedSuccess["data"] = '{} Row Deleted'.format(rowcount)
        if rowcount == 0:
            ErrorMsg.RemovedSuccess["success"] = False
            ErrorMsg.RemovedSuccess["description"] = 'Given Trade id not Available'
        return ErrorMsg.RemovedSuccess
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/portfolio/insertStock', methods=['POST'])
def add_stock():
    conn = None
    cursor = None
    try:
        request_obj = request.get_json()
        stock_name = request_obj['stock_name']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT IGNORE INTO stock_list (name) VALUES (%s)", stock_name)
        rowcount = cursor.rowcount
        conn.commit()
        ErrorMsg.InsertSuccess["data"] = '{} Row Successfully Inserted'.format(rowcount)
        return ErrorMsg.InsertSuccess
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400


if __name__ == "__main__":
    app.run()
