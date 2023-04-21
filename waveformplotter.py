def plot_waveform(directory,wds,left_channel_label, right_channel_label):
    wd = os.getcwd();
    print(wd)
    if(wd != wds):
      os.chdir(directory)
      print(wd)
    for each_file in os.listdir(directory):
      #print(each_file)
      filename = os.fsdecode(each_file)
      if filename.endswith(".wav"):
        samplerate,data =  wavfile.read(filename)
        length = data.shape[0] / samplerate
        time = np.linspace(0.,length,data.shape[0])
        plt.plot(time,data[:],label=left_channel_label)
        plt.plot(time,data[:],label= right_channel_label)
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.savefig('wave')
        plt.title('hi_galaxy_resampled')
        plt.show()