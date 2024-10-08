import java.net.*;
import java.awt.image.*;
import javax.imageio.*;
import java.io.*;
public class Client {
    public static void main(String args[])throws Exception{
        System.out.print("hellO\n");
        Socket soc ;
        BufferedImage img = null;
        soc = new Socket("localHost", 4000);
        System.out.println("client is running");
        try{
            System.out.println("reading image form the disk");
            img = ImageIO.read(new File("cat.jpg"));
            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ImageIO.write(img,"jpg",baos);
            baos.flush();
            byte[] bytes = baos.toByteArray();
            baos.close();
            OutputStream out = soc.getOutputStream();
            DataOutputStream dos = new DataOutputStream(out);
            dos.writeInt(bytes.length);
            dos.write(bytes,0,bytes.length);
            dos.close(); 
            out.close(); 
        }catch(Exception e){
            System.out.println("Exception:"+e.getMessage());
        }
        soc.close();
    }
}
