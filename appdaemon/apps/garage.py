import appdaemon.plugins.hass.hassapi as hass

#
# Garage automation for resetting a momentary contact switch
#
# Args:
#   switch: The switch to be reset
#   delay: The amount of time to wait before delaying
#   verbose_log: Turns on verbose logging

class Garage(hass.Hass):
  def initialize(self):
        self.listen_state(self.state_change, self.args["switch"], new="on")

  def state_change(self, entity, attribute, old, new, kwargs):
      self.log_notify("{} turned {}".format(entity, new))
      self.run_in(self.switch_off, self.args["delay"], switch=entity)

  def switch_off(self, kwargs):
      self.log_notify("Turning {} off".format(kwargs["switch"]))
      self.turn_off(self.args["switch"])

  def log_notify(self, message):
      if "verbose_log" in self.args:
          self.log(message)
