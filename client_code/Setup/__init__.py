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
    course = self.course.selected_value
    username = self.username.text
    open_form('Dashboard')
