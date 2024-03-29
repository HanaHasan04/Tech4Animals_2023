# Horse Emotion Classification
We have a directory 'data/frames' (with all the frames we extracted from the videos) like this:

                                                  |-----> anticipation
                                                  |-----> baseline
                          |---------> S1 --------->
                          |                       |-----> disappointment
                          |                       |-----> frustration
                          |
                          |                       .
                          |                       .
      data --> frames --->|                       .
                          |                       .
                          |                       .
                          |
                          |                       |-----> anticipation
                          |                       |-----> baseline
                          |---------> S30 -------->
                                                  |-----> disappointment
                                                  |-----> frustration
                    
## **Running instructions:**
1. Make sure you have a directory 'data/frames' as described above.
2. Run step_1_preprocessing.py.
3. Run step_2_embeddings.py.
4. Run step_3_train.py (remember to select k).
5. Run step_4_retrain.py.
6. The final results in 'data/metrics'.

## **The process:**  
- **Step 1: pre-processing:**

  Run step_1_preprocessing.py.

  Sampling will be done for every video of every fifth frame. All unnecessary frames will be deleted from the 'frames' directory.In addition, grayST will be executed. For each video, every 3 consecutive frames will become one RGB frame.
  
- **Step 2: embedding:**
  
  Run step_2_embeddings.py.

  We will get a new directory 'data/metadata' that will contain 30 excels, 1 for each horse, with all the feature vectors of all the frames we sampled.

- **Step 3: train the model and select top k frames:**
  
  Run step_3_train.py.

  Training LOOCV-SVM model with confidence level selection on all metadata. For each horse and each emotion, selecting the k frames that were correctly classified and received the highest accuracy (a total of 4k frames will be received for each horse).

  We will get a new directory 'data/new_metadata' that will contain 30 excels, 1 for each horse, with all the feature vectors of all the top k frames of that horse.
- **Step 4: re-train the model:**
  
  Run step_4_retrain.py.

  Training the model again but now the test-set contains frames from 'data/metadata' while the train-set contains frames from 'data/new_metadata'.
  
  We will get a new directory 'data/metrics' that will contain 30 excels, 1 for each horse, with the accuracy, the precision, the recall, the F1-score and the confusion matrix.
