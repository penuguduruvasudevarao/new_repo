from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class GooglePay(Payment):

    def pay(self):
        print("Payment using Google Pay")


class PhonePe(Payment):

    def pay(self):
        print("Payment using PhonePe")


g = GooglePay()
p = PhonePe()

g.pay()
p.pay()