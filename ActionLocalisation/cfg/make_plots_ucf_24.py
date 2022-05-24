# make plots
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
epoch = [1, 2, 3, 4, 5]

class_accuracy = [0.846, 0.867, 0.859, 0.869, 0.887]
locc_recall = [0.811, 0.849, 0.866, 0.881, 0.885]
best_score = [0.6954959542035535, 0.7528851016652371, 0.761232241027815, 0.7827600963948105, 0.8032339866871153]
# Classification accuracy: 
  # Locolization recall: 
  # New best score is achieved:  0.8032339866871153

fig = plt.figure()
ax2 = fig.add_axes((.1,.4,.8,.5))
plt.bar(epoch, class_accuracy, 0.5)
ax2.set_xlabel('epoch')
ax2.set_ylabel('classification_accuracy')
plt.show()

fig = plt.figure()
ax2 = fig.add_axes((.1,.4,.8, .5))
plt.plot(epoch, locc_recall)
ax2.set_xlabel('epoch')
ax2.set_ylabel('localisation_recall')
plt.show()

fig = plt.figure()
ax2 = fig.add_axes((.1,.4,.8,.5))
plt.plot(epoch, best_score)
ax2.set_xlabel('epoch')
ax2.set_ylabel('best_score')
plt.show()

"""

df = pd.DataFrame({'Epoch': [1,2,3,4,5],'Classification accuracy': [0.846, 0.867, 0.859, 0.869, 0.887], 'Localization recall': [0.811, 0.849, 0.866, 0.881, 0.885], 'Best F1 score': [0.6954959542035535, 0.7528851016652371, 0.761232241027815, 0.7827600963948105, 0.8032339866871153]})
lines = df.plot(kind="line",x="Epoch")
plt.show()

"""
# Importing packages
import matplotlib.pyplot as plt

# Define data values
x = [7, 14, 21, 28, 35, 42, 49]
y = [5, 12, 19, 21, 31, 27, 35]
z = [3, 5, 11, 20, 15, 29, 31]

# Plot a simple line chart
plt.plot(x, y)

# Plot another line on the same chart/graph
plt.plot(x, z)

plt.show()
"""

#%%
 precision = 1.0*correct/(proposals+eps)
            recall = 1.0*correct/(total+eps)
            fscore = 2.0*precision*recall/(precision+recall+eps)
            logging("[%d/%d] precision: %f, recall: %f, fscore: %f" % (batch_idx, nbatch, precision, recall, fscore))

    classification_accuracy = 1.0 * correct_classification / (total_detected + eps)
    locolization_recall = 1.0 * total_detected / (total + eps)

    print("Classification accuracy: %.3f" % classification_accuracy)
    print("Locolization recall: %.3f" % locolization_recall)

    return fscore