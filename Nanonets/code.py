# subjet, message, recepient_email
# sendgrid
# success-failure

from abc import ABC, abstractmethod


class SendEmailNotification(ABC):
    @abstractmethod
    def send_email():
        pass

class TP1(SendEmailNotification):
    def send_email():
        pass

class TP2(SendEmailNotification):
    def send_email():
        pass

def perform_validation(request_payload):
    """
    perform data validations and accordingly throw error
    """
    print("Validation was a success")
    

# def call_sendgrip_api():
#     pass

def get_domain(email):
    pass

def send_email(email_subject, email_message, email_recepient):
    """
    call the sendgrid API with the provided parameters
    """
    # call_sendgrip_api(email_subject=email_subject,email_message=email_message,email_recepient=email_recepient)
    for rec in email_recepient:
        email = rec[0]
        message = rec[1]
        domain = get_domain(email)
        if domain in ["gmail.com","yahoo.com"]:
            spawn_thread
            send_email_in_this_thread
            tp1 = TP1()
            tp1.send_email(email)
            spawn_thread
        elif domain in ["x@y.in"]:
            tp2 = TP2()
            tp2.send_email(email)

class TPFactory:
    pass

    print(f"email successfully sent to {email_recepient}")
    """
    EmailNotificationException
    """

def handleEmailNotification(request_payload):
    if request_payload["method"] == "POST":
        try:
            perform_validation(request_payload)
        except Exception as e:
            return "Operation Failed due to a validation error"
        
        try:
            email_subject = request_payload["data"]["subject"]
            email_message = request_payload["data"]["message"]
            email_recepient = request_payload["data"]["recepient_email"]
            send_email(email_subject,email_message,email_recepient)
            return "Success"
        except Exception as e:
            # notify_dev_team(exception_info=e)
            print(e)
            return "FAILURE"
    else:
        return "Method not supported"
    

# client code

if __name__ == "__main__":
    request_payload = {
        "data": {
            "subject": "hello rajat",
            # "message": "Thanks for reaching out to us.",
            "recepient_list": [("email","message"), ("email","message")]
        },
        "method": "POST"
    }
    response = handleEmailNotification(request_payload)
    print(response)

## concurrent
## different third party for different domains
## different message for diff recep