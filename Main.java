import java.awt.image.*;
import java.io.*;
import javax.imageio.ImageIO;

public class Main extends CannyEdgeDetector {
    public static void main(String[] args) {
        CannyEdgeDetector detector = new CannyEdgeDetector();
        
        detector.setLowThreshold(0.5f);
        detector.setHighThreshold(1f);

        try {
            BufferedImage image = ImageIO.read(new File("image.png"));
            
            detector.setSourceImage(image);
            detector.process();
            BufferedImage edges = detector.getEdgesImage();
        }
        catch (IOException e) {

        }

        
    }
}
