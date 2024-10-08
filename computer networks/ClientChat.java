import java.net.*;
import java.io.*;
public class ClientChat{
    public static void main(String args[]){
        Socket c = null;

        String line;
        DataInputStream is = null , is1 =null;
        PrintStream os;
        try{
            c = new Socket("10.0.200.36",9999);

        }catch(IOException e){
            System.out.println(e);
        }
        try{
            os = new PrintStream(c.getOutputStream());
            is = new DataInputStream(System.in);
            is1 = new DataInputStream(c.getInputStream());
            do{
            System.out.print("Client /n enter:");
            line =is.readLine();
            os.println(line);
            System.out.println("Server says:"+is1.readLine());
        
            }while(!line.equalsIgnoreCase("exit"));
            os.close();
            is.close();
            is1.close();
        }catch( Exception e){
            System.out.println(e);
        }
    }
}