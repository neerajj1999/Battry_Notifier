import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percentage = battery.percent

if percentage >=30:

    Notification(
        title="Battery Percentage Remain",
        description=str(percentage) + " % battery remain!!",
        duration=5,
        urgency=Notification.URGENCY_LOW,

    ).send()