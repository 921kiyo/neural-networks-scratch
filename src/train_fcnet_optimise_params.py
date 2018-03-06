import numpy as np

from src.fcnet import FullyConnectedNet
from src.utils.solver import Solver
from src.utils.data_utils import get_FeR2013_data
import json
import pickle
"""
TODO: Use a Solver instance to train a TwoLayerNet that achieves at least 50%
accuracy on the validation set.
"""
###########################################################################
#                           BEGIN OF YOUR CODE                            #
###########################################################################
data = get_FeR2013_data()
model = FullyConnectedNet(hidden_dims=[544,801],input_dim=48*48*1, num_classes=7,dtype=np.float64)#,dropout=0.0reg=0,
model.mean_image = data['mean_image']
lr = 0.0013182567385564034
solver = Solver(model, data,
                update_rule='sgd_momentum',
                optim_config={'learning_rate': lr,}, lr_decay = 1.0,
                num_epochs=100, batch_size=70,
                print_every=100,checkpoint_name="intermediate")

solver.train()
acc1 = solver.check_accuracy(data['X_val'], data['y_val'])
acc2 = solver.check_accuracy(data['X_train'], data['y_train'])







































#val_acc = solver.best_val_acc
#acc = max(solver.train_acc_history)
#json_log = open("output_test.json", mode='wt', buffering=1)
#json_log.write(json.dumps({'Learning Rate': lr,'accuracy': acc, 'val_acc': val_acc,}) + '\n')

##############################################################################
#                             END OF YOUR CODE                               #
##############################################################################
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.title("Training loss")
plt.plot(solver.loss_history, "o")
plt.xlabel('Iteration')
plt.subplot(2, 1, 2)
plt.title('Accuracy')
plt.plot(solver.train_acc_history, '-o', label='train')
plt.plot(solver.val_acc_history, '-o', label='val')
plt.plot([0.5] * len(solver.val_acc_history), 'k--')
plt.xlabel('Epoch')
plt.legend(loc='lower right')
plt.gcf().set_size_inches(15, 12)
plt.show()
