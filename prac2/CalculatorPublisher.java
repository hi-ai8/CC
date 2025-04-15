import javax.xml.ws.Endpoint;

public class CalculatorPublisher {
    public static void main(String[] args) {
        Endpoint.publish("http://localhost:8080/calculator", new CalculatorServiceImpl());
        System.out.println("Calculator Web Service is running...");
    }
}