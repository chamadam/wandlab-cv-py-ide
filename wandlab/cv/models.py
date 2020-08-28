# -*- encoding: utf-8 -*-
#-------------------------------------------------#
# Date created          : 2020. 8. 18.
# Date last modified    : 2020. 8. 19.
# Author                : chamadams@gmail.com
# Site                  : http://wandlab.com
# License               : GNU General Public License(GPL) 2.0
# Version               : 0.1.0
# Python Version        : 3.6+
#-------------------------------------------------#
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.tools import freeze_graph

class TF_CNN() :
    
    def __init__(self ) :
        
        pass
    
    def load_graph(self, model_path ) :
        
        path = tf.keras.utils.get_file()