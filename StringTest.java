public class StringTest {
    public static void main(String[] args) {
        /*String s1 = "  abc  ";
        String s2 = s1.trim(); //Remove spaces from string

        System.out.println(s1);
        System.out.println(s2);*/
        /*
        String s1 = "a";
        String s2 = "b";
        String s3 = "c";
        String s = s1 + s2 + s3; //Concatenate string
        System.out.println(s); */
        /*
        String firstString = "Test123";
        String secondString = "Test" + 123;

        if (firstString.equals(secondString)) {
            System.out.println("Both strings are equal");
        } */

        String firstString = "Test123";
        String secondString = "TEST123";

        if (firstString.equals(secondString)) {
            System.out.println("Both strings are equal");
        } else {
            System.out.println("Both strings are not equal");
        }
    } 
}