import javax.jws.WebService;

@WebService(endpointInterface = "CalculatorService")
public class CalculatorServiceImpl implements CalculatorService {

    public int add(int a, int b) {
        return a + b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public int largestOfTwo(int a, int b) {
        return Math.max(a, b);
    }

    public int largestOfThree(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }

    public int square(int a) {
        return a * a;
    }

    public int cube(int a) {
        return a * a * a;
    }

    public int addThree(int a, int b, int c) {
        return a + b + c;
    }
}