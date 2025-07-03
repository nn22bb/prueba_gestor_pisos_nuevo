# payments.py

class CreditCardPayment:
    def process(self, amount, card_number):
        print(f"Procesando pago con tarjeta por {amount}€ con número {card_number}")
        return True

class PayPalPayment:
    def process(self, amount, email):
        print(f"Procesando pago por PayPal por {amount}€ desde {email}")
        return True

class BankTransferPayment:
    def process(self, amount, account_number):
        print(f"Procesando transferencia bancaria por {amount}€ desde cuenta {account_number}")
        return True

class SimpleReportGenerator:
    def generate(self, amount, method):
        return f"Pago de {amount}€ realizado mediante {method}."

class DetailedReportGenerator:
    def generate(self, amount, method):
        return (
            f"--- Informe Detallado ---\n"
            f"Método: {method}\n"
            f"Cantidad: {amount}€\n"
            f"Estado: Completado\n"
        )

class PaymentProcessor:
    def __init__(self, reporter):
        self.reporter = reporter

    def process_payment(self, method_obj, amount, details):
        if method_obj.process(amount, details):
            report = self.reporter.generate(amount, method_obj.__class__.__name__)
            print(report)
            return True
        return False