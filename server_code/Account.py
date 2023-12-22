import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
course_options = ["GCSE or iGCSE Higher Maths (9-1)", "GCSE or iGCSE Foundation Maths", "General Maths Knowledge (include everything)"]
@anvil.server.callable
def configure_user_account_properties(email, username, course):
  user = app_tables.users.search(email=email)
  if user == None:
    return "Server Error: User does not exist"
  elif course not in course_options:
    return "Server Error: Course Not Available, try again later"
  else:
    user['course'] = course
    user['username'] = username
    return True