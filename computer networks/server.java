import javax.imageio.ImageIO;
import javax.swing.*;
import java.net.*;
import java.awt.image.*;
import java.io.*;

public class server{
    public static void main(String args[])throws Exception{
        System.out.print("hello");
        Socket soc;
        ServerSocket server = new ServerSocket(4000);
        
        System.out.println("Server wating for image");
        soc = server.accept();
        
        System.out.println("client is connected");

        InputStream in = soc.getInputStream();
        DataInputStream dis = new DataInputStream(in);
        int len = dis.readInt();
        System.out.println("image size = "+len/1024+"KB");
        byte[] data = new byte[len];
        dis.readFully(data);
        dis.close();
        in.close();
        InputStream ian = new ByteArrayInputStream(data);
        BufferedImage bImage = ImageIO.read(ian);
        JFrame f = new JFrame("Server");
        ImageIcon icon = new ImageIcon(bImage);
        JLabel l = new JLabel();
        l.setIcon(icon);
        f.add(l);
        f.pack();
        f.setVisible(true);
        server.close();

    }
}