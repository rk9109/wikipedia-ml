from keras.layers import *
from keras.models import Sequential
from keras.regularizers import *
from keras.optimizers import SGD, Adam
from keras.callbacks import EarlyStopping

def threelayer_model(input_dim, nclasses, loss, output, l1Reg=0):
	"""
	Three hidden layers
	"""
	model = Sequential()

	layers = [Dense(input_dim=input_dim, units=25, kernel_initializer='random_uniform', activation='relu',
			  W_regularizer = l1(l1Reg)),
			  Dense(units=25, kernel_initializer='random_uniform', activation='relu',
			  W_regularizer = l1(l1Reg)),
			  Dense(units=10, kernel_initializer='random_uniform', activation='relu',
			  W_regularizer = l1(l1Reg)),
			  Dense(units=nclasses, kernel_initializer='random_uniform', activation=output,
			  W_regularizer = l1(l1Reg))]

	for layer in layers:
		model.add(layer)

	model.compile(loss=loss, optimizer=Adam(), metrics=['accuracy'])

return model

def lstm_model_small(input_shape, nclasses, loss, output, l1Reg=0):
	"""
	Small LSTM
	"""
	model = Sequential()

	layers = [LSTM(input_shape=input_shape, units=16, activation='relu', return_sequences=False, W_regularizer = l1(l1Reg)),
			  Dense(units=nclasses, kernel_initializer='random_uniform', activation=output, W_regularizer = l1(l1Reg))]

	for layer in layers:
		model.add(layer)

	model.compile(loss=loss, optimizer=Adam(), metrics=['accuracy'])

	return model

def lstm_model_medium(input_shape, nclasses, loss, output, l1Reg=0):
	"""
	Medium LSTM
	"""
	model = Sequential()

	layers = [LSTM(input_shape=input_shape, units=64, return_sequences=True, W_regularizer = l1(l1Reg)),
			  Flatten(),
			  Dense(units=nclasses, kernel_initializer='random_uniform', activation=output, W_regularizer = l1(l1Reg))]

	for layer in layers:
		model.add(layer)

	model.compile(loss=loss, optimizer=Adam(), metrics=['accuracy'])

	return model

def lstm_model_large(input_shape, nclasses, loss, output, l1Reg=0):
	"""
	Large LSTM
	"""
	model = Sequential()

	layers = [LSTM(input_shape=input_shape, units=64, return_sequences=True, W_regularizer = l1(l1Reg)),
			  LSTM(units=32, return_sequences=True, W_regularizer = l1(l1Reg)),
			  LSTM(units=16, return_sequences=True, W_regularizer = l1(l1Reg)),
			  Flatten(),
			  Dense(units=nclasses, kernel_initializer='random_uniform', activation=output, W_regularizer = l1(l1Reg))]

	for layer in layers:
		model.add(layer)

	model.compile(loss=loss, optimizer=Adam(), metrics=['accuracy'])

	return model

def gru_model(input_shape, nclasses, loss, output, l1Reg=0):
	"""
	Simple GRU
	"""
	model = Sequential()

	layers = [GRU(input_shape=input_shape, units=64, return_sequences=True, W_regularizer = l1(l1Reg)),
			  GRU(units=32, return_sequences=True, W_regularizer = l1(l1Reg)),
			  GRU(units=16, return_sequences=True, W_regularizer = l1(l1Reg)),
			  Flatten(),
			  Dense(units=nclasses, kernel_initializer='random_uniform', activation=output,
				    W_regularizer = l1(l1Reg))]

	for layer in layers:
		model.add(layer)

	model.compile(loss=loss, optimizer=Adam(), metrics=['accuracy'])

    return model

def train_model(x_train, y_train, x_test, y_test, model, epochs, batch, val_split=0.25, verbose=True):
	"""
	Train model
	"""
	# Fit model
	early_stopping = EarlyStopping(monitor='val_loss', patience=10)
	history = model.fit(x_train, y_train, epochs=epochs, batch_size=batch,
					    callbacks=[early_stopping], validation_split=val_split, verbose=verbose)

	test_loss, test_acc = model.evaluate(x_test, y_test, batch_size=batch)
	print('\nLoss on test set: ' + str(test_loss) + ' Accuracy on test set: ' + str(test_acc))

    return model, history, test_loss, test_acc

if __name__ == '__main__':
    # TODO generate model from function

    # TODO generate train/test data

    # Parameters
    epochs = 1024
    batch  = 512

    model, history, _, _ = train_model(x_train, y_train, x_test, y_test, model, epochs, batch)
