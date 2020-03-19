from flask import Flask
import pymysql
from app import app
from db import mysql
from flask import request
import json

app = Flask(__name__)


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
                holdings.append(result)
            portfolio_data['holdings'] = holdings

        return json.dumps(portfolio_data, indent=4, sort_keys=True, default=str)

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
        cursor.execute("INSERT INTO user_trade(rate,trade,quantity,date,stock_id) VALUES \
        (%s,%s,%s,%s,(SELECT id from stock_list WHERE stock_list.name=%s))", (rate, trade, quantity, date, stock_name))
        conn.commit()
        return 'Inserted Successfully'
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
        cursor.execute("UPDATE user_trade set rate=%s,trade=%s,quantity=%s,date=%s,\
        stock_id=(SELECT id from stock_list WHERE stock_list.name=%s) \
        where id =%s", (rate, trade, quantity, date, stock_name, trade_id))
        conn.commit()
        return 'Updated Successfully'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/portfolio/removeTrade', methods=['POST'])
def removeTrade():
    conn = None
    cursor = None
    try:
        request_obj = request.get_json()
        trade_id = request_obj['trade_id']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM user_trade WHERE id=%s", trade_id)
        conn.commit()
        return 'Removed Successfully'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()
