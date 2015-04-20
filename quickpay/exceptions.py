
class ApiError(Exception):
  def __init__(self, api_error):
      self.body = api_error
      if isinstance(api_error, dict):
        self.message = "Error from Quickpay API. Details:\n Message: {0}".format(api_error["message"])
        
        if 'errors' in api_error:
          self.message = self.message + "\n errors: {0}".format(api_error['errors'])
      else:
        self.message = api_error
        
  def __str__(self):
    return self.message
      