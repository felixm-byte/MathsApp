from ._anvil_designer import SetupTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Setup(SetupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    user = anvil.users.get_user()
    #Returns true if accepted changes by server
    OK = anvil.server.call('configure_user_account_properties', user['email'], self.username.text, self.course.selected_value)
    if OK:
      open_form('Dashboard')
    else:
      alert(OK)
