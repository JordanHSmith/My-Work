/*
Jordan Smith
PPMFile.java
12/11/23
GrayScale a Photo Using Parallelism
*/ 

import java.io.*;
import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;

public class PPMFile {
    private Pixel[] pixels;
    private int width;
    private int height;
    private int maxColorValue;

    public void readFile(String inputFile) throws IOException {
        // Open the input file for reading
        FileInputStream fis = new FileInputStream(inputFile);
        BufferedReader br = new BufferedReader(new InputStreamReader(fis));
        try {
            // Read the PPM file header
            String magicNumber = br.readLine();
            String line = br.readLine(); // has width and height on the same line
            String parts[] = line.split(" ");
            this.width = Integer.parseInt(parts[0]);
            this.height = Integer.parseInt(parts[1]);
            this.pixels = new Pixel[height * width];
            this.maxColorValue = Integer.parseInt(br.readLine());
        } finally {
            // Close the input and output files
            br.close();
        }

        fis = new FileInputStream(inputFile);
        DataInputStream di = new DataInputStream(fis);
        try {
            // find the 3 newlines, the first byte after that should be data
            int char_byte;
            int newline_count = 0;
            int char_counter = 0;
            for (char_counter = 0; char_counter < 100 && newline_count < 3; char_counter++) {
                // Look for 3 bytes with the value 0
                // they should be the newlines
                char_byte = di.readUnsignedByte();
                if ((char) char_byte == '\n') {
                    newline_count++;
                }
            }
            for (int idx = 0; idx < height * width; idx++) {
                // Read the RGB values of the pixel
                int red = di.readUnsignedByte();
                int green = di.readUnsignedByte();
                int blue = di.readUnsignedByte();
                // store them in the array
                this.pixels[idx] = new Pixel(red, green, blue);
            }
        } finally {
            // Close the input and output files
            di.close();
        }
    }

    public void grayscale(int numThreads) {
        int chunkSize = height * width / numThreads;
        Thread[] threads = new Thread[numThreads];
        AtomicInteger currentIndex = new AtomicInteger(0);

        for (int i = 0; i < numThreads; i++) {
            int start = i * chunkSize;
            int end = (i == numThreads - 1) ? height * width : (i + 1) * chunkSize;

            threads[i] = new Thread(() -> {
                for (int idx = start; idx < end; idx++) {
                    Pixel pix = this.pixels[idx];
                    int avg = (pix.r + pix.g + pix.b) / 3;
                    pix.r = avg;
                    pix.g = avg;
                    pix.b = avg;
                }
            });
            threads[i].start();
        }

        // Wait for all threads to finish
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void writeFile(String outputFile) throws IOException {
        FileOutputStream fos = new FileOutputStream(outputFile);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
        bw.write("P6");
        bw.newLine();
        bw.write(this.width + " " + this.height);
        bw.newLine();
        bw.write(Integer.toString(this.maxColorValue));
        bw.newLine();
        bw.close();

        fos = new FileOutputStream(outputFile, true); // open in append mode
        DataOutputStream di = new DataOutputStream(fos);
        for (int idx = 0; idx < height * width; idx++) {
            // Write the RGB values of the pixel
            di.writeByte(pixels[idx].r);
            di.writeByte(pixels[idx].g);
            di.writeByte(pixels[idx].b);
        }
        di.close();
    }

    public static void main(String[] args) {
        PPMFile ppm = new PPMFile();
        String inputFile = "IMG_4203.ppm";
        String outputFile = "outputParallel.ppm";

        try {
            ppm.readFile(inputFile);

            for (int numThreads : Arrays.asList(1, 2, 4)) {
                System.out.println("Processing with " + numThreads + " thread(s):");

                long cumulativeTime = System.currentTimeMillis();

                for (int i = 0; i < 1000; i++) {
                    // ppm.readFile(inputFile); // Reset the image data
                    ppm.grayscale(numThreads);
                }

                cumulativeTime = System.currentTimeMillis() - cumulativeTime;

                System.out.println("Cumulative time for " + numThreads + " thread(s): " + cumulativeTime + " milliseconds");
            }

            ppm.writeFile(outputFile);
        } catch (IOException e) {
            System.out.println("Error processing PPM file: " + e.getMessage());
        }
    }
}