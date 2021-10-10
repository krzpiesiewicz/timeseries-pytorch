class StepsLoss:
    def __init__(self, loss):
        self.steps = None
        self.loss = loss

    def set_steps(self, steps):
        self.steps = steps

    def __call__(self, y_pred, y_true):
        if self.steps is not None:
            y_pred = y_pred[:, :, : self.steps]
            y_true = y_true[:, :, : self.steps]
        #             print(f"y_pred.shape: {y_pred.shape}, y_true.shape: {y_true.shape}")
        return self.loss(y_pred, y_true)
