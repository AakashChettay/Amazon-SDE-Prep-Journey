public class Factory {
    // Payment Interface
    interface Payment {
        void pay(int amount);
    }

    static class CreditCardPayment implements Payment {
        @Override
        public void pay(int amount) {
            System.out.println("Paid " + amount + " using Credit Card.");
        }
    }

    public static class DebitCardPayment implements Payment {
        @Override
        public void pay(int amount) {
            System.out.println("Paid " + amount + " using Debit Card.");
        }
    }

    public static class PayPalPayment implements Payment {
        @Override
        public void pay(int amount) {
            System.out.println("Paid " + amount + " using PayPal.");
        }
    }

    //Factory Class
    public class PaymentFactory {
        public static Payment getPaymentMethod(String type)
        {
            if (type == "CreditCard") {
                return new CreditCardPayment();
            } else if (type == "DebitCard") {
                return new DebitCardPayment();
            } else 
                return new PayPalPayment();
        }
    }

    class PaymentService {
        public void paymentGateway(String type, int amount)
        {
            Payment payment = PaymentFactory.getPaymentMethod(type);
            payment.pay(amount);
        }
    }

    public static void main(String args[])
    {
        Factory f = new Factory();
        PaymentService service = f.new PaymentService();
        service.paymentGateway("DebitCard", 1000);
    }
}
