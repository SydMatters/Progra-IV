import java.util.*;

public class FinalProject {
    public static Scanner scanner = new Scanner(System.in);

    //Constants for the array of each user
    public static final byte ID_TYPE = 0;
    public static final byte ID = 1;
    public static final byte NAME = 2;
    public static final byte LAST_NAME = 3;
    public static final byte EMAIL = 4;
    public static final byte ADRESS = 5;
    public static final byte RESIDENCE_CITY = 6;
    public static final byte CELLPHONE = 7;
    public static final byte PASSWORD = 8;
    public static final byte CONFIRM_PASSWORD = 9;

    //The declaration of the list of users.
    public static List <String []> users = new ArrayList<>();

    //Method to clear terminal.
    public static void clearTerminal() {
        try {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.flush();
    }

    //Method to show the menu and recieve the user's choice
    public static byte menuLoginRegister() {

        System.out.println("Welcom to MyVegaHotel...\nMore than a place to rest.");
        System.out.println("----------------------------------------------------------------");
        System.out.println("Enter the desired option");
        System.out.println("1. Register as client.");
        System.out.println("2. Sing in.");
        System.out.println("3. Exit");
        byte option = scanner.nextByte();
        scanner.nextLine(); //I add this nextLine cause nextByte only recive the next Byte and not the \n character.
        return option;

    }

    //Method that applies the logic of the singIn request.
    public static boolean signIn(String entryEmail, String entryPassword) {
        if (users.isEmpty()) {
            System.out.println("There are no registered users!!!");
            return false;
        } else {
            for (String[] user : users) {
                if (user[EMAIL].equals(entryEmail)) {
                    if (user[PASSWORD].equals(entryPassword)) {
                        System.out.println("Login successful.");
                        System.out.println("Please press enter to continue...");
                        scanner.nextLine();
                        return true;
                    } else {
                        System.out.println("Wrong password. Please try again.");
                        return false;
                    }
                }
            }
            System.out.println("There's no registered user with email " + entryEmail);//Shows the wrong email address.
            return false;
        }
    }
    

    //Method that request the users sign-in date and limits the number of tries to sign in.
    public static void menuSignIn() {
        int triesOfSign = 0;
    
        System.out.println("------------------------------------------------------------");
        System.out.println("---------------------------SIGN IN--------------------------");
        System.out.println("------------------------------------------------------------");
        System.out.println("Email: ");
        String email = scanner.nextLine(); 
        System.out.println("Password: ");
        String password = scanner.nextLine(); 
    
        do {
            if (signIn(email, password)) {
                break;
            }
            triesOfSign++;
            if (triesOfSign == 3) {
                System.out.println("You have reached the limit of sign-in attempts.");
                System.out.println("Please press Enter to continue...");
                scanner.nextLine();
                System.exit(0);
            }
            System.out.println("Please try again.");
            System.out.println("Email: ");
            email = scanner.nextLine();
            System.out.println("Password: ");
            password = scanner.nextLine();
        } while (triesOfSign < 3); //3 tries.
    }
    

    //Method to add an user at the list of users.
    public static void userRegister(String[] dataUser){
        String [] userForList = new String[10]; //The exescie indicates that the asignation of the variables has to be one by one, i have my doubts if there is problem with
        //this form of implementation.
        for(byte i = 0; i < userForList.length; i++)
            userForList[i] = dataUser[i];
            users.add(userForList);
    }

    //Method to recieve the user information for the register.
    public static void getUser(){
        String [] user = new String[10];

        System.out.println("------------------------------------------------------------");
        System.out.println("----------------------CLIENT REGISTER-----------------------");
        System.out.println("------------------------------------------------------------");
        System.out.println("Enter the data.");
        System.out.println("Identification type: ");
        user[ID_TYPE] = scanner.nextLine();
        System.out.println("Identification: ");
        user[ID] = scanner.nextLine();
        System.out.println("Name: ");
        user[NAME] = scanner.nextLine();
        System.out.println("Last name: ");
        user[LAST_NAME] = scanner.nextLine();
        System.out.println("Email: ");
        user[EMAIL] = scanner.nextLine();
        System.out.println("Adress: ");
        user[ADRESS] = scanner.nextLine();
        System.out.println("Residence city: ");
        user[RESIDENCE_CITY] = scanner.nextLine();
        System.out.println("Cellphone: ");
        user[CELLPHONE] = scanner.nextLine();

        do {//Confirmation of password.
           System.out.println("Password: ");
           user[PASSWORD] = scanner.nextLine();
           System.out.println("Confirm password: ");
           user[CONFIRM_PASSWORD] = scanner.nextLine();

           if (!user[CONFIRM_PASSWORD].equals(user[PASSWORD]))
                System.out.println("Passwords do not match, try again."); 
            
        } while (!user[PASSWORD].equals(user[CONFIRM_PASSWORD]));

        userRegister(user);
    }

    //Main method.
    public static void main(String[] args) {
        
        byte optionMenu;//Menu is a byte type, this is for save efford.
        do {
            clearTerminal();
            optionMenu = menuLoginRegister();
            switch (optionMenu) {
                case 1:
                    clearTerminal();
                    getUser();
                    break;
                case 2:
                    clearTerminal();
                    menuSignIn();
                    break;
                case 3:
                    clearTerminal();
                    System.out.println("Good bye, see you soon!");
                    System.out.println("Please press enter to continue..");
                    scanner.nextLine();
                    System.exit(0);
                    clearTerminal();
                default:
                    break;
            }
            clearTerminal();
        } while (optionMenu != 3);
        
    }
}