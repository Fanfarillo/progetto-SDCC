import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import weka.classifiers.trees.RandomForest;
import weka.core.Instances;

public class MachineLearning {

    public static void main(String[] args) throws Exception {

        BufferedReader bReader = null;
        bReader = new BufferedReader(new FileReader("Train.arff"));
        Instances train = new Instances(bReader);
        train.setClassIndex(train.numAttributes()-1);

        bReader = new BufferedReader(new FileReader("Test.arff"));
        Instances test = new Instances(bReader);
        test.setClassIndex(train.numAttributes()-1);

        bReader.close();

        RandomForest tree = new RandomForest();     //new instance of tree
        tree.buildClassifier(train);                //build classifier
        Instances labeled = new Instances(test);

        //label instances in testing set
        for(int i=0; i<test.numInstances(); i++) {
            double clsLabel = tree.classifyInstance(test.instance(i));
            labeled.instance(i).setClassValue(clsLabel);
        }
        
        //save labeled data in a new file
        BufferedWriter bWriter = new BufferedWriter(new FileWriter("Labeled.arff"));
        bWriter.write(labeled.toString());

        bWriter.close();

    }

}
