public class Isp {
	//Voilates ISP
    /* 
    interface UberUser {
    void bookRide();
    void acceptRide();
    void trackEarnings();
    void ratePassenger();
    void rateDriver();
    }
    class Rider implements UberUser {
    public void bookRide() {  yes  }
    public void acceptRide() { not needed  }
    public void trackEarnings() { not needed }
    public void ratePassenger() { not needed }
    public void rateDriver() { yes }
    }
    */

    //Follows ISP
    interface RiderInterface {
    void bookRide();
    void rateDriver();
}

    interface DriverInterface {
        void acceptRide();
        void trackEarnings();
        void ratePassenger();
    }
    class Rider implements RiderInterface {
        public void bookRide() { /* yes */ }
        public void rateDriver() { /* yes */ }
    }

    class Driver implements DriverInterface {
        public void acceptRide() { /* yes */ }
        public void trackEarnings() { /* yes */ }
        public void ratePassenger() { /* yes */ }
    }


}
