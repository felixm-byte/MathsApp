from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
MESSAGES = ["⏰ It's always a good time to revise.", "📜 The mathematics you learn today is forged by the creations of generations past."]
class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    MESSAGES = random.shuffle(MESSAGES)
    self.motivational.text = MESSAGES[0]
    # Any code you write here will run before the form opens.
    