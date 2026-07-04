public class Strings {
    public static void main(String[] args) {
        String name = "Rishab";
        System.out.println(name.length());
        System.out.println(name.charAt(4));
        System.out.println(name.substring(3, 6));
        System.out.println(name.contains("Ris"));
        System.out.println(name.toUpperCase());
        for(int i = name.length()-1; i < name.length(); i--){
            System.out.println(name.charAt(i));
        }
    }
}
