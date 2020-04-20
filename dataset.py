
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt


import sys
sys.path.append('/Users/AadityaMAC/Desktop/mypython/fsdl-text-recognizer-project/lab1')


# In[2]:


from text_recognizer.datasets.emnist import EmnistDataset


# In[13]:


emnist_data = EmnistDataset()
print(emnist_data)


# In[4]:


emnist_data.load_or_generate_data()
emnist_data.x_train.shape, emnist_data.y_train.shape 


# In[5]:


emnist_data.x_test.shape, emnist_data.y_test.shape 


# In[10]:


fig = plt.figure(figsize=(5,5))
for i in range(25):
    ax = fig.add_subplot(5, 5, i + 1)
    ax.imshow(emnist_data.x_test[i+50].reshape(28, 28), cmap='hot')
    ax.set_title(emnist_data.mapping[np.argmax(emnist_data.y_test[i+50])])

