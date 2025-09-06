 public class Netflix {

    // Low level modules
    public interface ReccomendationStrategy {
        void recommend();
    }   

    class GenreBasedReccomendation implements ReccomendationStrategy {
        @Override
        public void recommend() {
            System.out.println("Recommending based on genre");
        }
    }
    class RecentReccomendation implements ReccomendationStrategy {
        @Override
        public void recommend() {
            System.out.println("Recommending based on recent watches");
        }
    }

    class RegionBasedReccomendation implements ReccomendationStrategy {
        @Override
        public void recommend() {
            System.out.println("Recommending based on region");
        }
    }

    // High level module
    class ReccomendationAlgorithm {
        private ReccomendationStrategy strategy;

        public ReccomendationAlgorithm(ReccomendationStrategy strategy) {
            this.strategy = strategy;
        }

        public void setStrategy(ReccomendationStrategy strategy) {
            this.strategy = strategy;
        }

        public void recommend() {
            strategy.recommend();
        }
    }

    public static void main(String[] args) {
        Netflix netflix = new Netflix();
        ReccomendationAlgorithm recAlgo = netflix.new ReccomendationAlgorithm(netflix.new GenreBasedReccomendation());
        recAlgo.recommend();

        recAlgo.setStrategy(netflix.new RecentReccomendation());
        recAlgo.recommend();

        recAlgo.setStrategy(netflix.new RegionBasedReccomendation());
        recAlgo.recommend();
    }
}
