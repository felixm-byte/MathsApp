from ._anvil_designer import InitialisationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

#Forms 
from ..Setup import Setup
class Initialisation(InitialisationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()

  def continue_click(self, **event_args):
    if anvil.users.get_user()['username'] == None:
      setup = Setup()
      get_open_form().content_panel.clear()
      get_open_form().content_panel.add_component(setup)
    else:
      open_form("Dashboard")
