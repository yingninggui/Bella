/**
 * Basically run
 */
import oscP5.*;

import java.io.File;
import java.io.PrintWriter;

public class MuseOscServer {

    // Connect to headband
    // Run in terminal: muse-io --device Muse-509D --osc-eeg-urls osc.udp://localhost:5000
    // Run this and the close after numbers finish printing and prompt, get file


    static MuseOscServer museOscServer;

    OscP5 museServer;
    static int recvPort = 5000;
    static int cnt = 4000;
    static int elements = 4;
    static double[] things = new double[cnt * elements];
    static PrintWriter writer;
    static int index = 0;

    public static void main(String[] args) {
        museOscServer = new MuseOscServer();
        museOscServer.museServer = new OscP5(museOscServer, recvPort);
    }

    void oscEvent(OscMessage msg) {
        if (cnt > 0) {
            double d;
            if (msg.checkAddrPattern("/muse/eeg") == true) {
                for (int i = 0; i < 4; i++) {
                    d = (double) msg.get(i).floatValue();
                    System.out.println(i + " " + d);
                    things[index] = d;
                    index++;
                }
                cnt--;
            }
        } else {
            System.out.println("done close this program");
            try {
                writer = new PrintWriter(new File("file.txt"));
                writer.println(cnt);
                writer.println(elements);
                for (int i = 0; i < things.length; i++) {
                    writer.println(things[i]);
                }
            } catch (Exception e) {

            }
            writer.close();
        }
    }
}