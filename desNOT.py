from plyer import notification
import schedule
import time

def notify(title, message, duration=10):
    notification.notify(
        title=title,
        message=message,
        timeout=duration
    )

def job(title, message, duration):
    notify(title, message, duration)

if __name__ == "__main__":
     
    custom_title = "Reminder"
    custom_message = "Don't forget to take a break!"
    custom_duration = 10  
  
    schedule.every().hour.do(job, title=custom_title, message=custom_message, duration=custom_duration)
    

    while True:
        schedule.run_pending()
        time.sleep(1)
