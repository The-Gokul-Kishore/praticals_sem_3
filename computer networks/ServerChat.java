import java.net.*;
import java.io.*;
public class ServerChat {
    public static void main(String args[]){
        ServerSocket s = null;
        String line;
        DataInputStream is = null,is1= null;
        PrintStream os = null;
        Socket c = null;
        try{
            s= new ServerSocket(9999);
            System.out.println("Server started. Waiting for connection...");
        }catch(IOException e){
            System.out.println("Error creating server socket: " + e.getMessage());
            return; 
        }
        try{
            c= s.accept();
            is = new DataInputStream(c.getInputStream());
            is1= new DataInputStream(System.in);
            os = new PrintStream(c.getOutputStream());
            do{
                line = is.readLine();
                System.out.println("Client:"+line);
                System.out.println("Server:");
                line = is1.readLine();
                os.println(line);
            }while(line.equalsIgnoreCase("quit")==false);
            is.close();
            os.close();
        }catch(IOException e){
            System.out.println(e);
        }
    }
}
