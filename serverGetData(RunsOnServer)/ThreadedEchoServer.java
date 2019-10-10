import javax.net.ssl.*;
import javax.net.*;
import java.io.*;
import java.net.*;

class EchoThread extends Thread {
    protected Socket socket;

    public EchoThread(Socket clientSocket) {
        this.socket = clientSocket;
    }

    public void run() {
        InputStream inp = null;
        BufferedReader brinp = null;
        PrintWriter out = null;
        try {
            inp = socket.getInputStream();
            brinp = new BufferedReader(new InputStreamReader(inp));
            //out = new DataOutputStream(socket.getOutputStream());
	    out=new PrintWriter(socket.getOutputStream(),true);

        } catch (IOException e) {
            return;
        }
        String line;
        while (true) {
            try {
                line = brinp.readLine();
		System.out.println("received");
                                
		if ((line == null) || line.equalsIgnoreCase("QUIT")) {
			System.out.println(socket.getInetAddress());
                    socket.close();
                    return;
                } else {
                    out.println(line.toUpperCase());
			System.out.println("Sent");
                    out.flush();
                }
            } catch (IOException e) {
                e.printStackTrace();
                return;
            }
        }
    }
}


public class ThreadedEchoServer {

    static final int PORT = 12345;

    public static void main(String args[]) {
        ServerSocket serverSocket = null;
        Socket socket = null;

        try {
            serverSocket = new ServerSocket(PORT);
        } catch (IOException e) {
            e.printStackTrace();

        }
        while (true) {
            try {
                socket = serverSocket.accept();
            } catch (IOException e) {
                System.out.println("I/O error: " + e);
            }
            // new thread for a client
            new EchoThread(socket).start();
        }
    }
}

