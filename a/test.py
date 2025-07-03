from payments import (
    CreditCardPayment,
    PayPalPayment,
    BankTransferPayment,
    SimpleReportGenerator,
    DetailedReportGenerator,
    PaymentProcessor
)

def test_payment_processing():
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()

    assert credit_card.process(100, "1234567890123456")
    assert paypal.process(50, "user@example.com")
    assert bank_transfer.process(200, "1234567890")

    simple_reporter = SimpleReportGenerator()
    detailed_reporter = DetailedReportGenerator()

    processor1 = PaymentProcessor(simple_reporter)
    processor2 = PaymentProcessor(detailed_reporter)

    assert processor1.process_payment(credit_card, 100, "1234567890123456")
    assert processor2.process_payment(paypal, 50, "user@example.com")