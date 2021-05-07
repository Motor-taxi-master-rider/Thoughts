import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

class A {
    public void f1() {
        System.out.println("hello java");
    }
}


public class Main {
    public static void main(String[] args) throws FileNotFoundException, ClassNotFoundException, NoSuchMethodException, InvocationTargetException, IllegalAccessException, InterruptedException, InstantiationException {
        System.out.println(System.getProperty("user.dir"));
        String line = "";
        try (var in = new Scanner(new FileInputStream("conf.txt"), StandardCharsets.UTF_8)) {
            line = in.nextLine();
        }
        String[] tokens = line.split(",");
        String cls = tokens[0];
        String method = tokens[1];
        Integer interval = Integer.parseInt(tokens[2]);
        Class a = Class.forName(cls);
        Method m = a.getMethod(method);
        Constructor[] cs = a.getDeclaredConstructors();
        Object o = null;
        for (var c : cs) {
            if (c.getParameterCount() == 0) {
                o = c.newInstance();
            }
        }
        while (true) {
            m.invoke(o);
            Thread.currentThread().sleep(interval * 1000);
        }
    }
}