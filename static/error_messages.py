
class ErrorMsg:
    InsertSuccess = {"success": True, "data": "Successfully Inserted"}
    UpdateSuccess = {"success": True, "data": "Successfully Updated"}
    RemovedSuccess = {"success": True, "data": "Successfully Removed"}
    StockNotAvailable = {"success": False, "data": "Stock name not available. To add new stock insert using portfolio/insertStock API"}
    NegativeValueError = {"success": False, "data": "Please provide positive value for the fields rate and quantity"}
    NonIntegerValueError = {"success": False, "data": "Please provide integer value for the fields rate and quantity"}
    TradeOptionSupport = {"success": False, "data": "Supported trade values are BUY or SELL"}


