def plot_acc_loss3(q_history, x_history, v_history):

    plt.figure()
    plt.style.use("seaborn")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 9))

    ax1.plot(v_history.history["val_accuracy"], "-ok", label="Baseline Attn-BiLSTM")
    ax1.plot(q_history.history["val_accuracy"], "-ob", label="With Quanv Layer")
    ax1.plot(x_history.history["val_accuracy"], "-og", label="With Conv Layer")
    ax1.set_ylabel("Accuracy")
    ax1.set_ylim([0, 1])
    ax1.set_xlabel("Epoch")
    ax1.legend()

    ax2.plot(v_history.history["val_loss"], "-ok", label="Baseline Attn-BiLSTM")
    ax2.plot(q_history.history["val_loss"], "-ob", label="With Quanv Layer")
    ax2.plot(x_history.history["val_loss"], "-og", label="With Conv Layer")
    ax2.set_ylabel("Loss")
    #ax2.set_ylim(top=5.5)
    ax2.set_xlabel("Epoch")
    ax2.legend()
    plt.tight_layout()
    plt.savefig("_conv_speech_loss.png")