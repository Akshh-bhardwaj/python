# ----------------------------------------------------
# 1. Singleton Pattern (Using Metaclass)
# ----------------------------------------------------
print("--- 1. Singleton Pattern ---")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Create and store instance if not cached
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnectionPool(metaclass=SingletonMeta):
    def __init__(self):
        self.connection_string = "postgresql://localhost:5432/production"
        print("Database Connection Pool Initialized (This should only run once!).")

# Test instantiation
pool1 = DatabaseConnectionPool()
pool2 = DatabaseConnectionPool()

print("Is pool1 the same instance as pool2?", pool1 is pool2)
print()


# ----------------------------------------------------
# 2. Factory Pattern
# ----------------------------------------------------
print("--- 2. Factory Pattern ---")

class Notification(object):
    def send(self, message):
        raise NotImplementedError

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: '{message}'")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: '{message}'")

class NotificationFactory:
    @staticmethod
    def get_notifier(notification_type):
        if notification_type.lower() == "sms":
            return SMSNotification()
        elif notification_type.lower() == "email":
            return EmailNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# client code
notifier_sms = NotificationFactory.get_notifier("sms")
notifier_sms.send("Hello, this is an SMS update!")

notifier_email = NotificationFactory.get_notifier("email")
notifier_email.send("Hello, this is an Email digest!")
print()


# ----------------------------------------------------
# 3. Observer Pattern
# ----------------------------------------------------
print("--- 3. Observer Pattern ---")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError

class EmailAlertSystem(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, message):
        print(f"Observer: sending email update to {self.email}: '{message}'")

class SMSAlertSystem(Observer):
    def __init__(self, phone):
        self.phone = phone

    def update(self, message):
        print(f"Observer: sending SMS alert to {self.phone}: '{message}'")

# Create subject
weather_station = Subject()

# Register observers
email_alert = EmailAlertSystem("admin@mycompany.com")
sms_alert = SMSAlertSystem("+1234567890")

weather_station.attach(email_alert)
weather_station.attach(sms_alert)

print("Broadcasting first weather update:")
weather_station.notify("Temperature is now 35 degrees Celsius!")

print("\nDetaching SMS alert...")
weather_station.detach(sms_alert)

print("Broadcasting second weather update:")
weather_station.notify("Storm warning issued!")
