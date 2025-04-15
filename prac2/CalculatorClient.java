import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import java.net.URL;

public class CalculatorClient {
    public static void main(String[] args) throws Exception {
        URL url = new URL("http://localhost:8080/calculator?wsdl");
        QName qname = new QName("http://soap.example.com/",
                "CalculatorServiceImplService");

        CalculatorService service = Service.create(url,
                qname).getPort(CalculatorService.class);

        System.out.println("Add: " + service.add(10, 5));
        System.out.println("Multiply: " + service.multiply(10, 5));
        System.out.println("Largest of Two: " + service.largestOfTwo(10, 5));
        System.out.println("Largest of Three: " + service.largestOfThree(10, 20,
                15));
        System.out.println("Square: " + service.square(6));
        System.out.println("Cube: " + service.cube(3));
        System.out.println("Add Three Numbers: " + service.addThree(1, 2, 3));
    }
}