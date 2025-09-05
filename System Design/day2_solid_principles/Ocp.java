// Implementation of Open/Closed Principle in Java using intefaces
// New functionality can be added by creating new classes that implement the TaxCalculator interface
// Existing code remains unchanged when new tax calculators are added

interface TaxCalculator {
    double calculateTax(double amount);
}

class IndianTaxCalculator implements TaxCalculator {
    @Override
    public double calculateTax(double amount) {
        return amount * 0.18; // 18% GST
    }
}

class USTaxCalculator implements TaxCalculator {
    @Override
    public double calculateTax(double amount) {
        return amount * 0.07; // 7% Sales Tax
    }
}

class UKTaxCalculator implements TaxCalculator {
    @Override
    public double calculateTax(double amount) {
        return amount * 0.10; // 10% VAT
    }
}

// Using dependency Injection
class Invoice {
    private double amount;
    private TaxCalculator taxCalculator;

    public Invoice(double amount, TaxCalculator taxCalculator) {
        this.amount = amount;
        this.taxCalculator = taxCalculator;
    }

    public double getTotalAmount() {
        return amount + taxCalculator.calculateTax(amount);
    }
}
class Ocp {
    public static void main(String[] args) {
        Invoice indianInvoice = new Invoice(32000, new IndianTaxCalculator());
        System.out.println("Indian Invoice Total: " + indianInvoice.getTotalAmount());
        Invoice usInvoice = new Invoice(32000, new USTaxCalculator());
        System.out.println("US Invoice Total: " + usInvoice.getTotalAmount());
        Invoice ukInvoice = new Invoice(32000, new UKTaxCalculator());
        System.out.println("UK Invoice Total: " + ukInvoice.getTotalAmount());
    }
}