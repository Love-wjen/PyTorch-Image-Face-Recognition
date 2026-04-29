import matplotlib.pyplot as plt

def plot_curves(losses, accuracies):
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.plot(losses)
    plt.title("Loss")

    plt.subplot(1, 2, 2)
    plt.plot(accuracies)
    plt.title("Accuracy")

    plt.show()
