package LSP;

// Notification class
class Notification {
    // method implementing send notification functionality 
    public void sendNotification() {
        System.out.println("Notification sent");
    }
}

// Subclass of Notification class for Email Notification
class EmailNotification extends Notification {
    @Override
    public void sendNotification() {
        System.out.println("Email Notification sent");
    }
}

// Subclass of Notification class for Text Notification
class TextNotification extends Notification {
    @Override
    public void sendNotification() {
        System.out.println("Text Notification sent");
    }
}

class WptNotification extends Notification {
    public void sendWptNotification() {
        System.out.println("Wpt Notification sent");
    }
}


// Main class
class Lsp {
    //  main method
    public static void main(String args[]) {
        /* Replaced the Notification class object
        with one of its subclass' objects */
        Notification notification = new WptNotification();
        
        // Working code on the notification object
        notification.sendNotification();
    }
}
// Implementation of Liskov Substitution Principle in Java
// Subtypes must be substitutable for their base types