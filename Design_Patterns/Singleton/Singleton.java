package Design_Patterns.Singleton;

//Eager Loading
public class Singleton {
    static class EagerLoading {
        //Single instance, created when class loads
        private static final EagerLoading instance = new EagerLoading();

        //Private constructor, restricts object creation
        private EagerLoading(){}

        public static Singleton.EagerLoading getInstance()
        {
            return instance;
        }
    }

    //Lazy Loading, Double Check Locking
    static class LazyLoadingDC {
    //Staatic variable to store Single instance 
    private static LazyLoadingDC instance;

    //Private constructor, restricts object creation
    private LazyLoadingDC(){}

    public static Singleton.LazyLoadingDC getInstance()
    {
        if(instance == null)
        {
            if(instance == null)
            {   //Creates at first time of getInstance() calling
                instance = new LazyLoadingDC();
            }
        }
        return instance;
    }
}

    // Synchronized Lazy Loading 
    static class LazyLoadingSync {
    //Staatic variable to store Single instance 
    private static LazyLoadingSync instance;

    //Private constructor, restricts object creation
    private LazyLoadingSync(){}

    //using synchronized allows only one thread to access
    public static synchronized Singleton.LazyLoadingSync getInstance()
    {
            if(instance == null)
            {   //Creates at first time of getInstance() calling
                instance = new LazyLoadingSync();
            }
        
        return instance;
    }
}

    // Double Check Locking
    static class LazyLoadingSyncOpt {
    //Staatic variable to store Single instance 
    private static volatile LazyLoadingSyncOpt instance;

    //Private constructor, restricts object creation
    private LazyLoadingSyncOpt(){}

    //using synchronized allows only one thread to access
    public static Singleton.LazyLoadingSyncOpt getInstance()
    {   
        if(instance == null)
        // synchronized only when getInstance() called for 1st time
        synchronized (Singleton.LazyLoadingSyncOpt.class){
            if(instance == null)
            {   //Creates at first time of getInstance() calling
                instance = new LazyLoadingSyncOpt();
            }
        }
        
        return instance;
    }
}

    // Bill Pugh Singleton
    // Best approach for Lazy loading ensuring thread safety
    static class LazyLoadingHelper { 

    //Private constructor, restricts object creation
    private LazyLoadingHelper(){}
    
    // Helper class
    private static class Holder {
        //Single instance
        private static final Singleton.LazyLoadingHelper instance = new LazyLoadingHelper();
    } 
    
    public static Singleton.LazyLoadingHelper getInstance()
    {
        // Instance created only for first time when Holder class is referenced using getInstance()
        return Holder.instance;
    }
}
}